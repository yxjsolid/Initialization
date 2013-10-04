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
        #print "getStationDaemon, sattionId ", stationId
        return self.daemonDict[stationId][1]

    def startStatusCheck(self):
        for stationId in self.daemonDict:
            self.getStationDaemon(stationId).daemonDoStatusCheck(1)

    def sendCanFrame(self, frame):
        self.dataProxy.sendCanFrame(frame)

    def doIoNodeOutput(self, outputNode):
        station = outputNode.station
        board = outputNode.board
        board.setPortStatus(outputNode.port, outputNode.onOffFlag)

        self.getStationDaemon(station.stationId).doSetStationBoardIo(board)

        return

    def daemonHandleCanFrameReceived(self, canFrame):
        stationId = canFrame.getCanStationId()
        self.getStationDaemon(stationId).daemonHandleCanFrameReceived(canFrame)
        return


class CanStationDaemon():
    def __init__(self, daemonMgmt=None, stationIn=None):
        self.station = stationIn
        self.boardStatusCheckEventDict = {}
        self.boardSetCmdEventDict = {}
        self.stationLock = None
        self.stationSendFrameEvent = None

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
        self.boardSetCmdEventDict[board] = threading.Event()

    def stationInit(self):
        self.stationLock = threading.Lock()
        self.stationSendFrameEvent = threading.Event()

        for board in self.station.InputBoardList:
            self.boardInit(board)

        for board in self.station.OutputBoardList:
            self.boardInit(board)

    def doStationLock(self):
        return self.stationLock.acquire()

    def doStationRelease(self):
        self.stationLock.release()


    def daemonDoStatusCheck(self, interval):
        _dict = self.boardStatusCheckEventDict
        for board in _dict:
            self.doBoardStatusCheck(board, _dict[board], interval)

        return

    def doBoardStatusCheck(self, board, event, interval):
        #print datetime.datetime.now(),  "doStatusCheck "
        #self.stationSendFrameEvent.wait(1)
        self.doStationLock()
        self.stationSendFrameEvent.wait(0.2)
        #print datetime.datetime.now(),  "station send frame"
        self.doStationRelease()

        frame = board.genStatusCheckData()
        self.daemonMgmt.sendCanFrame(frame)
        #self.setPendingRequest()
        event.wait(3)
        if not event.isSet():
            print  datetime.datetime.now(), board.getBoardTypeStr(), " id: [%d] " % board.boardId, " timeout"

        self.startStatusCheckTimer(board, event, interval)

    def startStatusCheckTimer(self, board, event, interval):
        t = threading.Timer(interval, self.doBoardStatusCheck, (board, event, interval))
        t.start()

    def getBoardStatusCheckEvent(self, board):
        _dict = self.boardStatusCheckEventDict
        event = _dict[board]
        return event

    def getCmdSetEvent(self, board):
        _dict = self.boardSetCmdEventDict
        event = _dict[board]
        return event

    def getPendingEvent(self, cmdType, board):
        if cmdType == CAN_FRAME.CAN_FRAME_SET_ACTION:
            event = self.getCmdSetEvent(board)
        elif cmdType == CAN_FRAME.CAN_FRAME_STATUS_CHECK:
            event = self.getBoardStatusCheckEvent(board)
        else:
            event = None

        return event

    def daemonHandleCanFrameReceived(self, canFrame):
        #print datetime.datetime.now(),  "station receive frame"
        #self.stationSendFrameEvent.set()

        # self.doStationRelease()

        #print "CanStationDaemon --> daemonHandleCanFrameReceived"
        boardType = canFrame.getCMDBoardType()
        boardId = canFrame.getCMDBoardID()
        board = self.station.getBoard(boardType, boardId)

        cmdType = canFrame.getCMDType()
        event = self.getPendingEvent(cmdType, board)

        if event is None:
            print "station[%d]" % self.station.stationId, board.getBoardTypeStr(), " id: [%r] " % board.boardId, "received packet with unknown cmd type"
            return

        event.set()

        #print board.getBoardTypeStr(), boardId, canFrame.getCMDBoardStatus()
        board.updateBoardStatus(canFrame.getCMDBoardStatus())
        board.updateIoStatus(canFrame.getCmdData())

        # #print "board.IoStatus = %x" % board.IoStatus
        #
        # if board.boardStatus == DeviceIoBoard.BOARD_STATUS_DISCONNECTED:
        #     print board.getBoardTypeStr(), " id: [%r] " % board.boardId, "disconnected"
        # else:
        #     #print board.getBoardTypeStr(), " id: [%d] " % board.boardId, " get reply"
        #     #print "self.IoStatus = %x " % board.IoStatus
        #     pass
        # #self.station.stationHandleCanFrameReply(canFrame)
        return

    def doSetStationBoardIo(self, board):
        print datetime.datetime.now(),  "doSetStationBoardIo "
        _dict = self.boardSetCmdEventDict
        canFrame = board.genSetIoCmdData()
        self.daemonMgmt.sendCanFrame(canFrame)

        #_dict[board] = threading.Event()
        _dict[board].wait(2)
        if not _dict[board].isSet():
            print " board[%d] setCmd" % board.boardId, " timeout"

        return


    def doSetIoCmd(self, IO_DATA):
        frame = self.genSetIoCmdData(IO_DATA)
        self.station.daemon.canProxy.sendCanFrame(frame)
        self.setIoEvent.wait(1)
        if not self.setIoEvent.isSet():
            print self.getBoardTypeStr(), " id: [%d] setCmd", self.boardId, " timeout"


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

    canStation.setBoardIo(1, 0x0)
