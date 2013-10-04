#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys
import wx
import MainBase
from MyGlobal import *
from MyIoNode import *
#from MyConfiguration import *


class IoCategoryViewControl():
    def __init__(self, ioNodeEditorIn):
        self.ioNodeEditor = ioNodeEditorIn
        self.root = None
        self.inputRoot = None
        self.outputRoot = None

        self.viewTree = self.ioNodeEditor.getIoCategoryViewTree()
        self.setupIoCategoryView()

        # self.viewTree.Bind(CT.EVT_TREE_ITEM_EXPANDED, self.OnItemExpanded)
        # self.viewTree.Bind(CT.EVT_TREE_ITEM_COLLAPSED, self.OnItemCollapsed)
        # self.viewTree.Bind(CT.EVT_TREE_SEL_CHANGED, self.OnSelChanged)
        # self.viewTree.Bind(CT.EVT_TREE_SEL_CHANGING, self.OnSelChanging)
        self.viewTree.Bind(wx.EVT_RIGHT_DOWN, self.OnRightDown)
        self.viewTree.Bind(wx.EVT_RIGHT_UP, self.OnRightUp)

        self.onLoadUpdate()

    def onLoadUpdate(self):
        cfg = globalGetCfg()
        inList = cfg.IoNodeCfg.getInputIoCategoryList()
        outList = cfg.IoNodeCfg.getOutputIoCategoryList()

        for cate in inList:
            cate.type = DeviceIoBoard.BOARD_TYPE_INPUT
            self.addNewCategory(self.viewTree, self.inputRoot, cate)

        for cate in outList:
            cate.type = DeviceIoBoard.BOARD_TYPE_OUTPUT
            self.addNewCategory(self.viewTree, self.outputRoot, cate)

        if not self.viewTree.ItemHasChildren(self.inputRoot):
            cate = IoNodeCategory()
            cate.type = DeviceIoBoard.BOARD_TYPE_INPUT
            self.addNewCategory(self.viewTree, self.inputRoot, cate)

        if not self.viewTree.ItemHasChildren(self.outputRoot):
            cate = IoNodeCategory()
            cate.type = DeviceIoBoard.BOARD_TYPE_OUTPUT
            self.addNewCategory(self.viewTree, self.outputRoot, cate)

        return

    def setupIoCategoryView(self):
        self.root = self.viewTree.AddRoot(IO_NODE_ROOT_NAME)
        self.inputRoot = self.viewTree.AppendItem(self.root, EDIT_IO_NODE_LABEL_INPUT)
        self.outputRoot = self.viewTree.AppendItem(self.root, EDIT_IO_NODE_LABEL_OUTPUT)

    def doPopUpMenu(self, groupItem):
        treeView = self.viewTree
        menu = wx.Menu()

        item = menu.Append(wx.ID_ANY, EDIT_IO_NODE_LABEL_NEW_GROUP)
        treeView.Bind(wx.EVT_MENU, self.OnItemAppend, item)
        if groupItem != self.outputRoot and groupItem != self.inputRoot:
            item.Enable(False)

        item = menu.Append(wx.ID_ANY, EDIT_IO_NODE_LABEL_RENAME_GROUP)
        treeView.Bind(wx.EVT_MENU, self.OnItemRename, item)

        if groupItem == self.outputRoot or groupItem == self.inputRoot:
            item.Enable(False)

        # menu.AppendSeparator()
        #
        # item = menu.Append(wx.ID_ANY, EDIT_IO_NODE_LABEL_EXPAND_GROUP)
        # treeView.Bind(wx.EVT_MENU, self.OnItemAppend, item)
        #
        # item = menu.Append(wx.ID_ANY, EDIT_IO_NODE_LABEL_COLLAPSE_GROUP)
        # treeView.Bind(wx.EVT_MENU, self.OnItemAppend, item)
        menu.AppendSeparator()

        item = menu.Append(wx.ID_ANY, EDIT_IO_NODE_LABEL_DEL_GROUP)
        treeView.Bind(wx.EVT_MENU, self.OnItemDelete, item)
        if groupItem == self.outputRoot or groupItem == self.inputRoot:
            item.Enable(False)

        treeView.PopupMenu(menu)
        menu.Destroy()

    def OnRightDown(self, event):
        pt = event.GetPosition()
        item, flags = self.viewTree.HitTest(pt)

        if item:
            self.item = item
            print "OnRightClick: %s, %s, %s"
            self.viewTree.SelectItem(item)

    def OnRightUp(self, event):

        groupItem = self.item

        if not groupItem:
            event.Skip()
            return

        self.doPopUpMenu(groupItem)

    def OnItemRename(self, event):
        currentItem = self.item
        groupNode = self.viewTree.GetItemPyData(currentItem)
        name = groupNode.name
        dlg = wx.TextEntryDialog(self.ioNodeEditor.frame, EDIT_IO_NODE_LABEL_GROUP_INPUT_NAME, EDIT_IO_NODE_LABEL_NEW_GROUP, name)

        if dlg.ShowModal() == wx.ID_OK:
            newName = dlg.GetValue()
            self.viewTree.SetItemText(currentItem, newName)
            groupNode.name = newName

        dlg.Destroy()

    def addNewCategory(self, viewTree, rootItem, category):
        newItem = viewTree.AppendItem(rootItem, category.name)
        viewTree.SetItemPyData(newItem, category)
        viewTree.EnsureVisible(newItem)
        return

    def deleteCategory(self, viewTree, delItem):
        viewTree.Delete(delItem)
        return

    def onCategoryItemSelChanged(self, event):
        selItem = self.viewTree.GetSelection()
        self.ioNodeEditor.ioNodeCtrl.updateAddNewToolStatus(0)

        if selItem == self.viewTree.GetRootItem():
            return

        if selItem == self.inputRoot:
            categoryList = self.getChildrenItem(self.viewTree, selItem)
        elif selItem == self.outputRoot:
            categoryList = self.getChildrenItem(self.viewTree, selItem)
        else:
            catObj = self.getSelectedCategoryObj()

            categoryList = [self.getSelectedCategoryObj()]
            self.ioNodeEditor.ioNodeCtrl.updateAddNewToolStatus(1)

        self.ioNodeEditor.ioNodeCtrl.updateIoNodeView(categoryList, True)
        return

    def OnItemAppend(self, event):

        dlg = wx.TextEntryDialog(self.ioNodeEditor.frame, EDIT_IO_NODE_LABEL_GROUP_INPUT_NAME, EDIT_IO_NODE_LABEL_NEW_GROUP, EDIT_IO_NODE_LABEL_GROUP_DEFAULT)

        if dlg.ShowModal() == wx.ID_OK:
            newName = dlg.GetValue()
            newCategory = IoNodeCategory()
            newCategory.name = newName

            if self.item is self.inputRoot:
                newCategory.type = DeviceIoBoard.BOARD_TYPE_INPUT
            elif self.item is self.outputRoot:
                newCategory.type = DeviceIoBoard.BOARD_TYPE_OUTPUT

            self.addNewCategory(self.viewTree, self.item, newCategory)

        dlg.Destroy()

    def OnItemDelete(self, event):
        currentItem = self.item
        # groupNode = self.viewTree.GetItemPyData(currentItem)
        #name = groupNode.name
        dlg = MainBase.ConfirmDIALOG(self.ioNodeEditor.frame)
        dlg.SetTitle(EDIT_IO_NODE_LABEL_DEL_GROUP)
        dlg.alert_msg_txt.SetLabel(EDIT_IO_NODE_LABEL_DEL_GROUP_CONFIRM)

        if dlg.ShowModal() == wx.ID_OK:
            self.deleteCategory(self.viewTree, currentItem)

        dlg.Destroy()

    def getChildrenItem(self, tree, parent):
        result = []
        item, cookie = tree.GetFirstChild(parent)

        while item:
            result.append(tree.GetItemPyData(item))
            item, cookie = tree.GetNextChild(parent, cookie)
        return result

    def getInputIoCategoryList(self):
        treeView = self.viewTree
        return self.getChildrenItem(treeView, self.inputRoot)

    def getOutputIoCategoryList(self):
        treeView = self.viewTree
        return self.getChildrenItem(treeView, self.outputRoot)

    def getSelectedCategoryObj(self):
        return self.viewTree.GetItemPyData(self.viewTree.GetSelection())


