import wx
from MyStatusDisplay import *

class Draggable(wx.Panel):
    def __init__(self, parent, size):
        wx.Panel.__init__(self, parent, size=size)
        self.SetBackgroundColour(wx.BLACK)
        self.Bind(wx.EVT_LEFT_DOWN, self.OnClick)
        self.Bind(wx.EVT_LEFT_UP, self.OnRelease)
        self.Bind(wx.EVT_MOTION, self.OnMouseMove)
    def OnClick(self, e):

        print "onClick"
        self.CaptureMouse()
        self.clickDelta = e.GetPositionTuple()
        self.oldPos = self.GetPositionTuple()
        self.SetBackgroundColour(wx.WHITE)
        self.Refresh()
    def OnRelease(self, e):

        print "OnRelease"
        if self.HasCapture():
            print "release mouse"
            self.ReleaseMouse()
    #        self.SetPosition(self.oldPos)
        self.SetBackgroundColour(wx.BLACK)
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

class Frame(wx.Frame):
    def __init__(self):
        wx.Frame.__init__(self, None, -1, size=(1000, 1000))
        sizer = wx.BoxSizer(wx.VERTICAL)
        self.SetSizer(sizer)

        d = Draggable(self, (500, 500))

        subP = Panel_Status_Display(d)
        #subP.Freeze()
        subP.Disable()

        d.SetFocusIgnoringChildren()

        d.SetPosition((50, 50))

class App(wx.App):
    def OnInit(self):
        f = Frame()
        self.SetTopWindow(f)
        f.Show()
        return True

app = App(0)
app.MainLoop()