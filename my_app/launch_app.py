#!/usr/bin/env python
# -*- coding:gb2312 -*- ＃
import wx
import sys
from  MyMiddleWare import *

class MyApp(wx.App):

    def __init__(self, redirect=True, filename=None):
        print "App __init__"
        wx.App.__init__(self, redirect, filename)

    def OnInit(self):
        print "OnInit"    #输出到stdout
        self.frame = MyFrame(parent=None)  #创建框架
        self.frame.Show()
        self.SetTopWindow(self.frame)
        print    sys.stderr, "A pretend error message"    #输出到stderr
        return True

    def OnExit(self):
        print "OnExit"

if __name__ == '__main__':
    app = MyApp(redirect=False) #1 文本重定向从这开始
    print "before MainLoop"
    app.MainLoop()  #2 进入主事件循环
    print "after MainLoop"
    
    
    wx.Treebook