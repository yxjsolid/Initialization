#!/usr/bin/env python
# -*- coding: utf-8 -*- 
import wx
import wx.lib.buttons as buttons
from MyGlobal import *


class MyBtnMixin:
    def setSizeFitImage(self):
        size = self.imageLabel.GetSize()
        
        print "size",size

        #help(size)
        #help(self.SetSize)
        self.SetSize(size)
        self.reloadButtonImage()

        #self.DoSetClientSize(200,200)
        #self.Refresh()
        
    def covnertImg2Bmp(self,img):
        x, y = self.GetSize()
        #img.Rescale(x,y, quality=wx.IMAGE_QUALITY_HIGH)
        img = img.Scale(x,y,quality=wx.IMAGE_QUALITY_HIGH)
        return img.ConvertToBitmap()


    def loadImageLabel(self, imageFile):
        img = wx.Image(imageFile)
        self.setImageLabel(img)

    def loadImageSelected(self, imageFile):
        img = wx.Image(imageFile)
        self.setImageSelected(img)

    def setImageLabel(self,img):
        self.imageLabel = img
        print "setImageLabel,size = ",self.imageLabel.GetSize()
        bmp = self.covnertImg2Bmp(img)
        self.SetBitmapLabel(bmp)

    def setImageSelected(self,img):
        self.imageSelected = img
        bmp = self.covnertImg2Bmp(img)
        self.SetBitmapSelected(bmp)

    def reloadButtonImage(self):
        self.setImageLabel(self.imageLabel)
        self.setImageSelected(self.imageSelected)   

    def loadButtonImage(self):
        self.loadImageLabel(btn_red_up)
        self.loadImageSelected(btn_green_down)


    def SetMoveBegin(self, pos):
        self.initPos = pos


    def SetMoveEnd(self, pos):
        self.initPos = pos
        self.GetParent().SetDoubleBuffered(0)

    def SetMoving(self,pos):
        dx = pos[0] - self.initPos[0]
        dy = pos[1] - self.initPos[1]
        
        self.Raise()

        x,y = self.GetPosition()
        x = x + dx
        y = y + dy
        self.MoveXY(x,y)
        #self.Refresh()
        #self.parent.Update()
        #sself.parent.Refresh()

    def OnPaint(self, event):
        (width, height) = self.GetClientSizeTuple()
        x1 = y1 = 0
        x2 = width-1
        y2 = height-1
        
        print "onpaint"

        dc = wx.PaintDC(self)
        self.DrawBezel(dc, x1, y1, x2, y2)
        self.DrawLabel(dc, width, height)
        if self.hasFocus and self.useFocusInd:
            self.DrawFocusIndicator(dc, width, height)

class MyGenBitmapButton(MyBtnMixin, buttons.GenBitmapButton):
    def __init__(self, parent, id=-1, bmp=wx.NullBitmap,
                 pos = wx.DefaultPosition, size = wx.DefaultSize,
                 style = 0, validator = wx.DefaultValidator,
                 name = "genbutton"):
        self.parent = parent
        self.index = 0

        if size == wx.DefaultSize:
            size = (100,100)

        buttons.GenBitmapButton.__init__(self, parent, id, None, pos , size,style , validator,name )
        self.loadButtonImage()
        
    def loadButtonImage(self):
        self.loadImageLabel(btn_red_up)
        self.loadImageSelected(btn_green_down)

   

class MyGenBitmapToggleButton(MyBtnMixin, buttons.GenBitmapToggleButton):
    def __init__(self, parent, id=-1, bmp=wx.NullBitmap,
                 pos = wx.DefaultPosition, size = wx.DefaultSize,
                 style = 0, validator = wx.DefaultValidator,
                 name = "genbutton"):
        self.parent = parent
        self.index = 0

        if size == wx.DefaultSize:
            size = (75,75)

        buttons.GenBitmapToggleButton.__init__(self, parent, id, None, pos , size,style , validator,name )
        self.loadButtonImage()

    def OnMotion(self, event):
        if not self.IsEnabled() or not self.HasCapture():
            return
        if event.LeftIsDown() and self.HasCapture():
            x,y = event.GetPositionTuple()
            w,h = self.GetClientSizeTuple()
            if self.up and x<w and x>=0 and y<h and y>=0:
                self.up = False
                self.Refresh()
                return
            if not self.up and (x<0 or y<0 or x>=w or y>=h):
                self.up = True
                self.Refresh()
                return
        event.Skip()
    
    def OnLeftDown(self, event):
        if not self.IsEnabled():
            return
        self.saveUp = self.up
        self.up = not self.up
        self.CaptureMouse()
        self.SetFocus()
        self.Refresh()
        event.Skip()

