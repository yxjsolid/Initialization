#!/usr/bin/env python
# -*- coding: utf-8 -*-

from MyStatusDisplay import *
from mySerial.mySerial import *
from MyCanStationDaemon import *
from MyConfiguration import *


class RuntimeManagement():
    def __init__(self):
        self.statusDisplayMgmt = StatusDisplayManagement()
        self.serialHandle = None
        self.stationDaemonMgmt = None
        self.canProxy = None

    def doRun(self):
        print "runtime run"
        self.buildCanStationManagement()

        self.openSerial()
        self.openCanProxy()
        self.stationDaemonMgmt.startStatusCheck()

    def openSerial(self):
        self.serialHandle = SerialHandler(Port=3)

        try:
            self.serialHandle.start()
        except Exception, se:
            print str(se)

    def buildCanStationManagement(self):
        stationCfg = globalGetCfg().stationCfg
        self.stationDaemonMgmt = CanStationDaemonManagement(stationCfg)

    def openCanProxy(self):
        self.canProxy = CanProxy(SerialHandler=self.serialHandle, stationDaemonMgmt=self.stationDaemonMgmt)
        return
