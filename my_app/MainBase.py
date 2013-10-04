# -*- coding: utf-8 -*- 

###########################################################################
## Python code generated with wxFormBuilder (version Oct  8 2012)
## http://www.wxformbuilder.org/
##
## PLEASE DO "NOT" EDIT THIS FILE!
###########################################################################

from MyClass import UlcListCtrl
from wx.gizmos import TreeListCtrl
from wx.lib.agw.customtreectrl import CustomTreeCtrl
import wx
import wx.xrc
import wx.richtext
import wx.grid

import gettext
_ = gettext.gettext

ID_MENU_SAVE = 1000
ID_MENU_LOAD = 1001
ID_MENU_EDIT_STATION = 1002
ID_MENU_EDIT_IO_NODE = 1003
ID_MENU_EDIT_ACTION = 1004
ID_MENU_ADD_DEVICE = 1005
ID_MENU_EDIT_DEVICE = 1006
ID_MENU_DELETE_DEVICE = 1007
ID_MENU_RUN = 1008
ctrl_new = 1009
ctrl_del = 1010
ctrl_up = 1011
ctrl_down = 1012
action_new = 1013
action_del = 1014
action_up = 1015
action_down = 1016
canStation_new = 1017
canStation_edit = 1018
canStation_del = 1019
ioBoard_new = 1020
ioBoard_edit = 1021
ioBoard_del = 1022
actionGrp_new = 1023
actionGrp_edit = 1024
actionGrp_del = 1025
action_edit = 1026
IO_NODE_NEW = 1027
IO_NODE_EDIT = 1028
IO_NODE_DEL = 1029
STATUS_ADD = 1030
STATUS_DEL = 1031

###########################################################################
## Class FrameBase
###########################################################################

class FrameBase ( wx.Frame ):
	
	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = _(u"my app"), pos = wx.DefaultPosition, size = wx.Size( 500,500 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )
		
		self.SetSizeHintsSz( wx.DefaultSize, wx.DefaultSize )
		
		self.m_statusBar1 = self.CreateStatusBar( 1, wx.ST_SIZEGRIP, wx.ID_ANY )
		self.m_menubar1 = wx.MenuBar( 0 )
		self.m_menu1 = wx.Menu()
		self.menuSave = wx.MenuItem( self.m_menu1, ID_MENU_SAVE, _(u"Save"), wx.EmptyString, wx.ITEM_NORMAL )
		self.m_menu1.AppendItem( self.menuSave )
		
		self.menuLoad = wx.MenuItem( self.m_menu1, ID_MENU_LOAD, _(u"Load"), wx.EmptyString, wx.ITEM_NORMAL )
		self.m_menu1.AppendItem( self.menuLoad )
		
		self.m_menubar1.Append( self.m_menu1, _(u"File") ) 
		
		self.m_menu2 = wx.Menu()
		self.menuEditStation = wx.MenuItem( self.m_menu2, ID_MENU_EDIT_STATION, _(u"Edit Station"), wx.EmptyString, wx.ITEM_NORMAL )
		self.m_menu2.AppendItem( self.menuEditStation )
		
		self.menuEditIoNode = wx.MenuItem( self.m_menu2, ID_MENU_EDIT_IO_NODE, _(u"Edit IO"), wx.EmptyString, wx.ITEM_NORMAL )
		self.m_menu2.AppendItem( self.menuEditIoNode )
		
		self.menuEditAction = wx.MenuItem( self.m_menu2, ID_MENU_EDIT_ACTION, _(u"Edit Action"), wx.EmptyString, wx.ITEM_NORMAL )
		self.m_menu2.AppendItem( self.menuEditAction )
		
		self.m_menubar1.Append( self.m_menu2, _(u"Edit") ) 
		
		self.SetMenuBar( self.m_menubar1 )
		
		self.m_toolBar2 = self.CreateToolBar( wx.TB_HORIZONTAL, wx.ID_ANY )
		self.m_toolBar2.SetToolSeparation( 10 )
		self.m_toolBar2.AddLabelTool( ID_MENU_ADD_DEVICE, _(u"tool"), wx.ArtProvider.GetBitmap( wx.ART_NEW, wx.ART_TOOLBAR ), wx.NullBitmap, wx.ITEM_NORMAL, _(u"添加设备"), wx.EmptyString, None ) 
		
		self.m_toolBar2.AddLabelTool( ID_MENU_EDIT_DEVICE, _(u"tool"), wx.ArtProvider.GetBitmap( wx.ART_EXECUTABLE_FILE, wx.ART_TOOLBAR ), wx.NullBitmap, wx.ITEM_NORMAL, wx.EmptyString, wx.EmptyString, None ) 
		
		self.m_toolBar2.AddLabelTool( ID_MENU_DELETE_DEVICE, _(u"tool"), wx.ArtProvider.GetBitmap( wx.ART_DELETE, wx.ART_TOOLBAR ), wx.NullBitmap, wx.ITEM_NORMAL, wx.EmptyString, wx.EmptyString, None ) 
		
		self.m_toolBar2.AddSeparator()
		
		self.m_toolBar2.AddLabelTool( ID_MENU_RUN, _(u"tool"), wx.ArtProvider.GetBitmap( wx.ART_GO_FORWARD, wx.ART_TOOLBAR ), wx.NullBitmap, wx.ITEM_NORMAL, wx.EmptyString, wx.EmptyString, None ) 
		
		self.m_toolBar2.Realize() 
		
		
		self.Centre( wx.BOTH )
		
		# Connect Events
		self.Bind( wx.EVT_MENU, self.onMenuBtnClicked, id = self.menuSave.GetId() )
		self.Bind( wx.EVT_MENU, self.onMenuBtnClicked, id = self.menuLoad.GetId() )
		self.Bind( wx.EVT_MENU, self.onMenuBtnClicked, id = self.menuEditStation.GetId() )
		self.Bind( wx.EVT_MENU, self.onMenuBtnClicked, id = self.menuEditIoNode.GetId() )
		self.Bind( wx.EVT_MENU, self.onMenuBtnClicked, id = self.menuEditAction.GetId() )
		self.Bind( wx.EVT_TOOL, self.onMenuBtnClicked, id = ID_MENU_ADD_DEVICE )
		self.Bind( wx.EVT_TOOL, self.onMenuBtnClicked, id = ID_MENU_EDIT_DEVICE )
		self.Bind( wx.EVT_TOOL, self.onMenuBtnClicked, id = ID_MENU_DELETE_DEVICE )
		self.Bind( wx.EVT_TOOL, self.onMenuBtnClicked, id = ID_MENU_RUN )
	
	def __del__( self ):
		pass
	
	
	# Virtual event handlers, overide them in your derived class
	def onMenuBtnClicked( self, event ):
		event.Skip()
	
	
	
	
	
	
	
	
	

###########################################################################
## Class SplitterPanelBase
###########################################################################

