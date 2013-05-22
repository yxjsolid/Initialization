# -*- encoding: utf-8 -*-
import wx

BASE  = 80.0    # sizes used in shapes drawn below
BASE2 = BASE/2
BASE4 = BASE/4

class wxGeoCanvas(wx.Panel):
    def __init__(self, parent):
        wx.Panel.__init__(self,parent,-1)
        self.Bind(wx.EVT_PAINT, self.OnPaint)
    def OnPaint(self, evt):
        dc = wx.PaintDC(self)

        dc.SetBrush(wx.GREY_BRUSH)
        dc.DrawPolygon(((0,0),(400,400),(400,0)))
        dc.SetBrush(wx.GREEN_BRUSH)
        dc.SetPen(wx.RED_PEN)
        dc.DrawPolygon(((200,100),(200,200),(100,200),(200,100), \
            (60,60), (300,0),(300,300),(0,300),(60,60)))

        #另一种方法
        try:
            gc = wx.GraphicsContext.Create(dc)
        except NotImplementedError:
            dc.DrawText("This build of wxPython does not support the wx.GraphicsContext "
                        "family of classes.",
                        25, 25)
            return

        path = gc.CreatePath()
        path.MoveToPoint(-BASE2, -BASE2)
        path.AddLineToPoint(-BASE2, BASE2)
        path.AddLineToPoint(BASE2, BASE2)
        path.AddLineToPoint(BASE2, -BASE2)
        path.CloseSubpath()
        path.AddRectangle(-BASE4, -BASE4/2, BASE2, BASE4)

        gc.SetPen(wx.Pen("navy", 1))
        gc.SetBrush(wx.BLUE_BRUSH)

        gc.PushState()             # save current translation/scale/other state
        gc.Translate(60, 65)       # reposition the context origin

        gc.FillPath(path)
        
app = wx.PySimpleApp(0)
mainframe = wx.Frame(None, -1, "")
geoCanvas = wxGeoCanvas(mainframe)
sizermain = wx.BoxSizer(wx.VERTICAL)
sizermain.Add(geoCanvas, 1, wx.EXPAND, 0)
mainframe.SetAutoLayout(True)
mainframe.SetSizer(sizermain)
mainframe.Layout()
mainframe.SetSize((600,400))
app.SetTopWindow(mainframe)
mainframe.Show()
app.MainLoop()

