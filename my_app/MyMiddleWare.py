import wx
import images
from MyFrameBase import *
from MyPanelBase import *
from MyMyPanel2 import *
from MyEmptyPanel import *
from wxPythonInAction.Chapter_15 import *
import wxPythonInAction.Chapter_15.data

from MyClass import *
from ViewSelectPanel import *


mydata = wxPythonInAction.Chapter_15.data.tree

#mydata = data.tree

class MyFrame1( wx.Frame ):
		def __init__( self, parent ):
				wx.Frame.__init__( self, parent )
#				self.panel = TestTreeCtrlPanel(self,0)
				self.panel = MySplitterPanel(self)
				
#				self.sp = wx.SplitterWindow(self, size=(200,200))
#				self.p1 = wx.Panel(self.sp, style=wx.SUNKEN_BORDER, size = (200, 200))
#				self.p2 = wx.Panel(self.sp, style=wx.SUNKEN_BORDER, size = (200, 200))
#				self.p1.SetBackgroundColour("pink")
#				self.p2.SetBackgroundColour("sky blue")
#				#self.sp.SplitHorizontally(self.p1, self.p2, 100)
#		  		self.sp.SplitVertically(self.p1, self.p2, 100)





class MyFrame( MyFrameBase ):
		def __init__( self, parent ):
				MyFrameBase.__init__( self, parent )
				self.parent = parent
				self.construceFrame()
				
		def construceFrame(self):
			self.panel = testMySplitterPanel(self)
			
			return
				
class MySplitterPanel( MainBase.SplitterPanelBase ):
	def __init__( self, parent ):
		MainBase.SplitterPanelBase.__init__( self, parent )	
		self.parent = parent			
				
				
class MyPanel( MyPanelBase ):
	def __init__( self, parent ):
		MyPanelBase.__init__( self, parent )
		
		
		
class MyPanel2( MyMyPanel2 ):
	def __init__( self, parent ):
		MyMyPanel2.__init__( self, parent )

class testMySplitterPanel( MySplitterPanel ):
	def __init__( self, parent ):
		MySplitterPanel.__init__( self, parent )
		self.parent = parent
		
		self.buildViewSelectPanel()
		#self.ViewPanelSetDsp()

	
	def buildViewSelectPanel(self):
		
		container = self.viewSelectPanel
		
		sizer = wx.BoxSizer( wx.VERTICAL )
		
