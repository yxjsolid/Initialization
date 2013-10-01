#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys
import wx
import MainBase
from MyGlobal import *
from MyIoNode import *
from MiddleWare_Edit_IO import *
from MyWidgetLibrary import *
from MyDraggablePanel import *


class StatusDisplayMgmt():
    def __init__(self):

        self.statusDisplay = []

        return

    def appendStatusDisplayList(self, panel):
        self.statusDisplay.append(panel)


class statusDisplayView():
    def __init__(self, viewCtrl, colSetting):
        self.viewCtrl = viewCtrl
        # self.SetupStatusDispList()
        self.colSetting = colSetting
        self.setupStatusDisplayGrid(colSetting)

        return


    def getDisplaySize(self):
        rowCnt = self.viewCtrl.GetNumberRows()
        height = 47 + rowCnt * 30
        width = 47 + self.colSetting[0] + self.colSetting[1]

        return (width, height)

    def setupStatusDisplayGrid(self, colSetting):
        self.viewCtrl.SetColLabelValue(0, STATUS_DISPLAY_NAME)
        self.viewCtrl.SetColLabelValue(1, STATUS_DISPLAY_STATUS)

        return

    def setRowItem(self, row, nodeObj):
        self.viewCtrl.SetRowSize(row, 30)
        print "self.colSetting", self.colSetting

        if self.colSetting is not None:
            self.viewCtrl.SetColSize(0, self.colSetting[0])
            self.viewCtrl.SetColSize(1, self.colSetting[1])

        self.viewCtrl.SetCellValue(row, 0, nodeObj.name)
        self.viewCtrl.SetCellValue(row, 1, u"关闭关闭关闭关闭关闭关闭关闭关闭关闭关闭")
        #self.viewCtrl.SetCellValue(1, 2, nodeObj.name)
        #self.viewCtrl.SetCellValue(0, 3, u"关闭")


    def gridInsertStatusIoNode(self, index, ioNode):
        """ ref SetStringItem """
        rowCnt = self.viewCtrl.GetNumberRows()

        #self.viewCtrl.AppendRows()

        print "rowCnt = ", rowCnt


        if index > rowCnt + 1:
            print "error"
            return

        if index == -1:
            if rowCnt == 0:
                self.viewCtrl.AppendRows()

                self.setRowItem(0, ioNode)
            else:
                self.viewCtrl.AppendRows()
                self.viewCtrl.SetRowSize(rowCnt, 30)
                self.setRowItem(rowCnt, ioNode)
        else:
            self.setRowItem(index, ioNode)

    def getColumnSetting(self):
        return [self.viewCtrl.GetColSize(0), self.viewCtrl.GetColSize(1)]

    # def SetupStatusDispList(self):
    #     listCtrl = self.viewCtrl
    #
    #     listCtrl.InsertColumn(0, "#", wx.LIST_FORMAT_LEFT)
    #     listCtrl.InsertColumn(1, STATUS_DISPLAY_NAME, wx.LIST_FORMAT_LEFT)
    #     listCtrl.InsertColumn(2, STATUS_DISPLAY_STATUS)
    #
    #     listCtrl.SetColumnWidth(0, 100)
    #     listCtrl.SetColumnWidth(1, 100)
    #     listCtrl.SetColumnWidth(2, 100)
    #
    # def setNodeItem(self, itemIndex, nodeObj):
    #     listCtrl = self.viewCtrl
    #
    #     listCtrl.SetStringItem(itemIndex, 0, str(itemIndex + 1), 0)
    #     listCtrl.SetStringItem(itemIndex, 1, nodeObj.name, 0)
    #     listCtrl.SetStringItem(itemIndex, 2, u"关闭", 0)
    #     listCtrl.SetPyData(itemIndex, nodeObj)
    #
    # def listInsertStatusIoNode(self, index, ioNode):
    #     """ ref SetStringItem """
    #     listCtrl = self.viewCtrl
    #     nodeCnt = listCtrl.GetItemCount()
    #
    #     if index > nodeCnt + 1:
    #         print "error"
    #         return
    #
    #     if index == -1:
    #         if nodeCnt == 0:
    #             index = listCtrl.InsertStringItem(sys.maxint, str(nodeCnt + 1), 0)
    #         else:
    #             index = listCtrl.InsertStringItem(nodeCnt, str(nodeCnt + 1), 0)
    #     else:
    #         index = listCtrl.InsertStringItem(index, str(index + 1), 0)
    #
    #     self.setNodeItem(index, ioNode)
    #     listCtrl.Select(index)


class Panel_Status_Display(MainBase.Panel_Status_Display_Base):
    def __init__(self, parent, nodeObjList, colSetting):
        MainBase.Panel_Status_Display_Base.__init__(self, parent)
        self.nodeObjList = nodeObjList
        self.viewCtrl = statusDisplayView(self.statusDispGrid, colSetting)
        self.onLoadUpdate()
        self.Show()

    def getDisplaySize(self):
        return self.viewCtrl.getDisplaySize()

    def onLoadUpdate(self):
        if self.nodeObjList is None:
            return

        for node in self.nodeObjList:
            self.viewCtrl.gridInsertStatusIoNode(-1, node)

        return


class Panel_Edit_Status_Display(MainBase.Panel_Edit_Status_Display_Base):
    def __init__(self, window, onEditPanel, pos):
        MainBase.Panel_Edit_Status_Display_Base.__init__(self, window.frame)
        #self.window = window
        self.viewCtrl = statusDisplayView(self.status_disp_grid, None)
        self.popupPos = wx.Point(pos.x, pos.y)
        self.onEditPanel = onEditPanel
        self.window = window
        self.nodeList = []
        self.Show()

    def onAddStatusUpdate(self, nodeObj):
        self.nodeList.append(nodeObj)
        self.viewCtrl.gridInsertStatusIoNode(-1, nodeObj)
        return


    def onAddNewStatus(self):
        window = MyPopupWindow(size=(600, 400), title=IO_NODE_ADD_NEW)
        panel = Panel_Manage_IO_Node(window, self, Panel_Manage_IO_Node.MODE_SELECT)
        panel.disableToolBar()
        window.windowPopup()

        return

    def onDeleteStatus(self):

        return

    def onApply(self, event):
        d = MyDraggable(self.onEditPanel, self.popupPos, (2000, 2000))

        colSetting = self.viewCtrl.getColumnSetting()
        subP = Panel_Status_Display(d, self.nodeList, colSetting)

        runtime = globalGetRuntime()
        runtime.statusDisplayMgmt.appendStatusDisplayList(subP)


        d.AdjustToChild(subP)
        subP.Refresh()
        d.Refresh()

        subP.Disable()

        #self.onEditPanel.Refresh()


        self.window.closeWindow()

        return

    def onStatusDispToolClicked(self, event):
        eventId = event.GetId()
        ret = {
            MainBase.STATUS_ADD: lambda: self.onAddNewStatus(),
            MainBase.STATUS_DEL: lambda: self.onDeleteStatus(),
            # MainBase.ioBoard_up:   lambda: self.onIoBoardMoveUp(),
            # MainBase.ioBoard_down: lambda: self.onIoBoardMoveDown(),
        }[eventId]()
