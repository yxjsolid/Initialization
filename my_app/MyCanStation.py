# -*- coding: utf-8 -*-

import wx
from MyGlobal import *
import sys,threading,time
import datetime
from mySerial.canData import *


class DeviceCanStation():
    def __init__(self, name=CAN_STATION_DEFAULT_NAME, info=CAN_STATION_DEFAULT_DESC):
        self.name = name
        self.info = info
        self.stationId = 0
        self.InputBoardList = []
        self.OutputBoardList = []
        self.pendingStatusCheck = 0

    def getStationInfo(self):
        infoFormat = "%s:[%s]  %s:[%d]"
        stationInfoStr = infoFormat % (LABEL_CAN_STATION_NAME, self.name, LABEL_CAN_STATION_ID, self.stationId)
        return stationInfoStr

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

    def setBoardIo(self, boardId, IO_DATA):
        board = self.getOutputBoard(boardId)
        board.doSetIoCmd(IO_DATA)

    def onLoadInit(self):
        for board in self.InputBoardList:
            board.onLoadInit()

        for board in self.OutputBoardList:
            board.onLoadInit()

    def dumpInfo(self):
        print self.name, " id:", self.stationId
        for board in self.InputBoardList:
            board.dumpInfo()

        for board in self.OutputBoardList:
            board.dumpInfo()


class DeviceIoBoard():

    BOARD_TYPE_UNKNOW = 0
    BOARD_TYPE_INPUT = 1
    BOARD_TYPE_OUTPUT = 2
    board_type_choices = [LABEL_IO_BOARD_TYPE_UNKNOWN, LABEL_IO_BOARD_INPUT, LABEL_IO_BOARD_OUTPUT]

    Board_status_Init = 0
    Board_status_Connected = 1
    Board_status_Disconnected = 2
    Board_status_Recover = 3
    Board_status_recover_Reply = 4
    Board_status_Ok = 5

    def __init__(self, stationIn=None):
        self.boardType = 0
        self.boardId = 0
        self.isOk = 0
        self.boardStatus = 0

        self.pendingReq = 0
        self.station = stationIn

        self.IoStatus = 0xff
        self.outputStatus = 0xff

        return

    def updateBoardStatus(self, boardId, status):
        self.clearPendingRequest()
        self.IoStatus = status
        return

    def setPendingRequest(self):
        self.pendingReq += 1

    def clearPendingRequest(self):
        self.pendingReq = 0

    def getBoardInfoStr(self):
        infoFormat = "%s:[%s]"
        boardInfoStr = infoFormat % (LABEL_IO_BOARD_COLUM_ID, str(self.boardId))
        return boardInfoStr

    def getBoardIdStr(self):
        return str(self.boardId)

    def getBoardTypeStr(self):
        return self.getBoardTypeStrByTypeId(self.boardType)

    def getBoardTypeStrByTypeId(self, boardType):
        return DeviceIoBoard.board_type_choices[boardType]

    def prepareNewCanFrame(self):
        canFrame = CAN_FRAME()
        #canFrame.setCanFrameType(frameType)
        canFrame.setCanStationId(self.station.stationId)
        return canFrame

    def genSetIoCmdData(self):
        canFrame = self.prepareNewCanFrame()
        canFrame.setCanFrameLen(5)

        canFrame.setCMDType(CAN_FRAME.CAN_FRAME_SET_ACTION)
        canFrame.setCMDBoardType(self.boardType)
        canFrame.setCMDBoardID(self.boardId)
        canFrame.setCMDBoardStatus(self.boardStatus)

       # print "outputstatus %x" % self.outputStatus
        canFrame.setCmdData(self.outputStatus)

        return canFrame

    def doSetIoCmd(self, IO_DATA):
        frame = self.genSetIoCmdData(IO_DATA)
        self.station.daemon.canProxy.sendCanFrame(frame)
        self.setIoEvent.wait(1)
        if not self.setIoEvent.isSet():
            print self.getBoardTypeStr(), " id: [%d] setCmd", self.boardId, " timeout"

    def genStatusCheckData(self):
        canFrame = self.prepareNewCanFrame()
        canFrame.setCanFrameLen(5)

        canFrame.setCMDType(CAN_FRAME.CAN_FRAME_STATUS_CHECK)
        canFrame.setCMDBoardType(self.boardType)
        canFrame.setCMDBoardID(self.boardId)
        canFrame.setCMDBoardStatus(self.boardStatus)

        #canFrame.dumpCanData()
        return canFrame

    def isPortOn(self, port):
        #print "iostatus = %x" % self.IoStatus
        flag = (~self.IoStatus) & (0x1 << (port - 1))
        return flag

    def setPortStatus(self, port, onOffFlag):
        if onOffFlag == 1:
            self.outputStatus &= ~(0x1 << (port - 1))
        elif onOffFlag == 0:
            self.outputStatus |= (0x1 << (port - 1))

    def onLoadInit(self):
        self.IoStatus = 0xff
        self.outputStatus = 0xff

    def dumpInfo(self):
        print self.getBoardTypeStr(), " id:",self.boardId, "status:%x" % self.outputStatus, "IO:%x" % self.IoStatus