class SplitterPanelBase ( wx.Panel ):
	
	def __init__( self, parent ):
		wx.Panel.__init__ ( self, parent, id = wx.ID_ANY, pos = wx.DefaultPosition, size = wx.Size( 527,589 ), style = wx.TAB_TRAVERSAL )
		
		bSizer6 = wx.BoxSizer( wx.VERTICAL )
		
		self.m_splitter4 = wx.SplitterWindow( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.SP_3D|wx.SP_LIVE_UPDATE )
		self.m_splitter4.Bind( wx.EVT_IDLE, self.m_splitter4OnIdle )
		
		self.viewSelectPanel = wx.Panel( self.m_splitter4, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.NO_BORDER|wx.TAB_TRAVERSAL )
		self.viewSelectPanel.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_BACKGROUND ) )
		
		self.viewContainPanel = wx.Panel( self.m_splitter4, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.SUNKEN_BORDER|wx.TAB_TRAVERSAL )
		bSizer12 = wx.BoxSizer( wx.VERTICAL )
		
		self.m_splitter6 = wx.SplitterWindow( self.viewContainPanel, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.SP_3D )
		self.m_splitter6.SetSashGravity( 1 )
		self.m_splitter6.SetSashSize( 5 )
		self.m_splitter6.Bind( wx.EVT_IDLE, self.m_splitter6OnIdle )
		self.m_splitter6.SetMinimumPaneSize( 100 )
		
		self.viewPanel = wx.Panel( self.m_splitter6, wx.ID_ANY, wx.DefaultPosition, wx.Size( 2000,1000 ), wx.TAB_TRAVERSAL )
		self.detailPanel = wx.Panel( self.m_splitter6, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		sbSizer17 = wx.StaticBoxSizer( wx.StaticBox( self.detailPanel, wx.ID_ANY, _(u"label") ), wx.VERTICAL )
		
		self.log_txt = wx.richtext.RichTextCtrl( self.detailPanel, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.TE_READONLY|wx.VSCROLL|wx.HSCROLL|wx.NO_BORDER|wx.WANTS_CHARS )
		sbSizer17.Add( self.log_txt, 1, wx.EXPAND |wx.ALL, 5 )
		
		
		self.detailPanel.SetSizer( sbSizer17 )
		self.detailPanel.Layout()
		sbSizer17.Fit( self.detailPanel )
		self.m_splitter6.SplitHorizontally( self.viewPanel, self.detailPanel, 350 )
		bSizer12.Add( self.m_splitter6, 1, wx.EXPAND, 5 )
		
		
		self.viewContainPanel.SetSizer( bSizer12 )
		self.viewContainPanel.Layout()
		bSizer12.Fit( self.viewContainPanel )
		self.m_splitter4.SplitVertically( self.viewSelectPanel, self.viewContainPanel, 100 )
		bSizer6.Add( self.m_splitter4, 1, wx.EXPAND, 5 )
		
		
		self.SetSizer( bSizer6 )
		self.Layout()
	
	def __del__( self ):
		pass
	
	def m_splitter4OnIdle( self, event ):
		self.m_splitter4.SetSashPosition( 100 )
		self.m_splitter4.Unbind( wx.EVT_IDLE )
	
	def m_splitter6OnIdle( self, event ):
		self.m_splitter6.SetSashPosition( 350 )
		self.m_splitter6.Unbind( wx.EVT_IDLE )
	

###########################################################################
## Class Panel_EditModuleIO_Base
###########################################################################

class Panel_EditModuleIO_Base ( wx.Panel ):
	
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
		self.attribute_panel = wx.Panel( self.m_notebook4, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		fgSizer511 = wx.FlexGridSizer( 2, 1, 0, 0 )
		fgSizer511.AddGrowableCol( 0 )
		fgSizer511.AddGrowableRow( 1 )
		fgSizer511.SetFlexibleDirection( wx.BOTH )
		fgSizer511.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )
		
		self.m_panel2311 = wx.Panel( self.attribute_panel, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.NO_BORDER|wx.TAB_TRAVERSAL )
		bSizer711 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.m_button811 = wx.Button( self.m_panel2311, wx.ID_ANY, _(u"Add"), wx.DefaultPosition, wx.DefaultSize, 0|wx.NO_BORDER )
		bSizer711.Add( self.m_button811, 0, wx.TOP|wx.LEFT, 5 )
		
		self.Edit = wx.Button( self.m_panel2311, wx.ID_ANY, _(u"Edit"), wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer711.Add( self.Edit, 0, wx.ALL, 5 )
		
		self.m_button911 = wx.Button( self.m_panel2311, wx.ID_ANY, _(u"Delete"), wx.DefaultPosition, wx.DefaultSize, 0|wx.NO_BORDER )
		bSizer711.Add( self.m_button911, 0, wx.TOP|wx.LEFT, 5 )
		
		
		self.m_panel2311.SetSizer( bSizer711 )
		self.m_panel2311.Layout()
		bSizer711.Fit( self.m_panel2311 )
		fgSizer511.Add( self.m_panel2311, 1, wx.EXPAND |wx.ALL, 0 )
		
		self.attribute_list = UlcListCtrl( self.attribute_panel, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LC_REPORT|wx.NO_BORDER )
		fgSizer511.Add( self.attribute_list, 0, wx.EXPAND|wx.ALL, 5 )
		
		
		self.attribute_panel.SetSizer( fgSizer511 )
		self.attribute_panel.Layout()
		fgSizer511.Fit( self.attribute_panel )
		self.m_notebook4.AddPage( self.attribute_panel, _(u"变量"), False )
		self.io_module_panel = wx.Panel( self.m_notebook4, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		self.io_module_panel.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_WINDOW ) )
		
		fgSizer51 = wx.FlexGridSizer( 2, 1, 0, 0 )
		fgSizer51.AddGrowableCol( 0 )
		fgSizer51.AddGrowableRow( 1 )
		fgSizer51.SetFlexibleDirection( wx.BOTH )
		fgSizer51.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )
		
		self.m_panel231 = wx.Panel( self.io_module_panel, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.NO_BORDER|wx.TAB_TRAVERSAL )
		bSizer71 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.m_button81 = wx.Button( self.m_panel231, wx.ID_ANY, _(u"Add"), wx.DefaultPosition, wx.DefaultSize, 0|wx.NO_BORDER )
		bSizer71.Add( self.m_button81, 0, wx.TOP|wx.LEFT, 5 )
		
		self.m_button91 = wx.Button( self.m_panel231, wx.ID_ANY, _(u"Delete"), wx.DefaultPosition, wx.DefaultSize, 0|wx.NO_BORDER )
		bSizer71.Add( self.m_button91, 0, wx.TOP|wx.LEFT, 5 )
		
		
		self.m_panel231.SetSizer( bSizer71 )
		self.m_panel231.Layout()
		bSizer71.Fit( self.m_panel231 )
		fgSizer51.Add( self.m_panel231, 1, wx.EXPAND |wx.ALL, 0 )
		
		self.moudleIo_list = UlcListCtrl( self.io_module_panel, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LC_REPORT|wx.NO_BORDER )
		fgSizer51.Add( self.moudleIo_list, 0, wx.EXPAND|wx.ALL, 5 )
		
		
		self.io_module_panel.SetSizer( fgSizer51 )
		self.io_module_panel.Layout()
		fgSizer51.Fit( self.io_module_panel )
		self.m_notebook4.AddPage( self.io_module_panel, _(u"输入输出"), False )
		self.contorl_panel = wx.Panel( self.m_notebook4, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer33 = wx.BoxSizer( wx.VERTICAL )
		
		self.m_splitter9 = wx.SplitterWindow( self.contorl_panel, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.SP_3D )
		self.m_splitter9.Bind( wx.EVT_IDLE, self.m_splitter9OnIdle )
		
		self.m_panel80 = wx.Panel( self.m_splitter9, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		fgSizer34 = wx.FlexGridSizer( 2, 0, 0, 0 )
		fgSizer34.AddGrowableCol( 0 )
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
		
		self.actionGroupTree = TreeListCtrl( self.m_panel80, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TR_DEFAULT_STYLE|wx.TR_FULL_ROW_HIGHLIGHT|wx.TR_HIDE_ROOT|wx.TR_LINES_AT_ROOT|wx.TR_ROW_LINES|wx.TR_SINGLE )
		fgSizer34.Add( self.actionGroupTree, 0, wx.ALL|wx.EXPAND, 5 )
		
		
		self.m_panel80.SetSizer( fgSizer34 )
		self.m_panel80.Layout()
		fgSizer34.Fit( self.m_panel80 )
		self.m_panel79 = wx.Panel( self.m_splitter9, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		fgSizer341 = wx.FlexGridSizer( 2, 0, 0, 0 )
		fgSizer341.AddGrowableCol( 0 )
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
		
		self.action_list = UlcListCtrl( self.m_panel79, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LC_REPORT )
		fgSizer341.Add( self.action_list, 0, wx.ALL|wx.EXPAND, 5 )
		
		
		self.m_panel79.SetSizer( fgSizer341 )
		self.m_panel79.Layout()
		fgSizer341.Fit( self.m_panel79 )
		self.m_splitter9.SplitVertically( self.m_panel80, self.m_panel79, 150 )
		bSizer33.Add( self.m_splitter9, 1, wx.EXPAND, 5 )
		
		
		self.contorl_panel.SetSizer( bSizer33 )
		self.contorl_panel.Layout()
		bSizer33.Fit( self.contorl_panel )
		self.m_notebook4.AddPage( self.contorl_panel, _(u"控制"), True )
		
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
		self.m_button811.Bind( wx.EVT_BUTTON, self.onAddAttribute )
		self.Edit.Bind( wx.EVT_BUTTON, self.onEditAttribute )
		self.m_button911.Bind( wx.EVT_BUTTON, self.onDeleteAttribute )
		self.attribute_list.Bind( wx.EVT_LIST_ITEM_DESELECTED, self.OnItemDeselected )
		self.attribute_list.Bind( wx.EVT_LIST_ITEM_SELECTED, self.OnItemSelected )
		self.m_button81.Bind( wx.EVT_BUTTON, self.onAddModuleIO )
		self.m_button91.Bind( wx.EVT_BUTTON, self.onDeleteModuleIO )
		self.moudleIo_list.Bind( wx.EVT_LIST_ITEM_DESELECTED, self.OnItemDeselected )
		self.moudleIo_list.Bind( wx.EVT_LIST_ITEM_SELECTED, self.OnItemSelected )
		self.Bind( wx.EVT_TOOL, self.onActGrpToolClicked, id = ctrl_new )
		self.Bind( wx.EVT_TOOL, self.onActGrpToolClicked, id = ctrl_del )
		self.Bind( wx.EVT_TOOL, self.onActGrpToolClicked, id = ctrl_up )
		self.Bind( wx.EVT_TOOL, self.onActGrpToolClicked, id = ctrl_down )
		self.actionGroupTree.Bind( wx.EVT_TREE_BEGIN_LABEL_EDIT, self.onActGrpItemBeginEdit )
		self.actionGroupTree.Bind( wx.EVT_TREE_DELETE_ITEM, self.onActGrpItemDelete )
		self.actionGroupTree.Bind( wx.EVT_TREE_END_LABEL_EDIT, self.onActGrpItemEndEdit )
		self.actionGroupTree.Bind( wx.EVT_TREE_SEL_CHANGED, self.onActGrpItemSelChanged )
		self.Bind( wx.EVT_TOOL, self.onActionToolClicked, id = action_new )
		self.Bind( wx.EVT_TOOL, self.onActionToolClicked, id = action_del )
		self.Bind( wx.EVT_TOOL, self.onActionToolClicked, id = action_up )
		self.Bind( wx.EVT_TOOL, self.onActionToolClicked, id = action_down )
		self.action_list.Bind( wx.EVT_LIST_ITEM_SELECTED, self.onListItemSelected )
		self.m_button6.Bind( wx.EVT_BUTTON, self.onApply )
		self.m_button7.Bind( wx.EVT_BUTTON, self.onCancel )
	
	def __del__( self ):
		pass
	
	
	# Virtual event handlers, overide them in your derived class
	def onAddAttribute( self, event ):
		event.Skip()
	
	def onEditAttribute( self, event ):
		event.Skip()
	
	def onDeleteAttribute( self, event ):
		event.Skip()
	
	def OnItemDeselected( self, event ):
		event.Skip()
	
	def OnItemSelected( self, event ):
		event.Skip()
	
	def onAddModuleIO( self, event ):
		event.Skip()
	
	def onDeleteModuleIO( self, event ):
		event.Skip()
	
	
	
	def onActGrpToolClicked( self, event ):
		event.Skip()
	
	
	
	
	def onActGrpItemBeginEdit( self, event ):
		event.Skip()
	
	def onActGrpItemDelete( self, event ):
		event.Skip()
	
	def onActGrpItemEndEdit( self, event ):
		event.Skip()
	
	def onActGrpItemSelChanged( self, event ):
		event.Skip()
	
	def onActionToolClicked( self, event ):
		event.Skip()
	
	
	
	
	def onListItemSelected( self, event ):
		event.Skip()
	
	def onApply( self, event ):
		event.Skip()
	
	def onCancel( self, event ):
		event.Skip()
	
	def m_splitter9OnIdle( self, event ):
		self.m_splitter9.SetSashPosition( 150 )
		self.m_splitter9.Unbind( wx.EVT_IDLE )
	

###########################################################################
## Class Panel_Edit_Can_Station_Base
###########################################################################

class Panel_Edit_Can_Station_Base ( wx.Panel ):
	
	def __init__( self, parent ):
		wx.Panel.__init__ ( self, parent, id = wx.ID_ANY, pos = wx.DefaultPosition, size = wx.Size( 411,215 ), style = wx.TAB_TRAVERSAL )
		
		fgSizer4 = wx.FlexGridSizer( 2, 1, 0, 0 )
		fgSizer4.AddGrowableCol( 0 )
		fgSizer4.AddGrowableCol( 1 )
		fgSizer4.AddGrowableRow( 0 )
		fgSizer4.SetFlexibleDirection( wx.BOTH )
		fgSizer4.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )
		
		bSizer18 = wx.BoxSizer( wx.VERTICAL )
		
		self.m_panel171 = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		self.m_panel171.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_WINDOW ) )
		self.m_panel171.SetMinSize( wx.Size( 100,100 ) )
		
		self.sizer112 = wx.StaticBoxSizer( wx.StaticBox( self.m_panel171, wx.ID_ANY, wx.EmptyString ), wx.VERTICAL )
		
		self.sizer112.SetMinSize( wx.Size( 200,-1 ) ) 
		fgSizer6812 = wx.FlexGridSizer( 0, 2, 0, 0 )
		fgSizer6812.AddGrowableCol( 1 )
		fgSizer6812.SetFlexibleDirection( wx.BOTH )
		fgSizer6812.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )
		
		self.nameStr = wx.StaticText( self.m_panel171, wx.ID_ANY, _(u"站点名称:"), wx.DefaultPosition, wx.DefaultSize, 0 )
		self.nameStr.Wrap( -1 )
		fgSizer6812.Add( self.nameStr, 1, wx.ALL, 5 )
		
		self.stationName_input = wx.TextCtrl( self.m_panel171, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer6812.Add( self.stationName_input, 0, wx.ALL|wx.EXPAND, 5 )
		
		self.m_staticText4312 = wx.StaticText( self.m_panel171, wx.ID_ANY, _(u"站点编号:"), wx.DefaultPosition, wx.Size( 70,-1 ), 0 )
		self.m_staticText4312.Wrap( -1 )
		fgSizer6812.Add( self.m_staticText4312, 0, wx.ALL, 5 )
		
		self.stationId_input = wx.TextCtrl( self.m_panel171, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer6812.Add( self.stationId_input, 0, wx.ALL|wx.EXPAND, 5 )
		
		self.m_staticText43121 = wx.StaticText( self.m_panel171, wx.ID_ANY, _(u"站点描述:"), wx.DefaultPosition, wx.Size( 70,-1 ), 0 )
		self.m_staticText43121.Wrap( -1 )
		fgSizer6812.Add( self.m_staticText43121, 0, wx.ALIGN_CENTER|wx.ALL, 5 )
		
		self.stationDesc_input = wx.TextCtrl( self.m_panel171, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer6812.Add( self.stationDesc_input, 0, wx.ALL|wx.EXPAND, 5 )
		
		
		self.sizer112.Add( fgSizer6812, 0, wx.EXPAND|wx.LEFT, 5 )
		
		
		self.m_panel171.SetSizer( self.sizer112 )
		self.m_panel171.Layout()
		self.sizer112.Fit( self.m_panel171 )
		bSizer18.Add( self.m_panel171, 1, wx.ALL|wx.EXPAND, 5 )
		
		
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
		self.m_button6.Bind( wx.EVT_BUTTON, self.onApply )
		self.m_button7.Bind( wx.EVT_BUTTON, self.onCancel )
	
	def __del__( self ):
		pass
	
	
	# Virtual event handlers, overide them in your derived class
	def onApply( self, event ):
		event.Skip()
	
	def onCancel( self, event ):
		event.Skip()
	

###########################################################################
## Class Panel_Edit_IO_Node_Base
###########################################################################

class Panel_Edit_IO_Node_Base ( wx.Panel ):
	
	def __init__( self, parent ):
		wx.Panel.__init__ ( self, parent, id = wx.ID_ANY, pos = wx.DefaultPosition, size = wx.Size( 590,389 ), style = wx.TAB_TRAVERSAL )
		
		fgSizer4 = wx.FlexGridSizer( 2, 1, 0, 0 )
		fgSizer4.AddGrowableCol( 0 )
		fgSizer4.AddGrowableRow( 0 )
		fgSizer4.SetFlexibleDirection( wx.BOTH )
		fgSizer4.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )
		
		bSizer18 = wx.BoxSizer( wx.VERTICAL )
		
		self.m_notebook4 = wx.Notebook( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_panel171 = wx.Panel( self.m_notebook4, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		self.m_panel171.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_WINDOW ) )
		self.m_panel171.SetMinSize( wx.Size( 100,100 ) )
		
		self.mainSizer = wx.FlexGridSizer( 2, 0, 0, 0 )
		self.mainSizer.SetFlexibleDirection( wx.BOTH )
		self.mainSizer.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )
		
		self.sizer112 = wx.StaticBoxSizer( wx.StaticBox( self.m_panel171, wx.ID_ANY, wx.EmptyString ), wx.VERTICAL )
		
		self.sizer112.SetMinSize( wx.Size( 400,-1 ) ) 
		fgSizer6812 = wx.FlexGridSizer( 0, 2, 0, 0 )
		fgSizer6812.AddGrowableCol( 1 )
		fgSizer6812.SetFlexibleDirection( wx.BOTH )
		fgSizer6812.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )
		
		self.nameStr = wx.StaticText( self.m_panel171, wx.ID_ANY, _(u"名 称:"), wx.DefaultPosition, wx.DefaultSize, 0 )
		self.nameStr.Wrap( -1 )
		fgSizer6812.Add( self.nameStr, 1, wx.ALL, 5 )
		
		self.nodeNameTxt = wx.TextCtrl( self.m_panel171, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer6812.Add( self.nodeNameTxt, 0, wx.ALL|wx.EXPAND, 5 )
		
		self.m_staticText4312 = wx.StaticText( self.m_panel171, wx.ID_ANY, _(u"描 述:"), wx.DefaultPosition, wx.Size( 70,-1 ), 0 )
		self.m_staticText4312.Wrap( -1 )
		fgSizer6812.Add( self.m_staticText4312, 0, wx.ALIGN_CENTER|wx.ALL|wx.LEFT|wx.RIGHT, 5 )
		
		self.nodeDescTxt = wx.TextCtrl( self.m_panel171, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer6812.Add( self.nodeDescTxt, 0, wx.ALL|wx.EXPAND, 5 )
		
		
		self.sizer112.Add( fgSizer6812, 0, wx.EXPAND|wx.LEFT, 5 )
		
		
		self.mainSizer.Add( self.sizer112, 1, wx.EXPAND, 5 )
		
		self.sizer1121 = wx.StaticBoxSizer( wx.StaticBox( self.m_panel171, wx.ID_ANY, wx.EmptyString ), wx.VERTICAL )
		
		fgSizer68121 = wx.FlexGridSizer( 0, 2, 0, 0 )
		fgSizer68121.AddGrowableCol( 1 )
		fgSizer68121.SetFlexibleDirection( wx.BOTH )
		fgSizer68121.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )
		
		self.m_staticText42121 = wx.StaticText( self.m_panel171, wx.ID_ANY, _(u"关状态信息:"), wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText42121.Wrap( -1 )
		fgSizer68121.Add( self.m_staticText42121, 1, wx.ALL, 5 )
		
		self.offInfoTxt = wx.TextCtrl( self.m_panel171, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer68121.Add( self.offInfoTxt, 0, wx.ALL|wx.EXPAND, 5 )
		
		self.m_staticText43121 = wx.StaticText( self.m_panel171, wx.ID_ANY, _(u"开状态信息:"), wx.DefaultPosition, wx.Size( -1,-1 ), 0 )
		self.m_staticText43121.Wrap( -1 )
		fgSizer68121.Add( self.m_staticText43121, 0, wx.ALIGN_CENTER|wx.ALL, 5 )
		
		self.onInfoTxt = wx.TextCtrl( self.m_panel171, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer68121.Add( self.onInfoTxt, 0, wx.ALL|wx.EXPAND, 5 )
		
		
		self.sizer1121.Add( fgSizer68121, 0, wx.EXPAND|wx.LEFT, 5 )
		
		
		self.mainSizer.Add( self.sizer1121, 1, wx.EXPAND, 5 )
		
		
		self.m_panel171.SetSizer( self.mainSizer )
		self.m_panel171.Layout()
		self.mainSizer.Fit( self.m_panel171 )
		self.m_notebook4.AddPage( self.m_panel171, _(u"基本信息"), True )
		self.attribute_panel = wx.Panel( self.m_notebook4, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		fgSizer511 = wx.FlexGridSizer( 2, 1, 0, 0 )
		fgSizer511.AddGrowableCol( 0 )
		fgSizer511.AddGrowableRow( 1 )
		fgSizer511.SetFlexibleDirection( wx.BOTH )
		fgSizer511.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )
		
		self.m_panel2311 = wx.Panel( self.attribute_panel, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.NO_BORDER|wx.TAB_TRAVERSAL )
		bSizer711 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.m_button811 = wx.Button( self.m_panel2311, wx.ID_ANY, _(u"Add"), wx.DefaultPosition, wx.DefaultSize, 0|wx.NO_BORDER )
		bSizer711.Add( self.m_button811, 0, wx.TOP|wx.LEFT, 5 )
		
		self.Edit = wx.Button( self.m_panel2311, wx.ID_ANY, _(u"Edit"), wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer711.Add( self.Edit, 0, wx.ALL, 5 )
		
		self.m_button911 = wx.Button( self.m_panel2311, wx.ID_ANY, _(u"Delete"), wx.DefaultPosition, wx.DefaultSize, 0|wx.NO_BORDER )
		bSizer711.Add( self.m_button911, 0, wx.TOP|wx.LEFT, 5 )
		
		
		self.m_panel2311.SetSizer( bSizer711 )
		self.m_panel2311.Layout()
		bSizer711.Fit( self.m_panel2311 )
		fgSizer511.Add( self.m_panel2311, 1, wx.EXPAND |wx.ALL, 0 )
		
		self.attribute_list = UlcListCtrl( self.attribute_panel, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LC_REPORT|wx.NO_BORDER )
		fgSizer511.Add( self.attribute_list, 0, wx.EXPAND|wx.ALL, 5 )
		
		
		self.attribute_panel.SetSizer( fgSizer511 )
		self.attribute_panel.Layout()
		fgSizer511.Fit( self.attribute_panel )
		self.m_notebook4.AddPage( self.attribute_panel, _(u"报警参数"), False )
		self.io_module_panel = wx.Panel( self.m_notebook4, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		self.io_module_panel.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_WINDOW ) )
		
		gSizer26 = wx.GridSizer( 0, 0, 0, 0 )
		
		self.sizer1122 = wx.StaticBoxSizer( wx.StaticBox( self.io_module_panel, wx.ID_ANY, wx.EmptyString ), wx.VERTICAL )
		
		self.sizer1122.SetMinSize( wx.Size( 400,-1 ) ) 
		fgSizer68122 = wx.FlexGridSizer( 0, 2, 0, 0 )
		fgSizer68122.AddGrowableCol( 1 )
		fgSizer68122.SetFlexibleDirection( wx.BOTH )
		fgSizer68122.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )
		
		self.m_staticText42122 = wx.StaticText( self.io_module_panel, wx.ID_ANY, _(u"站 点:"), wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText42122.Wrap( -1 )
		fgSizer68122.Add( self.m_staticText42122, 1, wx.ALL, 5 )
		
		stationChoiceChoices = []
		self.stationChoice = wx.Choice( self.io_module_panel, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, stationChoiceChoices, 0 )
		self.stationChoice.SetSelection( 0 )
		fgSizer68122.Add( self.stationChoice, 0, wx.ALL|wx.EXPAND, 5 )
		
		self.m_staticText43122 = wx.StaticText( self.io_module_panel, wx.ID_ANY, _(u"子 板:"), wx.DefaultPosition, wx.Size( 70,-1 ), 0 )
		self.m_staticText43122.Wrap( -1 )
		fgSizer68122.Add( self.m_staticText43122, 0, wx.ALL, 5 )
		
		boardChoiceChoices = []
		self.boardChoice = wx.Choice( self.io_module_panel, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, boardChoiceChoices, 0 )
		self.boardChoice.SetSelection( 0 )
		fgSizer68122.Add( self.boardChoice, 0, wx.ALL|wx.EXPAND, 5 )
		
		self.m_staticText431221 = wx.StaticText( self.io_module_panel, wx.ID_ANY, _(u"端 子:"), wx.DefaultPosition, wx.Size( 70,-1 ), 0 )
		self.m_staticText431221.Wrap( -1 )
		fgSizer68122.Add( self.m_staticText431221, 0, wx.ALL, 5 )
		
		portChoiceChoices = []
		self.portChoice = wx.Choice( self.io_module_panel, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, portChoiceChoices, 0 )
		self.portChoice.SetSelection( 0 )
		fgSizer68122.Add( self.portChoice, 0, wx.ALL|wx.EXPAND, 5 )
		
		
		self.sizer1122.Add( fgSizer68122, 0, wx.EXPAND|wx.LEFT, 5 )
		
		
		gSizer26.Add( self.sizer1122, 1, wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		
		self.io_module_panel.SetSizer( gSizer26 )
		self.io_module_panel.Layout()
		gSizer26.Fit( self.io_module_panel )
		self.m_notebook4.AddPage( self.io_module_panel, _(u"数据连接"), False )
		
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
		self.m_button811.Bind( wx.EVT_BUTTON, self.onAddAttribute )
		self.Edit.Bind( wx.EVT_BUTTON, self.onEditAttribute )
		self.m_button911.Bind( wx.EVT_BUTTON, self.onDeleteAttribute )
		self.attribute_list.Bind( wx.EVT_LIST_ITEM_DESELECTED, self.OnItemDeselected )
		self.attribute_list.Bind( wx.EVT_LIST_ITEM_SELECTED, self.OnItemSelected )
		self.stationChoice.Bind( wx.EVT_CHOICE, self.onStationChoice )
		self.m_button6.Bind( wx.EVT_BUTTON, self.onApply )
		self.m_button7.Bind( wx.EVT_BUTTON, self.onCancel )
	
	def __del__( self ):
		pass
	
	
	# Virtual event handlers, overide them in your derived class
	def onAddAttribute( self, event ):
		event.Skip()
	
	def onEditAttribute( self, event ):
		event.Skip()
	
	def onDeleteAttribute( self, event ):
		event.Skip()
	
	def OnItemDeselected( self, event ):
		event.Skip()
	
	def OnItemSelected( self, event ):
		event.Skip()
	
	def onStationChoice( self, event ):
		event.Skip()
	
	def onApply( self, event ):
		event.Skip()
	
	def onCancel( self, event ):
		event.Skip()
	

###########################################################################
## Class Panel_Manage_Can_Station_Base
###########################################################################

class Panel_Manage_Can_Station_Base ( wx.Panel ):
	
	def __init__( self, parent ):
		wx.Panel.__init__ ( self, parent, id = wx.ID_ANY, pos = wx.DefaultPosition, size = wx.Size( 698,429 ), style = wx.TAB_TRAVERSAL )
		
		fgSizer4 = wx.FlexGridSizer( 2, 1, 0, 0 )
		fgSizer4.AddGrowableCol( 0 )
		fgSizer4.AddGrowableCol( 1 )
		fgSizer4.AddGrowableRow( 0 )
		fgSizer4.SetFlexibleDirection( wx.BOTH )
		fgSizer4.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )
		
		bSizer18 = wx.BoxSizer( wx.VERTICAL )
		
		sbSizer25 = wx.StaticBoxSizer( wx.StaticBox( self, wx.ID_ANY, wx.EmptyString ), wx.VERTICAL )
		
		self.IoStation_panel = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer33 = wx.BoxSizer( wx.VERTICAL )
		
		self.m_splitter9 = wx.SplitterWindow( self.IoStation_panel, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.SP_3D )
		self.m_splitter9.Bind( wx.EVT_IDLE, self.m_splitter9OnIdle )
		
		self.m_panel80 = wx.Panel( self.m_splitter9, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		fgSizer34 = wx.FlexGridSizer( 2, 0, 0, 0 )
		fgSizer34.AddGrowableCol( 0 )
		fgSizer34.AddGrowableCol( 1 )
		fgSizer34.AddGrowableRow( 1 )
		fgSizer34.SetFlexibleDirection( wx.BOTH )
		fgSizer34.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )
		
		self.canStation_toolbar = wx.ToolBar( self.m_panel80, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TB_HORIZONTAL ) 
		self.canStation_toolbar.AddLabelTool( canStation_new, _(u"tool"), wx.ArtProvider.GetBitmap( wx.ART_NEW, wx.ART_TOOLBAR ), wx.NullBitmap, wx.ITEM_NORMAL, wx.EmptyString, wx.EmptyString, None ) 
		
		self.canStation_toolbar.AddLabelTool( canStation_edit, _(u"tool"), wx.ArtProvider.GetBitmap( wx.ART_EXECUTABLE_FILE, wx.ART_TOOLBAR ), wx.NullBitmap, wx.ITEM_NORMAL, wx.EmptyString, wx.EmptyString, None ) 
		
		self.canStation_toolbar.AddLabelTool( canStation_del, _(u"tool"), wx.ArtProvider.GetBitmap( wx.ART_DELETE, wx.ART_TOOLBAR ), wx.NullBitmap, wx.ITEM_NORMAL, wx.EmptyString, wx.EmptyString, None ) 
		
		self.canStation_toolbar.AddSeparator()
		
		self.canStation_toolbar.Realize() 
		
		fgSizer34.Add( self.canStation_toolbar, 0, wx.EXPAND, 5 )
		
		self.canStationList = UlcListCtrl( self.m_panel80, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LC_REPORT )
		fgSizer34.Add( self.canStationList, 0, wx.ALL|wx.EXPAND, 5 )
		
		
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
		
		self.ioBoard_toolbar = wx.ToolBar( self.m_panel79, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TB_HORIZONTAL ) 
		self.ioBoard_toolbar.AddLabelTool( ioBoard_new, _(u"tool"), wx.ArtProvider.GetBitmap( wx.ART_NEW, wx.ART_TOOLBAR ), wx.NullBitmap, wx.ITEM_NORMAL, wx.EmptyString, wx.EmptyString, None ) 
		
		self.ioBoard_toolbar.AddLabelTool( ioBoard_edit, _(u"tool"), wx.ArtProvider.GetBitmap( wx.ART_EXECUTABLE_FILE, wx.ART_TOOLBAR ), wx.NullBitmap, wx.ITEM_NORMAL, wx.EmptyString, wx.EmptyString, None ) 
		
		self.ioBoard_toolbar.AddLabelTool( ioBoard_del, _(u"tool"), wx.ArtProvider.GetBitmap( wx.ART_DELETE, wx.ART_TOOLBAR ), wx.NullBitmap, wx.ITEM_NORMAL, wx.EmptyString, wx.EmptyString, None ) 
		
		self.ioBoard_toolbar.Realize() 
		
		fgSizer341.Add( self.ioBoard_toolbar, 0, wx.EXPAND, 5 )
		
		self.ioBoard_list = UlcListCtrl( self.m_panel79, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LC_REPORT )
		fgSizer341.Add( self.ioBoard_list, 0, wx.ALL|wx.EXPAND, 5 )
		
		
		self.m_panel79.SetSizer( fgSizer341 )
		self.m_panel79.Layout()
		fgSizer341.Fit( self.m_panel79 )
		self.m_splitter9.SplitVertically( self.m_panel80, self.m_panel79, 361 )
		bSizer33.Add( self.m_splitter9, 1, wx.EXPAND, 5 )
		
		
		self.IoStation_panel.SetSizer( bSizer33 )
		self.IoStation_panel.Layout()
		bSizer33.Fit( self.IoStation_panel )
		sbSizer25.Add( self.IoStation_panel, 1, wx.EXPAND |wx.ALL, 5 )
		
		
		bSizer18.Add( sbSizer25, 1, wx.ALL|wx.EXPAND, 5 )
		
		
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
		self.Bind( wx.EVT_TOOL, self.onCanStationToolClicked, id = canStation_new )
		self.Bind( wx.EVT_TOOL, self.onCanStationToolClicked, id = canStation_edit )
		self.Bind( wx.EVT_TOOL, self.onCanStationToolClicked, id = canStation_del )
		self.canStationList.Bind( wx.EVT_LIST_ITEM_SELECTED, self.onCanStationItemSelected )
		self.Bind( wx.EVT_TOOL, self.onIoBoardToolClicked, id = ioBoard_new )
		self.Bind( wx.EVT_TOOL, self.onIoBoardToolClicked, id = ioBoard_edit )
		self.Bind( wx.EVT_TOOL, self.onIoBoardToolClicked, id = ioBoard_del )
		self.ioBoard_list.Bind( wx.EVT_LIST_ITEM_SELECTED, self.onIoBoardListItemSelected )
		self.m_button6.Bind( wx.EVT_BUTTON, self.onApply )
		self.m_button7.Bind( wx.EVT_BUTTON, self.onCancel )
	
	def __del__( self ):
		pass
	
	
	# Virtual event handlers, overide them in your derived class
	def onCanStationToolClicked( self, event ):
		event.Skip()
	
	
	
	def onCanStationItemSelected( self, event ):
		event.Skip()
	
	def onIoBoardToolClicked( self, event ):
		event.Skip()
	
	
	
	def onIoBoardListItemSelected( self, event ):
		event.Skip()
	
	def onApply( self, event ):
		event.Skip()
	
	def onCancel( self, event ):
		event.Skip()
	
	def m_splitter9OnIdle( self, event ):
		self.m_splitter9.SetSashPosition( 361 )
		self.m_splitter9.Unbind( wx.EVT_IDLE )
	

###########################################################################
## Class Panel_Manage_Action_Base
###########################################################################

class Panel_Manage_Action_Base ( wx.Panel ):
	
	def __init__( self, parent ):
		wx.Panel.__init__ ( self, parent, id = wx.ID_ANY, pos = wx.DefaultPosition, size = wx.Size( 698,429 ), style = wx.TAB_TRAVERSAL )
		
		fgSizer4 = wx.FlexGridSizer( 2, 1, 0, 0 )
		fgSizer4.AddGrowableCol( 0 )
		fgSizer4.AddGrowableCol( 1 )
		fgSizer4.AddGrowableRow( 0 )
		fgSizer4.SetFlexibleDirection( wx.BOTH )
		fgSizer4.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )
		
		bSizer18 = wx.BoxSizer( wx.VERTICAL )
		
		sbSizer26 = wx.StaticBoxSizer( wx.StaticBox( self, wx.ID_ANY, wx.EmptyString ), wx.VERTICAL )
		
		self.IoStation_panel = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer33 = wx.BoxSizer( wx.VERTICAL )
		
		self.m_splitter9 = wx.SplitterWindow( self.IoStation_panel, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.SP_3D )
		self.m_splitter9.Bind( wx.EVT_IDLE, self.m_splitter9OnIdle )
		
		self.m_panel80 = wx.Panel( self.m_splitter9, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		fgSizer34 = wx.FlexGridSizer( 2, 0, 0, 0 )
		fgSizer34.AddGrowableCol( 0 )
		fgSizer34.AddGrowableCol( 1 )
		fgSizer34.AddGrowableRow( 1 )
		fgSizer34.SetFlexibleDirection( wx.BOTH )
		fgSizer34.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )
		
		self.actionGrp_toolbar = wx.ToolBar( self.m_panel80, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TB_HORIZONTAL ) 
		self.actionGrp_toolbar.AddLabelTool( actionGrp_new, _(u"tool"), wx.ArtProvider.GetBitmap( wx.ART_NEW, wx.ART_TOOLBAR ), wx.NullBitmap, wx.ITEM_NORMAL, wx.EmptyString, wx.EmptyString, None ) 
		
		self.actionGrp_toolbar.AddLabelTool( actionGrp_edit, _(u"tool"), wx.ArtProvider.GetBitmap( wx.ART_EXECUTABLE_FILE, wx.ART_TOOLBAR ), wx.NullBitmap, wx.ITEM_NORMAL, wx.EmptyString, wx.EmptyString, None ) 
		
		self.actionGrp_toolbar.AddLabelTool( actionGrp_del, _(u"tool"), wx.ArtProvider.GetBitmap( wx.ART_DELETE, wx.ART_TOOLBAR ), wx.NullBitmap, wx.ITEM_NORMAL, wx.EmptyString, wx.EmptyString, None ) 
		
		self.actionGrp_toolbar.AddSeparator()
		
		self.actionGrp_toolbar.Realize() 
		
		fgSizer34.Add( self.actionGrp_toolbar, 0, wx.EXPAND, 5 )
		
		self.actionGrpList = UlcListCtrl( self.m_panel80, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LC_REPORT )
		fgSizer34.Add( self.actionGrpList, 0, wx.ALL|wx.EXPAND, 5 )
		
		
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
		
		self.action_toolbar.AddLabelTool( action_edit, _(u"tool"), wx.ArtProvider.GetBitmap( wx.ART_EXECUTABLE_FILE, wx.ART_TOOLBAR ), wx.NullBitmap, wx.ITEM_NORMAL, wx.EmptyString, wx.EmptyString, None ) 
		
		self.action_toolbar.AddLabelTool( action_del, _(u"tool"), wx.ArtProvider.GetBitmap( wx.ART_DELETE, wx.ART_TOOLBAR ), wx.NullBitmap, wx.ITEM_NORMAL, wx.EmptyString, wx.EmptyString, None ) 
		
		self.action_toolbar.Realize() 
		
		fgSizer341.Add( self.action_toolbar, 0, wx.EXPAND, 5 )
		
		self.action_list = UlcListCtrl( self.m_panel79, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LC_REPORT )
		fgSizer341.Add( self.action_list, 0, wx.ALL|wx.EXPAND, 5 )
		
		
		self.m_panel79.SetSizer( fgSizer341 )
		self.m_panel79.Layout()
		fgSizer341.Fit( self.m_panel79 )
		self.m_splitter9.SplitVertically( self.m_panel80, self.m_panel79, 200 )
		bSizer33.Add( self.m_splitter9, 1, wx.EXPAND, 5 )
		
		
		self.IoStation_panel.SetSizer( bSizer33 )
		self.IoStation_panel.Layout()
		bSizer33.Fit( self.IoStation_panel )
		sbSizer26.Add( self.IoStation_panel, 1, wx.EXPAND |wx.ALL, 5 )
		
		
		bSizer18.Add( sbSizer26, 1, wx.ALL|wx.EXPAND, 5 )
		
		
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
		self.Bind( wx.EVT_TOOL, self.onActionGrpToolClicked, id = actionGrp_new )
		self.Bind( wx.EVT_TOOL, self.onActionGrpToolClicked, id = actionGrp_edit )
		self.Bind( wx.EVT_TOOL, self.onActionGrpToolClicked, id = actionGrp_del )
		self.actionGrpList.Bind( wx.EVT_LIST_ITEM_SELECTED, self.onActionGrpItemSelected )
		self.Bind( wx.EVT_TOOL, self.onActionToolClicked, id = action_new )
		self.Bind( wx.EVT_TOOL, self.onActionToolClicked, id = action_edit )
		self.Bind( wx.EVT_TOOL, self.onActionToolClicked, id = action_del )
		self.action_list.Bind( wx.EVT_LIST_ITEM_SELECTED, self.onActionItemSelected )
		self.m_button6.Bind( wx.EVT_BUTTON, self.onApply )
		self.m_button7.Bind( wx.EVT_BUTTON, self.onCancel )
	
	def __del__( self ):
		pass
	
	
	# Virtual event handlers, overide them in your derived class
	def onActionGrpToolClicked( self, event ):
		event.Skip()
	
	
	
	def onActionGrpItemSelected( self, event ):
		event.Skip()
	
	def onActionToolClicked( self, event ):
		event.Skip()
	
	
	
	def onActionItemSelected( self, event ):
		event.Skip()
	
	def onApply( self, event ):
		event.Skip()
	
	def onCancel( self, event ):
		event.Skip()
	
	def m_splitter9OnIdle( self, event ):
		self.m_splitter9.SetSashPosition( 200 )
		self.m_splitter9.Unbind( wx.EVT_IDLE )
	

###########################################################################
## Class Panel_Manage_IO_Node_Base1
###########################################################################

class Panel_Manage_IO_Node_Base1 ( wx.Panel ):
	
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
		self.IoStation_panel = wx.Panel( self.m_notebook4, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer33 = wx.BoxSizer( wx.VERTICAL )
		
		self.m_splitter9 = wx.SplitterWindow( self.IoStation_panel, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.SP_3D )
		self.m_splitter9.Bind( wx.EVT_IDLE, self.m_splitter9OnIdle )
		
		self.m_panel80 = wx.Panel( self.m_splitter9, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.RAISED_BORDER|wx.TAB_TRAVERSAL )
		fgSizer34 = wx.FlexGridSizer( 0, 0, 0, 0 )
		fgSizer34.AddGrowableCol( 0 )
		fgSizer34.AddGrowableRow( 0 )
		fgSizer34.SetFlexibleDirection( wx.BOTH )
		fgSizer34.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )
		
		self.io_category_tree = wx.TreeCtrl( self.m_panel80, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TR_DEFAULT_STYLE|wx.TR_LINES_AT_ROOT )
		fgSizer34.Add( self.io_category_tree, 0, wx.ALL|wx.EXPAND, 5 )
		
		
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
		
		self.ioNode_toolbar = wx.ToolBar( self.m_panel79, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TB_HORIZONTAL ) 
		self.ioNode_toolbar.AddLabelTool( IO_NODE_NEW, _(u"tool"), wx.ArtProvider.GetBitmap( wx.ART_NEW, wx.ART_TOOLBAR ), wx.NullBitmap, wx.ITEM_NORMAL, wx.EmptyString, wx.EmptyString, None ) 
		
		self.ioNode_toolbar.AddLabelTool( IO_NODE_EDIT, _(u"tool"), wx.ArtProvider.GetBitmap( wx.ART_EXECUTABLE_FILE, wx.ART_TOOLBAR ), wx.NullBitmap, wx.ITEM_NORMAL, wx.EmptyString, wx.EmptyString, None ) 
		
		self.ioNode_toolbar.AddLabelTool( IO_NODE_DEL, _(u"tool"), wx.ArtProvider.GetBitmap( wx.ART_DELETE, wx.ART_TOOLBAR ), wx.NullBitmap, wx.ITEM_NORMAL, wx.EmptyString, wx.EmptyString, None ) 
		
		self.ioNode_toolbar.AddSeparator()
		
		self.ioNode_toolbar.Realize() 
		
		fgSizer341.Add( self.ioNode_toolbar, 0, wx.EXPAND, 5 )
		
		self.ioNode_list = UlcListCtrl( self.m_panel79, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LC_REPORT )
		fgSizer341.Add( self.ioNode_list, 0, wx.ALL|wx.EXPAND, 5 )
		
		
		self.m_panel79.SetSizer( fgSizer341 )
		self.m_panel79.Layout()
		fgSizer341.Fit( self.m_panel79 )
		self.m_splitter9.SplitVertically( self.m_panel80, self.m_panel79, 361 )
		bSizer33.Add( self.m_splitter9, 1, wx.EXPAND, 5 )
		
		
		self.IoStation_panel.SetSizer( bSizer33 )
		self.IoStation_panel.Layout()
		bSizer33.Fit( self.IoStation_panel )
		self.m_notebook4.AddPage( self.IoStation_panel, _(u"控制"), True )
		
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
		self.io_category_tree.Bind( wx.EVT_TREE_SEL_CHANGED, self.onCategoryItemSelChanged )
		self.Bind( wx.EVT_TOOL, self.onIoNodeToolClicked, id = IO_NODE_NEW )
		self.Bind( wx.EVT_TOOL, self.onIoNodeToolClicked, id = IO_NODE_EDIT )
		self.Bind( wx.EVT_TOOL, self.onIoNodeToolClicked, id = IO_NODE_DEL )
		self.ioNode_list.Bind( wx.EVT_LIST_ITEM_SELECTED, self.onIoNodeListItemSelected )
		self.m_button6.Bind( wx.EVT_BUTTON, self.onApply )
		self.m_button7.Bind( wx.EVT_BUTTON, self.onCancel )
	
	def __del__( self ):
		pass
	
	
	# Virtual event handlers, overide them in your derived class
	def onCategoryItemSelChanged( self, event ):
		event.Skip()
	
	def onIoNodeToolClicked( self, event ):
		event.Skip()
	
	
	
	def onIoNodeListItemSelected( self, event ):
		event.Skip()
	
	def onApply( self, event ):
		event.Skip()
	
	def onCancel( self, event ):
		event.Skip()
	
	def m_splitter9OnIdle( self, event ):
		self.m_splitter9.SetSashPosition( 361 )
		self.m_splitter9.Unbind( wx.EVT_IDLE )
	

###########################################################################
## Class Panel_Manage_IO_Node_Base
###########################################################################

class Panel_Manage_IO_Node_Base ( wx.Panel ):
	
	def __init__( self, parent ):
		wx.Panel.__init__ ( self, parent, id = wx.ID_ANY, pos = wx.DefaultPosition, size = wx.Size( 698,429 ), style = wx.TAB_TRAVERSAL )
		
		fgSizer4 = wx.FlexGridSizer( 2, 1, 0, 0 )
		fgSizer4.AddGrowableCol( 0 )
		fgSizer4.AddGrowableCol( 1 )
		fgSizer4.AddGrowableRow( 0 )
		fgSizer4.SetFlexibleDirection( wx.BOTH )
		fgSizer4.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )
		
		bSizer18 = wx.BoxSizer( wx.VERTICAL )
		
		sbSizer24 = wx.StaticBoxSizer( wx.StaticBox( self, wx.ID_ANY, wx.EmptyString ), wx.VERTICAL )
		
		self.IoStation_panel = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer33 = wx.BoxSizer( wx.VERTICAL )
		
		self.m_splitter9 = wx.SplitterWindow( self.IoStation_panel, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.SP_3D )
		self.m_splitter9.SetSashGravity( 0 )
		self.m_splitter9.Bind( wx.EVT_IDLE, self.m_splitter9OnIdle )
		
		self.m_panel80 = wx.Panel( self.m_splitter9, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.STATIC_BORDER|wx.TAB_TRAVERSAL )
		fgSizer34 = wx.FlexGridSizer( 0, 0, 0, 0 )
		fgSizer34.AddGrowableCol( 0 )
		fgSizer34.AddGrowableRow( 0 )
		fgSizer34.SetFlexibleDirection( wx.BOTH )
		fgSizer34.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )
		
		self.io_category_tree = CustomTreeCtrl( self.m_panel80, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TR_DEFAULT_STYLE|wx.TR_LINES_AT_ROOT )
		fgSizer34.Add( self.io_category_tree, 0, wx.ALL|wx.EXPAND, 5 )
		
		
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
		
		self.ioNode_toolbar = wx.ToolBar( self.m_panel79, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TB_HORIZONTAL ) 
		self.ioNode_toolbar.AddLabelTool( IO_NODE_NEW, _(u"tool"), wx.ArtProvider.GetBitmap( wx.ART_NEW, wx.ART_TOOLBAR ), wx.NullBitmap, wx.ITEM_NORMAL, wx.EmptyString, wx.EmptyString, None ) 
		
		self.ioNode_toolbar.AddLabelTool( IO_NODE_EDIT, _(u"tool"), wx.ArtProvider.GetBitmap( wx.ART_EXECUTABLE_FILE, wx.ART_TOOLBAR ), wx.NullBitmap, wx.ITEM_NORMAL, wx.EmptyString, wx.EmptyString, None ) 
		
		self.ioNode_toolbar.AddLabelTool( IO_NODE_DEL, _(u"tool"), wx.ArtProvider.GetBitmap( wx.ART_DELETE, wx.ART_TOOLBAR ), wx.NullBitmap, wx.ITEM_NORMAL, wx.EmptyString, wx.EmptyString, None ) 
		
		self.ioNode_toolbar.AddSeparator()
		
		self.ioNode_toolbar.Realize() 
		
		fgSizer341.Add( self.ioNode_toolbar, 0, wx.EXPAND, 5 )
		
		self.ioNode_list = UlcListCtrl( self.m_panel79, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LC_REPORT )
		fgSizer341.Add( self.ioNode_list, 0, wx.ALL|wx.EXPAND, 5 )
		
		
		self.m_panel79.SetSizer( fgSizer341 )
		self.m_panel79.Layout()
		fgSizer341.Fit( self.m_panel79 )
		self.m_splitter9.SplitVertically( self.m_panel80, self.m_panel79, 150 )
		bSizer33.Add( self.m_splitter9, 1, wx.EXPAND, 5 )
		
		
		self.IoStation_panel.SetSizer( bSizer33 )
		self.IoStation_panel.Layout()
		bSizer33.Fit( self.IoStation_panel )
		sbSizer24.Add( self.IoStation_panel, 1, wx.EXPAND |wx.ALL, 5 )
		
		
		bSizer18.Add( sbSizer24, 1, wx.ALL|wx.EXPAND, 5 )
		
		
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
		self.io_category_tree.Bind( wx.EVT_TREE_SEL_CHANGED, self.onCategoryItemSelChanged )
		self.Bind( wx.EVT_TOOL, self.onIoNodeToolClicked, id = IO_NODE_NEW )
		self.Bind( wx.EVT_TOOL, self.onIoNodeToolClicked, id = IO_NODE_EDIT )
		self.Bind( wx.EVT_TOOL, self.onIoNodeToolClicked, id = IO_NODE_DEL )
		self.ioNode_list.Bind( wx.EVT_LIST_ITEM_SELECTED, self.onIoNodeListItemSelected )
		self.m_button6.Bind( wx.EVT_BUTTON, self.onApply )
		self.m_button7.Bind( wx.EVT_BUTTON, self.onCancel )
	
	def __del__( self ):
		pass
	
	
	# Virtual event handlers, overide them in your derived class
	def onCategoryItemSelChanged( self, event ):
		event.Skip()
	
	def onIoNodeToolClicked( self, event ):
		event.Skip()
	
	
	
	def onIoNodeListItemSelected( self, event ):
		event.Skip()
	
	def onApply( self, event ):
		event.Skip()
	
	def onCancel( self, event ):
		event.Skip()
	
	def m_splitter9OnIdle( self, event ):
		self.m_splitter9.SetSashPosition( 150 )
		self.m_splitter9.Unbind( wx.EVT_IDLE )
	

###########################################################################
## Class Panel_EditAction_Base2
###########################################################################

class Panel_EditAction_Base2 ( wx.Panel ):
	
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
		self.addOutputBtn.Bind( wx.EVT_BUTTON, self.onAddModuleIO )
		self.addFeedbackBtn.Bind( wx.EVT_BUTTON, self.onAddModuleIO )
		self.m_button40.Bind( wx.EVT_BUTTON, self.onApply )
		self.m_button41.Bind( wx.EVT_BUTTON, self.onCancel )
	
	def __del__( self ):
		pass
	
	
	# Virtual event handlers, overide them in your derived class
	def onChoice( self, event ):
		event.Skip()
	
	def onAddModuleIO( self, event ):
		event.Skip()
	
	
	def onApply( self, event ):
		event.Skip()
	
	def onCancel( self, event ):
		event.Skip()
	

###########################################################################
## Class Panel_IoBoard_Base
###########################################################################

class Panel_IoBoard_Base ( wx.Panel ):
	
	def __init__( self, parent ):
		wx.Panel.__init__ ( self, parent, id = wx.ID_ANY, pos = wx.DefaultPosition, size = wx.Size( 344,211 ), style = wx.TAB_TRAVERSAL )
		
		fgSizer86 = wx.FlexGridSizer( 2, 1, 0, 0 )
		fgSizer86.AddGrowableCol( 0 )
		fgSizer86.AddGrowableRow( 0 )
		fgSizer86.SetFlexibleDirection( wx.BOTH )
		fgSizer86.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )
		
		self.mainSizer = wx.FlexGridSizer( 0, 1, 0, 0 )
		self.mainSizer.SetFlexibleDirection( wx.BOTH )
		self.mainSizer.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )
		
		bSizer57 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.m_staticText47 = wx.StaticText( self, wx.ID_ANY, _(u"子板类型:"), wx.DefaultPosition, wx.Size( 70,-1 ), 0 )
		self.m_staticText47.Wrap( -1 )
		bSizer57.Add( self.m_staticText47, 1, wx.ALIGN_CENTER|wx.ALL, 5 )
		
		boardType_choiceChoices = [ _(u"信号量输出"), _(u"信号量输入") ]
		self.boardType_choice = wx.Choice( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, boardType_choiceChoices, 0 )
		self.boardType_choice.SetSelection( 0 )
		bSizer57.Add( self.boardType_choice, 2, wx.ALIGN_CENTER|wx.ALL|wx.EXPAND, 5 )
		
		
		self.mainSizer.Add( bSizer57, 0, wx.BOTTOM, 15 )
		
		bSizer571 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.m_staticText731 = wx.StaticText( self, wx.ID_ANY, _(u"子板编号:"), wx.DefaultPosition, wx.Size( 70,-1 ), 0 )
		self.m_staticText731.Wrap( -1 )
		bSizer571.Add( self.m_staticText731, 0, wx.ALL, 5 )
		
		self.boardId_text = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer571.Add( self.boardId_text, 0, wx.ALL, 5 )
		
		
		self.mainSizer.Add( bSizer571, 1, wx.EXPAND, 5 )
		
		
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
		self.boardType_choice.Bind( wx.EVT_CHOICE, self.onIoBoardTypeChoice )
		self.m_button40.Bind( wx.EVT_BUTTON, self.onApply )
		self.m_button41.Bind( wx.EVT_BUTTON, self.onCancel )
	
	def __del__( self ):
		pass
	
	
	# Virtual event handlers, overide them in your derived class
	def onIoBoardTypeChoice( self, event ):
		event.Skip()
	
	def onApply( self, event ):
		event.Skip()
	
	def onCancel( self, event ):
		event.Skip()
	

