#!/usr/bin/env python
# -*- coding: utf-8 -*- 
import wx
import sys
import MyGlobal as gl
from  MyMiddleWare import *

class MyApp(wx.App):

    def __init__(self, redirect=True, filename=None):
        print "App __init__"
        wx.App.__init__(self, redirect, filename)
		
    def OnInit(self):
        print "OnInit"
        self.frame = wx.Frame(parent=None)
        self.frame.Show()
        self.SetTopWindow(self.frame)
        testPanel(self.frame)
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
