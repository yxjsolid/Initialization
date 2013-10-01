#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys
import wx



class MyDraggable(wx.Panel):
    def __init__(self, parent, pos, size):
        wx.Panel.__init__(self, parent, pos=pos, size=size)
        self.SetBackgroundColour(wx.CYAN)
        self.Bind(wx.EVT_LEFT_DOWN, self.OnClick)
        self.Bind(wx.EVT_LEFT_UP, self.OnRelease)
        self.Bind(wx.EVT_MOTION, self.OnMouseMove)

    def OnClick(self, e):

        print "onClick"
        self.CaptureMouse()
        self.clickDelta = e.GetPositionTuple()
        self.oldPos = self.GetPositionTuple()
        self.SetBackgroundColour(wx.LIGHT_GREY)
        self.Refresh()
    def OnRelease(self, e):

        print "OnRelease"
        if self.HasCapture():
            print "release mouse"
            self.ReleaseMouse()
            #        self.SetPosition(self.oldPos)
        self.SetBackgroundColour(wx.CYAN)
        self.Refresh()
    def OnMouseMove(self, e):
        if e.Dragging():

            print "on dragging"

            dx, dy = self.clickDelta
            mx, my = e.GetPositionTuple()
            x,y = self.GetPositionTuple()
            x += mx-dx
            y += my-dy
            self.SetPosition((x,y))
            #self.Refresh()

    def AdjustToChild(self, child):
        print "child.GetEffectiveMinSize()", child.GetEffectiveMinSize()

        #self.AdjustToSize(child.GetEffectiveMinSize())
#getDisplySize
        #self.AdjustToSize(child.GetEffectiveMinSize())


        x, y = child.getDisplaySize()

        child.SetSize(wx.Size(x, y))

        self.AdjustToSize(wx.Size(x, y))

    def AdjustToSize(self, size):
        size = wx.Size(*size)
        # self._bestSize = size + (RW_THICKNESS, RW_THICKNESS)
        self._bestSize = size
        self.SetSize(self._bestSize)