###########################################################################
## Class Panel_EditAttribute_Base
###########################################################################

class Panel_EditAttribute_Base ( wx.Panel ):
	
	def __init__( self, parent ):
		wx.Panel.__init__ ( self, parent, id = wx.ID_ANY, pos = wx.DefaultPosition, size = wx.Size( 350,200 ), style = wx.TAB_TRAVERSAL )
		
		self.SetMinSize( wx.Size( 350,200 ) )
		self.SetMaxSize( wx.Size( 350,200 ) )
		
		fgSizer86 = wx.FlexGridSizer( 1, 1, 0, 0 )
		fgSizer86.AddGrowableCol( 0 )
		fgSizer86.AddGrowableRow( 0 )
		fgSizer86.SetFlexibleDirection( wx.BOTH )
		fgSizer86.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )
		
		self.sizer2 = wx.StaticBoxSizer( wx.StaticBox( self, wx.ID_ANY, wx.EmptyString ), wx.HORIZONTAL )
		
		fgSizer70 = wx.FlexGridSizer( 1, 2, 0, 0 )
		fgSizer70.AddGrowableCol( 1 )
		fgSizer70.SetFlexibleDirection( wx.BOTH )
		fgSizer70.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )
		
		self.m_staticText44 = wx.StaticText( self, wx.ID_ANY, _(u"变量名："), wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText44.Wrap( -1 )
		fgSizer70.Add( self.m_staticText44, 0, wx.ALL, 5 )
		
		self.text_name = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer70.Add( self.text_name, 0, wx.ALL|wx.EXPAND|wx.FIXED_MINSIZE, 5 )
		
		self.m_staticText441 = wx.StaticText( self, wx.ID_ANY, _(u"描 述："), wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText441.Wrap( -1 )
		fgSizer70.Add( self.m_staticText441, 0, wx.ALL, 5 )
		
		self.text_desc = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer70.Add( self.text_desc, 0, wx.ALL|wx.EXPAND, 5 )
		
		self.m_staticText36 = wx.StaticText( self, wx.ID_ANY, _(u"类 型："), wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText36.Wrap( -1 )
		fgSizer70.Add( self.m_staticText36, 0, wx.ALL, 5 )
		
		m_choice11Choices = []
		self.m_choice11 = wx.Choice( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, m_choice11Choices, 0 )
		self.m_choice11.SetSelection( 0 )
		fgSizer70.Add( self.m_choice11, 0, wx.ALL|wx.EXPAND, 5 )
		
		
		self.sizer2.Add( fgSizer70, 1, wx.EXPAND, 5 )
		
		
		fgSizer86.Add( self.sizer2, 1, wx.ALIGN_CENTER_HORIZONTAL|wx.ALL|wx.EXPAND, 10 )
		
		gSizer15 = wx.GridSizer( 0, 2, 0, 0 )
		
		self.m_button40 = wx.Button( self, wx.ID_ANY, _(u"Apply"), wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer15.Add( self.m_button40, 0, wx.ALIGN_RIGHT|wx.ALL, 5 )
		
		self.m_button41 = wx.Button( self, wx.ID_ANY, _(u"Cancel"), wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer15.Add( self.m_button41, 0, wx.ALL, 5 )
		
		
		fgSizer86.Add( gSizer15, 1, wx.EXPAND|wx.BOTTOM, 10 )
		
		
		self.SetSizer( fgSizer86 )
		self.Layout()
		
		# Connect Events
		self.m_button40.Bind( wx.EVT_BUTTON, self.onApply )
		self.m_button41.Bind( wx.EVT_BUTTON, self.onCancel )
	
	def __del__( self ):
		pass
	
	
	# Virtual event handlers, overide them in your derived class
	def onApply( self, event ):
		event.Skip()
	
	def onCancel( self, event ):
		event.Skip()
	

###########################################################################
## Class Panel_Edit_Action_Group_Base
###########################################################################

class Panel_Edit_Action_Group_Base ( wx.Panel ):
	
	def __init__( self, parent ):
		wx.Panel.__init__ ( self, parent, id = wx.ID_ANY, pos = wx.DefaultPosition, size = wx.Size( 350,180 ), style = wx.TAB_TRAVERSAL )
		
		self.SetMinSize( wx.Size( 350,180 ) )
		self.SetMaxSize( wx.Size( 350,200 ) )
		
		fgSizer86 = wx.FlexGridSizer( 1, 1, 0, 0 )
		fgSizer86.AddGrowableCol( 0 )
		fgSizer86.AddGrowableRow( 0 )
		fgSizer86.SetFlexibleDirection( wx.BOTH )
		fgSizer86.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )
		
		self.sizer2 = wx.StaticBoxSizer( wx.StaticBox( self, wx.ID_ANY, wx.EmptyString ), wx.HORIZONTAL )
		
		fgSizer70 = wx.FlexGridSizer( 1, 2, 0, 0 )
		fgSizer70.AddGrowableCol( 1 )
		fgSizer70.SetFlexibleDirection( wx.BOTH )
		fgSizer70.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )
		
		self.m_staticText44 = wx.StaticText( self, wx.ID_ANY, _(u"动作脚本："), wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText44.Wrap( -1 )
		fgSizer70.Add( self.m_staticText44, 0, wx.ALL, 5 )
		
		self.actGrpName_txt = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer70.Add( self.actGrpName_txt, 0, wx.ALL|wx.EXPAND|wx.FIXED_MINSIZE, 5 )
		
		self.m_staticText441 = wx.StaticText( self, wx.ID_ANY, _(u"描 述："), wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText441.Wrap( -1 )
		fgSizer70.Add( self.m_staticText441, 0, wx.ALL, 5 )
		
		self.actDesc_txt = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer70.Add( self.actDesc_txt, 0, wx.ALL|wx.EXPAND, 5 )
		
		
		self.sizer2.Add( fgSizer70, 1, wx.EXPAND, 5 )
		
		
		fgSizer86.Add( self.sizer2, 1, wx.ALIGN_CENTER_HORIZONTAL|wx.ALL|wx.EXPAND, 10 )
		
		gSizer15 = wx.GridSizer( 0, 2, 0, 0 )
		
		self.m_button40 = wx.Button( self, wx.ID_ANY, _(u"Apply"), wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer15.Add( self.m_button40, 0, wx.ALIGN_RIGHT|wx.ALL, 5 )
		
		self.m_button41 = wx.Button( self, wx.ID_ANY, _(u"Cancel"), wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer15.Add( self.m_button41, 0, wx.ALL, 5 )
		
		
		fgSizer86.Add( gSizer15, 1, wx.EXPAND|wx.BOTTOM, 10 )
		
		
		self.SetSizer( fgSizer86 )
		self.Layout()
		
		# Connect Events
		self.m_button40.Bind( wx.EVT_BUTTON, self.onApply )
		self.m_button41.Bind( wx.EVT_BUTTON, self.onCancel )
	
	def __del__( self ):
		pass
	
	
	# Virtual event handlers, overide them in your derived class
	def onApply( self, event ):
		event.Skip()
	
	def onCancel( self, event ):
		event.Skip()
	

###########################################################################
## Class Panel_EditAction_Base
###########################################################################

class Panel_EditAction_Base ( wx.Panel ):
	
	def __init__( self, parent ):
		wx.Panel.__init__ ( self, parent, id = wx.ID_ANY, pos = wx.DefaultPosition, size = wx.Size( 333,483 ), style = wx.TAB_TRAVERSAL )
		
		fgSizer86 = wx.FlexGridSizer( 2, 1, 0, 0 )
		fgSizer86.AddGrowableCol( 0 )
		fgSizer86.AddGrowableRow( 0 )
		fgSizer86.SetFlexibleDirection( wx.BOTH )
		fgSizer86.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )
		
		self.mainSizer = wx.FlexGridSizer( 0, 1, 0, 0 )
		self.mainSizer.AddGrowableCol( 0 )
		self.mainSizer.SetFlexibleDirection( wx.BOTH )
		self.mainSizer.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )
		
		bSizer57 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.m_staticText47 = wx.StaticText( self, wx.ID_ANY, _(u"动作类型:"), wx.DefaultPosition, wx.Size( 70,-1 ), 0 )
		self.m_staticText47.Wrap( -1 )
		bSizer57.Add( self.m_staticText47, 1, wx.ALIGN_CENTER|wx.ALL, 5 )
		
		actionType_choiceChoices = [ _(u"信号输出"), _(u"延时等待"), _(u"变量设置") ]
		self.actionType_choice = wx.Choice( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, actionType_choiceChoices, 0 )
		self.actionType_choice.SetSelection( 0 )
		bSizer57.Add( self.actionType_choice, 2, wx.ALIGN_CENTER|wx.ALL|wx.EXPAND, 5 )
		
		
		self.mainSizer.Add( bSizer57, 0, wx.BOTTOM, 15 )
		
		self.sizeTimeDelay = wx.StaticBoxSizer( wx.StaticBox( self, wx.ID_ANY, _(u"延时") ), wx.HORIZONTAL )
		
		self.m_staticText73 = wx.StaticText( self, wx.ID_ANY, _(u"延时时间(秒):"), wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText73.Wrap( -1 )
		self.sizeTimeDelay.Add( self.m_staticText73, 0, wx.ALL, 5 )
		
		self.delayTime_txt = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.sizeTimeDelay.Add( self.delayTime_txt, 0, wx.ALL, 5 )
		
		
		self.mainSizer.Add( self.sizeTimeDelay, 1, wx.ALL|wx.EXPAND, 5 )
		
		self.SizerIO = wx.BoxSizer( wx.VERTICAL )
		
		self.sizer1 = wx.StaticBoxSizer( wx.StaticBox( self, wx.ID_ANY, _(u"动作输出") ), wx.VERTICAL )
		
		fgSizer68 = wx.FlexGridSizer( 0, 3, 0, 0 )
		fgSizer68.AddGrowableCol( 1 )
		fgSizer68.SetFlexibleDirection( wx.BOTH )
		fgSizer68.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )
		
		self.m_staticText42 = wx.StaticText( self, wx.ID_ANY, _(u"输出点:"), wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText42.Wrap( -1 )
		fgSizer68.Add( self.m_staticText42, 1, wx.ALL, 5 )
		
		self.output_txt = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer68.Add( self.output_txt, 0, wx.ALL|wx.EXPAND, 5 )
		
		self.selOutputBtn = wx.BitmapButton( self, wx.ID_ANY, wx.ArtProvider.GetBitmap( wx.ART_NEW, wx.ART_BUTTON ), wx.DefaultPosition, wx.DefaultSize, wx.BU_AUTODRAW )
		fgSizer68.Add( self.selOutputBtn, 0, wx.ALL, 5 )
		
		self.m_staticText43 = wx.StaticText( self, wx.ID_ANY, _(u"输出值:"), wx.DefaultPosition, wx.Size( 70,-1 ), 0 )
		self.m_staticText43.Wrap( -1 )
		fgSizer68.Add( self.m_staticText43, 0, wx.ALIGN_CENTER|wx.ALL|wx.LEFT|wx.RIGHT, 5 )
		
		self.outVal_txt = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer68.Add( self.outVal_txt, 0, wx.ALL, 5 )
		
		
		self.sizer1.Add( fgSizer68, 0, wx.EXPAND, 5 )
		
		
		self.SizerIO.Add( self.sizer1, 0, wx.EXPAND, 5 )
		
		self.sizer2 = wx.StaticBoxSizer( wx.StaticBox( self, wx.ID_ANY, _(u"动作反馈") ), wx.VERTICAL )
		
		bSizer49 = wx.BoxSizer( wx.VERTICAL )
		
		self.needFeedback_cb = wx.CheckBox( self, wx.ID_ANY, _(u"检测反馈信号"), wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer49.Add( self.needFeedback_cb, 0, wx.ALL, 5 )
		
		fgSizer70 = wx.FlexGridSizer( 2, 3, 0, 0 )
		fgSizer70.AddGrowableCol( 1 )
		fgSizer70.SetFlexibleDirection( wx.BOTH )
		fgSizer70.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )
		
		self.m_staticText44 = wx.StaticText( self, wx.ID_ANY, _(u"输入点:"), wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText44.Wrap( -1 )
		fgSizer70.Add( self.m_staticText44, 0, wx.ALL, 5 )
		
		self.feedback_txt = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer70.Add( self.feedback_txt, 0, wx.ALL|wx.EXPAND, 5 )
		
		self.selFeedbackBtn = wx.BitmapButton( self, wx.ID_ANY, wx.ArtProvider.GetBitmap( wx.ART_NEW, wx.ART_BUTTON ), wx.DefaultPosition, wx.DefaultSize, wx.BU_AUTODRAW )
		fgSizer70.Add( self.selFeedbackBtn, 0, wx.ALL, 5 )
		
		self.m_staticText46 = wx.StaticText( self, wx.ID_ANY, _(u"超时(秒)："), wx.DefaultPosition, wx.Size( 70,-1 ), 0 )
		self.m_staticText46.Wrap( -1 )
		fgSizer70.Add( self.m_staticText46, 0, wx.ALL, 5 )
		
		self.feedbackTimeout_txt = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer70.Add( self.feedbackTimeout_txt, 0, wx.ALL, 5 )
		
		
		bSizer49.Add( fgSizer70, 1, wx.EXPAND, 5 )
		
		
		self.sizer2.Add( bSizer49, 1, wx.EXPAND, 5 )
		
		
		self.SizerIO.Add( self.sizer2, 1, wx.EXPAND, 5 )
		
		
		self.mainSizer.Add( self.SizerIO, 1, wx.ALL|wx.EXPAND, 5 )
		
		self.SizerAttr = wx.BoxSizer( wx.VERTICAL )
		
		self.sizer11 = wx.StaticBoxSizer( wx.StaticBox( self, wx.ID_ANY, _(u"变量设置") ), wx.VERTICAL )
		
		fgSizer681 = wx.FlexGridSizer( 0, 3, 0, 0 )
		fgSizer681.AddGrowableCol( 1 )
		fgSizer681.SetFlexibleDirection( wx.BOTH )
		fgSizer681.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )
		
		self.m_staticText421 = wx.StaticText( self, wx.ID_ANY, _(u"变 量"), wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText421.Wrap( -1 )
		fgSizer681.Add( self.m_staticText421, 1, wx.ALL, 5 )
		
		self.internalVal_txt = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer681.Add( self.internalVal_txt, 0, wx.ALL|wx.EXPAND, 5 )
		
		self.selInternalVal = wx.BitmapButton( self, wx.ID_ANY, wx.ArtProvider.GetBitmap( wx.ART_NEW, wx.ART_BUTTON ), wx.DefaultPosition, wx.DefaultSize, wx.BU_AUTODRAW )
		fgSizer681.Add( self.selInternalVal, 0, wx.ALL, 5 )
		
		self.m_staticText431 = wx.StaticText( self, wx.ID_ANY, _(u"输出值:"), wx.DefaultPosition, wx.Size( 70,-1 ), 0 )
		self.m_staticText431.Wrap( -1 )
		fgSizer681.Add( self.m_staticText431, 0, wx.ALIGN_CENTER|wx.ALL|wx.LEFT|wx.RIGHT, 5 )
		
		self.outPutVal_txt = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer681.Add( self.outPutVal_txt, 0, wx.ALL, 5 )
		
		
		self.sizer11.Add( fgSizer681, 0, wx.EXPAND, 5 )
		
		
		self.SizerAttr.Add( self.sizer11, 1, wx.EXPAND, 5 )
		
		
		self.mainSizer.Add( self.SizerAttr, 1, wx.ALL|wx.EXPAND, 5 )
		
		
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
		self.actionType_choice.Bind( wx.EVT_CHOICE, self.onChoice )
		self.selOutputBtn.Bind( wx.EVT_BUTTON, self.onSelectOutput )
		self.selFeedbackBtn.Bind( wx.EVT_BUTTON, self.onSelectInput )
		self.selInternalVal.Bind( wx.EVT_BUTTON, self.onSelectInternal )
		self.m_button40.Bind( wx.EVT_BUTTON, self.onApply )
		self.m_button41.Bind( wx.EVT_BUTTON, self.onCancel )
	
	def __del__( self ):
		pass
	
	
	# Virtual event handlers, overide them in your derived class
	def onChoice( self, event ):
		event.Skip()
	
	def onSelectOutput( self, event ):
		event.Skip()
	
	def onSelectInput( self, event ):
		event.Skip()
	
	def onSelectInternal( self, event ):
		event.Skip()
	
	def onApply( self, event ):
		event.Skip()
	
	def onCancel( self, event ):
		event.Skip()
	

###########################################################################
## Class Panel_ButtonSetting_Base
###########################################################################

class Panel_ButtonSetting_Base ( wx.Panel ):
	
	def __init__( self, parent ):
		wx.Panel.__init__ ( self, parent, id = wx.ID_ANY, pos = wx.DefaultPosition, size = wx.Size( 300,207 ), style = wx.TAB_TRAVERSAL )
		
		fgSizer33 = wx.FlexGridSizer( 2, 1, 0, 0 )
		fgSizer33.AddGrowableCol( 0 )
		fgSizer33.AddGrowableRow( 0 )
		fgSizer33.SetFlexibleDirection( wx.BOTH )
		fgSizer33.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )
		
		fgSizer34 = wx.FlexGridSizer( 2, 1, 0, 0 )
		fgSizer34.AddGrowableCol( 0 )
		fgSizer34.SetFlexibleDirection( wx.BOTH )
		fgSizer34.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )
		
		sbSizer13 = wx.StaticBoxSizer( wx.StaticBox( self, wx.ID_ANY, _(u"按钮开启") ), wx.HORIZONTAL )
		
		fgSizer35 = wx.FlexGridSizer( 1, 3, 0, 0 )
		fgSizer35.AddGrowableCol( 1 )
		fgSizer35.SetFlexibleDirection( wx.BOTH )
		fgSizer35.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )
		
		bSizer42 = wx.BoxSizer( wx.VERTICAL )
		
		self.m_staticText37 = wx.StaticText( self, wx.ID_ANY, _(u"动 作"), wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText37.Wrap( -1 )
		bSizer42.Add( self.m_staticText37, 0, wx.ALL|wx.EXPAND, 5 )
		
		
		fgSizer35.Add( bSizer42, 1, wx.ALL|wx.EXPAND, 5 )
		
		self.txt_oprOn = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.TE_READONLY )
		self.txt_oprOn.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_WINDOW ) )
		
		fgSizer35.Add( self.txt_oprOn, 0, wx.ALL|wx.EXPAND, 5 )
		
		self.m_button27 = wx.Button( self, wx.ID_ANY, _(u"选择"), wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer35.Add( self.m_button27, 0, wx.ALL, 5 )
		
		
		sbSizer13.Add( fgSizer35, 1, wx.EXPAND, 5 )
		
		
		fgSizer34.Add( sbSizer13, 1, wx.ALL|wx.EXPAND, 5 )
		
		sbSizer15 = wx.StaticBoxSizer( wx.StaticBox( self, wx.ID_ANY, _(u"按钮关闭") ), wx.HORIZONTAL )
		
		fgSizer351 = wx.FlexGridSizer( 1, 3, 0, 0 )
		fgSizer351.AddGrowableCol( 1 )
		fgSizer351.SetFlexibleDirection( wx.BOTH )
		fgSizer351.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )
		
		bSizer43 = wx.BoxSizer( wx.VERTICAL )
		
		self.m_staticText371 = wx.StaticText( self, wx.ID_ANY, _(u"动 作"), wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText371.Wrap( -1 )
		bSizer43.Add( self.m_staticText371, 0, wx.ALL, 5 )
		
		
		fgSizer351.Add( bSizer43, 1, wx.ALL|wx.EXPAND, 5 )
		
		self.txt_oprOff = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.TE_READONLY )
		fgSizer351.Add( self.txt_oprOff, 0, wx.ALL|wx.EXPAND, 5 )
		
		self.m_button271 = wx.Button( self, wx.ID_ANY, _(u"选择"), wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer351.Add( self.m_button271, 0, wx.ALL, 5 )
		
		
		sbSizer15.Add( fgSizer351, 1, wx.EXPAND, 5 )
		
		
		fgSizer34.Add( sbSizer15, 1, wx.ALL|wx.EXPAND, 5 )
		
		
		fgSizer33.Add( fgSizer34, 1, wx.ALL|wx.EXPAND, 5 )
		
		gSizer15 = wx.GridSizer( 0, 2, 0, 0 )
		
		self.applyBtn = wx.Button( self, wx.ID_ANY, _(u"Apply"), wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer15.Add( self.applyBtn, 0, wx.ALIGN_RIGHT|wx.ALL, 5 )
		
		self.m_button41 = wx.Button( self, wx.ID_ANY, _(u"Cancel"), wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer15.Add( self.m_button41, 0, wx.ALL, 5 )
		
		
		fgSizer33.Add( gSizer15, 1, wx.BOTTOM|wx.EXPAND, 5 )
		
		
		self.SetSizer( fgSizer33 )
		self.Layout()
		
		# Connect Events
		self.m_button27.Bind( wx.EVT_BUTTON, self.onSelectOperationOn )
		self.m_button271.Bind( wx.EVT_BUTTON, self.onSelectOperationOff )
		self.applyBtn.Bind( wx.EVT_BUTTON, self.onApply )
		self.m_button41.Bind( wx.EVT_BUTTON, self.onCancel )
	
	def __del__( self ):
		pass
	
	
	# Virtual event handlers, overide them in your derived class
	def onSelectOperationOn( self, event ):
		event.Skip()
	
	def onSelectOperationOff( self, event ):
		event.Skip()
	
	def onApply( self, event ):
		event.Skip()
	
	def onCancel( self, event ):
		event.Skip()
	

###########################################################################
## Class Panel_OperationSelect_Base
###########################################################################

class Panel_OperationSelect_Base ( wx.Panel ):
	
	def __init__( self, parent ):
		wx.Panel.__init__ ( self, parent, id = wx.ID_ANY, pos = wx.DefaultPosition, size = wx.Size( 800,600 ), style = wx.TAB_TRAVERSAL )
		
		fgSizer33 = wx.FlexGridSizer( 2, 1, 0, 0 )
		fgSizer33.AddGrowableCol( 0 )
		fgSizer33.AddGrowableRow( 0 )
		fgSizer33.SetFlexibleDirection( wx.BOTH )
		fgSizer33.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )
		
		bSizer36 = wx.BoxSizer( wx.VERTICAL )
		
		self.m_splitter8 = wx.SplitterWindow( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.SP_3D|wx.SP_LIVE_UPDATE )
		self.m_splitter8.SetSashGravity( 0 )
		self.m_splitter8.Bind( wx.EVT_IDLE, self.m_splitter8OnIdle )
		
		self.m_panel26 = wx.Panel( self.m_splitter8, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer38 = wx.BoxSizer( wx.VERTICAL )
		
		sbSizer40 = wx.StaticBoxSizer( wx.StaticBox( self.m_panel26, wx.ID_ANY, _(u"设备") ), wx.VERTICAL )
		
		fgSizer62 = wx.FlexGridSizer( 0, 0, 0, 0 )
		fgSizer62.AddGrowableCol( 0 )
		fgSizer62.AddGrowableRow( 0 )
		fgSizer62.SetFlexibleDirection( wx.BOTH )
		fgSizer62.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )
		
		self.deviceListCtrl = UlcListCtrl( self.m_panel26, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LC_REPORT|wx.LC_SINGLE_SEL )
		fgSizer62.Add( self.deviceListCtrl, 0, wx.ALL|wx.EXPAND, 5 )
		
		
		sbSizer40.Add( fgSizer62, 1, wx.EXPAND, 5 )
		
		
		bSizer38.Add( sbSizer40, 1, wx.ALL|wx.EXPAND, 5 )
		
		
		self.m_panel26.SetSizer( bSizer38 )
		self.m_panel26.Layout()
		bSizer38.Fit( self.m_panel26 )
		self.m_panel27 = wx.Panel( self.m_splitter8, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer37 = wx.BoxSizer( wx.VERTICAL )
		
		sbSizer41 = wx.StaticBoxSizer( wx.StaticBox( self.m_panel27, wx.ID_ANY, _(u"操作") ), wx.VERTICAL )
		
		fgSizer63 = wx.FlexGridSizer( 0, 0, 0, 0 )
		fgSizer63.AddGrowableCol( 0 )
		fgSizer63.AddGrowableRow( 0 )
		fgSizer63.SetFlexibleDirection( wx.BOTH )
		fgSizer63.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )
		
		self.operationList = UlcListCtrl( self.m_panel27, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LC_REPORT|wx.LC_SINGLE_SEL )
		fgSizer63.Add( self.operationList, 0, wx.ALL|wx.EXPAND, 5 )
		
		
		sbSizer41.Add( fgSizer63, 1, wx.EXPAND, 5 )
		
		
		bSizer37.Add( sbSizer41, 1, wx.ALL|wx.EXPAND, 5 )
		
		
		self.m_panel27.SetSizer( bSizer37 )
		self.m_panel27.Layout()
		bSizer37.Fit( self.m_panel27 )
		self.m_splitter8.SplitVertically( self.m_panel26, self.m_panel27, 250 )
		bSizer36.Add( self.m_splitter8, 1, wx.EXPAND, 5 )
		
		
		fgSizer33.Add( bSizer36, 1, wx.EXPAND, 5 )
		
		gSizer15 = wx.GridSizer( 0, 2, 0, 0 )
		
		self.applyBtn = wx.Button( self, wx.ID_ANY, _(u"Apply"), wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer15.Add( self.applyBtn, 0, wx.ALIGN_RIGHT|wx.ALL, 5 )
		
		self.m_button41 = wx.Button( self, wx.ID_ANY, _(u"Cancel"), wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer15.Add( self.m_button41, 0, wx.ALL, 5 )
		
		
		fgSizer33.Add( gSizer15, 1, wx.BOTTOM|wx.EXPAND, 5 )
		
		
		self.SetSizer( fgSizer33 )
		self.Layout()
		
		# Connect Events
		self.deviceListCtrl.Bind( wx.EVT_LIST_ITEM_SELECTED, self.onDeviceItemSelected )
		self.operationList.Bind( wx.EVT_LIST_ITEM_SELECTED, self.onOperationItemSelected )
		self.applyBtn.Bind( wx.EVT_BUTTON, self.onApply )
		self.m_button41.Bind( wx.EVT_BUTTON, self.onCancel )
	
	def __del__( self ):
		pass
	
	
	# Virtual event handlers, overide them in your derived class
	def onDeviceItemSelected( self, event ):
		event.Skip()
	
	def onOperationItemSelected( self, event ):
		event.Skip()
	
	def onApply( self, event ):
		event.Skip()
	
	def onCancel( self, event ):
		event.Skip()
	
	def m_splitter8OnIdle( self, event ):
		self.m_splitter8.SetSashPosition( 250 )
		self.m_splitter8.Unbind( wx.EVT_IDLE )
	

###########################################################################
## Class Panel_Action_Group_Select_Base
###########################################################################

class Panel_Action_Group_Select_Base ( wx.Panel ):
	
	def __init__( self, parent ):
		wx.Panel.__init__ ( self, parent, id = wx.ID_ANY, pos = wx.DefaultPosition, size = wx.Size( 400,400 ), style = wx.TAB_TRAVERSAL )
		
		fgSizer33 = wx.FlexGridSizer( 2, 1, 0, 0 )
		fgSizer33.AddGrowableCol( 0 )
		fgSizer33.AddGrowableRow( 0 )
		fgSizer33.SetFlexibleDirection( wx.BOTH )
		fgSizer33.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )
		
		bSizer36 = wx.BoxSizer( wx.VERTICAL )
		
		self.m_panel26 = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer38 = wx.BoxSizer( wx.VERTICAL )
		
		sbSizer40 = wx.StaticBoxSizer( wx.StaticBox( self.m_panel26, wx.ID_ANY, _(u"动作脚本") ), wx.VERTICAL )
		
		fgSizer62 = wx.FlexGridSizer( 0, 0, 0, 0 )
		fgSizer62.AddGrowableCol( 0 )
		fgSizer62.AddGrowableRow( 0 )
		fgSizer62.SetFlexibleDirection( wx.BOTH )
		fgSizer62.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )
		
		self.actionGrpListView = UlcListCtrl( self.m_panel26, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LC_REPORT|wx.LC_SINGLE_SEL )
		fgSizer62.Add( self.actionGrpListView, 0, wx.ALL|wx.EXPAND, 5 )
		
		
		sbSizer40.Add( fgSizer62, 1, wx.EXPAND, 5 )
		
		
		bSizer38.Add( sbSizer40, 1, wx.ALL|wx.EXPAND, 5 )
		
		
		self.m_panel26.SetSizer( bSizer38 )
		self.m_panel26.Layout()
		bSizer38.Fit( self.m_panel26 )
		bSizer36.Add( self.m_panel26, 1, wx.EXPAND |wx.ALL, 5 )
		
		
		fgSizer33.Add( bSizer36, 1, wx.EXPAND, 5 )
		
		gSizer15 = wx.GridSizer( 0, 2, 0, 0 )
		
		self.applyBtn = wx.Button( self, wx.ID_ANY, _(u"Apply"), wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer15.Add( self.applyBtn, 0, wx.ALIGN_RIGHT|wx.ALL, 5 )
		
		self.m_button41 = wx.Button( self, wx.ID_ANY, _(u"Cancel"), wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer15.Add( self.m_button41, 0, wx.ALL, 5 )
		
		
		fgSizer33.Add( gSizer15, 1, wx.BOTTOM|wx.EXPAND, 5 )
		
		
		self.SetSizer( fgSizer33 )
		self.Layout()
		
		# Connect Events
		self.actionGrpListView.Bind( wx.EVT_LIST_ITEM_SELECTED, self.onDeviceItemSelected )
		self.applyBtn.Bind( wx.EVT_BUTTON, self.onApply )
		self.m_button41.Bind( wx.EVT_BUTTON, self.onCancel )
	
	def __del__( self ):
		pass
	
	
	# Virtual event handlers, overide them in your derived class
	def onDeviceItemSelected( self, event ):
		event.Skip()
	
	def onApply( self, event ):
		event.Skip()
	
	def onCancel( self, event ):
		event.Skip()
	

###########################################################################
## Class Panel_AnimationCondition_Setting_Base
###########################################################################

class Panel_AnimationCondition_Setting_Base ( wx.Panel ):
	
	def __init__( self, parent ):
		wx.Panel.__init__ ( self, parent, id = wx.ID_ANY, pos = wx.DefaultPosition, size = wx.Size( 391,241 ), style = wx.TAB_TRAVERSAL )
		
		fgSizer33 = wx.FlexGridSizer( 2, 1, 0, 0 )
		fgSizer33.AddGrowableCol( 0 )
		fgSizer33.AddGrowableRow( 0 )
		fgSizer33.SetFlexibleDirection( wx.BOTH )
		fgSizer33.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )
		
		fgSizer34 = wx.FlexGridSizer( 2, 1, 0, 0 )
		fgSizer34.AddGrowableCol( 0 )
		fgSizer34.SetFlexibleDirection( wx.BOTH )
		fgSizer34.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )
		
		sbSizer13 = wx.StaticBoxSizer( wx.StaticBox( self, wx.ID_ANY, _(u"活动设置") ), wx.VERTICAL )
		
		fgSizer35 = wx.FlexGridSizer( 1, 3, 0, 0 )
		fgSizer35.AddGrowableCol( 1 )
		fgSizer35.SetFlexibleDirection( wx.BOTH )
		fgSizer35.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )
		
		bSizer42 = wx.BoxSizer( wx.VERTICAL )
		
		self.m_staticText37 = wx.StaticText( self, wx.ID_ANY, _(u"绑定数据点"), wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText37.Wrap( -1 )
		bSizer42.Add( self.m_staticText37, 0, wx.ALL|wx.EXPAND, 5 )
		
		
		fgSizer35.Add( bSizer42, 1, wx.ALL|wx.EXPAND, 5 )
		
		self.txt_attribute = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.TE_READONLY )
		self.txt_attribute.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_WINDOW ) )
		
		fgSizer35.Add( self.txt_attribute, 0, wx.ALL|wx.EXPAND, 5 )
		
		self.m_button27 = wx.Button( self, wx.ID_ANY, _(u"选择"), wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer35.Add( self.m_button27, 0, wx.ALL, 5 )
		
		
		sbSizer13.Add( fgSizer35, 1, wx.EXPAND, 5 )
		
		sbSizer15 = wx.StaticBoxSizer( wx.StaticBox( self, wx.ID_ANY, _(u"活动条件") ), wx.HORIZONTAL )
		
		fgSizer29 = wx.FlexGridSizer( 0, 2, 0, 0 )
		fgSizer29.AddGrowableCol( 0 )
		fgSizer29.AddGrowableCol( 1 )
		fgSizer29.AddGrowableRow( 0 )
		fgSizer29.SetFlexibleDirection( wx.BOTH )
		fgSizer29.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )
		
		self.radioTrue = wx.RadioButton( self, wx.ID_ANY, _(u"变量值为真"), wx.DefaultPosition, wx.DefaultSize, 0 )
		self.radioTrue.SetValue( True ) 
		fgSizer29.Add( self.radioTrue, 0, wx.ALL|wx.EXPAND, 5 )
		
		self.radioFalse = wx.RadioButton( self, wx.ID_ANY, _(u"变量值为假"), wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer29.Add( self.radioFalse, 0, wx.ALL|wx.EXPAND, 5 )
		
		
		sbSizer15.Add( fgSizer29, 1, wx.EXPAND, 5 )
		
		
		sbSizer13.Add( sbSizer15, 1, wx.EXPAND, 5 )
		
		
		fgSizer34.Add( sbSizer13, 1, wx.ALL|wx.EXPAND, 5 )
		
		
		fgSizer33.Add( fgSizer34, 1, wx.ALL|wx.EXPAND, 5 )
		
		gSizer15 = wx.GridSizer( 0, 2, 0, 0 )
		
		self.applyBtn = wx.Button( self, wx.ID_ANY, _(u"Apply"), wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer15.Add( self.applyBtn, 0, wx.ALIGN_RIGHT|wx.ALL, 5 )
		
		self.m_button41 = wx.Button( self, wx.ID_ANY, _(u"Cancel"), wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer15.Add( self.m_button41, 0, wx.ALL, 5 )
		
		
		fgSizer33.Add( gSizer15, 1, wx.BOTTOM|wx.EXPAND, 5 )
		
		
		self.SetSizer( fgSizer33 )
		self.Layout()
		
		# Connect Events
		self.m_button27.Bind( wx.EVT_BUTTON, self.onSelectConditionBind )
		self.applyBtn.Bind( wx.EVT_BUTTON, self.onApply )
		self.m_button41.Bind( wx.EVT_BUTTON, self.onCancel )
	
	def __del__( self ):
		pass
	
	
	# Virtual event handlers, overide them in your derived class
	def onSelectConditionBind( self, event ):
		event.Skip()
	
	def onApply( self, event ):
		event.Skip()
	
	def onCancel( self, event ):
		event.Skip()
	

###########################################################################
## Class ConfirmDIALOG
###########################################################################

class ConfirmDIALOG ( wx.Dialog ):
	
	def __init__( self, parent ):
		wx.Dialog.__init__ ( self, parent, id = wx.ID_ANY, title = wx.EmptyString, pos = wx.DefaultPosition, size = wx.Size( 279,139 ), style = wx.DEFAULT_DIALOG_STYLE|wx.STAY_ON_TOP )
		
		self.SetSizeHintsSz( wx.DefaultSize, wx.DefaultSize )
		
		fgSizer33 = wx.FlexGridSizer( 2, 1, 0, 0 )
		fgSizer33.AddGrowableCol( 0 )
		fgSizer33.AddGrowableRow( 0 )
		fgSizer33.SetFlexibleDirection( wx.BOTH )
		fgSizer33.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )
		
		gSizer151 = wx.GridSizer( 1, 1, 0, 0 )
		
		self.alert_msg_txt = wx.StaticText( self, wx.ID_ANY, _(u"some alert"), wx.DefaultPosition, wx.DefaultSize, 0 )
		self.alert_msg_txt.Wrap( -1 )
		gSizer151.Add( self.alert_msg_txt, 0, wx.ALIGN_CENTER|wx.ALIGN_CENTER_HORIZONTAL|wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )
		
		
		fgSizer33.Add( gSizer151, 1, wx.EXPAND, 5 )
		
		gSizer15 = wx.GridSizer( 0, 2, 0, 0 )
		
		self.applyBtn = wx.Button( self, wx.ID_OK, _(u"确定"), wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer15.Add( self.applyBtn, 0, wx.ALIGN_RIGHT|wx.ALL, 5 )
		
		self.m_button41 = wx.Button( self, wx.ID_CANCEL, _(u"取消"), wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer15.Add( self.m_button41, 0, wx.ALL, 5 )
		
		
		fgSizer33.Add( gSizer15, 1, wx.BOTTOM|wx.EXPAND, 5 )
		
		
		self.SetSizer( fgSizer33 )
		self.Layout()
		
		self.Centre( wx.BOTH )
		
		# Connect Events
		self.applyBtn.Bind( wx.EVT_BUTTON, self.onApply )
		self.m_button41.Bind( wx.EVT_BUTTON, self.onCancel )
	
	def __del__( self ):
		pass
	
	
	# Virtual event handlers, overide them in your derived class
	def onApply( self, event ):
		event.Skip()
	
	def onCancel( self, event ):
		event.Skip()
	

###########################################################################
## Class Panel_Status_Display_Base
###########################################################################

class Panel_Status_Display_Base ( wx.Panel ):
	
	def __init__( self, parent ):
		wx.Panel.__init__ ( self, parent, id = wx.ID_ANY, pos = wx.DefaultPosition, size = wx.Size( 247,208 ), style = wx.STATIC_BORDER )
		
		fgSizer61 = wx.FlexGridSizer( 0, 0, 0, 0 )
		fgSizer61.AddGrowableCol( 0 )
		fgSizer61.AddGrowableRow( 0 )
		fgSizer61.SetFlexibleDirection( wx.BOTH )
		fgSizer61.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )
		
		self.statusDispGrid = wx.grid.Grid( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, 0 )
		
		# Grid
		self.statusDispGrid.CreateGrid( 0, 2 )
		self.statusDispGrid.EnableEditing( False )
		self.statusDispGrid.EnableGridLines( True )
		self.statusDispGrid.EnableDragGridSize( False )
		self.statusDispGrid.SetMargins( 0, 0 )
		
		# Columns
		self.statusDispGrid.SetColSize( 0, 100 )
		self.statusDispGrid.SetColSize( 1, 100 )
		self.statusDispGrid.EnableDragColMove( False )
		self.statusDispGrid.EnableDragColSize( True )
		self.statusDispGrid.SetColLabelSize( 30 )
		self.statusDispGrid.SetColLabelAlignment( wx.ALIGN_CENTRE, wx.ALIGN_CENTRE )
		
		# Rows
		self.statusDispGrid.EnableDragRowSize( False )
		self.statusDispGrid.SetRowLabelSize( 30 )
		self.statusDispGrid.SetRowLabelAlignment( wx.ALIGN_CENTRE, wx.ALIGN_CENTRE )
		
		# Label Appearance
		self.statusDispGrid.SetLabelFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), 70, 90, 91, False, wx.EmptyString ) )
		
		# Cell Defaults
		self.statusDispGrid.SetDefaultCellFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), 70, 90, 92, False, wx.EmptyString ) )
		self.statusDispGrid.SetDefaultCellAlignment( wx.ALIGN_LEFT, wx.ALIGN_CENTRE )
		fgSizer61.Add( self.statusDispGrid, 0, wx.ALL|wx.EXPAND, 5 )
		
		
		self.SetSizer( fgSizer61 )
		self.Layout()
	
	def __del__( self ):
		pass
	

