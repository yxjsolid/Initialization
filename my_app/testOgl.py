# shapedrop.py

import wx
import wx.lib.ogl as ogl

import cPickle

class TaskShape(ogl.RectangleShape):
    def __init__(self, w=100, h=50):
        ogl.RectangleShape.__init__(self, w, h)
class FlowCanvas(ogl.ShapeCanvas):
    def __init__(self, parent,frame):
        ogl.ShapeCanvas.__init__(self, parent)

        maxWidth  = 500
        maxHeight = 500
        self.SetScrollbars(20, 20, maxWidth/20, maxHeight/20)

        self.frame = frame
        self.SetBackgroundColour("LIGHT BLUE") #wx.WHITE)
        self.diagram = ogl.Diagram()
        self.SetDiagram(self.diagram)
        self.diagram.SetCanvas(self)
        self.shapes = []
        
        rRectBrush = wx.Brush("GREEN", wx.SOLID)
        
        self.add_shape(
            TaskShape(100, 80), 
            200, 158, wx.Pen(wx.BLUE, 2), rRectBrush, "Task Shape1"
        )
        
    def add_shape(self, shape, x, y, pen, brush, text):
        # Composites have to be moved for all children to get in place
        if isinstance(shape, ogl.CompositeShape):
            dc = wx.ClientDC(self)
            self.PrepareDC(dc)
            shape.Move(dc, x, y)
        else:
            shape.SetDraggable(True, True)
        shape.SetCanvas(self)
        shape.SetX(x)
        shape.SetY(y)
        if pen:    shape.SetPen(pen)
        if brush:  shape.SetBrush(brush)
        if text:
            for line in text.split('\n'):
                shape.AddText(line)
        #shape.SetShadowMode(ogl.SHADOW_RIGHT)
        self.diagram.AddShape(shape)
        shape.Show(True)
        
        self.shapes.append(shape)
        return shape
    
    def on_drop():
        frame.on_drag_init()
    
class TempCanvas(ogl.ShapeCanvas):
    def __init__(self, parent,frame):
        ogl.ShapeCanvas.__init__(self, parent)

        maxWidth  = 500
        maxHeight = 500
        self.SetScrollbars(20, 20, maxWidth/20, maxHeight/20)

        #self.log = log
        self.frame = frame
        self.SetBackgroundColour("LIGHT GREY") #wx.WHITE)
        self.diagram = ogl.Diagram()
        self.SetDiagram(self.diagram)
        self.diagram.SetCanvas(self)
        self.shapes = []
        self.save_gdi = []
        
class TaskShapeDropTarget(wx.PyDropTarget):
    
    def __init__(self, canvas):
        wx.PyDropTarget.__init__(self)
        #self.log = log
        
        # specify the type of data we will accept
        self.data = wx.CustomDataObject("TaskShape")
        self.SetDataObject(self.data)
    def on_drop_taskshape(self, x, y, data):
        self.canvas.add_shape(
            TaskShape(), 
            380,158, wx.BLACK_PEN, dsBrush, ''
        )
class FlowFrame(wx.Frame):
    def __init__(self, *args, **kwds):
        wx.Frame.__init__(self, *args, **kwds)
        #panel = wx.Panel(self)
        global obj
        obj ={}
        
        self.StatusBar = wx.StatusBar(self)
        splitter1 = wx.SplitterWindow(self, -1, style=wx.SP_3D)
        splitter2 = wx.SplitterWindow(splitter1, -1, style=wx.SP_3D)
        #log = open('log.log')

        self.SetTitle("OGL TEST")
        self.SetSize((800,600))
        self.SetBackgroundColour(wx.Colour(8, 197, 248))
        
        self.canvas = FlowCanvas(splitter1,self)
        self.canvas_temp = TempCanvas(splitter2,self)
        
        splitter1.SplitVertically(self.canvas, splitter2)
        splitter2.Initialize(self.canvas_temp)
        self.Center()
        
        # create the droptaaget
        self.shapetaget = TaskShapeDropTarget(self.canvas_temp)
        self.canvas_temp.SetDropTarget(self.shapetaget)
        self.canvas.Bind(wx.EVT_LEFT_DOWN, self.on_drag_init, id=self.canvas.GetId())
    def on_drag_init(self,event):
        
        # create our own data format and use it in a custom data object
        self.data = wx.CustomDataObject("TaskShape")
        # pickle the shape list
        obj['1234']=self.canvas.shapes
        shape_data = cPickle.dumps(obj['1234'])
        self.data.SetData(shape_data)
        
        
        
        tds = wx.DropSource(self.canvas)
        tds.SetData(self.data)
        tds.DoDragDrop(True)
        
app = wx.PySimpleApp(False)
wx.InitAllImageHandlers()
ogl.OGLInitialize()
frame = FlowFrame(None, -1, "")
app.SetTopWindow(frame)
frame.Show(True)
app.MainLoop()
