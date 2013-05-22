#!/usr/bin/env python
# -*- coding: utf-8 -*- 
import wx
import sys
import MyGlobal as gl
from  MyMiddleWare import *

import wx.lib.buttons as buttons
import wx.lib.agw.shapedbutton as sbbutton
import wx.lib.platebtn as platebtn
import  wx.gizmos   as  gizmos
from wx.lib.embeddedimage import PyEmbeddedImage

Monkey = PyEmbeddedImage(
    "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"
    "nMQUbKYAAAAASUVORK5CYII=")
#----------------------------------------------------------------------

class TestPanel(wx.Panel):
    def __init__(self, parent):
        wx.Panel.__init__(self, parent, -1)
        self.Bind(wx.EVT_SIZE, self.OnSize)

        self.tree = gizmos.TreeListCtrl(self, -1, style =
                                        wx.TR_DEFAULT_STYLE
                                        #| wx.TR_HAS_BUTTONS
                                        #| wx.TR_TWIST_BUTTONS
                                        #| wx.TR_ROW_LINES
                                        #| wx.TR_COLUMN_LINES
                                        #| wx.TR_NO_LINES 
                                        | wx.TR_FULL_ROW_HIGHLIGHT
                                        #| wx.TR_EDIT_LABELS
                                        #| wx.LC_EDIT_LABELS
                                   )

     
        # create some columns
        self.tree.AddColumn("Main column")
        self.tree.AddColumn("Column 1")
        self.tree.AddColumn("Column 2")
        self.tree.SetMainColumn(0) # the one with the tree in it...
        self.tree.SetColumnWidth(0, 175)


        self.tree.SetColumnEditable(0, True)
        self.tree.SetColumnEditable(1, True)
        self.tree.SetColumnEditable(2, True)
       # self.tree.SetColumnEditable(3, True)
        
        self.root = self.tree.AddRoot("The Root Item")
        self.tree.SetItemText(self.root, "col 1 root", 1)
        self.tree.SetItemText(self.root, "col 2 root", 2)
       

        for x in range(15):
            txt = "Item %d" % x
            child = self.tree.AppendItem(self.root, txt)
            self.tree.SetItemText(child, txt + "(c1)", 1)
            self.tree.SetItemText(child, txt + "(c2)", 2)
    
    def OnSize(self, evt):
        self.tree.SetSize(self.GetSize())