###########################################################################
## Class Panel_Status_Display_Base1
###########################################################################

class Panel_Status_Display_Base1 ( wx.Panel ):
	
	def __init__( self, parent ):
		wx.Panel.__init__ ( self, parent, id = wx.ID_ANY, pos = wx.DefaultPosition, size = wx.Size( 500,300 ), style = wx.STATIC_BORDER )
		
		self.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_HIGHLIGHT ) )
		
		fgSizer61 = wx.FlexGridSizer( 0, 0, 0, 0 )
		fgSizer61.AddGrowableCol( 0 )
		fgSizer61.AddGrowableRow( 0 )
		fgSizer61.SetFlexibleDirection( wx.BOTH )
		fgSizer61.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )
		
		self.statusNodeList = UlcListCtrl( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LC_REPORT )
		fgSizer61.Add( self.statusNodeList, 0, wx.ALL|wx.EXPAND, 5 )
		
		
		self.SetSizer( fgSizer61 )
		self.Layout()
		
		# Connect Events
		self.statusNodeList.Bind( wx.EVT_LIST_ITEM_SELECTED, self.onIoNodeListItemSelected )
	
	def __del__( self ):
		pass
	
	
	# Virtual event handlers, overide them in your derived class
	def onIoNodeListItemSelected( self, event ):
		event.Skip()
	