#		self.viewPanel_sub = wx.Panel( self.viewPanel, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
#		sizer.Add( self.viewPanel_sub, 1, wx.EXPAND |wx.ALL, 5 )
		
		self.viewPanel_sub = ViewSelectPanel(self, container, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		sizer.Add( self.viewPanel_sub, 1, wx.EXPAND |wx.ALL, 5 )
		self.viewPanel_sub.SetBackgroundColour("sky blue")
		container.SetSizer( sizer )
		container.Layout()
		sizer.Fit(container)
		return
	
	def GetViewPanel(self):
		return self.viewPanel
	
	def ViewPanelSetDsp(self, txt, i):
		
		
		self.viewPanel.DestroyChildren()
		
		sizer = wx.BoxSizer( wx.VERTICAL )
		
		self.viewPanel_sub = wx.Panel( self.viewPanel, wx.ID_ANY, wx.DefaultPosition, self.viewPanel.GetClientSize(), wx.TAB_TRAVERSAL )
#		self.viewPanel_sub = wx.Panel( self.viewPanel, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
	
		sizer.Add( self.viewPanel_sub, 1, wx.EXPAND |wx.ALL, 5 )
		
		#		self.m_panel25.SetBackgroundColour( wx.SystemSettings.GetColour( "sky blue" ) )
		
		self.viewPanel_sub.SetBackgroundColour("sky blue")
		
		wx.StaticText(self.viewPanel_sub, -1, txt, (20*i, 10*i))
		
#		
		self.viewPanel.SetSizer( sizer )
		self.viewPane.SetSizer(sizer)
		self.viewPane.SetAutoLayout(True)
		self.viewPane.Layout()
		
		
		
		
	def ViewPanelSetDsp2(self):
		sizer = wx.BoxSizer( wx.VERTICAL )
		
		self.viewPanel_sub = wx.Panel( self.viewPanel, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		sizer.Add( self.viewPanel_sub, 1, wx.EXPAND |wx.ALL, 5 )
		
		#		self.m_panel25.SetBackgroundColour( wx.SystemSettings.GetColour( "sky blue" ) )
		
		self.viewPanel_sub.SetBackgroundColour("pink")
		self.viewPanel.SetSizer( sizer )
		self.viewPanel.Layout()
		sizer.Fit( self.viewPanel )
		
		


class testMySplitterPanel2( MySplitterPanel ):
	def __init__( self, parent ):
		MySplitterPanel.__init__( self, parent )
		
		panel_L = self.p_L
		_initElementsOfTreePanel(panel_L)
		
		# Add nodes from our
		
class testMySplitterPanel1( MySplitterPanel ):
	def __init__( self, parent ):
		MySplitterPanel.__init__( self, parent )
		
		panel_L = self.p_L
#		panel_L.tree = wx.TreeCtrl(panel_L)
#		root = panel_L.tree.AddRoot("wx.Object")
#		self.AddTreeNodes(panel_L, root, mydata)
#		panel_L.tree.Expand(root)
		
		
		panel_L.tree = MyTreeCtrl(panel_L, -1, wx.DefaultPosition, wx.DefaultSize,
                               wx.TR_DEFAULT_STYLE
                               #wx.TR_HAS_BUTTONS
                               #| wx.TR_EDIT_LABELS
                               #| wx.TR_MULTIPLE
                               #| wx.TR_HIDE_ROOT
                               , 0)

	
	def AddTreeNodes(self, parent, parentItem, items):
		"""
		Recursively traverses the data structure, adding tree nodes to
		match it.
		"""
		for item in items:
		    if type(item) == str:
		        parent.tree.AppendItem(parentItem, item)
		    else:
		        newItem = parent.tree.AppendItem(parentItem, item[0])
		        self.AddTreeNodes(parent, newItem, item[1])
                
	def GetItemText(self, item):
		if item:
			return self.tree.GetItemText(item)
		else:
			return ""
        
	def OnItemExpanded(self, evt):
	    print "OnItemExpanded: ", self.GetItemText(evt.GetItem())
	    
	def OnItemCollapsed(self, evt):
	    print "OnItemCollapsed:", self.GetItemText(evt.GetItem())
	
	def OnSelChanged(self, evt):
	    print "OnSelChanged:   ", self.GetItemText(evt.GetItem())
	
	def OnActivated(self, evt):
	    print "OnActivated:    ", self.GetItemText(evt.GetItem())
		
		
class testSplitterInEmptyPanel( MyEmptyPanel ):
	def __init__( self, parent ):
		MyEmptyPanel.__init__( self, parent )
		self.sp = wx.SplitterWindow(self, size=(200,200))
		self.p1 = wx.Panel(self.sp, style=wx.SUNKEN_BORDER, size = (200, 200))
		self.p2 = wx.Panel(self.sp, style=wx.SUNKEN_BORDER, size = (200, 200))
		self.p1.SetBackgroundColour("pink")
		self.p2.SetBackgroundColour("sky blue")
		#self.sp.SplitHorizontally(self.p1, self.p2, 100)
		self.sp.SplitVertically(self.p1, self.p2, 100)
		
		
def _initElementsOfTreePanel(panel):
    tree = wx.TreeCtrl(panel, -1, wx.Point(0, 0), wx.DefaultSize, wx.NO_BORDER | wx.TR_DEFAULT_STYLE)

    root = tree.AddRoot("Elements")
    items = []
    imglist = wx.ImageList(16, 16, True, 2)
    imglist.Add(wx.ArtProvider_GetBitmap(wx.ART_FOLDER, wx.ART_OTHER, wx.Size(16, 16)))
    imglist.Add(wx.ArtProvider_GetBitmap(wx.ART_NORMAL_FILE, wx.ART_OTHER, wx.Size(16, 16)))
    tree.AssignImageList(imglist)

# #        Create the element Tree (the left hand side panel). Places in it all the found functions 
    def appendSubitems(item, func_list, tree):
        print item
        for func in func_list:
            itemid = tree.AppendItem(item, func.__name__, 1)
            print"GUIFrame._initElementsofTreePanel, func:",func.__name__,"id:",itemid

#        print "TreeItemId:",
#    appendSubitems(tree.AppendItem(root, "Input functions", 0), self._elemdisco.input_functions, tree) 
#    appendSubitems(tree.AppendItem(root, "Processing functions", 0), self._elemdisco.processing_functions, tree)
#    appendSubitems(tree.AppendItem(root, "Output functions", 0), self._elemdisco.output_functions, tree)
#    appendSubitems(tree.AppendItem(root, "Other functions", 0), self._elemdisco.other_functions, tree)
#
#
#    tree.ExpandAll()
#    self.Bind(wx.EVT_TREE_ITEM_ACTIVATED, self._addNodeToSchema, self.treePanel.tree)

def _addNodeToSchema(self,event):
    print event.GetItem()
    
    
class MyTreeCtrl(wx.TreeCtrl):
    def __init__(self, parent, id, pos, size, style, log):
        wx.TreeCtrl.__init__(self, parent, id, pos, size, style)
        self.log = log

    def OnCompareItems(self, item1, item2):
        t1 = self.GetItemText(item1)
        t2 = self.GetItemText(item2)
        self.log.WriteText('compare: ' + t1 + ' <> ' + t2 + '\n')
        if t1 < t2: return -1
        if t1 == t2: return 0
        return 1

#---------------------------------------------------------------------------
class TestTreeCtrlPanel(wx.Panel):
    def __init__(self, parent, log):

        # Use the WANTS_CHARS style so the panel doesn't eat the Return key.
        wx.Panel.__init__(self, parent, -1, style=wx.WANTS_CHARS)
        self.Bind(wx.EVT_SIZE, self.OnSize)

        self.log = log
        tID = wx.NewId()

        self.tree = MyTreeCtrl(self, tID, wx.DefaultPosition, wx.DefaultSize,
                               wx.TR_DEFAULT_STYLE
                               #wx.TR_HAS_BUTTONS
                               #| wx.TR_EDIT_LABELS
                               #| wx.TR_MULTIPLE
                               #| wx.TR_HIDE_ROOT
                               , self.log)

        isz = (16,16)
        il = wx.ImageList(isz[0], isz[1])
        fldridx     = il.Add(wx.ArtProvider_GetBitmap(wx.ART_FOLDER,      wx.ART_OTHER, isz))
        fldropenidx = il.Add(wx.ArtProvider_GetBitmap(wx.ART_FILE_OPEN,   wx.ART_OTHER, isz))
        fileidx     = il.Add(wx.ArtProvider_GetBitmap(wx.ART_NORMAL_FILE, wx.ART_OTHER, isz))
        self.il = il
        smileidx    = il.Add(images.Smiles.GetBitmap())

        self.tree.SetImageList(il)

        # NOTE:  For some reason tree items have to have a data object in
        #        order to be sorted.  Since our compare just uses the labels
        #        we don't need any real data, so we'll just use None below for
        #        the item data.

        self.root = self.tree.AddRoot("The Root Item")
        self.tree.SetPyData(self.root, None)
        self.tree.SetItemImage(self.root, fldridx, wx.TreeItemIcon_Normal)
        self.tree.SetItemImage(self.root, fldropenidx, wx.TreeItemIcon_Expanded)


        for x in range(15):
            child = self.tree.AppendItem(self.root, "Item %d" % x)
            self.tree.SetPyData(child, None)
            self.tree.SetItemImage(child, fldridx, wx.TreeItemIcon_Normal)
            self.tree.SetItemImage(child, fldropenidx, wx.TreeItemIcon_Expanded)

            for y in range(5):
                last = self.tree.AppendItem(child, "item %d-%s" % (x, chr(ord("a")+y)))
                self.tree.SetPyData(last, None)
                self.tree.SetItemImage(last, fldridx, wx.TreeItemIcon_Normal)
                self.tree.SetItemImage(last, fldropenidx, wx.TreeItemIcon_Expanded)

                for z in range(5):
                    item = self.tree.AppendItem(last,  "item %d-%s-%d" % (x, chr(ord("a")+y), z))
                    self.tree.SetPyData(item, None)
                    self.tree.SetItemImage(item, fileidx, wx.TreeItemIcon_Normal)
                    self.tree.SetItemImage(item, smileidx, wx.TreeItemIcon_Selected)

        self.tree.Expand(self.root)
        self.Bind(wx.EVT_TREE_ITEM_EXPANDED, self.OnItemExpanded, self.tree)
        self.Bind(wx.EVT_TREE_ITEM_COLLAPSED, self.OnItemCollapsed, self.tree)
        self.Bind(wx.EVT_TREE_SEL_CHANGED, self.OnSelChanged, self.tree)
        self.Bind(wx.EVT_TREE_BEGIN_LABEL_EDIT, self.OnBeginEdit, self.tree)
        self.Bind(wx.EVT_TREE_END_LABEL_EDIT, self.OnEndEdit, self.tree)
        self.Bind(wx.EVT_TREE_ITEM_ACTIVATED, self.OnActivate, self.tree)

        self.tree.Bind(wx.EVT_LEFT_DCLICK, self.OnLeftDClick)
        self.tree.Bind(wx.EVT_RIGHT_DOWN, self.OnRightDown)
        self.tree.Bind(wx.EVT_RIGHT_UP, self.OnRightUp)


    def OnRightDown(self, event):
        pt = event.GetPosition();
        item, flags = self.tree.HitTest(pt)
        if item:
            self.log.WriteText("OnRightClick: %s, %s, %s\n" %
                               (self.tree.GetItemText(item), type(item), item.__class__))
            self.tree.SelectItem(item)
            
            
           



    def OnRightUp(self, event):
        pt = event.GetPosition();
        item, flags = self.tree.HitTest(pt)
        if item:        
            self.log.WriteText("OnRightUp: %s (manually starting label edit)\n"
                               % self.tree.GetItemText(item))
            self.tree.EditLabel(item)



    def OnBeginEdit(self, event):
        self.log.WriteText("OnBeginEdit\n")
        # show how to prevent edit...
        item = event.GetItem()
        if item and self.tree.GetItemText(item) == "The Root Item":
            wx.Bell()
            self.log.WriteText("You can't edit this one...\n")

            # Lets just see what's visible of its children
            cookie = 0
            root = event.GetItem()
            (child, cookie) = self.tree.GetFirstChild(root)

            while child.IsOk():
                self.log.WriteText("Child [%s] visible = %d" %
                                   (self.tree.GetItemText(child),
                                    self.tree.IsVisible(child)))
                (child, cookie) = self.tree.GetNextChild(root, cookie)

            event.Veto()


    def OnEndEdit(self, event):
        self.log.WriteText("OnEndEdit: %s %s\n" %
                           (event.IsEditCancelled(), event.GetLabel()) )
        # show how to reject edit, we'll not allow any digits
        for x in event.GetLabel():
            if x in string.digits:
                self.log.WriteText("You can't enter digits...\n")
                event.Veto()
                return


    def OnLeftDClick(self, event):
        pt = event.GetPosition();
        item, flags = self.tree.HitTest(pt)
        if item:
            self.log.WriteText("OnLeftDClick: %s\n" % self.tree.GetItemText(item))
            parent = self.tree.GetItemParent(item)
            if parent.IsOk():
                self.tree.SortChildren(parent)
        event.Skip()


    def OnSize(self, event):
        w,h = self.GetClientSizeTuple()
        print "onSize"
        self.tree.SetDimensions(0, 0, w, h)


    def OnItemExpanded(self, event):
        item = event.GetItem()
        if item:
            self.log.WriteText("OnItemExpanded: %s\n" % self.tree.GetItemText(item))

    def OnItemCollapsed(self, event):
        item = event.GetItem()
        if item:
            self.log.WriteText("OnItemCollapsed: %s\n" % self.tree.GetItemText(item))

    def OnSelChanged(self, event):
        self.item = event.GetItem()
        if self.item:
            self.log.WriteText("OnSelChanged: %s\n" % self.tree.GetItemText(self.item))
            if wx.Platform == '__WXMSW__':
                self.log.WriteText("BoundingRect: %s\n" %
                                   self.tree.GetBoundingRect(self.item, True))
            #items = self.tree.GetSelections()
            #print map(self.tree.GetItemText, items)
        event.Skip()


    def OnActivate(self, event):
        if self.item:
            self.log.WriteText("OnActivate: %s\n" % self.tree.GetItemText(self.item))


#---------------------------------------------------------------------------
class SplitterPanel ( wx.Panel ):
	
	def __init__( self, parent ):
		wx.Panel.__init__ ( self, parent, id = wx.ID_ANY, pos = wx.DefaultPosition, size = wx.Size( 500,300 ), style = wx.TAB_TRAVERSAL )
		
		bSizer6 = wx.BoxSizer( wx.VERTICAL )
		
		self.m_splitter4 = wx.SplitterWindow( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.SP_3D )
		self.m_splitter4.Bind( wx.EVT_IDLE, self.m_splitter4OnIdle )
		
#		self.p_L = wx.Panel( self.m_splitter4, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
#		self.p_L.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_BACKGROUND ) )
#		
		self.p_L = TestTreeCtrlPanel(self.m_splitter4, 0)
		
		
		self.m_scrolledWindow1 = wx.ScrolledWindow( self.m_splitter4, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.HSCROLL|wx.VSCROLL )
		self.m_scrolledWindow1.SetScrollRate( 5, 5 )
		bSizer9 = wx.BoxSizer( wx.VERTICAL )
		
		self.m_treeCtrl6 = wx.TreeCtrl( self.m_scrolledWindow1, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TR_DEFAULT_STYLE )
		bSizer9.Add( self.m_treeCtrl6, 0, wx.ALL, 5 )
		
		
		self.m_scrolledWindow1.SetSizer( bSizer9 )
		self.m_scrolledWindow1.Layout()
		bSizer9.Fit( self.m_scrolledWindow1 )
		self.m_splitter4.SplitVertically( self.p_L, self.m_scrolledWindow1, 0 )
		bSizer6.Add( self.m_splitter4, 1, wx.EXPAND, 5 )
		
		
		self.SetSizer( bSizer6 )
		self.Layout()
	
	def __del__( self ):
		pass
	
	def m_splitter4OnIdle( self, event ):
		self.m_splitter4.SetSashPosition( 0 )
		self.m_splitter4.Unbind( wx.EVT_IDLE )
				
