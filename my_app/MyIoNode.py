# -*- coding: utf-8 -*-

import wx
import sys,threading,time
import datetime
from MyGlobal import *
from MyCanStation import *


class IoNode():
    def __init__(self):
        self.name = ""
        self.desc = ""
        self.offInfo = ""
        self.onInfo = ""

        self.category = None
        self.station = None
        self.board = None
        self.port = 0

    def getIoInfoStr(self):
        info = ""

        stationInfo = self.station.getStationInfo()
        boardInfo = self.board.getBoardInfoStr()
        portInfo = "%s:[%d]" % (LABEL_IO_PORT, self.port)
        info += stationInfo + " " + boardInfo + " " + portInfo
        return info

    def getNodeNameWithCategory(self):
        info = self.category.name + "\\" + self.name
        return info



class IoNodeCategory():
    def __init__(self):
        self.name = EDIT_IO_NODE_LABEL_GROUP_DEFAULT
        self.ioNodeList = []
        return

    def removeIoNode(self, nodeObj):
        self.ioNodeList.remove(nodeObj)

