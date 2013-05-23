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
from MyButton import *
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
        self.testBtn = None
        self.panel = panel
        newPanel = wx.Panel(panel, size=(100,200))

        #newPanel.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_CAPTIONTEXT ) )
        newPanel.SetBackgroundColour( (255,0,0,0) )


        #self.m_button14 = wx.Button( panel, wx.ID_ANY, "MyButton",(100,180), wx.DefaultSize,wx.NO_BORDER,name = "teset")
	
        self.testButton(panel) 

        panel.SetDoubleBuffered(1) 

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
      
 

        self.index = 1


        self.testBtn =  MyGenBitmapButton(panel, -1,  pos = (470,300), style =   wx.BORDER_NONE|wx.TRANSPARENT_WINDOW)#通用位图按钮  
        
        self.testBtn.Enable(1)
        self.testBtn.Bind( wx.EVT_BUTTON, self.onButton )
        self.Bind(wx.EVT_MOUSE_EVENTS,           self.OnMouse)
        self.testBtn.loadImageLabel(btn_red_up)
        self.testBtn.loadImageSelected(btn_red_down)


        self.testBtn1 =  MyGenBitmapToggleButton(panel, -1,  pos = (520,300), style =   wx.BORDER_NONE|wx.TRANSPARENT_WINDOW)#通用位图按钮  
        
        self.testBtn1.Enable(1)
        self.testBtn1.Bind( wx.EVT_BUTTON, self.onButton )
        self.Bind(wx.EVT_MOUSE_EVENTS,           self.OnMouse)



       
        self.testBtn2 =  MyGenBitmapToggleButton(panel, -1,  pos = (520,300), style =   wx.BORDER_NONE|wx.TRANSPARENT_WINDOW)#通用位图按钮  
        
        self.testBtn2.Enable(1)
        self.testBtn2.Bind( wx.EVT_BUTTON, self.onButton )
        self.testBtn2.loadImageLabel(btn_on)
        self.testBtn2.loadImageSelected(btn_off)
        self.testBtn2.setSizeFitImage()




         
        self.testBtn3 =  MyGenBitmapToggleButton(panel, -1,  pos = (520,300), style =   wx.BORDER_NONE|wx.TRANSPARENT_WINDOW)#通用位图按钮  
        
        self.testBtn3.Enable(1)
        self.testBtn3.Bind( wx.EVT_BUTTON, self.onButton )
        self.testBtn3.loadImageLabel(circle_btn_on)
        self.testBtn3.loadImageSelected(circle_btn_off)
        self.testBtn3.setSizeFitImage()





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
    def OnMouse(self, event):


        if event.GetEventObject() is not self:
            pass

        if event.LeftDown():

            print "left",(event.GetX(),event.GetY())

            print "getButton",event.GetButton()
            btn = event.GetEventObject()
            #help(event)
            btn.SetMoveBegin((event.GetX(),event.GetY()))
          

        elif event.LeftUp():
            print "left up"
            self.SetMoveEnd()
        elif event.RightDown():
            print "reight do",(event.GetX(),event.GetY())
            self.removeSelectedSprite()   


        elif event.Dragging():
            print "left drag", (event.GetX(),event.GetY())

            btn = event.GetEventObject()

            #print btn

            btn.SetMoving((event.GetX(),event.GetY()))

        event.Skip()
    def onMotion1(self,event):
        
        #print event

        print "onMothion"
        if event.Dragging():
            print "dragging"

            print self.testBtn.GetPosition()
            pos = event.GetPosition()
            print pos
            self.testBtn.Move(pos)
            self.panel.Refresh()    
    
  
    def onButton(self,event):
        print "onButton"
        x = self.index
        self.index += 1
        #self.testBtn.MoveXY(470+x,300)
       
        #self.testBtn.Refresh()
        #self.panel.Refresh()
        #event.Skip()

    def onLeft(self,event):
        print "onLeft:",event.GetId()
            
        #event.pass() 
#PlateButton

    def OnExit(self):
        print "OnExit"
    
    def SetAppViewSelectPanel(self, panel):
        self.ViewSelectPanel = panel
        return
    
    def GetAppViewSelectPane(self):
        return self.ViewSelectPanel
    


if __name__ == '__main__':
    app = MyApp(redirect=False)
    print "before MainLoop"
    app.MainLoop()
    
    gl.app = app
    print "after MainLoop"
