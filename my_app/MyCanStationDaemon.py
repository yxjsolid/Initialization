# -*- coding: utf-8 -*-

import wx
import sys,threading,time
import datetime
from MyGlobal import *
from MyCanStation import *
from mySerial.canData import *
from mySerial.mySerial import *


class CanStationDaemonMgmt():
    def __init__(self):
        self.daemonDict = {}

        return

    def addStationDaemon(self, station, daemon):
        self.daemonDict[station.stationId] = [station, daemon]
        return

    def getStationDaemon(self, stationId):
        print "getStationDaemon, sattionId ", stationId

        return self.daemonDict[stationId][1]


class CanStationDaemon():
    def __init__(self, stationIn=None, canProxyIn=None):
        self.station = stationIn
        self.canProxy = canProxyIn

        self.station.daemon = self
        # self.statusCheckTask = None
        #
        # self.statusCheckTaskEvent = threading.Event()

        return

    def daemonHandleCanFrameReceived(self, canFrame):
        print "CanStationDaemon --> daemonHandleCanFrameReceived"

        self.station.stationHandleCanFrameReply(canFrame)
        return

    def doStatusCheck(self, interval):
        print datetime.datetime.now(),  "doStatusCheck "

        self.station.doStatusCheck(interval)
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
    daemonMgmt = CanStationDaemonMgmt()

    rt = SerialHandler(Port=3)

    try:
        rt.start()
    except Exception, se:
        print str(se)

    canProxy = CanProxy(SerialHandler=rt, daemonMgmtIn=daemonMgmt)

    rt.dataHandler = canProxy

    canStation = buildCanStationTest(5)

    daemon = CanStationDaemon(canStation, canProxy)

    daemonMgmt.addStationDaemon(canStation, daemon)

    daemon.doStatusCheck(1)

    canStation.setBoardIo(1, 0x0)
