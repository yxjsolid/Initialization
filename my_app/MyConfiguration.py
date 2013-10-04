import wx
from MySprite import *


class ActionGroupConfiguration():
    def __init__(self):
        self.actionGrpList = []
        return

    def addActionGroup(self, actionGrp):
        self.actionGrpList.append(actionGrp)
        return

    def getActionGroupList(self):
        return self.actionGrpList

    def setActionGroupList(self, actGrpList):
        self.actionGrpList = actGrpList


class StationConfiguration():
    def __init__(self):
        self.stationList = []
        return

    def addCanStation(self, canStation):
        self.stationList.append(canStation)

    def setCanStationList(self, canStationList):
        self.stationList = canStationList

    def getCanStationList(self):
        return self.stationList

    def dumpStationCfg(self):
        for station in self.stationList:
            station.dumpInfo()

    def onLoadInit(self):
        for station in self.stationList:
            station.onLoadInit()



class TransporterLayoutCfg():
    def __init__(self, pos):
        self.pos = (pos[0], pos[1])

        #self.operationOn = None
        #self.operationOff = None
        return

    def updatePos(self, dx, dy):
        self.pos = (self.pos[0] + dx, self.pos[1] + dy)

    def createSprite(self):
        sprite = AnimateTansporterSprite(initPos=(self.pos[0], self.pos[1]), width=400, height=60)
        sprite.guiCfg = self
        return sprite


class ButtonLayoutCfg():
    def __init__(self, pos, resourceDict):
        self.pos = (pos[0], pos[1])
        self.resourceDict = resourceDict

        self.operationOn = None
        self.operationOff = None

        return

    def createSprite(self):
        sprite = ButtonSprite(initPos=(self.pos[0], self.pos[1]), dicts=self.resourceDict)
        sprite.operationOn = self.operationOn
        sprite.operationOff = self.operationOff
        sprite.guiCfg = self
        return sprite

    def updatePos(self, dx, dy):
        self.pos = (self.pos[0] + dx, self.pos[1] + dy)


class GuiStatusDisplayLayoutCfg():
    def __init__(self, pos, colSetting, nodeList):
        self.pos = pos
        self.colSetting = colSetting
        self.nodeList = nodeList
        return

    def dumpSelf(self):
        print "pos", self.pos
        print "colSetting", self.colSetting
        print "nodeList", self.nodeList


class GuiLayoutConfiguration():
    def __init__(self):
        self.statusDisplayCfgList = []
        self.buttonLayoutCfgList = []
        return

    def appendStatusDisplayCfg(self, cfg):
        self.statusDisplayCfgList.append(cfg)

    def getStatusDisplayCfg(self):
        return self.statusDisplayCfgList

    def appendButtonLayoutCfg(self, cfg):
        self.buttonLayoutCfgList.append(cfg)

    def getButtonLayoutCfg(self):
        return self.buttonLayoutCfgList

    def appendWidgetLayoutCfg(self, cfg):
        self.buttonLayoutCfgList.append(cfg)
        return

    def onCfgLoadUpdateStatusDiaplay(self, hmiPanel):
        statusDisplayMgmt = globalGetRuntime().statusDisplayMgmt
        statusDisplayMgmt.onCfgLoadUpdate(hmiPanel, self.statusDisplayCfgList)

    def onCfgLoadUpdateButtonLayout(self, hmiPanel):

        for btnCfg in self.getButtonLayoutCfg():
            sprite = btnCfg.createSprite()
            hmiPanel.addSpriteToPanel(sprite)

        return

    def onCfgLoadUpdate(self, hmiPanel):
        self.onCfgLoadUpdateStatusDiaplay(hmiPanel)
        self.onCfgLoadUpdateButtonLayout(hmiPanel)


class IoNodeConfiguration():
    def __init__(self):
        self.inputIoCategoryList = []
        self.outputIoCategoryList = []

    def setInputIoCategoryList(self, listIn):
        self.inputIoCategoryList = listIn

    def setOutputIoCategoryList(self, listIn):
        self.outputIoCategoryList = listIn

    def getInputIoCategoryList(self):
        return self.inputIoCategoryList

    def getOutputIoCategoryList(self):
        return self.outputIoCategoryList


class CfgContainer():
    def __init__(self):
        self.stationCfg = StationConfiguration()
        self.guiCfg = GuiLayoutConfiguration()
        self.actionGroupCfg = ActionGroupConfiguration()

        self.deviceController = None
        self.IoNodeCfg = IoNodeConfiguration()

    def getActionGroupCfgList(self):
        return self.actionGroupCfg.getActionGroupList()

    def testDump(self, pickle, file):
        print "test guiCfg"
        pickle.dump(self.guiCfg, file)

        print "test IoNodeCfg"
        pickle.dump(self.IoNodeCfg, file)

        print "test stationCfg"
        pickle.dump(self.stationCfg, file)

    def getGuiLayoutCfg(self):
        return self.guiCfg

    def appendStatusDisplayCfg(self, cfg):
        self.guiCfg.appendStatusDisplayCfg(cfg)

    def getStatusDisplayCfg(self):
        return self.guiCfg.getStatusDisplayCfg()

    def setActionGroupCfg(self, actionGroupList):
        self.actionGroupCfg.setActionGroupList(actionGroupList)

    def onCfgLoadUpdate(self, hmiPanel):
        self.guiCfg.onCfgLoadUpdate(hmiPanel)