class IoNodeViewControl():
    def __init__(self, ioNodeEditorIn):
        self.ioNodeEditor = ioNodeEditorIn
        self.listView = self.ioNodeEditor.getIoNodeViewList()
        self.SetupIoNodeList()
        self.updateAddNewToolStatus(0)
        self.updateToolStatus(0)

    def SetupIoNodeList(self):
        listView = self.listView

        listView.InsertColumn(0, "#", wx.LIST_FORMAT_RIGHT)
        listView.InsertColumn(1, IO_NODE_LIST_COL_NAME)
        listView.InsertColumn(2, IO_NODE_LIST_COL_DESC)
        listView.InsertColumn(3, IO_NODE_LIST_COL_IO)

        listView.SetColumnWidth(0, wx.LIST_AUTOSIZE_USEHEADER)
        listView.SetColumnWidth(1, wx.LIST_AUTOSIZE_USEHEADER)
        listView.SetColumnWidth(2, 100)
        listView.SetColumnWidth(3, 400)

    def onIoNodeToolClicked(self, event):
        eventId = event.GetId()
        ret = {
            MainBase.IO_NODE_NEW: lambda: self.onAddNewIoNode(),
            MainBase.IO_NODE_EDIT: lambda: self.onEditIoNode(),
            MainBase.IO_NODE_DEL: lambda: self.OnDeleteIoNode(),
            } [eventId]()

    def getSelectedCategoryObj(self):
        return self.ioNodeEditor.categoryCtrl.getSelectedCategoryObj()

    def onAddNewIoNode(self):
        categoryObj = self.ioNodeEditor.categoryCtrl.getSelectedCategoryObj()
        window = MyPopupWindow(size=(600, 400), title=IO_NODE_ADD_NEW)
        Panel_Edit_IO_Node(window, self, cateObj=categoryObj)
        window.windowPopup()
        return

    def getCurrentSelectedObj(self):
        editItem = self.listView.GetFirstSelected()
        categoryObj = self.listView.GetItemPyData(editItem)[0]
        nodeObj = self.listView.GetItemPyData(editItem)[1]

        return categoryObj, nodeObj

    def onEditIoNode(self):
        # editItem = self.listView.GetFirstSelected()
        #
        # categoryObj = self.listView.GetItemPyData(editItem)[0]
        # nodeObj = self.listView.GetItemPyData(editItem)[1]

        categoryObj, nodeObj = self.getCurrentSelectedObj()

        window = MyPopupWindow(size=(600, 400), title=IO_NODE_EDIT)
        Panel_Edit_IO_Node(window, self, self.listView.GetFirstSelected(), categoryObj, nodeObj)
        window.windowPopup()

        return

    def onIoNodeDelUpdate(self, delIndex):
        #station = self.getCurrentCanStation()
        self.updateToolStatus(0)
        categoryObj, nodeObj = self.getCurrentSelectedObj()
        self.updateIoNodeView([categoryObj], False)

        ctrl = self.listView
        listCnt = ctrl.GetItemCount()

        if listCnt > 0:
            if delIndex > 0:
                ctrl.Select(delIndex - 1)
            else:
                ctrl.Select(0)

    def OnDeleteIoNode(self):
        # ctrl = self.listView
        # itemIndex = tree.GetFirstSelected()
        delIndex = self.listView.GetFirstSelected()

        categoryObj, nodeObj = self.getCurrentSelectedObj()

        dlg = MainBase.ConfirmDIALOG(self.ioNodeEditor.frame)
        dlg.SetTitle(WINDOW_TITLE_DEL_IO_NODE)
        dlg.alert_msg_txt.SetLabel(DIALOG_ALERT_DEL_IO_NODE)

        if dlg.ShowModal() == wx.ID_OK:
            if nodeObj:
                categoryObj.removeIoNode(nodeObj)
        dlg.Destroy()

        self.onIoNodeDelUpdate(delIndex)

        return

    def onIoNodeListItemSelected(self):
        self.updateToolStatus(1)
        return

    def updateAddNewToolStatus(self, isEnable):
        if isEnable:
            self.ioNodeEditor.ioNode_toolbar.EnableTool(MainBase.IO_NODE_NEW, 1)
        else:
            self.ioNodeEditor.ioNode_toolbar.EnableTool(MainBase.IO_NODE_NEW, 0)
            self.updateToolStatus(0)

    def updateToolStatus(self, isEnable):
        if isEnable:
            self.ioNodeEditor.ioNode_toolbar.EnableTool(MainBase.IO_NODE_EDIT, 1)
            self.ioNodeEditor.ioNode_toolbar.EnableTool(MainBase.IO_NODE_DEL, 1)
        else:
            self.ioNodeEditor.ioNode_toolbar.EnableTool(MainBase.IO_NODE_EDIT, 0)
            self.ioNodeEditor.ioNode_toolbar.EnableTool(MainBase.IO_NODE_DEL, 0)

    def setDefaultSelect(self):
        ctrl = self.listView
        listCnt = ctrl.GetItemCount()

        if listCnt > 0:
            ctrl.Select(0)

    def updateIoNodeView(self, categoryList, isOnLoad):
        self.listView.DeleteAllItems()
        for cateObj in categoryList:
            if cateObj:
                for ioNode in cateObj.ioNodeList:
                    self.listInsertIoNode(-1, cateObj, ioNode)

        if isOnLoad:
            self.setDefaultSelect()

        return

    def editUpdateIoNodeItem(self, itemIndex, categoryObj, nodeObj):
        self.setNodeItem(itemIndex, categoryObj, nodeObj)

    def appendIoNodeListView(self, nodeObj):
        categoryObj = self.getSelectedCategoryObj()
        categoryObj.ioNodeList.append(nodeObj)

        ctrl = self.listView
        nodeCnt = ctrl.GetItemCount()

        if nodeCnt == 0:
            index = ctrl.InsertStringItem(sys.maxint, "", 0)
        else:
            index = ctrl.InsertStringItem(nodeCnt, "", 0)

        self.setNodeItem(index, categoryObj, nodeObj)
        ctrl.Select(index)

    def listInsertIoNode(self, index, categoryObj, ioNode):
        """ ref SetStringItem """
        nodeCnt = self.listView.GetItemCount()

        if index > nodeCnt + 1:
            print "error"
            return

        if index == -1:
            if nodeCnt == 0:
                index = self.listView.InsertStringItem(sys.maxint, str(nodeCnt + 1), 0)
            else:
                index = self.listView.InsertStringItem(nodeCnt, str(nodeCnt + 1), 0)
        else:
            index = self.listView.InsertStringItem(index, str(index + 1), 0)

        self.setNodeItem(index, categoryObj, ioNode)
        self.listView.Select(index)

    def setNodeItem(self, itemIndex, categoryObj, nodeObj):
        self.listView.SetStringItem(itemIndex, 0, str(itemIndex + 1), 0)
        self.listView.SetStringItem(itemIndex, 1, nodeObj.name, 0)
        self.listView.SetStringItem(itemIndex, 2, nodeObj.desc, 0)

        self.listView.SetStringItem(itemIndex, 3, nodeObj.getIoInfoStr(), 0)
        self.listView.SetPyData(itemIndex, [categoryObj, nodeObj])


