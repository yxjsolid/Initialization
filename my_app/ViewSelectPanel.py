# -*- coding: utf-8 -*- 

import wx
import images
import string


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

class ViewSelectPanel(wx.Panel):
    i = 0
    root = 0
    deviceViewNode = 0
    defaultViewNode = 0
    
    
    def __init__( self, parent, container, id = wx.ID_ANY, pos = wx.DefaultPosition, size = wx.Size( 500,300 ), style = wx.TAB_TRAVERSAL ):
        
        # Use the WANTS_CHARS style so the panel doesn't eat the Return key.
        wx.Panel.__init__(self, container, -1, style=wx.WANTS_CHARS)
        self.Bind(wx.EVT_SIZE, self.OnSize)
        self.parent = parent
        
        wx.GetApp().SetAppViewSelectPanel(self)

        #self.log = log
        tID = wx.NewId()

        self.tree = MyTreeCtrl(self, tID, wx.DefaultPosition, wx.DefaultSize,
                               wx.TR_DEFAULT_STYLE
                               #wx.TR_HAS_BUTTONS
                               #| wx.TR_EDIT_LABELS
                               #| wx.TR_MULTIPLE
                               #| wx.TR_HIDE_ROOT
                               , 0)

        isz = (16,16)
        il = wx.ImageList(isz[0], isz[1])
        self.fldridx     = il.Add(wx.ArtProvider_GetBitmap(wx.ART_FOLDER,      wx.ART_OTHER, isz))
        self.fldropenidx = il.Add(wx.ArtProvider_GetBitmap(wx.ART_FILE_OPEN,   wx.ART_OTHER, isz))
        self.fileidx     = il.Add(wx.ArtProvider_GetBitmap(wx.ART_NORMAL_FILE, wx.ART_OTHER, isz))
        self.il = il
        smileidx    = il.Add(images.Smiles.GetBitmap())

        self.tree.SetImageList(il)

        # NOTE:  For some reason tree items have to have a data object in
        #        order to be sorted.  Since our compare just uses the labels
        #        we don't need any real data, so we'll just use None below for
        #        the item data.

        self.root = self.tree.AddRoot("The Root Item")
        self.tree.SetPyData(self.root, None)
        self.tree.SetItemImage(self.root, self.fldridx, wx.TreeItemIcon_Normal)
        self.tree.SetItemImage(self.root, self.fldropenidx, wx.TreeItemIcon_Expanded)

       
        
        self.defaultViewNode = self.AddViewOption("总览")
        self.deviceViewNode = self.AddViewOption("设备")
        self.tree.Expand(self.root)
        
        self.AddDeviceNode("皮带机1")
       
       
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
        
        self.i += 1
        if self.item:
            #self.log.WriteText("OnSelChanged: %s\n" % self.tree.GetItemText(self.item))
            
#           self.parent.ViewPanelSetDsp()
            
        
            self.ViewPanelSetDsp(self.parent, self.tree.GetItemText(self.item), self.i)
            
            if wx.Platform == '__WXMSW__':
                self.log.WriteText("BoundingRect: %s\n" %
                                   self.tree.GetBoundingRect(self.item, True))
            #items = self.tree.GetSelections()
            #print map(self.tree.GetItemText, items)
        event.Skip()


    def OnActivate(self, event):
        if self.item:
            self.log.WriteText("OnActivate: %s\n" % self.tree.GetItemText(self.item))
    
    def AddViewOption(self, name):
        child = self.tree.AppendItem(self.root, name)
        self.tree.SetPyData(child, None)
        self.tree.SetItemImage(child, self.fldridx, wx.TreeItemIcon_Normal)
        self.tree.SetItemImage(child, self.fldropenidx, wx.TreeItemIcon_Expanded)
        return child

    def getDeviceViewNode(self):
        return self.deviceViewNode

    def AddDeviceNode(self, name):
        child = self.tree.AppendItem(self.getDeviceViewNode(), name)
        self.tree.SetPyData(child, None)
        self.tree.SetItemImage(child, self.fldridx, wx.TreeItemIcon_Normal)
        self.tree.SetItemImage(child, self.fldropenidx, wx.TreeItemIcon_Expanded)

    def ViewPanelSetDsp(self, parent, txt, i):
        
        container = parent.viewPanel
        
        container.DestroyChildren()
        
        sizer = wx.BoxSizer( wx.VERTICAL )
        
        self.dispanel = wx.Panel(container, wx.ID_ANY, wx.DefaultPosition, container.GetClientSize(), wx.TAB_TRAVERSAL )
#        self.viewPanel_sub = wx.Panel( self.viewPanel, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
    
        sizer.Add( self.dispanel, 1, wx.EXPAND |wx.ALL, 5 )
        
        #        self.m_panel25.SetBackgroundColour( wx.SystemSettings.GetColour( "sky blue" ) )
        
        self.dispanel.SetBackgroundColour("sky blue")
        wx.StaticText(self.dispanel, -1, txt, (20*i, 10*i))
        

        container.SetSizer(sizer)
#        container.SetAutoLayout(True)
        container.Layout()
        
