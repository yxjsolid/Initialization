#!/usr/bin/env python
# -*- coding: utf-8 -*- 
import wx
import sys
import MyGlobal as gl
from  MyMiddleWare import *



from MyDevice import *

class CfgContainer():
    def __init__(self):
        self.stationManagement = None
        self.deviceController = None



class MyApp(wx.App):
    deviceController = None


    def __init__(self, redirect=True, filename=None):
        print "App __init__"
        wx.App.__init__(self, redirect, filename)
        self.cfgContainer = CfgContainer()

        self.cfgContainer.stationManagement = StationManagement()
        self.cfgContainer.deviceController = None

    def getDeviceCtrl(self):
        return self.getConfigure().deviceController

    def getStationMgmt(self):
        return self.getConfigure().stationManagement

    def getConfigure(self):
        return self.cfgContainer

    def setConfigure(self, cfg):
        self.cfgContainer = cfg


    def getAllDeviceList(self):
        return self.deviceController.getDevices()
        
    def OnInit(self):
        print "OnInit"
        self.deviceController = DeviceController()
        self.frame = MyFrame(parent=None)
        self.frame.Show()
        
        self.viewPanel_sub = self.frame.viewPanel_sub
        self.SetTopWindow(self.frame)
        print    sys.stderr, "A pretend error message"
        return True

    def OnExit(self):
        print "OnExit"
    
    def SetAppViewSelectPanel(self, panel):
        self.ViewSelectPanel = panel
        return

    
    def GetAppViewSelectPane(self):
        return self.ViewSelectPanel
        

if __name__ == '__main__':
    app = MyApp(redirect=False)
    print "before MainLoop"
    app.MainLoop()
    
    gl.app = app
    print "after MainLoop"
    
