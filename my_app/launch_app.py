#!/usr/bin/env python
# -*- coding:gb2312 -*- ��
import wx
import sys
from  MyMiddleWare import *

class MyApp(wx.App):

    def __init__(self, redirect=True, filename=None):
        print "App __init__"
        wx.App.__init__(self, redirect, filename)

    def OnInit(self):
        print "OnInit"    #�����stdout
        self.frame = MyFrame(parent=None)  #�������
        self.frame.Show()
        self.SetTopWindow(self.frame)
        print    sys.stderr, "A pretend error message"    #�����stderr
        return True

    def OnExit(self):
        print "OnExit"

if __name__ == '__main__':
    app = MyApp(redirect=False) #1 �ı��ض�����⿪ʼ
    print "before MainLoop"
    app.MainLoop()  #2 �������¼�ѭ��
    print "after MainLoop"
    
    
    wx.Treebook