class testPanel1 ( wx.Panel ):
	
	def __init__( self, parent ):
		wx.Panel.__init__ ( self, parent, id = wx.ID_ANY, pos = wx.DefaultPosition, size = wx.Size( 500,300 ), style = wx.TAB_TRAVERSAL )
		
		bSizer17 = wx.BoxSizer( wx.VERTICAL )
		
		self.m_listbook4 = wx.Treebook( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LB_DEFAULT )
		self.m_panel53 = wx.Panel( self.m_listbook4, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		self.m_listbook4.AddPage( self.m_panel53, "a pageaaaaaaaaaaaaa", False )
		self.m_panel54 = wx.Panel( self.m_listbook4, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		self.m_listbook4.AddPage( self.m_panel54, "a page", False )
		
		bSizer17.Add( self.m_listbook4, 1, wx.EXPAND |wx.ALL, 5 )
		
		
		self.SetSizer( bSizer17 )
		self.Layout()
	
	def __del__( self ):
		pass

class mytestPanel(MainBase.testPanel):
    def __init__(self, parent):
        MainBase.testPanel.__init__(self,parent)


    def onChoice(self, event):

  #      help(event)
        num = event.GetInt()
        print "getint:", num
        print "GetSelection:", event.GetSelection()
    
       
        if num == 1:
            self.mainSizer.Hide(self.SizerIO)
            self.mainSizer.Show(self.sizeTimeDelay)

        else:
            self.mainSizer.Show(self.SizerIO)
            self.mainSizer.Hide(self.sizeTimeDelay)

        self.mainSizer.Layout()



class MyApp(wx.App):

    def __init__(self, redirect=True, filename=None):
        print "App __init__"
        wx.App.__init__(self, redirect, filename)
		
    def OnInit(self):
        print "OnInit"
        self.frame = wx.Frame(parent=None)
        
        self.frame.SetSize((1024,1000))
        self.SetTopWindow(self.frame)
        panel = mytestPanel(self.frame)
       

        newPanel = wx.Panel(panel, size=(100,200))

        #newPanel.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_CAPTIONTEXT ) )
        newPanel.SetBackgroundColour( (255,0,0,0) )


        #self.m_button14 = wx.Button( panel, wx.ID_ANY, "MyButton",(100,180), wx.DefaultSize,wx.NO_BORDER,name = "teset")
	
        self.testButton(panel)    

        panel.SetTransparent(0)
        
        panel.SetBackgroundColour( (255,0,0,0))

        #self.frame.SetTransparent(50)
        self.frame.Show()
        print    sys.stderr, "A pretend error message"
        return True

    def testButton(self,panel):
        self.m_button14 = wx.Button( panel, wx.ID_ANY, "MyButton", (200,200), wx.DefaultSize, wx.NO_BORDER|wx.NO_BORDER )
        #self.m_button14.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_HIGHLIGHT ) )  
        #self.m_button14.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_HIGHLIGHT ) )
        self.m_button14.SetToolTipString( "tooltip" )
        self.m_button14.SetHelpText( "help" )

       ## self.m_button15 = wx.Button( panel, wx.ID_ANY, "MyButton", (300,200), wx.DefaultSize, wx.NO_BORDER|wx.NO_BORDER )
        
        self.m_button15 = wx.Button( panel, wx.ID_ANY, "MyButton", (300,200), wx.DefaultSize, style = wx.NO_BORDER )
       
        #self.m_button15.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_CAPTIONTEXT ) )
        #self.m_button15.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_WINDOW ) )

        #self.m_button15.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_WINDOW ) )
        self.m_button15.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_WINDOW ) )
        self.m_button15.SetBackgroundColour((255,0,0))
        self.m_button15.SetDefault()  
        
        print self.m_button15.GetWindowBorderSize()
    
        collor = panel.GetBackgroundColour()



        self.m_bpButton3 = wx.BitmapButton( panel, wx.ID_ANY, wx.ArtProvider.GetBitmap( wx.ART_TICK_MARK, wx.ART_BUTTON ), (400,200), wx.DefaultSize, wx.BU_AUTODRAW )

        self.m_bpButton3.SetBitmapSelected( wx.ArtProvider.GetBitmap( wx.ART_REMOVABLE, wx.ART_MENU ) )
        self.m_bpButton3.SetBitmapFocus( wx.ArtProvider.GetBitmap( wx.ART_CROSS_MARK, wx.ART_BUTTON ) )
        self.m_bpButton3.SetBitmapHover( wx.ArtProvider.GetBitmap( wx.ART_TIP, wx.ART_BUTTON ) )


        self.testCommonBtn(panel)

        #self.m_button15.SetBackgroundColour( collor )

    def testCommonBtn(self, panel):


        b = buttons.GenButton(panel, -1, pos = (500,200),name='Genric Button')#基本的通用按钮  
       
        b = buttons.GenButton(panel, -1,  label='disabled Generic',pos = (500,290),name='disabled Generic')#无效的通用按钮  
        #b.Enable(False)  
          
        """
        b = buttons.GenButton(panel, -1,  pos = (500,400),name='bigger')#自定义尺寸和颜色的按钮  
        b.SetFont(wx.Font(20, wx.SWISS, wx.NORMAL, wx.BOLD, False))  
        b.SetBezelWidth(5)  
        b.SetBackgroundColour("Navy")  
        b.SetForegroundColour("white")  
        b.SetToolTipString("This is a BIG button...")  
        """        
        file = r"D:\workspace\myGitProj\init\my_app\image\btn1.png"
        file = r"D:\workspace\myGitProj\init\my_app\image\fugu.png"

        #file = r"D:\workspace\myGitProj\init\my_app\image\3.bmp"
        bmp = wx.Image(file).ConvertToBitmap()

        #bmp.SetMask(wx.Mask(bmp,(255,255,255,0))) 

       # img = bmp.ConvertToImage()

        #help(img)
        #img.Show()
        

        #help(bmp)
  


        #b =  platebtn.PlateButton(panel, -1,  pos = (470,300),bmp=Monkey.GetBitmap(), style =   platebtn.PB_STYLE_NOBG)#通用位图按钮  
        #b =  platebtn.PlateButton(panel, -1,  pos = (470,300),bmp=bmp, style =   platebtn.PB_STYLE_NOBG)#通用位图按钮  
        b =  MyGenBitmapButton(panel, -1,  pos = (470,300),bitmap=bmp, style =   wx.BORDER_NONE|wx.TRANSPARENT_WINDOW)#通用位图按钮  
       
        b.Enable(1)
        #print b.GetBackgroundMode()

        bc = panel.GetBackgroundColour()
       # b.SetBackgroundColour((255,0,0,0)) 

        print "can transpant:",b.CanSetTransparent()
 
        #b.SetTransparent(0)
        #b.SetBezelWidth(1) 



        b = sbbutton.SToggleButton(panel, -1,  pos = (450,600))
        #b = sbbutton.SBitmapButton(panel, -1, pos = (500,400),bitmap=bmp)#通用位图开关按钮  
        
        #bitmap = wx.BitmapFromImage(image)


       # b = buttons.GenBitmapTextButton(panel, -1, pos = (500,700),bitmap=bmp, name="Bitmapped Text",size=(175, 75))#位图文本按钮  
       # b.SetUseFocusIndicator(False)  
       
        #b = buttons.GenToggleButton(panel, -1, "Toggle Button")#通用开关按钮  
        

