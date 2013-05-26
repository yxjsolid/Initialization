#!/usr/bin/env python
# -*- coding: utf-8 -*- 
import wx
import wx.lib.buttons as buttons
from MyGlobal import *


class __MyBtnMixin:
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

        x, y = self.GetSize()
        if x == 0 or y == 0:
            self.SetSize(img.GetSize())
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

    def getIconBmp(self, size=None):

        if size:
            x,y = size
            img = self.imageLabel.Scale(x,y,quality=wx.IMAGE_QUALITY_HIGH)
        else:
            img = self.imageLabel

        return img.ConvertToBitmap()

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

    def OnDrawBtn(self):

        (width, height) = self.GetClientSizeTuple()
        x1 = y1 = 0
        x2 = width-1
        y2 = height-1

        print "__MyBtnMixin onpaint"

        #dc = wx.PaintDC(self)
        #dc = wx.ClientDC(self)

        dc = wx.ClientDC(self)  # Device context for drawing the bitmap
        #dc = wx.PaintDC(self)
        dc = wx.BufferedDC( dc)
        #dc.Clear()
        self.DrawBezel(dc, x1, y1, x2, y2)
        self.DrawLabel(dc, width, height)
        if self.hasFocus and self.useFocusInd:
            self.DrawFocusIndicator(dc, width, height)

        return dc

    def OnPaint(self, event):
        (width, height) = self.GetClientSizeTuple()
        x1 = y1 = 0
        x2 = width-1
        y2 = height-1
        
        print "__MyBtnMixin onpaint"

        #dc = wx.PaintDC(self)

        dc = wx.BufferedPaintDC(self)

        # gc = wx.GCDC(dc)
        #
        # dc.SetBrush(wx.TRANSPARENT_BRUSH)
        # dc.SetBackground(wx.TRANSPARENT_BRUSH)
        # dc.SetBackgroundMode(wx.TRANSPARENT)
        # dc.SetPen(wx.TRANSPARENT_PEN)
        #dc = wx.ClientDC(self)
        #dc.Clear()
        self.DrawBezel(dc, x1, y1, x2, y2)
        self.DrawLabel(dc, width, height)
        if self.hasFocus and self.useFocusInd:
            self.DrawFocusIndicator(dc, width, height)

class MyGenBitmapButton(__MyBtnMixin, buttons.GenBitmapButton):
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


class MyGenBitmapToggleButton(__MyBtnMixin, buttons.GenBitmapToggleButton):
    def __init__(self, parent=None, id=-1, bmp=wx.NullBitmap,
                 pos = wx.DefaultPosition, size = wx.DefaultSize,
                 style = wx.BORDER_NONE|wx.TRANSPARENT_WINDOW, validator = wx.DefaultValidator,
                 name = "genbutton"):
        self.parent = parent
        self.index = 0

        if size == wx.DefaultSize:
            size = (75,75)

        buttons.GenBitmapToggleButton.__init__(self, parent, id, None, pos , size,style , validator,name )


        self.loadButtonImage()
        self.Bind(wx.EVT_PAINT, self.OnPaint)
        self.Bind(wx.EVT_ERASE_BACKGROUND, self.OnErase)

    def OnErase(self, evt):

        print "MyGenBitmapToggleButton onerase"
        return

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

    def OnPaint1(self, event):
        print "MyGenBitmapToggleButton onPaint"
        buttons.GenBitmapToggleButton.OnPaint(self, event)

    def DrawLabel(self, dc, width, height, dx=0, dy=0):
        bmp = self.bmpLabel
        if self.bmpDisabled and not self.IsEnabled():
            bmp = self.bmpDisabled
        if self.bmpFocus and self.hasFocus:
            bmp = self.bmpFocus
        if self.bmpSelected and not self.up:
            bmp = self.bmpSelected
        bw,bh = bmp.GetWidth(), bmp.GetHeight()
        if not self.up:
            dx = dy = self.labelDelta
        hasMask = bmp.GetMask() != None
        dc.DrawBitmap(bmp, (width-bw)/2+dx, (height-bh)/2+dy, 1)