###########################################################################
## Class Panel_Edit_Status_Display_Base_List
###########################################################################

class Panel_Edit_Status_Display_Base_List ( wx.Panel ):
	
	def __init__( self, parent ):
		wx.Panel.__init__ ( self, parent, id = wx.ID_ANY, pos = wx.DefaultPosition, size = wx.Size( 500,300 ), style = wx.TAB_TRAVERSAL )
		
		fgSizer4 = wx.FlexGridSizer( 2, 1, 0, 0 )
		fgSizer4.AddGrowableCol( 0 )
		fgSizer4.AddGrowableCol( 1 )
		fgSizer4.AddGrowableRow( 0 )
		fgSizer4.SetFlexibleDirection( wx.BOTH )
		fgSizer4.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )
		
		fgSizer341 = wx.FlexGridSizer( 2, 0, 0, 0 )
		fgSizer341.AddGrowableCol( 0 )
		fgSizer341.AddGrowableCol( 1 )
		fgSizer341.AddGrowableRow( 1 )
		fgSizer341.SetFlexibleDirection( wx.BOTH )
		fgSizer341.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )
		
		self.edit_status_disp_toolbar = wx.ToolBar( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TB_HORIZONTAL ) 
		self.edit_status_disp_toolbar.AddLabelTool( STATUS_ADD, _(u"tool"), wx.ArtProvider.GetBitmap( wx.ART_NEW, wx.ART_TOOLBAR ), wx.NullBitmap, wx.ITEM_NORMAL, wx.EmptyString, wx.EmptyString, None ) 
		
		self.edit_status_disp_toolbar.AddLabelTool( STATUS_DEL, _(u"tool"), wx.ArtProvider.GetBitmap( wx.ART_DELETE, wx.ART_TOOLBAR ), wx.NullBitmap, wx.ITEM_NORMAL, wx.EmptyString, wx.EmptyString, None ) 
		
		self.edit_status_disp_toolbar.AddSeparator()
		
		self.edit_status_disp_toolbar.Realize() 
		
		fgSizer341.Add( self.edit_status_disp_toolbar, 0, wx.EXPAND, 5 )
		
		self.status_disp_list = UlcListCtrl( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LC_REPORT )
		fgSizer341.Add( self.status_disp_list, 0, wx.ALL|wx.EXPAND, 5 )
		
		
		fgSizer4.Add( fgSizer341, 1, wx.EXPAND, 5 )
		
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
		self.Bind( wx.EVT_TOOL, self.onStatusDispToolClicked, id = STATUS_ADD )
		self.Bind( wx.EVT_TOOL, self.onStatusDispToolClicked, id = STATUS_DEL )
		self.status_disp_list.Bind( wx.EVT_LIST_ITEM_SELECTED, self.onIoNodeListItemSelected )
		self.m_button6.Bind( wx.EVT_BUTTON, self.onApply )
		self.m_button7.Bind( wx.EVT_BUTTON, self.onCancel )
	
	def __del__( self ):
		pass
	
	
	# Virtual event handlers, overide them in your derived class
	def onStatusDispToolClicked( self, event ):
		event.Skip()
	
	
	def onIoNodeListItemSelected( self, event ):
		event.Skip()
	
	def onApply( self, event ):
		event.Skip()
	
	def onCancel( self, event ):
		event.Skip()
	

