# -*- coding: utf-8 -*-

import wx
from MyGlobal import *
from serial.canData import *


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

    def addNewIoBoard(self, board):

        if board.boardType == DeviceIoBoard.BOARD_TYPE_INPUT:
            self.InputBoardList.append(board)
        elif board.boardType == DeviceIoBoard.BOARD_TYPE_OUTPUT:
            self.OutputBoardList.append(board)
        else:
            print "addNewIoBoard error"

    def prepareNewCanFrame(self, frameType):
        canFrame = CAN_FRAME()
        canFrame.setCanFrameType(frameType)
        canFrame.setCanStationId(self.stationId)

        return canFrame

    def getStatusCheckData(self):
        statusCheckFrames = []
        canFrame = self.prepareNewCanFrame(CAN_FRAME.CAN_FRAME_STATUS_CHECK)

        frameLen = 0
        inputBoardCnt = 0
        for inputBoard in self.InputBoardList:
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

    def __init__(self):
        self.boardType = 0
        self.boardId = 0

        return

    def getBoardIdStr(self):

        return str(self.boardId)

    def getBoardTypeStr(self):
        return DeviceIoBoard.board_type_choices[self.boardType]