class Panel_Manage_IO_Node(MainBase.Panel_Manage_IO_Node_Base):
    MODE_MANAGE, MODE_SELECT = range(2)

    def __init__(self, window, onEditParent=None, mode=MODE_MANAGE):
        MainBase.Panel_Manage_IO_Node_Base.__init__(self, window.frame)
        self.categoryCtrl = IoCategoryViewControl(self)
        self.ioNodeCtrl = IoNodeViewControl(self)
        self.mode = mode
        self.onEditParent = onEditParent
        self.window = window

        return

    def disableToolBar(self):
        self.ioNode_toolbar.Disable()

    def getSelectedIoNode(self):
        return self.ioNodeCtrl.getCurrentSelectedObj()

    def onCategoryItemSelChanged(self, event):
        self.categoryCtrl.onCategoryItemSelChanged(event)

    def getIoCategoryViewTree(self):
        return self.io_category_tree

    def getIoNodeViewList(self):
        return self.ioNode_list

    def onIoNodeToolClicked(self, event):
        self.ioNodeCtrl.onIoNodeToolClicked(event)

    def getInputIoCategoryList(self):
        return self.categoryCtrl.getInputIoCategoryList()

    def getOutputIoCategoryList(self):
        return self.categoryCtrl.getOutputIoCategoryList()

    def onIoNodeListItemSelected(self, event):
        return self.ioNodeCtrl.onIoNodeListItemSelected()

    def closeWindow(self):
        self.window.closeWindow()

    def onApply(self, event):

        if self.mode == Panel_Manage_IO_Node.MODE_MANAGE:
            cfg = globalGetCfg()
            inList = self.getInputIoCategoryList()
            outList = self.getOutputIoCategoryList()

            cfg.IoNodeCfg.setInputIoCategoryList(inList)
            cfg.IoNodeCfg.setOutputIoCategoryList(outList)

        elif self.mode == Panel_Manage_IO_Node.MODE_SELECT:
            categoryObj, nodeObj = self.getSelectedIoNode()
            self.onEditParent.onSelectIoNodeUpdate(nodeObj)

        self.closeWindow()
        return


