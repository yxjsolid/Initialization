#!/usr/bin/env python
#coding:utf-8
from wx import *

class Trans(Frame):    
    def __init__(self, parent, id, title):        
        Frame.__init__(self, parent, id, title, size=(700, 800), style=DEFAULT_FRAME_STYLE | STAY_ON_TOP)        
        #self.Text = ListCtrl(self, style=TE_MULTILINE | HSCROLL)        
        #self.Text.SetBackgroundColour('White'), self.Text.SetForegroundColour('Steel Blue')        
        self.SetTransparent(100)        
        self.Show()
app = App()
Trans(None, 1, "Transparent Window")
app.MainLoop()
