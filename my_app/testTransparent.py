import wx
class myframe (wx.Frame):
    def __init__(self, parent):
        wx.Frame.__init__ (self, parent, id = wx.ID_ANY, title =
wx.EmptyString, pos = wx.DefaultPosition, size = wx.Size( 500,300 ),
style = wx.RESIZE_BORDER|wx.SUNKEN_BORDER)
        self.SetSizeHintsSz(wx.DefaultSize, wx.DefaultSize)
        self.SetBackgroundColour(wx.Colour(0, 0, 0))
        self.Centre(wx.BOTH)
        self.Bind(wx.EVT_LEFT_DOWN, self.OnLeftDown)
        self.Bind(wx.EVT_LEFT_UP, self.OnLeftUp)
        self.Bind(wx.EVT_MOTION, self.OnMouseMove)
        self.Bind(wx.EVT_RIGHT_UP, self.OnExit)
        self.Bind(wx.EVT_PAINT, self.OnPaint)

    def OnExit(self, evt):
        self.SetEvtHandlerEnabled(False)
        self.Destroy()

    def OnLeftDown(self, evt):
        parent = wx.GetTopLevelParent(self)
        self.CaptureMouse()
        x, y = parent.ClientToScreen(evt.GetPosition())
        originx, originy = parent.GetPosition()
        dx = x - originx
        dy = y - originy
        self.delta = ((dx, dy))

    def OnLeftUp(self, evt):
        if self.HasCapture():
            self.ReleaseMouse()

    def OnMouseMove(self, evt):
        if evt.Dragging() and evt.LeftIsDown():
            parent = wx.GetTopLevelParent(self)
            x, y = self.ClientToScreen(evt.GetPosition())
            fp = (x - self.delta[0], y - self.delta[1])
            parent.Move(fp)

    def GetBg(self):
        x,y=self.GetPosition()
        xx,yy=self.GetSizeTuple()
        bmp = wx.EmptyBitmap(xx, yy)
        dc = wx.MemoryDC()
        dc.SelectObject(bmp)
        dc.Blit(x,y,xx,yy,wx.ScreenDC(),x,y)
        return bmp

    def OnPaint(self, evt):
        x,y=self.GetPosition()
        dc = wx.ScreenDC()
        bmp = self.GetBg()
        brush = wx.BrushFromBitmap(bmp)
        dc.SetBackground(brush)
        orange = wx.Colour(255,132.0)
        dc.SetTextForeground(orange)
        dc.DrawText('Hello transparent window! This text is not transparent.', x+13, y+11)

app = wx.App(False)
fr = myframe(None)
fr.SetTransparent(0)
fr.Show()
app.MainLoop() 
