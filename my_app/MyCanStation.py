# -*- coding: utf-8 -*-

import wx
from MyGlobal import *
from mySerial.canData import *


class StationManagement():
    def __init__(self):

        self.stationList = []

        return


    def addCanStation(self, canStation):
        self.stationList.append(canStation)

    def setCanStationList(self, canStationList):
        self.stationList = canStationList

    def getCanStationList(self):
        return self.stationList


class DeviceCanStation():
    def __init__(self, name=LABEL_STATION_NAME, info=LABEL_STATION_INFO):
        self.name = name
        self.info = info
        self.stationId = 0
        self.InputBoardList = []
        self.OutputBoardList = []
        self.pendingStatusCheck = 0

    def addNewIoBoard(self, board):

        if board.boardType == DeviceIoBoard.BOARD_TYPE_INPUT:
            self.InputBoardList.append(board)
        elif board.boardType == DeviceIoBoard.BOARD_TYPE_OUTPUT:
            self.OutputBoardList.append(board)
        else:
            print "addNewIoBoard error"

    def getInputBoard(self, boardId):
        for board in self.InputBoardList:
            if board.boardId == (boardId & 0x7f):
                return board

        return None

    def getOutputBoard(self, boardId):
        for board in self.OutputBoardList:
            if board.boardId == (boardId & 0x7f):
                return board

        return None

    def setPendingStatusCheck(self):
        self.pendingStatusCheck += 1

    def clearPendingStatusCheck(self):
        self.pendingStatusCheck = 0

    def prepareNewCanFrame(self, frameType):
        canFrame = CAN_FRAME()
        canFrame.setCanFrameType(frameType)
        canFrame.setCanStationId(self.stationId)

        return canFrame

    def handleStatusCheckReply(self, canFrame):
        inBoardCnt = canFrame.getInputBoardCnt()
        outBoardCnt = canFrame.getOutputBoardCnt()

        self.clearPendingStatusCheck()

        for i in range(inBoardCnt):
            boardId = canFrame.getCanFrameData(self, i * 2)
            boardStatus = canFrame.getCanFrameData(self, i * 2 + 1)
            board = self.getInputBoard(boardId)
            board.updateBoardStatus(boardId, boardStatus)

        for i in range(outBoardCnt):
            boardId = canFrame.getCanFrameData(self, i)
            board = self.getOutputBoard(boardId)
            board.updateBoardStatus(boardId, 0)

        return

    def getStatusCheckData(self):
        statusCheckFrames = []
        canFrame = self.prepareNewCanFrame(CAN_FRAME.CAN_FRAME_STATUS_CHECK)

        frameLen = 0
        inputBoardCnt = 0
        for inputBoard in self.InputBoardList:
            inputBoard.setPendingRequest()
            frameLen += 1
            inputBoardCnt += 1
            if frameLen == 9:
                canFrame.setCanFrameLen(8)
                canFrame.setInputBoardCnt(8)
                statusCheckFrames.append(canFrame)

                canFrame = self.prepareNewCanFrame(CAN_FRAME.CAN_FRAME_STATUS_CHECK)
                frameLen = 1
                inputBoardCnt = 1

            canFrame.setCanFrameData(frameLen - 1, inputBoard.boardId)
            canFrame.setInputBoardCnt(frameLen)
            canFrame.setCanFrameLen(frameLen)

        for outputBoard in self.OutputBoardList:
            outputBoard.setPendingRequest()
            frameLen += 1
            if frameLen == 9:
                canFrame.setCanFrameLen(8)
                canFrame.setOutputBoardCnt(8 - inputBoardCnt)
                statusCheckFrames.append(canFrame)

                canFrame = self.prepareNewCanFrame(CAN_FRAME.CAN_FRAME_STATUS_CHECK)
                frameLen = 1

            canFrame.setCanFrameData(frameLen - 1, outputBoard.boardId)
            canFrame.setOutputBoardCnt(frameLen - inputBoardCnt)
            canFrame.setCanFrameLen(frameLen)

        statusCheckFrames.append(canFrame)
        return statusCheckFrames


class DeviceIoBoard():

    BOARD_TYPE_INPUT, BOARD_TYPE_OUTPUT = range(2)
    board_type_choices = [LABEL_IO_BOARD_INPUT, LABEL_IO_BOARD_OUTPUT]

    BOARD_STAT_INIT = 0
    BOARD_STAT_CONNECT = 1
    BOARD_STAT_TIMEOUT = 2
    BOARD_STAT_RECOVER = 3

    def __init__(self):
        self.boardType = 0
        self.boardId = 0
        self.isOk = 0
        self.boardStatus = 0
        self.IoStatus = 0
        self.pendingReq = 0

        return

    def updateBoardStatus(self, boardId, status):
        self.clearPendingRequest()
        self.IoStatus = status
        return

    def setPendingRequest(self):
        self.pendingReq += 1

    def clearPendingRequest(self):
        self.pendingReq = 0

    def getBoardIdStr(self):

        return str(self.boardId)

    def getBoardTypeStr(self):
        return DeviceIoBoard.board_type_choices[self.boardType]