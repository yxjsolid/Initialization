# -*- coding: utf-8 -*-

import wx
import sys,threading,time
import datetime
from MyGlobal import *
from MyCanStation import *
from serial.canData import *


class CanStationDaemonMgmt():
    def __init__(self):
        self.daemonDict = {}

        return

    def addStationDaemon(self, station, daemon):
        self.daemonDict[station.stationId] = [station, daemon]
        return

    def getStationDaemon(self, stationId):
        return self.daemonDict[stationId]


class CanStationDaemon():
    def __init__(self, stationIn=None, canProxyIn=None):
        self.station = stationIn
        self.canProxy = canProxyIn
        self.statusCheckTask = None

        self.statusCheckTaskEvent = threading.Event()

        return

    def handleCanFrameReceived(self, canFrame):

        return

    def doStatusCheck(self, interval):
        print datetime.datetime.now(),  "doStatusCheck "

        frameList = self.station.getStatusCheckData()

        for frame in frameList:
            frame.structureToByteArray()
            self.canProxy.sendCanFrame(frame)
            self.statusCheckTaskEvent.wait(5)
            print "doStatusCheck -> ",  self.statusCheckTaskEvent.isSet()

        self.startStatusCheckTimer(interval)

    def startStatusCheckTimer(self, interval):
        t = threading.Timer(interval, self.doStatusCheck, (interval, ))
        t.start()


def buildTestIoBoard(idIn, typeIn):
    ioBoard = DeviceIoBoard()
    ioBoard.boardId = idIn
    ioBoard.boardType = typeIn
    return ioBoard


def buildCanStationTest(idIn):
    canStation = DeviceCanStation()
    canStation.stationId = idIn

    canStation.InputBoardList.append(buildTestIoBoard(3, DeviceIoBoard.BOARD_TYPE_INPUT))
    canStation.InputBoardList.append(buildTestIoBoard(3, DeviceIoBoard.BOARD_TYPE_INPUT))
    canStation.InputBoardList.append(buildTestIoBoard(3, DeviceIoBoard.BOARD_TYPE_INPUT))
    canStation.InputBoardList.append(buildTestIoBoard(6, DeviceIoBoard.BOARD_TYPE_INPUT))

    canStation.OutputBoardList.append(buildTestIoBoard(1, DeviceIoBoard.BOARD_TYPE_OUTPUT))
    canStation.OutputBoardList.append(buildTestIoBoard(2, DeviceIoBoard.BOARD_TYPE_OUTPUT))
    canStation.OutputBoardList.append(buildTestIoBoard(3, DeviceIoBoard.BOARD_TYPE_OUTPUT))

    return canStation


if __name__ == '__main__':
    daemonMgmt = CanStationDaemonMgmt()

    canProxy = CanProxy(daemonMgmtIn=daemonMgmt)
    canStation = buildCanStationTest(5)

    daemon = CanStationDaemon(canStation, canProxy)

    daemonMgmt.addStationDaemon(canStation, daemon)

    daemon.doStatusCheck(1)
