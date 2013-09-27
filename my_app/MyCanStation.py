# -*- coding: utf-8 -*-

import wx
from MyGlobal import *
import sys,threading,time
import datetime
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
        self.daemon = None

    def addNewIoBoard(self, board):

        if board.boardType == DeviceIoBoard.BOARD_TYPE_INPUT:
            self.InputBoardList.append(board)
            board.station = self
        elif board.boardType == DeviceIoBoard.BOARD_TYPE_OUTPUT:
            self.OutputBoardList.append(board)
            board.station = self
        else:
            print "addNewIoBoard error"

    def getBoard(self, boardType, boardId):

        if boardType == DeviceIoBoard.BOARD_TYPE_INPUT:
            return self.getInputBoard(boardId)

        if boardType == DeviceIoBoard.BOARD_TYPE_OUTPUT:
            return self.getOutputBoard(boardId)

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

    def stationHandleCanFrameReply(self, canFrame):
        boardType = canFrame.canData[0]
        boardId = canFrame.canData[1]
        board = self.getBoard(boardType, boardId)
        board.boardHandleCanFrameReply(canFrame)

        return

    def handleStatusCheckReply(self, canFrame):
        inBoardCnt = canFrame.getInputBoardCnt()
        outBoardCnt = canFrame.getOutputBoardCnt()

        self.clearPendingStatusCheck()

        for i in range(inBoardCnt):
            boardId = canFrame.getCanFrameData(i * 2)
            boardStatus = canFrame.getCanFrameData(i * 2 + 1)

            print "boardid = ", boardId

            board = self.getInputBoard(boardId)
            board.updateBoardStatus(boardId, boardStatus)

        for i in range(outBoardCnt):
            boardId = canFrame.getCanFrameData(i)
            board = self.getOutputBoard(boardId)
            board.updateBoardStatus(boardId, 0)

        return

    def doStatusCheck(self, interval):

        for board in self.InputBoardList:
            board.doStatusCheck(interval)

        for board in self.OutputBoardList:
            board.doStatusCheck(interval)

        return

    def stationHandleCanFrameReceived(self, canFrame):

        return

    # def getStatusCheckData(self):
    #     statusCheckFrames = []
    #     canFrame = self.prepareNewCanFrame(CAN_FRAME.CAN_FRAME_STATUS_CHECK)
    #
    #     frameLen = 0
    #     inputBoardCnt = 0
    #     for inputBoard in self.InputBoardList:
    #         inputBoard.setPendingRequest()
    #         frameLen += 1
    #         inputBoardCnt += 1
    #         if frameLen == 9:
    #             canFrame.setCanFrameLen(8)
    #             canFrame.setInputBoardCnt(8)
    #             statusCheckFrames.append(canFrame)
    #
    #             canFrame = self.prepareNewCanFrame(CAN_FRAME.CAN_FRAME_STATUS_CHECK)
    #             frameLen = 1
    #             inputBoardCnt = 1
    #
    #         canFrame.setCanFrameData(frameLen - 1, inputBoard.boardId)
    #         canFrame.setInputBoardCnt(frameLen)
    #         canFrame.setCanFrameLen(frameLen)
    #
    #     for outputBoard in self.OutputBoardList:
    #         outputBoard.setPendingRequest()
    #         frameLen += 1
    #         if frameLen == 9:
    #             canFrame.setCanFrameLen(8)
    #             canFrame.setOutputBoardCnt(8 - inputBoardCnt)
    #             statusCheckFrames.append(canFrame)
    #
    #             canFrame = self.prepareNewCanFrame(CAN_FRAME.CAN_FRAME_STATUS_CHECK)
    #             frameLen = 1
    #
    #         canFrame.setCanFrameData(frameLen - 1, outputBoard.boardId)
    #         canFrame.setOutputBoardCnt(frameLen - inputBoardCnt)
    #         canFrame.setCanFrameLen(frameLen)
    #
    #     statusCheckFrames.append(canFrame)
    #     return statusCheckFrames

class DeviceIoBoard():

    BOARD_TYPE_INPUT, BOARD_TYPE_OUTPUT = range(2)
    board_type_choices = [LABEL_IO_BOARD_INPUT, LABEL_IO_BOARD_OUTPUT]

    BOARD_STAT_INIT = 0
    BOARD_STAT_CONNECT = 1
    BOARD_STAT_TIMEOUT = 2
    BOARD_STAT_RECOVER = 3

    def __init__(self, stationIn=None):
        self.boardType = 0
        self.boardId = 0
        self.isOk = 0
        self.boardStatus = 0
        self.IoStatus = 0
        self.pendingReq = 0
        self.station = stationIn
        self.statusCheckTaskEvent = threading.Event()

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

    def prepareNewCanFrame(self):
        canFrame = CAN_FRAME()
        #canFrame.setCanFrameType(frameType)
        canFrame.setCanStationId(self.station.stationId)

        return canFrame

    def genStatusCheckData(self):
        canFrame = self.prepareNewCanFrame()
        canFrame.setCanFrameLen(5)

        canFrame.setCMDBoardType(self.boardType)
        canFrame.setCMDBoardID(self.boardId)
        canFrame.setCMDType(CAN_FRAME.CAN_FRAME_STATUS_CHECK)
        canFrame.setCMDBoardStatus(self.boardStatus)
        #canFrame.setCMDBoardType(self.boardType)

        return canFrame

    def doStatusCheck(self, interval):
        print datetime.datetime.now(),  "doStatusCheck "

        frame = self.genStatusCheckData()
        self.station.daemon.canProxy.sendCanFrame(frame)
        self.setPendingRequest()
        self.statusCheckTaskEvent.wait(1)
        if not self.statusCheckTaskEvent.isSet():
            print self.getBoardTypeStr(), " id: [%d] ", self.boardId, " timeout"

        self.startStatusCheckTimer(interval)

    def startStatusCheckTimer(self, interval):
        t = threading.Timer(interval, self.doStatusCheck, (interval, ))
        t.start()

    def boardHandleCanFrameReply(self, canFrame):
        print self.getBoardTypeStr(), " id: [%d] ", self.boardId, " get reply"
        self.boardStatus = canFrame.getCMDBoardStatus()
        self.IoStatus = canFrame.getCmdData()
        self.clearPendingRequest()

        return