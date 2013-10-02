import wx


def globalGetCfg():
    cfgObj = wx.GetApp().getConfigure()
    return cfgObj


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


class GuiStatusDisplayCfg():
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
        return

    def appendStatusDisplayCfg(self, cfg):
        self.statusDisplayCfgList.append(cfg)

    def getStatusDisplayCfg(self):
        return self.statusDisplayCfgList


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

        self.deviceController = None
        self.IoNodeCfg = IoNodeConfiguration()

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