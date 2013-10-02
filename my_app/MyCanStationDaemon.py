# -*- coding: utf-8 -*-

import wx
import sys,threading,time
import datetime
from MyGlobal import *
from MyCanStation import *
from mySerial.canData import *
from mySerial.mySerial import *


class CanStationDaemonManagement():
    def __init__(self, stationCfg=None):
        self.daemonDict = {}
        self.setupStationDaemon(stationCfg)
        self.dataProxy = None
        return

    def setupStationDaemon(self, stationCfg):
        if stationCfg is None:
            return

        for station in stationCfg.getCanStationList():
            self.addStationDaemon(station)
        return

    def addStationDaemon(self, station):
        daemon = CanStationDaemon(self, station)
        self.daemonDict[station.stationId] = [station, daemon]
        return

    def getStationDaemon(self, stationId):
        print "getStationDaemon, sattionId ", stationId

        return self.daemonDict[stationId][1]

    def startStatusCheck(self):
        for stationId in self.daemonDict:
            self.getStationDaemon(stationId).daemonDoStatusCheck(1)

    def sendCanFrame(self, frame):
        self.dataProxy.sendCanFrame(frame)


class CanStationDaemon():
    def __init__(self, daemonMgmt=None, stationIn=None):
        self.station = stationIn
        self.boardStatusCheckEventDict = {}
        self.boardActionEventDict = {}
        self.daemonMgmt = daemonMgmt
        self.doInit()
        # self.statusCheckTask = None
        #
        # self.statusCheckTaskEvent = threading.Event()
        return

    def doInit(self):
        self.stationInit()

    def boardInit(self, board):
        self.boardStatusCheckEventDict[board] = threading.Event()
        self.boardActionEventDict[board] = threading.Event()

    def stationInit(self):
        for board in self.station.InputBoardList:
            self.boardInit(board)

        for board in self.station.OutputBoardList:
            self.boardInit(board)

    def daemonDoStatusCheck(self, interval):
        _dict = self.boardStatusCheckEventDict
        for board in _dict:
            self.doBoardStatusCheck(board, _dict[board], interval)

        return

    def doBoardStatusCheck(self, board, event, interval):
        print datetime.datetime.now(),  "doStatusCheck "

        frame = board.genStatusCheckData()
        self.daemonMgmt.sendCanFrame(frame)
        #self.setPendingRequest()
        event.wait(3)
        if not event.isSet():
            print board.getBoardTypeStr(), " id: [%d] ", board.boardId, " timeout"

        self.startStatusCheckTimer(board, event, interval)

    def startStatusCheckTimer(self, board, event, interval):
        t = threading.Timer(interval, self.doBoardStatusCheck, (board, event, interval))
        t.start()

    def getBoardStatusCheckEvent(self, board):
        _dict = self.boardStatusCheckEventDict
        event = _dict[board]
        return event

    def daemonHandleCanFrameReceived(self, canFrame):
        print "CanStationDaemon --> daemonHandleCanFrameReceived"

        boardType = canFrame.getCMDBoardType()
        boardId = canFrame.getCMDBoardID()
        board = self.station.getBoard(boardType, boardId)

        event = self.getBoardStatusCheckEvent(board)
        event.set()

        board.boardStatus = canFrame.getCMDBoardStatus()
        board.IoStatus = canFrame.getCmdData()

        if board.boardStatus == DeviceIoBoard.Board_status_Disconnected:
            print board.getBoardTypeStr(), " id: [%r] " % board.boardId, "disconnected"
        else:
            print board.getBoardTypeStr(), " id: [%d] " % board.boardId, " get reply"
            print "self.IoStatus = %x " % board.IoStatus

        #self.station.stationHandleCanFrameReply(canFrame)
        return

    def doStationDeamonStatusCheck(self, interval):
        print datetime.datetime.now(),  "doStatusCheck "

        self.station.doStationInit()
        self.station.doStationStatusCheck(interval)
    #     frameList = self.station.getStatusCheckData()
    #
    #     for frame in frameList:
    #         frame.structureToByteArray()
    #         self.canProxy.sendCanFrame(frame)
    #         self.station.setPendingStatusCheck()
    #
    #         self.statusCheckTaskEvent.wait(1)
    #         print "doStatusCheck -> ",  self.statusCheckTaskEvent.isSet()
    #
    #         #if not self.statusCheckTaskEvent.isSet():
    #
    #     self.startStatusCheckTimer(interval)
    #
    # def startStatusCheckTimer(self, interval):
    #     t = threading.Timer(interval, self.doStatusCheck, (interval, ))
    #     t.start()


def buildTestIoBoard(idIn, typeIn):
    ioBoard = DeviceIoBoard()
    ioBoard.boardId = idIn
    ioBoard.boardType = typeIn
    return ioBoard


def buildCanStationTest(idIn):
    canStation = DeviceCanStation()
    canStation.stationId = idIn

    #canStation.InputBoardList.append(buildTestIoBoard(3, DeviceIoBoard.BOARD_TYPE_INPUT))
    #canStation.InputBoardList.append(buildTestIoBoard(3, DeviceIoBoard.BOARD_TYPE_INPUT))
    #canStation.InputBoardList.append(buildTestIoBoard(3, DeviceIoBoard.BOARD_TYPE_INPUT))
    #canStation.InputBoardList.append(buildTestIoBoard(6, DeviceIoBoard.BOARD_TYPE_INPUT))

    canStation.addNewIoBoard(buildTestIoBoard(1, DeviceIoBoard.BOARD_TYPE_INPUT))

    canStation.addNewIoBoard(buildTestIoBoard(1, DeviceIoBoard.BOARD_TYPE_OUTPUT))
    #canStation.addNewIoBoard(buildTestIoBoard(2, DeviceIoBoard.BOARD_TYPE_OUTPUT))
    #canStation.addNewIoBoard(buildTestIoBoard(3, DeviceIoBoard.BOARD_TYPE_OUTPUT))

    return canStation


if __name__ == '__main__':
    daemonMgmt = CanStationDaemonManagement()

    rt = SerialHandler(Port=3)

    try:
        rt.start()
    except Exception, se:
        print str(se)

    canProxy = CanProxy(SerialHandler=rt, stationDaemonMgmt=daemonMgmt)

    rt.dataHandler = canProxy

    canStation = buildCanStationTest(5)

    daemonMgmt.addStationDaemon(canStation)

    daemonMgmt.startStatusCheck()

    #canStation.setBoardIo(1, 0x0)