class Panel_Edit_IO_Node(MainBase.Panel_Edit_IO_Node_Base):
    def __init__(self, window, viewCtrlIn=None, editListItemIn=-1, cateObj=None, ioNodeIn=None):
        MainBase.Panel_Edit_IO_Node_Base.__init__(self, window.frame)
        self.window = window
        self.viewCtrl = viewCtrlIn

        self.categoryObj = cateObj
        self.onEditListItem = editListItemIn
        self.onEditNode = ioNodeIn

        self.onLoadUpdate()
        return

    def onApply(self, event):
        name = self.nodeNameTxt.GetValue()
        desc = self.nodeDescTxt.GetValue()
        offInfo = self.offInfoTxt.GetValue()
        onInfo = self.onInfoTxt.GetValue()

        sel = self.stationChoice.GetCurrentSelection()
        station = self.stationChoice.GetClientData(sel)

        sel = self.boardChoice.GetCurrentSelection()
        board = self.boardChoice.GetClientData(sel)

        sel = self.portChoice.GetCurrentSelection()
        port = self.portChoice.GetClientData(sel)

        if self.onEditNode is not None:
            self.onEditNode.name = name
            self.onEditNode.desc = desc
            self.onEditNode.offInfo = offInfo
            self.onEditNode.onInfo = onInfo
            self.onEditNode.station = station
            self.onEditNode.board = board
            self.onEditNode.port = port

            self.viewCtrl.editUpdateIoNodeItem(self.onEditListItem, self.categoryObj, self.onEditNode)
            #self.viewCtrl.updateBoardListView(self.editListItem, self.onEditBoard)
        else:
            newIoNode = IoNode()
            newIoNode.name = name
            newIoNode.desc = desc
            newIoNode.offInfo = offInfo
            newIoNode.onInfo = onInfo
            newIoNode.station = station
            newIoNode.board = board
            newIoNode.port = port
            newIoNode.category = self.categoryObj

            self.viewCtrl.appendIoNodeListView(newIoNode)

        self.window.closeWindow()

    def onLoadUpdate(self):
        cfgObj = wx.GetApp().getConfigure()
        stationCfg = cfgObj.stationCfg
        self.buildChoice(stationCfg)

        if self.onEditListItem != -1:
            self.onEditUpdate()

        return

    def setSelectObj(self, choiceObj, clientData):
        for i in range(choiceObj.GetCount()):
            if clientData == choiceObj.GetClientData(i):
                choiceObj.SetSelection(i)

    def onEditUpdate(self):
        self.nodeNameTxt.SetValue(self.onEditNode.name)
        self.nodeDescTxt.SetValue(self.onEditNode.desc)
        self.offInfoTxt.SetValue(self.onEditNode.offInfo)
        self.onInfoTxt.SetValue(self.onEditNode.onInfo)

        self.setSelectObj(self.stationChoice, self.onEditNode.station)
        self.buildBoardChoice(self.onEditNode.station)

        self.setSelectObj(self.boardChoice, self.onEditNode.board)
        self.setSelectObj(self.portChoice, self.onEditNode.port)

        return

    def buildChoice(self, stationMgmt):
        self.buildStationChoice(stationMgmt)
        if stationMgmt.stationList:
            station = stationMgmt.stationList[0]
            self.buildBoardChoice(station)
            self.buildPortChoice()

    def buildStationChoice(self, stationMgmt):
        """select the previous selected item after update"""

        choiceObj = self.stationChoice
        choiceObj.Clear()

        for station in stationMgmt.stationList:
            stationInfoStr = station.getStationInfo()
            choiceObj.Append(stationInfoStr, station)

        choiceObj.SetSelection(0)

    def buildBoardChoice(self, station):
        """select the previous selected item after update"""

        choiceObj = self.boardChoice
        choiceObj.Clear()

        if self.categoryObj.type == DeviceIoBoard.BOARD_TYPE_OUTPUT:
            boardList = station.OutputBoardList
        elif self.categoryObj.type == DeviceIoBoard.BOARD_TYPE_INPUT:
            boardList = station.InputBoardList

        for board in boardList:
            choiceObj.Append(str(board.boardId), board)

        choiceObj.SetSelection(0)

    def buildPortChoice(self):
        choiceObj = self.portChoice
        choiceObj.Clear()

        for i in range(8):
            choiceObj.Append(str(i + 1), i + 1)

        choiceObj.SetSelection(0)

    def onStationChoice(self, event):
        print "onStationChoice"
        station = event.GetClientData()
        self.buildBoardChoice(station)
        return