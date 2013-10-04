#!/usr/bin/env python
# -*- coding: utf-8 -*-

from MyStatusDisplay import *
from mySerial.mySerial import *
from MyCanStationDaemon import *
from MyAction import *
from MyConfiguration import *


class RuntimeManagement():
    def __init__(self):
        self.statusDisplayMgmt = StatusDisplayManagement()
        self.actionMgmt = ActionManagement()
        self.serialHandle = None
        self.stationDaemonMgmt = None
        self.canProxy = None
        self.buildCanStationManagement()

    def doRun(self):
        print "RuntimeManagement run"

        self.openSerial()
        self.openCanProxy()

        self.stationDaemonMgmt.startStatusCheck()
        self.statusDisplayMgmt.displayUpdateCheck(0.5)

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
