# -*- coding: utf-8 -*- 

###########################################################################
## Python code generated with wxFormBuilder (version Oct  8 2012)
## http://www.wxformbuilder.org/
##
## PLEASE DO "NOT" EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc

import gettext
_ = gettext.gettext

###########################################################################
## Class FrameBase
###########################################################################

class FrameBase ( wx.Frame ):
	
	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = _(u"my app"), pos = wx.DefaultPosition, size = wx.Size( 771,447 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )
		
		self.SetSizeHintsSz( wx.DefaultSize, wx.DefaultSize )
		
		self.m_statusBar1 = self.CreateStatusBar( 1, wx.ST_SIZEGRIP, wx.ID_ANY )
		self.m_menubar1 = wx.MenuBar( 0 )
		self.m_menu1 = wx.Menu()
		self.m_menubar1.Append( self.m_menu1, _(u"File") ) 
		
		self.m_menu2 = wx.Menu()
		self.m_menubar1.Append( self.m_menu2, _(u"Edit") ) 
		
		self.SetMenuBar( self.m_menubar1 )
		
		self.m_toolBar2 = self.CreateToolBar( wx.TB_HORIZONTAL, wx.ID_ANY )
		self.m_toolBar2.SetToolSeparation( 10 )
		self.m_toolBar2.AddLabelTool( wx.ID_ANY, _(u"tool"), wx.ArtProvider.GetBitmap( wx.ART_ADD_BOOKMARK, wx.ART_MENU ), wx.NullBitmap, wx.ITEM_NORMAL, _(u"添加设备"), wx.EmptyString, None ) 
		
		self.m_toolBar2.AddLabelTool( wx.ID_ANY, _(u"tool"), wx.ArtProvider.GetBitmap( wx.ART_WARNING, wx.ART_TOOLBAR ), wx.NullBitmap, wx.ITEM_NORMAL, wx.EmptyString, wx.EmptyString, None ) 
		
		self.m_toolBar2.Realize() 
		
		
		self.Centre( wx.BOTH )
		
		# Connect Events
		self.Bind( wx.EVT_TOOL, self.addDevice, id = wx.ID_ANY )
	
	def __del__( self ):
		pass
	
	
	# Virtual event handlers, overide them in your derived class
	def addDevice( self, event ):
		event.Skip()
	

###########################################################################
## Class PanelBase
###########################################################################

class PanelBase ( wx.Panel ):
	
	def __init__( self, parent ):
		wx.Panel.__init__ ( self, parent, id = wx.ID_ANY, pos = wx.DefaultPosition, size = wx.Size( 947,485 ), style = wx.TAB_TRAVERSAL )
		
		self.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_WINDOW ) )
		
		fgSizer2 = wx.FlexGridSizer( 0, 2, 0, 0 )
		fgSizer2.SetFlexibleDirection( wx.BOTH )
		fgSizer2.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )
		
		self.m_panel16 = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.Size( 200,300 ), wx.TAB_TRAVERSAL )
		self.m_panel16.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_CAPTIONTEXT ) )
		
		fgSizer2.Add( self.m_panel16, 1, wx.EXPAND |wx.ALL, 5 )
		
		self.m_panel17 = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		self.m_panel17.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_3DLIGHT ) )
		
		fgSizer2.Add( self.m_panel17, 1, wx.EXPAND |wx.ALL, 5 )
		
		self.m_panel18 = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		self.m_panel18.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_SCROLLBAR ) )
		
		fgSizer2.Add( self.m_panel18, 1, wx.EXPAND |wx.ALL, 5 )
		
		self.m_listCtrl2 = wx.ListCtrl( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LC_EDIT_LABELS|wx.LC_ICON )
		self.m_listCtrl2.SetHelpText( _(u"sdfsfsdf") )
		
		fgSizer2.Add( self.m_listCtrl2, 0, wx.ALL, 5 )
		
		self.m_panel20 = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		fgSizer2.Add( self.m_panel20, 1, wx.EXPAND |wx.ALL, 5 )
		
		self.m_panel19 = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		self.m_panel19.SetBackgroundColour( wx.Colour( 0, 255, 0 ) )
		
		fgSizer2.Add( self.m_panel19, 1, wx.EXPAND |wx.ALL, 5 )
		
		self.m_panel21 = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		fgSizer2.Add( self.m_panel21, 1, wx.EXPAND |wx.ALL, 5 )
		
		self.m_panel22 = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		fgSizer2.Add( self.m_panel22, 1, wx.EXPAND |wx.ALL, 5 )
		
		self.m_panel23 = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		fgSizer2.Add( self.m_panel23, 1, wx.EXPAND |wx.ALL, 5 )
		
		self.m_panel24 = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		fgSizer2.Add( self.m_panel24, 1, wx.EXPAND |wx.ALL, 5 )
		
		self.m_panel25 = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		fgSizer2.Add( self.m_panel25, 1, wx.EXPAND |wx.ALL, 5 )
		
		
		self.SetSizer( fgSizer2 )
		self.Layout()
	
	def __del__( self ):
		pass
	

