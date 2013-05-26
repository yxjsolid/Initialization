#!/usr/bin/env python
# -*- coding: utf-8 -*-
import wx



class MyTestApplication():
    def __init__(self):
        self.app = wx.App(redirect=False)

    def setFrame(self):
        self.window = wx.Frame(parent=None, id = wx.ID_ANY, title = u"my app", pos = wx.DefaultPosition, size = wx.Size( 1024,768 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )

    def setDialog(self):
        self.window = wx.Dialog(parent=None, id = wx.ID_ANY, title = u"my dialog", pos = wx.DefaultPosition, size = wx.Size( 1024,768 ), style = wx.DEFAULT_DIALOG_STYLE |wx.RESIZE_BORDER)

        self.window.Layout()
        self.window.Centre( wx.BOTH )

    def launchApp(self):
        self.window.Show()
        self.app.MainLoop()


