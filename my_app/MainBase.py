# -*- coding: utf-8 -*- 

###########################################################################
## Python code generated with wxFormBuilder (version Oct  8 2012)
## http://www.wxformbuilder.org/
##
## PLEASE DO "NOT" EDIT THIS FILE!
###########################################################################

from MyClass import CheckListCtrl
from wx.gizmos import TreeListCtrl
import wx
import wx.xrc

import gettext
_ = gettext.gettext

ctrl_new = 1000
ctrl_del = 1001
ctrl_up = 1002
ctrl_down = 1003
action_new = 1004
action_del = 1005
action_up = 1006
action_down = 1007

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
## Class Panel_AddDevice_Base1
###########################################################################

class Panel_AddDevice_Base1 ( wx.Panel ):
	
	def __init__( self, parent ):
		wx.Panel.__init__ ( self, parent, id = wx.ID_ANY, pos = wx.DefaultPosition, size = wx.Size( 685,303 ), style = wx.TAB_TRAVERSAL )
		
		fgSizer4 = wx.FlexGridSizer( 2, 1, 0, 0 )
		fgSizer4.AddGrowableCol( 0 )
		fgSizer4.AddGrowableCol( 1 )
		fgSizer4.AddGrowableRow( 0 )
		fgSizer4.SetFlexibleDirection( wx.BOTH )
		fgSizer4.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )
		
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
		
		self.label_name = wx.StaticText( self.m_panel17, wx.ID_ANY, _(u"Name:"), wx.DefaultPosition, wx.DefaultSize, 0 )
		self.label_name.Wrap( -1 )
		fgSizer2.Add( self.label_name, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALIGN_RIGHT, 5 )
		
		self.text_name = wx.TextCtrl( self.m_panel17, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer2.Add( self.text_name, 0, wx.ALL|wx.EXPAND, 5 )
		
		self.label_pos = wx.StaticText( self.m_panel17, wx.ID_ANY, _(u"Position:"), wx.DefaultPosition, wx.DefaultSize, 0 )
		self.label_pos.Wrap( -1 )
		fgSizer2.Add( self.label_pos, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALIGN_RIGHT, 5 )
		
		self.text_pos = wx.TextCtrl( self.m_panel17, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer2.Add( self.text_pos, 0, wx.ALL|wx.EXPAND, 5 )
		
		self.label_desc = wx.StaticText( self.m_panel17, wx.ID_ANY, _(u"Description:"), wx.DefaultPosition, wx.DefaultSize, 0 )
		self.label_desc.Wrap( -1 )
		fgSizer2.Add( self.label_desc, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALIGN_RIGHT, 5 )
		
		self.text_desc = wx.TextCtrl( self.m_panel17, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer2.Add( self.text_desc, 0, wx.ALL|wx.EXPAND, 5 )
		
		
		bSizer19.Add( fgSizer2, 1, wx.EXPAND, 5 )
		
		
		self.m_panel17.SetSizer( bSizer19 )
		self.m_panel17.Layout()
		bSizer19.Fit( self.m_panel17 )
		self.m_panel18 = wx.Panel( self.m_splitter5, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		self.m_panel18.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_HIGHLIGHT ) )
		
		fgSizer5 = wx.FlexGridSizer( 2, 1, 0, 0 )
		fgSizer5.AddGrowableCol( 0 )
		fgSizer5.AddGrowableCol( 1 )
		fgSizer5.AddGrowableRow( 1 )
		fgSizer5.SetFlexibleDirection( wx.BOTH )
		fgSizer5.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )
		
		self.m_panel23 = wx.Panel( self.m_panel18, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer7 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.m_button8 = wx.Button( self.m_panel23, wx.ID_ANY, _(u"Add"), wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer7.Add( self.m_button8, 0, wx.ALL, 5 )
		
		self.m_button9 = wx.Button( self.m_panel23, wx.ID_ANY, _(u"Delete"), wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer7.Add( self.m_button9, 0, wx.ALL, 5 )
		
		
		self.m_panel23.SetSizer( bSizer7 )
		self.m_panel23.Layout()
		bSizer7.Fit( self.m_panel23 )
		fgSizer5.Add( self.m_panel23, 1, wx.EXPAND |wx.ALL, 5 )
		
		self.list = CheckListCtrl( self.m_panel18, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LC_REPORT )
		fgSizer5.Add( self.list, 0, wx.EXPAND|wx.ALL, 5 )
		
		
		self.m_panel18.SetSizer( fgSizer5 )
		self.m_panel18.Layout()
		fgSizer5.Fit( self.m_panel18 )
		self.m_splitter5.SplitVertically( self.m_panel17, self.m_panel18, 251 )
		fgSizer4.Add( self.m_splitter5, 1, wx.EXPAND, 5 )
		
		self.m_panel27 = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		gSizer3 = wx.GridSizer( 0, 2, 0, 0 )
		
		self.m_button6 = wx.Button( self.m_panel27, wx.ID_ANY, _(u"Apply"), wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer3.Add( self.m_button6, 0, wx.ALIGN_RIGHT|wx.ALL, 5 )
		
		self.m_button7 = wx.Button( self.m_panel27, wx.ID_ANY, _(u"Cancel"), wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer3.Add( self.m_button7, 0, wx.ALIGN_LEFT|wx.ALL, 5 )
		
		
		self.m_panel27.SetSizer( gSizer3 )
		self.m_panel27.Layout()
		gSizer3.Fit( self.m_panel27 )
		fgSizer4.Add( self.m_panel27, 1, wx.EXPAND |wx.ALL, 5 )
		
		
		self.SetSizer( fgSizer4 )
		self.Layout()
		
		# Connect Events
		self.m_button8.Bind( wx.EVT_BUTTON, self.onAddModule )
		self.m_button9.Bind( wx.EVT_BUTTON, self.onDeleteModule )
		self.list.Bind( wx.EVT_LIST_ITEM_DESELECTED, self.OnItemDeselected )
		self.list.Bind( wx.EVT_LIST_ITEM_SELECTED, self.OnItemSelected )
		self.m_button6.Bind( wx.EVT_BUTTON, self.onApply )
		self.m_button7.Bind( wx.EVT_BUTTON, self.onCancel )
	
	def __del__( self ):
		pass
	
	
	# Virtual event handlers, overide them in your derived class
	def onAddModule( self, event ):
		event.Skip()
	
	def onDeleteModule( self, event ):
		event.Skip()
	
	def OnItemDeselected( self, event ):
		event.Skip()
	
	def OnItemSelected( self, event ):
		event.Skip()
	
	def onApply( self, event ):
		event.Skip()
	
	def onCancel( self, event ):
		event.Skip()
	
	def m_splitter5OnIdle( self, event ):
		self.m_splitter5.SetSashPosition( 251 )
		self.m_splitter5.Unbind( wx.EVT_IDLE )
	

###########################################################################
## Class Panel_AddModule_Base
###########################################################################

class Panel_AddModule_Base ( wx.Panel ):
	
	def __init__( self, parent ):
		wx.Panel.__init__ ( self, parent, id = wx.ID_ANY, pos = wx.DefaultPosition, size = wx.Size( 500,300 ), style = wx.TAB_TRAVERSAL )
		
		fgSizer10 = wx.FlexGridSizer( 2, 1, 0, 0 )
		fgSizer10.AddGrowableCol( 0 )
		fgSizer10.AddGrowableRow( 0 )
		fgSizer10.SetFlexibleDirection( wx.BOTH )
		fgSizer10.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )
		
		gSizer6 = wx.GridSizer( 0, 2, 0, 0 )
		
		self.m_staticText5 = wx.StaticText( self, wx.ID_ANY, _(u"名称:"), wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText5.Wrap( -1 )
		gSizer6.Add( self.m_staticText5, 0, wx.ALIGN_RIGHT|wx.ALL, 5 )
		
		self.text_name = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer6.Add( self.text_name, 0, wx.ALL|wx.EXPAND, 5 )
		
		self.m_staticText7 = wx.StaticText( self, wx.ID_ANY, _(u"I/O:"), wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText7.Wrap( -1 )
		gSizer6.Add( self.m_staticText7, 0, wx.ALIGN_RIGHT|wx.ALL, 5 )
		
		self.text_io = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer6.Add( self.text_io, 0, wx.ALIGN_LEFT|wx.ALL|wx.EXPAND, 5 )
		
		self.m_staticText6 = wx.StaticText( self, wx.ID_ANY, _(u"类型:"), wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText6.Wrap( -1 )
		gSizer6.Add( self.m_staticText6, 0, wx.ALIGN_RIGHT|wx.ALL, 5 )
		
		choiceChoices = []
		self.choice = wx.Choice( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, choiceChoices, 0 )
		self.choice.SetSelection( 0 )
		gSizer6.Add( self.choice, 0, wx.ALIGN_LEFT|wx.ALL|wx.EXPAND, 5 )
		
		
		fgSizer10.Add( gSizer6, 1, 0, 5 )
		
		gSizer3 = wx.GridSizer( 0, 2, 0, 0 )
		
		self.m_button12 = wx.Button( self, wx.ID_ANY, _(u"Apply"), wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer3.Add( self.m_button12, 0, wx.ALIGN_RIGHT|wx.ALL, 5 )
		
		self.m_button13 = wx.Button( self, wx.ID_ANY, _(u"Cancel"), wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer3.Add( self.m_button13, 0, wx.ALIGN_LEFT|wx.ALL, 5 )
		
		
		fgSizer10.Add( gSizer3, 1, wx.ALIGN_CENTER, 5 )
		
		
		self.SetSizer( fgSizer10 )
		self.Layout()
		
		# Connect Events
		self.choice.Bind( wx.EVT_CHOICE, self.onChoice )
		self.m_button12.Bind( wx.EVT_BUTTON, self.onApply )
		self.m_button13.Bind( wx.EVT_BUTTON, self.onCancel )
	
	def __del__( self ):
		pass
	
	
	# Virtual event handlers, overide them in your derived class
	def onChoice( self, event ):
		event.Skip()
	
	def onApply( self, event ):
		event.Skip()
	
	def onCancel( self, event ):
		event.Skip()
	

###########################################################################
## Class Panel_AddDevice_Base
###########################################################################

class Panel_AddDevice_Base ( wx.Panel ):
	
	def __init__( self, parent ):
		wx.Panel.__init__ ( self, parent, id = wx.ID_ANY, pos = wx.DefaultPosition, size = wx.Size( 698,429 ), style = wx.TAB_TRAVERSAL )
		
		fgSizer4 = wx.FlexGridSizer( 2, 1, 0, 0 )
		fgSizer4.AddGrowableCol( 0 )
		fgSizer4.AddGrowableCol( 1 )
		fgSizer4.AddGrowableRow( 0 )
		fgSizer4.SetFlexibleDirection( wx.BOTH )
		fgSizer4.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )
		
		bSizer18 = wx.BoxSizer( wx.VERTICAL )
		
		self.m_notebook4 = wx.Notebook( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_panel171 = wx.Panel( self.m_notebook4, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		self.m_panel171.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_WINDOW ) )
		self.m_panel171.SetMinSize( wx.Size( 100,100 ) )
		
		bSizer191 = wx.BoxSizer( wx.VERTICAL )
		
		self.m_staticText201 = wx.StaticText( self.m_panel171, wx.ID_ANY, _(u"设备信息"), wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText201.Wrap( -1 )
		self.m_staticText201.SetFont( wx.Font( 18, 74, 90, 90, False, "Tahoma" ) )
		
		bSizer191.Add( self.m_staticText201, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALIGN_LEFT, 5 )
		
		self.m_staticline11 = wx.StaticLine( self.m_panel171, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_HORIZONTAL )
		bSizer191.Add( self.m_staticline11, 0, wx.EXPAND |wx.ALL, 5 )
		
		fgSizer21 = wx.FlexGridSizer( 0, 2, 0, 0 )
		fgSizer21.AddGrowableCol( 1 )
		fgSizer21.SetFlexibleDirection( wx.BOTH )
		fgSizer21.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )
		
		self.label_name = wx.StaticText( self.m_panel171, wx.ID_ANY, _(u"Name:"), wx.DefaultPosition, wx.DefaultSize, 0 )
		self.label_name.Wrap( -1 )
		fgSizer21.Add( self.label_name, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALIGN_RIGHT, 5 )
		
		self.text_name = wx.TextCtrl( self.m_panel171, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer21.Add( self.text_name, 0, wx.ALL|wx.EXPAND, 5 )
		
		self.label_pos = wx.StaticText( self.m_panel171, wx.ID_ANY, _(u"Position:"), wx.DefaultPosition, wx.DefaultSize, 0 )
		self.label_pos.Wrap( -1 )
		fgSizer21.Add( self.label_pos, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALIGN_RIGHT, 5 )
		
		self.text_pos = wx.TextCtrl( self.m_panel171, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer21.Add( self.text_pos, 0, wx.ALL|wx.EXPAND, 5 )
		
		self.label_desc = wx.StaticText( self.m_panel171, wx.ID_ANY, _(u"Description:"), wx.DefaultPosition, wx.DefaultSize, 0 )
		self.label_desc.Wrap( -1 )
		fgSizer21.Add( self.label_desc, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALIGN_RIGHT, 5 )
		
		self.text_desc = wx.TextCtrl( self.m_panel171, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer21.Add( self.text_desc, 0, wx.ALL|wx.EXPAND, 5 )
		
		
		bSizer191.Add( fgSizer21, 1, wx.EXPAND, 5 )
		
		
		self.m_panel171.SetSizer( bSizer191 )
		self.m_panel171.Layout()
		bSizer191.Fit( self.m_panel171 )
		self.m_notebook4.AddPage( self.m_panel171, _(u"基本信息"), False )
		self.m_panel181 = wx.Panel( self.m_notebook4, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		self.m_panel181.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_WINDOW ) )
		
		fgSizer51 = wx.FlexGridSizer( 2, 1, 0, 0 )
		fgSizer51.AddGrowableCol( 0 )
		fgSizer51.AddGrowableCol( 1 )
		fgSizer51.AddGrowableRow( 1 )
		fgSizer51.SetFlexibleDirection( wx.BOTH )
		fgSizer51.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )
		
		self.m_panel231 = wx.Panel( self.m_panel181, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.NO_BORDER|wx.TAB_TRAVERSAL )
		bSizer71 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.m_button81 = wx.Button( self.m_panel231, wx.ID_ANY, _(u"Add"), wx.DefaultPosition, wx.DefaultSize, 0|wx.NO_BORDER )
		bSizer71.Add( self.m_button81, 0, wx.TOP|wx.LEFT, 5 )
		
		self.m_button91 = wx.Button( self.m_panel231, wx.ID_ANY, _(u"Delete"), wx.DefaultPosition, wx.DefaultSize, 0|wx.NO_BORDER )
		bSizer71.Add( self.m_button91, 0, wx.TOP|wx.LEFT, 5 )
		
		
		self.m_panel231.SetSizer( bSizer71 )
		self.m_panel231.Layout()
		bSizer71.Fit( self.m_panel231 )
		fgSizer51.Add( self.m_panel231, 1, wx.EXPAND |wx.ALL, 0 )
		
		self.list = CheckListCtrl( self.m_panel181, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LC_REPORT|wx.NO_BORDER )
		fgSizer51.Add( self.list, 0, wx.EXPAND|wx.ALL, 5 )
		
		
		self.m_panel181.SetSizer( fgSizer51 )
		self.m_panel181.Layout()
		fgSizer51.Fit( self.m_panel181 )
		self.m_notebook4.AddPage( self.m_panel181, _(u"输入输出"), False )
		self.m_panel75 = wx.Panel( self.m_notebook4, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		fgSizer511 = wx.FlexGridSizer( 2, 1, 0, 0 )
		fgSizer511.AddGrowableCol( 0 )
		fgSizer511.AddGrowableCol( 1 )
		fgSizer511.AddGrowableRow( 1 )
		fgSizer511.SetFlexibleDirection( wx.BOTH )
		fgSizer511.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )
		
		self.m_panel2311 = wx.Panel( self.m_panel75, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.NO_BORDER|wx.TAB_TRAVERSAL )
		bSizer711 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.m_button811 = wx.Button( self.m_panel2311, wx.ID_ANY, _(u"Add"), wx.DefaultPosition, wx.DefaultSize, 0|wx.NO_BORDER )
		bSizer711.Add( self.m_button811, 0, wx.TOP|wx.LEFT, 5 )
		
		self.m_button911 = wx.Button( self.m_panel2311, wx.ID_ANY, _(u"Delete"), wx.DefaultPosition, wx.DefaultSize, 0|wx.NO_BORDER )
		bSizer711.Add( self.m_button911, 0, wx.TOP|wx.LEFT, 5 )
		
		
		self.m_panel2311.SetSizer( bSizer711 )
		self.m_panel2311.Layout()
		bSizer711.Fit( self.m_panel2311 )
		fgSizer511.Add( self.m_panel2311, 1, wx.EXPAND |wx.ALL, 0 )
		
		self.list1 = CheckListCtrl( self.m_panel75, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LC_REPORT|wx.NO_BORDER )
		fgSizer511.Add( self.list1, 0, wx.EXPAND|wx.ALL, 5 )
		
		
		self.m_panel75.SetSizer( fgSizer511 )
		self.m_panel75.Layout()
		fgSizer511.Fit( self.m_panel75 )
		self.m_notebook4.AddPage( self.m_panel75, _(u"控制"), False )
		self.m_panel97 = wx.Panel( self.m_notebook4, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer33 = wx.BoxSizer( wx.VERTICAL )
		
		self.m_splitter9 = wx.SplitterWindow( self.m_panel97, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.SP_3D )
		self.m_splitter9.Bind( wx.EVT_IDLE, self.m_splitter9OnIdle )
		
		self.m_panel80 = wx.Panel( self.m_splitter9, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		fgSizer34 = wx.FlexGridSizer( 2, 0, 0, 0 )
		fgSizer34.AddGrowableCol( 0 )
		fgSizer34.AddGrowableCol( 1 )
		fgSizer34.AddGrowableRow( 1 )
		fgSizer34.SetFlexibleDirection( wx.BOTH )
		fgSizer34.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )
		
		self.ctrl_toolbar = wx.ToolBar( self.m_panel80, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TB_HORIZONTAL ) 
		self.ctrl_toolbar.AddLabelTool( ctrl_new, _(u"tool"), wx.ArtProvider.GetBitmap( wx.ART_NEW, wx.ART_TOOLBAR ), wx.NullBitmap, wx.ITEM_NORMAL, wx.EmptyString, wx.EmptyString, None ) 
		
		self.ctrl_toolbar.AddLabelTool( ctrl_del, _(u"tool"), wx.ArtProvider.GetBitmap( wx.ART_DELETE, wx.ART_TOOLBAR ), wx.NullBitmap, wx.ITEM_NORMAL, wx.EmptyString, wx.EmptyString, None ) 
		
		self.ctrl_toolbar.AddSeparator()
		
		self.ctrl_toolbar.AddLabelTool( ctrl_up, _(u"tool"), wx.ArtProvider.GetBitmap( wx.ART_GO_UP, wx.ART_TOOLBAR ), wx.NullBitmap, wx.ITEM_NORMAL, wx.EmptyString, wx.EmptyString, None ) 
		
		self.ctrl_toolbar.AddLabelTool( ctrl_down, _(u"tool"), wx.ArtProvider.GetBitmap( wx.ART_GO_DOWN, wx.ART_TOOLBAR ), wx.NullBitmap, wx.ITEM_NORMAL, wx.EmptyString, wx.EmptyString, None ) 
		
		self.ctrl_toolbar.Realize() 
		
		fgSizer34.Add( self.ctrl_toolbar, 0, wx.EXPAND, 5 )
		
		self.ctrl_tree = TreeListCtrl( self.m_panel80, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TR_DEFAULT_STYLE|wx.TR_FULL_ROW_HIGHLIGHT|wx.TR_HIDE_ROOT|wx.TR_LINES_AT_ROOT|wx.TR_ROW_LINES|wx.TR_SINGLE )
		fgSizer34.Add( self.ctrl_tree, 0, wx.ALL|wx.EXPAND, 5 )
		
		
		self.m_panel80.SetSizer( fgSizer34 )
		self.m_panel80.Layout()
		fgSizer34.Fit( self.m_panel80 )
		self.m_panel79 = wx.Panel( self.m_splitter9, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		fgSizer341 = wx.FlexGridSizer( 2, 0, 0, 0 )
		fgSizer341.AddGrowableCol( 0 )
		fgSizer341.AddGrowableCol( 1 )
		fgSizer341.AddGrowableRow( 1 )
		fgSizer341.SetFlexibleDirection( wx.BOTH )
		fgSizer341.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )
		
		self.action_toolbar = wx.ToolBar( self.m_panel79, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TB_HORIZONTAL ) 
		self.action_toolbar.AddLabelTool( action_new, _(u"tool"), wx.ArtProvider.GetBitmap( wx.ART_NEW, wx.ART_TOOLBAR ), wx.NullBitmap, wx.ITEM_NORMAL, wx.EmptyString, wx.EmptyString, None ) 
		
		self.action_toolbar.AddLabelTool( action_del, _(u"tool"), wx.ArtProvider.GetBitmap( wx.ART_DELETE, wx.ART_TOOLBAR ), wx.NullBitmap, wx.ITEM_NORMAL, wx.EmptyString, wx.EmptyString, None ) 
		
		self.action_toolbar.AddSeparator()
		
		self.action_toolbar.AddLabelTool( action_up, _(u"tool"), wx.ArtProvider.GetBitmap( wx.ART_GO_UP, wx.ART_TOOLBAR ), wx.NullBitmap, wx.ITEM_NORMAL, wx.EmptyString, wx.EmptyString, None ) 
		
		self.action_toolbar.AddLabelTool( action_down, _(u"tool"), wx.ArtProvider.GetBitmap( wx.ART_GO_DOWN, wx.ART_TOOLBAR ), wx.NullBitmap, wx.ITEM_NORMAL, wx.EmptyString, wx.EmptyString, None ) 
		
		self.action_toolbar.Realize() 
		
		fgSizer341.Add( self.action_toolbar, 0, wx.EXPAND, 5 )
		
		self.action_list = wx.ListCtrl( self.m_panel79, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LC_REPORT|wx.LC_VRULES )
		fgSizer341.Add( self.action_list, 0, wx.ALL|wx.EXPAND, 5 )
		
		
		self.m_panel79.SetSizer( fgSizer341 )
		self.m_panel79.Layout()
		fgSizer341.Fit( self.m_panel79 )
		self.m_splitter9.SplitVertically( self.m_panel80, self.m_panel79, 150 )
		bSizer33.Add( self.m_splitter9, 1, wx.EXPAND, 5 )
		
		
		self.m_panel97.SetSizer( bSizer33 )
		self.m_panel97.Layout()
		bSizer33.Fit( self.m_panel97 )
		self.m_notebook4.AddPage( self.m_panel97, _(u"a page"), True )
		
		bSizer18.Add( self.m_notebook4, 1, wx.ALL|wx.EXPAND, 5 )
		
		
		fgSizer4.Add( bSizer18, 1, wx.EXPAND, 5 )
		
		self.m_panel27 = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		gSizer3 = wx.GridSizer( 0, 2, 0, 0 )
		
		self.m_button6 = wx.Button( self.m_panel27, wx.ID_ANY, _(u"Apply"), wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer3.Add( self.m_button6, 0, wx.ALIGN_RIGHT|wx.ALL, 5 )
		
		self.m_button7 = wx.Button( self.m_panel27, wx.ID_ANY, _(u"Cancel"), wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer3.Add( self.m_button7, 0, wx.ALIGN_LEFT|wx.ALL, 5 )
		
		
		self.m_panel27.SetSizer( gSizer3 )
		self.m_panel27.Layout()
		gSizer3.Fit( self.m_panel27 )
		fgSizer4.Add( self.m_panel27, 1, wx.EXPAND |wx.ALL, 5 )
		
		
		self.SetSizer( fgSizer4 )
		self.Layout()
		
		# Connect Events
		self.m_button81.Bind( wx.EVT_BUTTON, self.onAddModule )
		self.m_button91.Bind( wx.EVT_BUTTON, self.onDeleteModule )
		self.list.Bind( wx.EVT_LIST_ITEM_DESELECTED, self.OnItemDeselected )
		self.list.Bind( wx.EVT_LIST_ITEM_SELECTED, self.OnItemSelected )
		self.m_button811.Bind( wx.EVT_BUTTON, self.onAddAction )
		self.m_button911.Bind( wx.EVT_BUTTON, self.onDeleteAction )
		self.list1.Bind( wx.EVT_LIST_ITEM_DESELECTED, self.OnItemDeselected )
		self.list1.Bind( wx.EVT_LIST_ITEM_SELECTED, self.OnItemSelected )
		self.Bind( wx.EVT_TOOL, self.onCtrlToolClicked, id = ctrl_new )
		self.Bind( wx.EVT_TOOL, self.onCtrlToolClicked, id = ctrl_del )
		self.Bind( wx.EVT_TOOL, self.onCtrlToolClicked, id = ctrl_up )
		self.Bind( wx.EVT_TOOL, self.onCtrlToolClicked, id = ctrl_down )
		self.ctrl_tree.Bind( wx.EVT_TREE_BEGIN_LABEL_EDIT, self.onCtrlItemBeginEdit )
		self.ctrl_tree.Bind( wx.EVT_TREE_DELETE_ITEM, self.onCtrlItemDelete )
		self.ctrl_tree.Bind( wx.EVT_TREE_END_LABEL_EDIT, self.onCtrlItemEndEdit )
		self.ctrl_tree.Bind( wx.EVT_TREE_SEL_CHANGED, self.onCtrlSelChanged )
		self.Bind( wx.EVT_TOOL, self.onActionToolClicked, id = action_new )
		self.Bind( wx.EVT_TOOL, self.onActionToolClicked, id = action_del )
		self.Bind( wx.EVT_TOOL, self.onActionToolClicked, id = action_up )
		self.Bind( wx.EVT_TOOL, self.onActionToolClicked, id = action_down )
		self.m_button6.Bind( wx.EVT_BUTTON, self.onApply )
		self.m_button7.Bind( wx.EVT_BUTTON, self.onCancel )
	
	def __del__( self ):
		pass
	
	
	# Virtual event handlers, overide them in your derived class
	def onAddModule( self, event ):
		event.Skip()
	
	def onDeleteModule( self, event ):
		event.Skip()
	
	def OnItemDeselected( self, event ):
		event.Skip()
	
	def OnItemSelected( self, event ):
		event.Skip()
	
	def onAddAction( self, event ):
		event.Skip()
	
	def onDeleteAction( self, event ):
		event.Skip()
	
	
	
	def onCtrlToolClicked( self, event ):
		event.Skip()
	
	
	
	
	def onCtrlItemBeginEdit( self, event ):
		event.Skip()
	
	def onCtrlItemDelete( self, event ):
		event.Skip()
	
	def onCtrlItemEndEdit( self, event ):
		event.Skip()
	
	def onCtrlSelChanged( self, event ):
		event.Skip()
	
	def onActionToolClicked( self, event ):
		event.Skip()
	
	
	
	
	def onApply( self, event ):
		event.Skip()
	
	def onCancel( self, event ):
		event.Skip()
	
	def m_splitter9OnIdle( self, event ):
		self.m_splitter9.SetSashPosition( 150 )
		self.m_splitter9.Unbind( wx.EVT_IDLE )
	

###########################################################################
## Class Panel_NewAction_Base
###########################################################################

class Panel_NewAction_Base ( wx.Panel ):
	
	def __init__( self, parent ):
		wx.Panel.__init__ ( self, parent, id = wx.ID_ANY, pos = wx.DefaultPosition, size = wx.Size( 344,397 ), style = wx.TAB_TRAVERSAL )
		
		fgSizer86 = wx.FlexGridSizer( 2, 1, 0, 0 )
		fgSizer86.AddGrowableCol( 0 )
		fgSizer86.AddGrowableRow( 0 )
		fgSizer86.SetFlexibleDirection( wx.BOTH )
		fgSizer86.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )
		
		self.mainSizer = wx.FlexGridSizer( 0, 1, 0, 0 )
		self.mainSizer.SetFlexibleDirection( wx.BOTH )
		self.mainSizer.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )
		
		bSizer57 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.m_staticText47 = wx.StaticText( self, wx.ID_ANY, _(u"动作类型:"), wx.DefaultPosition, wx.Size( 70,-1 ), 0 )
		self.m_staticText47.Wrap( -1 )
		bSizer57.Add( self.m_staticText47, 1, wx.ALIGN_CENTER|wx.ALL, 5 )
		
		m_choice4Choices = [ _(u"信号输出"), _(u"延时等待") ]
		self.m_choice4 = wx.Choice( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, m_choice4Choices, 0 )
		self.m_choice4.SetSelection( 0 )
		bSizer57.Add( self.m_choice4, 2, wx.ALIGN_CENTER|wx.ALL|wx.EXPAND, 5 )
		
		
		self.mainSizer.Add( bSizer57, 0, wx.BOTTOM, 15 )
		
		self.sizeTimeDelay = wx.StaticBoxSizer( wx.StaticBox( self, wx.ID_ANY, _(u"延时") ), wx.HORIZONTAL )
		
		self.m_staticText73 = wx.StaticText( self, wx.ID_ANY, _(u"延时时间(秒):"), wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText73.Wrap( -1 )
		self.sizeTimeDelay.Add( self.m_staticText73, 0, wx.ALL, 5 )
		
		self.m_textCtrl45 = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.sizeTimeDelay.Add( self.m_textCtrl45, 0, wx.ALL, 5 )
		
		
		self.mainSizer.Add( self.sizeTimeDelay, 1, wx.EXPAND, 5 )
		
		self.SizerIO = wx.BoxSizer( wx.VERTICAL )
		
		self.sizer1 = wx.StaticBoxSizer( wx.StaticBox( self, wx.ID_ANY, _(u"动作输出") ), wx.VERTICAL )
		
		fgSizer68 = wx.FlexGridSizer( 0, 3, 0, 0 )
		fgSizer68.SetFlexibleDirection( wx.BOTH )
		fgSizer68.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )
		
		self.m_staticText42 = wx.StaticText( self, wx.ID_ANY, _(u"输出点:"), wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText42.Wrap( -1 )
		fgSizer68.Add( self.m_staticText42, 1, wx.ALL, 5 )
		
		choice_outputChoices = []
		self.choice_output = wx.Choice( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, choice_outputChoices, 0 )
		self.choice_output.SetSelection( 0 )
		fgSizer68.Add( self.choice_output, 1, wx.ALL|wx.EXPAND, 5 )
		
		self.addOutputBtn = wx.BitmapButton( self, wx.ID_ANY, wx.ArtProvider.GetBitmap( wx.ART_NEW, wx.ART_BUTTON ), wx.DefaultPosition, wx.DefaultSize, wx.BU_AUTODRAW )
		fgSizer68.Add( self.addOutputBtn, 0, wx.ALL, 5 )
		
		self.m_staticText43 = wx.StaticText( self, wx.ID_ANY, _(u"输出值:"), wx.DefaultPosition, wx.Size( 70,-1 ), 0 )
		self.m_staticText43.Wrap( -1 )
		fgSizer68.Add( self.m_staticText43, 0, wx.ALIGN_CENTER|wx.ALL|wx.LEFT|wx.RIGHT, 5 )
		
		self.text_output = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer68.Add( self.text_output, 0, wx.ALL|wx.EXPAND, 5 )
		
		
		self.sizer1.Add( fgSizer68, 0, wx.EXPAND, 5 )
		
		
		self.SizerIO.Add( self.sizer1, 0, wx.EXPAND, 5 )
		
		self.sizer2 = wx.StaticBoxSizer( wx.StaticBox( self, wx.ID_ANY, _(u"动作反馈") ), wx.VERTICAL )
		
		bSizer49 = wx.BoxSizer( wx.VERTICAL )
		
		self.m_checkBox3 = wx.CheckBox( self, wx.ID_ANY, _(u"检测反馈信号"), wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer49.Add( self.m_checkBox3, 0, wx.ALL, 5 )
		
		fgSizer70 = wx.FlexGridSizer( 2, 3, 0, 0 )
		fgSizer70.SetFlexibleDirection( wx.BOTH )
		fgSizer70.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )
		
		self.m_staticText44 = wx.StaticText( self, wx.ID_ANY, _(u"输入点:"), wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText44.Wrap( -1 )
		fgSizer70.Add( self.m_staticText44, 0, wx.ALL, 5 )
		
		choice_feedbackChoices = []
		self.choice_feedback = wx.Choice( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, choice_feedbackChoices, 0 )
		self.choice_feedback.SetSelection( 0 )
		fgSizer70.Add( self.choice_feedback, 0, wx.ALL|wx.EXPAND, 5 )
		
		self.addFeedbackBtn = wx.BitmapButton( self, wx.ID_ANY, wx.ArtProvider.GetBitmap( wx.ART_NEW, wx.ART_BUTTON ), wx.DefaultPosition, wx.DefaultSize, wx.BU_AUTODRAW )
		fgSizer70.Add( self.addFeedbackBtn, 0, wx.ALL, 5 )
		
		self.m_staticText46 = wx.StaticText( self, wx.ID_ANY, _(u"超时(秒)："), wx.DefaultPosition, wx.Size( 70,-1 ), 0 )
		self.m_staticText46.Wrap( -1 )
		fgSizer70.Add( self.m_staticText46, 0, wx.ALL, 5 )
		
		self.text_timeout = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer70.Add( self.text_timeout, 0, wx.ALL|wx.EXPAND, 5 )
		
		
		bSizer49.Add( fgSizer70, 1, wx.EXPAND, 5 )
		
		
		self.sizer2.Add( bSizer49, 1, wx.EXPAND, 5 )
		
		
		self.SizerIO.Add( self.sizer2, 1, wx.EXPAND, 5 )
		
		
		self.mainSizer.Add( self.SizerIO, 1, wx.EXPAND, 5 )
		
		
		fgSizer86.Add( self.mainSizer, 1, wx.EXPAND|wx.TOP|wx.LEFT, 15 )
		
		gSizer15 = wx.GridSizer( 0, 2, 0, 0 )
		
		self.m_button40 = wx.Button( self, wx.ID_ANY, _(u"Apply"), wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer15.Add( self.m_button40, 0, wx.ALIGN_RIGHT|wx.ALL, 5 )
		
		self.m_button41 = wx.Button( self, wx.ID_ANY, _(u"Cancel"), wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer15.Add( self.m_button41, 0, wx.ALL, 5 )
		
		
		fgSizer86.Add( gSizer15, 1, wx.EXPAND|wx.BOTTOM, 10 )
		
		
		self.SetSizer( fgSizer86 )
		self.Layout()
		
		# Connect Events
		self.m_choice4.Bind( wx.EVT_CHOICE, self.onChoice )
		self.addOutputBtn.Bind( wx.EVT_BUTTON, self.onAddModule )
		self.addFeedbackBtn.Bind( wx.EVT_BUTTON, self.onAddModule )
		self.m_button40.Bind( wx.EVT_BUTTON, self.onApply )
		self.m_button41.Bind( wx.EVT_BUTTON, self.onCancel )
	
	def __del__( self ):
		pass
	
	
	# Virtual event handlers, overide them in your derived class
	def onChoice( self, event ):
		event.Skip()
	
	def onAddModule( self, event ):
		event.Skip()
	
	
	def onApply( self, event ):
		event.Skip()
	
	def onCancel( self, event ):
		event.Skip()
	