###########################################################################
## Class MyPanel2
###########################################################################

class MyPanel2 ( wx.Panel ):
	
	def __init__( self, parent ):
		wx.Panel.__init__ ( self, parent, id = wx.ID_ANY, pos = wx.DefaultPosition, size = wx.Size( 500,300 ), style = wx.TAB_TRAVERSAL )
		
		bSizer1 = wx.BoxSizer( wx.HORIZONTAL )
		
		bSizer1.SetMinSize( wx.Size( 100,200 ) ) 
		self.m_splitter5 = wx.SplitterWindow( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.SP_LIVE_UPDATE )
		self.m_splitter5.SetSashGravity( 0 )
		self.m_splitter5.Bind( wx.EVT_IDLE, self.m_splitter5OnIdle )
		
		self.m_splitter5.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_INFOTEXT ) )
		
		self.m_panel21 = wx.Panel( self.m_splitter5, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer4 = wx.BoxSizer( wx.VERTICAL )
		
		self.m_treeCtrl12 = wx.TreeCtrl( self.m_panel21, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TR_DEFAULT_STYLE|wx.HSCROLL )
		self.m_treeCtrl12.SetMinSize( wx.Size( 200,400 ) )
		
		bSizer4.Add( self.m_treeCtrl12, 0, wx.ALL, 5 )
		
		
		self.m_panel21.SetSizer( bSizer4 )
		self.m_panel21.Layout()
		bSizer4.Fit( self.m_panel21 )
		self.m_panel22 = wx.Panel( self.m_splitter5, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		self.m_splitter5.SplitVertically( self.m_panel21, self.m_panel22, 264 )
		bSizer1.Add( self.m_splitter5, 1, wx.EXPAND, 5 )
		
		
		self.SetSizer( bSizer1 )
		self.Layout()
	
	def __del__( self ):
		pass
	
	def m_splitter5OnIdle( self, event ):
		self.m_splitter5.SetSashPosition( 264 )
		self.m_splitter5.Unbind( wx.EVT_IDLE )
	

###########################################################################
## Class EmptyPanel
###########################################################################

class EmptyPanel ( wx.Panel ):
	
	def __init__( self, parent ):
		wx.Panel.__init__ ( self, parent, id = wx.ID_ANY, pos = wx.DefaultPosition, size = wx.Size( 500,300 ), style = wx.TAB_TRAVERSAL )
		
		self.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_GRAYTEXT ) )
		
	
	def __del__( self ):
		pass
	

###########################################################################
## Class SplitterPanelBase
###########################################################################