###########################################################################
## Class Panel_Edit_Status_Display_Base
###########################################################################

class Panel_Edit_Status_Display_Base ( wx.Panel ):
	
	def __init__( self, parent ):
		wx.Panel.__init__ ( self, parent, id = wx.ID_ANY, pos = wx.DefaultPosition, size = wx.Size( 464,296 ), style = wx.TAB_TRAVERSAL )
		
		fgSizer4 = wx.FlexGridSizer( 2, 1, 0, 0 )
		fgSizer4.AddGrowableCol( 0 )
		fgSizer4.AddGrowableCol( 1 )
		fgSizer4.AddGrowableRow( 0 )
		fgSizer4.SetFlexibleDirection( wx.BOTH )
		fgSizer4.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )
		
		fgSizer341 = wx.FlexGridSizer( 2, 0, 0, 0 )
		fgSizer341.AddGrowableCol( 0 )
		fgSizer341.AddGrowableCol( 1 )
		fgSizer341.AddGrowableRow( 1 )
		fgSizer341.SetFlexibleDirection( wx.BOTH )
		fgSizer341.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )
		
		self.edit_status_disp_toolbar = wx.ToolBar( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TB_HORIZONTAL ) 
		self.edit_status_disp_toolbar.AddLabelTool( STATUS_ADD, _(u"tool"), wx.ArtProvider.GetBitmap( wx.ART_NEW, wx.ART_TOOLBAR ), wx.NullBitmap, wx.ITEM_NORMAL, wx.EmptyString, wx.EmptyString, None ) 
		
		self.edit_status_disp_toolbar.AddLabelTool( STATUS_DEL, _(u"tool"), wx.ArtProvider.GetBitmap( wx.ART_DELETE, wx.ART_TOOLBAR ), wx.NullBitmap, wx.ITEM_NORMAL, wx.EmptyString, wx.EmptyString, None ) 
		
		self.edit_status_disp_toolbar.AddSeparator()
		
		self.edit_status_disp_toolbar.Realize() 
		
		fgSizer341.Add( self.edit_status_disp_toolbar, 0, wx.EXPAND, 5 )
		
		self.status_disp_grid = wx.grid.Grid( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, 0 )
		
		# Grid
		self.status_disp_grid.CreateGrid( 0, 2 )
		self.status_disp_grid.EnableEditing( False )
		self.status_disp_grid.EnableGridLines( True )
		self.status_disp_grid.EnableDragGridSize( False )
		self.status_disp_grid.SetMargins( 0, 0 )
		
		# Columns
		self.status_disp_grid.SetColSize( 0, 200 )
		self.status_disp_grid.SetColSize( 1, 200 )
		self.status_disp_grid.EnableDragColMove( False )
		self.status_disp_grid.EnableDragColSize( True )
		self.status_disp_grid.SetColLabelSize( 30 )
		self.status_disp_grid.SetColLabelValue( 0, _(u"aaa") )
		self.status_disp_grid.SetColLabelValue( 1, _(u"bbb") )
		self.status_disp_grid.SetColLabelAlignment( wx.ALIGN_CENTRE, wx.ALIGN_CENTRE )
		
		# Rows
		self.status_disp_grid.EnableDragRowSize( False )
		self.status_disp_grid.SetRowLabelSize( 30 )
		self.status_disp_grid.SetRowLabelAlignment( wx.ALIGN_CENTRE, wx.ALIGN_CENTRE )
		
		# Label Appearance
		
		# Cell Defaults
		self.status_disp_grid.SetDefaultCellAlignment( wx.ALIGN_LEFT, wx.ALIGN_CENTRE )
		fgSizer341.Add( self.status_disp_grid, 0, wx.ALL|wx.EXPAND, 5 )
		
		
		fgSizer4.Add( fgSizer341, 1, wx.EXPAND, 5 )
		
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
		self.Bind( wx.EVT_TOOL, self.onStatusDispToolClicked, id = STATUS_ADD )
		self.Bind( wx.EVT_TOOL, self.onStatusDispToolClicked, id = STATUS_DEL )
		self.m_button6.Bind( wx.EVT_BUTTON, self.onApply )
		self.m_button7.Bind( wx.EVT_BUTTON, self.onCancel )
	
	def __del__( self ):
		pass
	
	
	# Virtual event handlers, overide them in your derived class
	def onStatusDispToolClicked( self, event ):
		event.Skip()
	
	
	def onApply( self, event ):
		event.Skip()
	
	def onCancel( self, event ):
		event.Skip()
	

###########################################################################
## Class MyFrame2
###########################################################################

class MyFrame2 ( wx.Frame ):
	
	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = wx.EmptyString, pos = wx.DefaultPosition, size = wx.Size( 500,274 ), style = wx.RESIZE_BORDER|wx.TAB_TRAVERSAL )
		
		self.SetSizeHintsSz( wx.DefaultSize, wx.DefaultSize )
		
		bSizer45 = wx.BoxSizer( wx.VERTICAL )
		
		self.m_panel51 = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer45.Add( self.m_panel51, 1, wx.EXPAND |wx.ALL, 5 )
		
		
		self.SetSizer( bSizer45 )
		self.Layout()
		
		self.Centre( wx.BOTH )
	
	def __del__( self ):
		pass
	