#PlateButton

    def OnExit(self):
        print "OnExit"
    
    def SetAppViewSelectPanel(self, panel):
        self.ViewSelectPanel = panel
        return
    
    def GetAppViewSelectPane(self):
        return self.ViewSelectPanel
    

class MyGenBitmapButton(buttons.GenBitmapButton):
    def __init__(self, parent, id=-1, bitmap=wx.NullBitmap,
                 pos = wx.DefaultPosition, size = wx.DefaultSize,
                 style = 0, validator = wx.DefaultValidator,
                 name = "genbutton"):
        self.parent = parent
        self.index = 0
        buttons.GenBitmapButton.__init__(self, parent, id, bitmap,pos , size,style , validator,name )
        
    def OnPaint2(self, event):
        (width, height) = self.GetClientSizeTuple()
        x1 = y1 = 0
        x2 = width-1
        y2 = height-1

        dc = wx.PaintDC(self)
        brush = self.GetBackgroundBrush(dc)
        if brush is not None:
            dc.SetBackground(brush)
            dc.Clear()

        self.DrawBezel(dc, x1, y1, x2, y2)
        self.DrawLabel(dc, width, height)
        if self.hasFocus and self.useFocusInd:
            self.DrawFocusIndicator(dc, width, height)

    def GetBackgroundBrush2(self, dc):
        if self.up:
            colBg = self.GetBackgroundColour()
            brush = wx.Brush(colBg, wx.SOLID)
            if self.style & wx.BORDER_NONE:
                myAttr = self.GetDefaultAttributes()
                parAttr = self.GetParent().GetDefaultAttributes()
                myDef = colBg == myAttr.colBg
                parDef = self.GetParent().GetBackgroundColour() == parAttr.colBg
                if myDef and parDef:
                    if wx.Platform == "__WXMAC__":
                        brush.MacSetTheme(1) # 1 == kThemeBrushDialogBackgroundActive
                    elif wx.Platform == "__WXMSW__":
                        if self.DoEraseBackground(dc):
                            brush = None
                elif myDef and not parDef:
                    colBg = self.GetParent().GetBackgroundColour()
                    brush = wx.Brush(colBg, wx.SOLID)
        else:
            # this line assumes that a pressed button should be hilighted with
            # a solid colour even if the background is supposed to be transparent
            brush = wx.Brush(self.faceDnClr, wx.SOLID)
        return brush
    def GetBackgroundBrush(self,dc):

        b = wx.Brush((255,0,0,0))
       
        return b

    
    def GetBg(self):
        x,y=self.GetPosition()
        xx,yy=self.GetSizeTuple()

        self.index += 1        
        print "x,y",x,y
        print "xx,yy",xx,yy
        print "index",self.index

        bmp = wx.EmptyBitmap(xx, yy)
        dc = wx.MemoryDC()
        dc.SelectObject(bmp)
        dc.Blit(x,y,xx,yy,wx.ScreenDC(),x,y)
        return bmp

    def OnPaint1(self, evt):
        x,y=self.GetPosition()
        dc = wx.ScreenDC()
        bmp = self.GetBg()
        brush = wx.BrushFromBitmap(bmp)
        dc.SetBackground(brush)
        orange = wx.Colour(255,132.0)
        dc.SetTextForeground(orange)
        dc.DrawText('Hello transparent window! This text is not transparent.', x+13, y+11) 

    def InitColours1(self):
        return
    def OnPaint(self, event):
        (width, height) = self.GetClientSizeTuple()
        x1 = y1 = 0
        x2 = width-1
        y2 = height-1
        
        print "onpaint"

        #help(event)

        #event.Skip()

        #dc = wx.ClientDC


       
        
        dc = wx.PaintDC(self)
        #return
        brush = self.GetBackgroundBrush(dc)
        if brush is not None:
            color =  brush.GetColour()
            brush.SetColour((255,255,0,0))
            dc.SetBackground(brush)
            #help(dc.GetBackground())
            #print dc.get            

            #dc.Clear()

       # self.DrawBezel(dc, x1, y1, x2, y2)
        self.DrawLabel(dc, width, height)
        if self.hasFocus and self.useFocusInd:
            #self.DrawFocusIndicator(dc, width, height)
            pass
        
        event.Skip()

    def GetBackgroundBrush(self, dc):
        if self.up:
            colBg = self.GetBackgroundColour()
            brush = wx.Brush(colBg, wx.SOLID)
            if self.style & wx.BORDER_NONE:
                myAttr = self.GetDefaultAttributes()
                parAttr = self.GetParent().GetDefaultAttributes()
                myDef = colBg == myAttr.colBg
                parDef = self.GetParent().GetBackgroundColour() == parAttr.colBg
                if myDef and parDef:
                    if wx.Platform == "__WXMAC__":
                        brush.MacSetTheme(1) # 1 == kThemeBrushDialogBackgroundActive
                    elif wx.Platform == "__WXMSW__":
                        if self.DoEraseBackground(dc):
                            brush = None
                elif myDef and not parDef:
                    colBg = self.GetParent().GetBackgroundColour()
                    brush = wx.Brush(colBg, wx.TRANSPARENT)
        else:
            # this line assumes that a pressed button should be hilighted with
            # a solid colour even if the background is supposed to be transparent
            brush = wx.Brush(self.faceDnClr, wx.TRANSPARENT)
        return brush

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
        #dc.Clear()
        
        #dc = wx.ClientDC(self)
        print wx.TRANSPARENT,dc.GetBackgroundMode()
        bmp = self.bmpLabel
        print "DrawLabel dc size= ",dc.GetSize()
        
        file = r"D:\workspace\myGitProj\init\my_app\image\fugu.png"

        #file = r"D:\workspace\myGitProj\init\my_app\image\3.bmp"
        bmp = wx.Image(file).ConvertToBitmap()
        dc.DrawBitmap(bmp, (width-bw)/2+dx, (height-bh)/2+dy, 1)

    def SetBackgroundColour(self, colour):

        return
        wx.PyControl.SetBackgroundColour(self, colour)
        self.InitColours()


    def SetForegroundColour(self, colour):
        return

    def _GetLabelSize1(self):
        return 10,10,0

if __name__ == '__main__':
    app = MyApp(redirect=False)
    print "before MainLoop"
    app.MainLoop()
    
    gl.app = app
    print "after MainLoop"