class SplitterPanelBase ( wx.Panel ):
	
	def __init__( self, parent ):
		wx.Panel.__init__ ( self, parent, id = wx.ID_ANY, pos = wx.DefaultPosition, size = wx.Size( 500,300 ), style = wx.TAB_TRAVERSAL )
		
		bSizer6 = wx.BoxSizer( wx.VERTICAL )
		
		self.m_splitter4 = wx.SplitterWindow( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.SP_3D|wx.SP_LIVE_UPDATE )
		self.m_splitter4.Bind( wx.EVT_IDLE, self.m_splitter4OnIdle )
		
		self.viewSelectPanel = wx.Panel( self.m_splitter4, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.NO_BORDER|wx.TAB_TRAVERSAL )
		self.viewSelectPanel.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_BACKGROUND ) )
		
		self.viewContainPanel = wx.Panel( self.m_splitter4, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.SUNKEN_BORDER|wx.TAB_TRAVERSAL )
		bSizer12 = wx.BoxSizer( wx.VERTICAL )
		
		self.m_splitter6 = wx.SplitterWindow( self.viewContainPanel, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.SP_3D )
		self.m_splitter6.SetSashSize( 5 )
		self.m_splitter6.Bind( wx.EVT_IDLE, self.m_splitter6OnIdle )
		
		self.viewPanel = wx.Panel( self.m_splitter6, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		self.viewPanel.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_GRAYTEXT ) )
		
		self.detailPanel = wx.Panel( self.m_splitter6, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		self.m_splitter6.SplitHorizontally( self.viewPanel, self.detailPanel, 0 )
		bSizer12.Add( self.m_splitter6, 1, wx.EXPAND, 5 )
		
		
		self.viewContainPanel.SetSizer( bSizer12 )
		self.viewContainPanel.Layout()
		bSizer12.Fit( self.viewContainPanel )
		self.m_splitter4.SplitVertically( self.viewSelectPanel, self.viewContainPanel, 0 )
		bSizer6.Add( self.m_splitter4, 1, wx.EXPAND, 5 )
		
		
		self.SetSizer( bSizer6 )
		self.Layout()
	
	def __del__( self ):
		pass
	
	def m_splitter4OnIdle( self, event ):
		self.m_splitter4.SetSashPosition( 0 )
		self.m_splitter4.Unbind( wx.EVT_IDLE )
	
	def m_splitter6OnIdle( self, event ):
		self.m_splitter6.SetSashPosition( 0 )
		self.m_splitter6.Unbind( wx.EVT_IDLE )
	

###########################################################################
## Class Panel_AddDevice_Base
###########################################################################

class Panel_AddDevice_Base ( wx.Panel ):
	
	def __init__( self, parent ):
		wx.Panel.__init__ ( self, parent, id = wx.ID_ANY, pos = wx.DefaultPosition, size = wx.Size( 500,300 ), style = wx.TAB_TRAVERSAL )
		
		bSizer7 = wx.BoxSizer( wx.VERTICAL )
		
		self.m_splitter5 = wx.SplitterWindow( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.SP_3D )
		self.m_splitter5.Bind( wx.EVT_IDLE, self.m_splitter5OnIdle )
		
		self.m_panel17 = wx.Panel( self.m_splitter5, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		self.m_panel17.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_WINDOW ) )
		self.m_panel17.SetMinSize( wx.Size( 100,100 ) )
		
		bSizer19 = wx.BoxSizer( wx.VERTICAL )
		
		self.m_staticText20 = wx.StaticText( self.m_panel17, wx.ID_ANY, _(u"设备信息"), wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText20.Wrap( -1 )
		self.m_staticText20.SetFont( wx.Font( 18, 74, 90, 90, False, "Tahoma" ) )
		
		bSizer19.Add( self.m_staticText20, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALIGN_LEFT, 5 )
		
		self.m_staticline1 = wx.StaticLine( self.m_panel17, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_HORIZONTAL )
		bSizer19.Add( self.m_staticline1, 0, wx.EXPAND |wx.ALL, 5 )
		
		fgSizer2 = wx.FlexGridSizer( 0, 2, 0, 0 )
		fgSizer2.AddGrowableCol( 1 )
		fgSizer2.SetFlexibleDirection( wx.BOTH )
		fgSizer2.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )
		
		self.m_staticText21 = wx.StaticText( self.m_panel17, wx.ID_ANY, _(u"名称："), wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText21.Wrap( -1 )
		fgSizer2.Add( self.m_staticText21, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALIGN_RIGHT, 5 )
		
		self.m_textCtrl21 = wx.TextCtrl( self.m_panel17, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer2.Add( self.m_textCtrl21, 0, wx.ALL|wx.EXPAND, 5 )
		
		self.m_staticText23 = wx.StaticText( self.m_panel17, wx.ID_ANY, _(u"位置："), wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText23.Wrap( -1 )
		fgSizer2.Add( self.m_staticText23, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALIGN_RIGHT, 5 )
		
		self.m_textCtrl22 = wx.TextCtrl( self.m_panel17, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer2.Add( self.m_textCtrl22, 0, wx.ALL|wx.EXPAND, 5 )
		
		self.m_staticText24 = wx.StaticText( self.m_panel17, wx.ID_ANY, _(u"描述："), wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText24.Wrap( -1 )
		fgSizer2.Add( self.m_staticText24, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALIGN_RIGHT, 5 )
		
		self.m_textCtrl23 = wx.TextCtrl( self.m_panel17, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer2.Add( self.m_textCtrl23, 0, wx.ALL|wx.EXPAND, 5 )
		
		
		bSizer19.Add( fgSizer2, 1, wx.EXPAND, 5 )
		
		
		self.m_panel17.SetSizer( bSizer19 )
		self.m_panel17.Layout()
		bSizer19.Fit( self.m_panel17 )
		self.m_panel18 = wx.Panel( self.m_splitter5, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		self.m_panel18.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_HIGHLIGHT ) )
		
		self.m_splitter5.SplitVertically( self.m_panel17, self.m_panel18, 0 )
		bSizer7.Add( self.m_splitter5, 1, wx.EXPAND, 5 )
		
		
		self.SetSizer( bSizer7 )
		self.Layout()
	
	def __del__( self ):
		pass
	
	def m_splitter5OnIdle( self, event ):
		self.m_splitter5.SetSashPosition( 0 )
		self.m_splitter5.Unbind( wx.EVT_IDLE )
	

