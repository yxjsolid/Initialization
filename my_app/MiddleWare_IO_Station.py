#!/usr/bin/env python
# -*- coding: utf-8 -*- 
import sys
import wx
import images  
from wxPythonInAction.Chapter_15 import *
import wxPythonInAction.Chapter_15.data
import MainBase
#from MainBase import *
from MyDevice import *
from MyCanStation import *
from ViewSelectPanel import *
import pickle

class CanStationViewControl():
    def __init__(self, canStationEditor):
        self.canStationEditor = canStationEditor
        self.viewTree = self.canStationEditor.getCanStationViewTree()
        self.setupCanStationTreeView()
        self.updateToolStatus(0)
        self.getCanStationCfg()

    def updateToolStatus(self, isEnable):
        if isEnable:
            self.canStationEditor.canStation_toolbar.EnableTool(MainBase.canStation_edit, 1)
            self.canStationEditor.canStation_toolbar.EnableTool(MainBase.canStation_del, 1)
        else:
            self.canStationEditor.canStation_toolbar.EnableTool(MainBase.canStation_edit, 0)
            self.canStationEditor.canStation_toolbar.EnableTool(MainBase.canStation_del, 0)

    def setupCanStationTreeView(self):
        tree = self.viewTree

        tree.SetSingleStyle(wx.LC_EDIT_LABELS, True)
        tree.InsertColumn(0, "#", wx.LIST_FORMAT_LEFT)
        tree.InsertColumn(1, LABEL_CAN_STATION_NAME)
        tree.InsertColumn(2, LABEL_CAN_STATION_ID)
        tree.InsertColumn(3, LABEL_CAN_STATION_DESC)

        tree.SetColumnWidth(0, wx.LIST_AUTOSIZE)
        tree.SetColumnWidth(1, 100)
        tree.SetColumnWidth(2, 100)
        tree.SetColumnWidth(3, 100)

    def clearAllStation(self):
        tree = self.viewTree
        tree.DeleteAllItems()

    def appendCanStationList(self, station):
        self.canStationList.append(station)

    def setDefaultSelect(self):
        tree = self.viewTree
        listCnt = tree.GetItemCount()

        if listCnt > 0:
            tree.Select(0)

    def appendCanStationListView(self, station):
        tree = self.viewTree
        listCnt = tree.GetItemCount()

        if listCnt == 0:
            index = tree.InsertStringItem(sys.maxint, str(listCnt + 1))
        else:
            index = tree.InsertStringItem(listCnt, str(listCnt + 1))

        tree.SetStringItem(index, 1, station.name)
        tree.SetStringItem(index, 2, str(station.stationId))
        tree.SetStringItem(index, 3, station.info)
        tree.SetItemPyData(index, station)

        tree.Select(index)


    def updateCanStationItem(self, itemIndex, station):
        tree = self.viewTree

        tree.SetStringItem(itemIndex, 0, str(itemIndex + 1))
        tree.SetStringItem(itemIndex, 1, station.name)
        tree.SetStringItem(itemIndex, 2, str(station.stationId))
        tree.SetStringItem(itemIndex, 3, station.info)

    def addNewCanStation(self):
        window = MyPopupWindow(size=(400, 200), title=WINDOW_TITLE_ADD_STATION)
        Panel_Edit_Can_Station(window, self)
        window.windowPopup()

    def editCanStation(self):
        window = MyPopupWindow(size=(400, 200), title=WINDOW_TITLE_EDIT_STATION)
        Panel_Edit_Can_Station(window, self, self.viewTree.GetFirstSelected(), self.getCurrentCanStation())
        window.windowPopup()

    def deleteCanStation(self):
        tree = self.viewTree
        itemIndex = tree.GetFirstSelected()

        station = self.getCurrentCanStation()

        dlg = MainBase.ConfirmDIALOG(self.canStationEditor.frame)
        dlg.SetTitle(WINDOW_TITLE_DEL_STATION)
        dlg.alert_msg_txt.SetLabel(DIALOG_ALERT_DEL_STATION)

        if dlg.ShowModal() == wx.ID_OK:
            if station:
                self.canStationList.remove(station)
        dlg.Destroy()

        self.onCanStationDelUpdate(itemIndex)

    def getCanStationCfg(self):
        self.canStationList = wx.GetApp().getStationMgmt().getCanStationList()[:]

    def onCanStationDelUpdate(self, delIndex):
        self.onCanStationUpdate(False)
        tree = self.viewTree
        listCnt = tree.GetItemCount()

        if listCnt > 0:
            if delIndex > 0:
                tree.Select(delIndex - 1)
            else:
                tree.Select(0)
        else:
            self.canStationEditor.ioBoardViewCtrl.updateIoBoardView(None, True)

    def onCanStationUpdate(self, isOnload):
        canStationList = self.canStationList
        self.clearAllStation()
        for station in canStationList:
            if station:
                self.appendCanStationListView(station)

        if isOnload:
            self.setDefaultSelect()
        return

    def getCurrentCanStation(self):
        tree = self.viewTree
        item = tree.GetFirstSelected()
        if item != -1:
            return tree.GetItemPyData(item)

        return None

    def setDefaultSelection(self):
        tree = self.viewTree

        #help(tree)
        # root = tree.GetRootItem()
        #
        # item = tree.GetNext(root)
        # if item.IsOk():
        #
        #     print "get item ok!!!!!!!"
        #     tree.SelectItem(item)

    def getCanStationList(self):
        stationList = []
        tree = self.viewTree
        listCnt = tree.GetItemCount()

        for index in range(listCnt):
            station = tree.GetItemPyData(index)
            stationList.append(station)

        return stationList

    def setCanStation(self, station, index, txtIn):
        if index is 0:
            station.id = txtIn
        elif index is 1:
            station.name = txtIn
        elif index is 2:
            station.info = txtIn

    def moveUpCanStation(self):
        tree = self.viewTree
        item = tree.GetSelection()
        prev = tree.GetPrev(item)
        ctrl = tree.GetItemPyData(item)

        if prev.IsOk():
            prev = tree.GetPrev(prev)
            if prev.IsOk():
                newItem = tree.InsertItem(tree.GetRootItem(), prev, ctrl.name)
                tree.SetItemText(newItem, ctrl.info,1)
                tree.SetItemPyData(newItem, ctrl)
            else:
                newItem = tree.InsertItemBefore(tree.GetRootItem(), 0, ctrl.name)
                tree.SetItemText(newItem, ctrl.info,1)
                tree.SetItemPyData(newItem, ctrl)

            tree.Delete(item)
            tree.SelectItem(newItem)
        return

    def moveDownCanStation(self):
        tree = self.viewTree
        item = tree.GetSelection()
        next = tree.GetNext(item)
        station = tree.GetItemPyData(item)

        if next.IsOk():
            newItem = tree.InsertItem(tree.GetRootItem(), next, station.name)
            tree.SetItemText(newItem, station.info, 1)
            tree.SetItemPyData(newItem, station)

            tree.Delete(item)
            tree.SelectItem(newItem)

    def onCanStationToolClicked(self, event):
        eventId = event.GetId()
        print "onCanStationToolClicked:", eventId
        ret = {
            MainBase.canStation_new:  lambda: self.addNewCanStation(),
            MainBase.canStation_edit:  lambda: self.editCanStation(),
            MainBase.canStation_del:  lambda: self.deleteCanStation(),
            # MainBase.canStation_up:   lambda: self.moveUpCanStation(),
            # MainBase.canStation_down: lambda: self.moveDownCanStation(),
            }[eventId]()

    #def onCanStationItemSelChanged(self, event):
    def onCanStationItemSelected(self, event):
        station = self.getCurrentCanStation()
        self.updateToolStatus(1)

        #self.canStationEditor.ioBoardViewCtrl.updateAddNewToolStatus(1)
        self.canStationEditor.ioBoardViewCtrl.updateIoBoardView(station, True)

    def onCanStationItemBeginEdit(self, event):
        print "\n\n onCanStationItemBeginEdit"
        tree = self.viewTree
        tree.editColumn =  event.GetInt()

    def onCanStationItemEndEdit(self, event):
        tree = self.viewTree
        item = event.GetItem()
        station = tree.GetItemPyData(item)
        newLable =  event.GetLabel()
        self.setCanStation(station, tree.editColumn, newLable)

    def onCanStationItemDelete(self, event):
        print "onActGrpItemDelete"

    def onAddModule(self, event):
        print "onAddModuel"
        #frame1 = wx.Frame(parent=self.parent, size=(800,400))
        frame1 = wx.Frame(parent=None, size=(800,400))

        Panel_EditActGroup(frame1, self, self)
        frame1.CenterOnScreen()
        frame1.Show()
        #------------------------------------------------------------------


class IoBoardViewControl():
    def __init__(self, canStationEditor):
        self.canStationEditor = canStationEditor
        self.viewCtrl = self.canStationEditor.getBoardViewCtrl()

        self.ioModuleList = []
        self.SetupIoBoardList()
        self.updateAddNewToolStatus(0)
        self.updateToolStatus(0)
        return

    def updateAddNewToolStatus(self, isEnable):
        if isEnable:
            self.canStationEditor.ioBoard_toolbar.EnableTool(MainBase.ioBoard_new, 1)
        else:
            self.canStationEditor.ioBoard_toolbar.EnableTool(MainBase.ioBoard_new, 0)
            self.updateToolStatus(0)

    def updateToolStatus(self, isEnable):
        if isEnable:
            self.canStationEditor.ioBoard_toolbar.EnableTool(MainBase.ioBoard_edit, 1)
            self.canStationEditor.ioBoard_toolbar.EnableTool(MainBase.ioBoard_del, 1)
        else:
            self.canStationEditor.ioBoard_toolbar.EnableTool(MainBase.ioBoard_edit, 0)
            self.canStationEditor.ioBoard_toolbar.EnableTool(MainBase.ioBoard_del, 0)

    def SetupIoBoardList(self):
        ioBoardList = self.canStationEditor.ioBoard_list

        ioBoardList.InsertColumn(0, LABEL_IO_BOARD_COLUM_ID, wx.LIST_FORMAT_LEFT)
        ioBoardList.InsertColumn(1, LABEL_IO_BOARD_COLUM_TYPE)

        ioBoardList.SetColumnWidth(0, 100)
        ioBoardList.SetColumnWidth(1, 100)
        #ioBoardList.SetColumnWidth(2, 100)

    def removeBoardObj(self, board):
        canStation = self.getCurrentCanStation()

        if canStation is None:
            return

        if board in canStation.InputBoardList:
            canStation.InputBoardList.remove(board)

        if board in canStation.OutputBoardList:
            canStation.OutputBoardList.remove(board)

    def listInsertIoBoard(self, index, board):
        ioBoardList = self.canStationEditor.ioBoard_list

        """ ref SetStringItem """
        boardCnt = ioBoardList.GetItemCount()

        if index > boardCnt+1:
            print "error"
            return

        if index == -1:
            if boardCnt == 0:
                index = ioBoardList.InsertStringItem(sys.maxint, board.getBoardIdStr(), 0)
            else:
                index = ioBoardList.InsertStringItem(boardCnt, board.getBoardIdStr(), 0)
        else:
            index = ioBoardList.InsertStringItem(index, board.getBoardIdStr(), 0)

        ioBoardList.SetStringItem(index, 1, board.getBoardTypeStr(), 0)
        ioBoardList.SetItemPyData(index, board)
        ioBoardList.Select(index)

    def getCurrentBoardObj(self):
        viewCtrl = self.viewCtrl
        item = viewCtrl.GetFirstSelected()
        if item != -1:
            return viewCtrl.GetItemPyData(item)

        return None

    def setDefaultSelect(self):
        tree = self.viewCtrl
        listCnt = tree.GetItemCount()

        if listCnt > 0:
            tree.Select(0)

    def updateBoardListView(self, itemIndex, board):
        ctrl = self.viewCtrl
        ctrl.SetStringItem(itemIndex, 0, board.getBoardIdStr())
        ctrl.SetStringItem(itemIndex, 1, board.getBoardTypeStr(), 0)
        ctrl.SetItemPyData(itemIndex, board)
        return

    def appendBoardListView(self, board):
        ctrl = self.viewCtrl
        boardCnt = ctrl.GetItemCount()

        if boardCnt == 0:
            index = ctrl.InsertStringItem(sys.maxint, board.getBoardIdStr(), 0)
        else:
            index = ctrl.InsertStringItem(boardCnt, board.getBoardIdStr(), 0)

        ctrl.SetStringItem(index, 1, board.getBoardTypeStr(), 0)
        ctrl.SetItemPyData(index, board)
        ctrl.Select(index)

    def updateBoardList(self, canStation, isOnLoad):
        self.viewCtrl.DeleteAllItems()

        if canStation is None:
            return

        for ioBoard in canStation.InputBoardList:
            self.listInsertIoBoard(-1, ioBoard)

        for ioBoard in canStation.OutputBoardList:
            self.listInsertIoBoard(-1, ioBoard)

        if isOnLoad:
            self.setDefaultSelect()

        return

    def onEditActionUpdate(self):
        actionList = self.canStationEditor.action_list
        actGrp = self.canStationEditor.actGrpCtrl.getCurrentActGrp()
        index = -1
        actions = []

        while True:
            index = actionList.GetNextItem(index)
            print "onEditActionUpdate", index
            if index == -1:
                break

            action = actionList.GetItemData(index)
            actions.append(action)
            #self.dumpAction(action)

        actGrp.setActions(actions)
        self.refreshActionList(actGrp)
        return

    def onAddNewIoBoard(self):
        station = self.canStationEditor.canStationViewCtrl.getCurrentCanStation()

        if station is None:
            print "Error: --> onAddNewIoBoard"

        window = MyPopupWindow(size=(600,400), title=WINDOW_TITLE_ADD_BOARD)
        Panel_EditIoBoard(window, self, targetStation=station)
        window.windowPopup()

    def onEditBoard(self):
        station = self.canStationEditor.canStationViewCtrl.getCurrentCanStation()
        if station is None:
            print "Error: --> onEditBoard"

        board = self.getCurrentBoardObj()

        window = MyPopupWindow(size=(600, 400), title=WINDOW_TITLE_EDIT_BOARD)
        Panel_EditIoBoard(window, self, self.viewCtrl.GetFirstSelected(), targetStation=station, boardIn=board)
        window.windowPopup()

    def onDelBoard(self):
        tree = self.viewCtrl
        itemIndex = tree.GetFirstSelected()
        board = self.getCurrentBoardObj()

        dlg = MainBase.ConfirmDIALOG(self.canStationEditor.frame)
        dlg.SetTitle(WINDOW_TITLE_DEL_BOARD)
        dlg.alert_msg_txt.SetLabel(DIALOG_ALERT_DEL_BOARD)

        if dlg.ShowModal() == wx.ID_OK:
            if board:
                self.removeBoardObj(board)
        dlg.Destroy()

        self.onBoardDelUpdate(itemIndex)

    def getCurrentCanStation(self):
        return self.canStationEditor.canStationViewCtrl.getCurrentCanStation()

    def onBoardDelUpdate(self, delIndex):
        station = self.getCurrentCanStation()
        self.updateIoBoardView(station, False)

        tree = self.viewCtrl
        listCnt = tree.GetItemCount()

        if listCnt > 0:
            if delIndex > 0:
                tree.Select(delIndex - 1)
            else:
                tree.Select(0)
        # else:
        #     self.canStationEditor.ioBoardViewCtrl.updateIoBoardView(None)






    def onIoBoardToolClicked(self, event):
        eventId = event.GetId()
        ret = {
            MainBase.ioBoard_new:  lambda: self.onAddNewIoBoard(),
            MainBase.ioBoard_del:  lambda: self.onDelBoard(),
            MainBase.ioBoard_edit:  lambda: self.onEditBoard(),
            # MainBase.ioBoard_up:   lambda: self.onIoBoardMoveUp(),
            # MainBase.ioBoard_down: lambda: self.onIoBoardMoveDown(),
            }[eventId]()

        print ret

    def updateIoBoardView(self, station, isOnLoad):
        self.canStationEditor.ioBoardViewCtrl.updateAddNewToolStatus(0)

        if station is not None:
            self.canStationEditor.ioBoardViewCtrl.updateAddNewToolStatus(1)

        self.updateBoardList(station, isOnLoad)

    def onIoBoardListItemSelected(self, event):
        board = self.getCurrentBoardObj()
        if board is not None:
            self.updateToolStatus(1)
        else:
            self.updateToolStatus(0)

        return


class Panel_Manage_Can_Station(MainBase.Panel_Manage_Can_Station_Base):
    def __init__(self, frame, device=None):
        MainBase.Panel_Manage_Can_Station_Base.__init__(self, frame)

        self.frame = frame
        self.canStationViewCtrl = CanStationViewControl(self)
        self.ioBoardViewCtrl = IoBoardViewControl(self)
        self.onLoadUpdate()

    def onIoBoardToolClicked(self, event):
        self.ioBoardViewCtrl.onIoBoardToolClicked(event)

    def onLoadUpdate(self):
        self.canStationViewCtrl.onCanStationUpdate(True)
        self.canStationViewCtrl.setDefaultSelection()
        return

    def onEditUpdate(self, targetObj=None):
        self.editDeviceUpdate()

    def editDeviceUpdate(self):
        self.getModuleIoViewControl().onModuleIOListUpdate()
        return



    """
    # main
    """
    def closeWindow(self):
        self.frame.Close()

    def onApply(self, event):
        print "my onApply"
        canStationList = self.canStationViewCtrl.getCanStationList()

        wx.GetApp().getStationMgmt().setCanStationList(canStationList)
        self.closeWindow()

        """ViewSelectPanel.onEditUpdate()"""
        #wx.GetApp().viewPanel_sub.onEditUpdate()

    def onCancel(self, event):
        print "my onCancel"

    def getBoardViewCtrl(self):
        return self.ioBoard_list

    def getCanStationViewTree(self):
        return self.canStationList

    def onCanStationToolClicked(self, event):
        self.canStationViewCtrl.onCanStationToolClicked(event)

    def onCanStationItemSelected(self, event):
        self.canStationViewCtrl.onCanStationItemSelected(event)

    def onCanStationItemBeginEdit(self, event):
        self.canStationViewCtrl.onCanStationItemBeginEdit(event)

    def onCanStationItemEndEdit(self, event):
        self.canStationViewCtrl.onCanStationItemEndEdit(event)

    def onCanStationItemDelete(self, event):
        self.canStationViewCtrl.onCanStationItemDelete(event)

    def onIoBoardListItemSelected(self, event):
        self.ioBoardViewCtrl.onIoBoardListItemSelected(event)
    ######################################################
    ######################################################


class Panel_Edit_Can_Station(MainBase.Panel_Edit_Can_Station_Base):

    def __init__(self, window, canStationViewCtrlIn, editListItemIn=-1, editStationIn=None):
        MainBase.Panel_Edit_Can_Station_Base.__init__(self, window.frame)
        self.canStationViewCtrl = canStationViewCtrlIn
        self.editListItem = editListItemIn
        self.editStation = editStationIn
        self.window = window
        self.onLoadUpdate()

        return

    def onLoadUpdate(self):

        if self.editStation is not None:
            stationName = self.editStation.name
            stationIdStr = str(self.editStation.stationId)
            stationDesc = self.editStation.info
        else:
            stationName = CAN_STATION_DEFAULT_NAME
            stationIdStr = "0"
            stationDesc = CAN_STATION_DEFAULT_DESC

        self.stationName_input.SetValue(stationName)
        self.stationDesc_input.SetValue(stationDesc)
        self.stationId_input.SetValue(stationIdStr)

        return

    def onApply(self, evt):
        stationName = self.stationName_input.GetValue()
        stationId = self.stationId_input.GetValue()
        stationDesc = self.stationDesc_input.GetValue()

        if self.editStation is None:
            station = DeviceCanStation()
            station.stationId = int(stationId)
            station.name = stationName
            station.info = stationDesc
            self.canStationViewCtrl.appendCanStationList(station)
            self.canStationViewCtrl.appendCanStationListView(station)
        else:
            station = self.editStation
            station.stationId = int(stationId)
            station.name = stationName
            station.info = stationDesc
            self.canStationViewCtrl.updateCanStationItem(self.editListItem, station)


        #self.canStationViewCtrl.onCanStationUpdate()
        self.window.closeWindow()
        return


    def onCancel(self, evt):
        self.window.closeWindow()
        return


class Panel_EditIoBoard(MainBase.Panel_IoBoard_Base):

    def __init__(self, window, viewCtrlIn, editListItemIn=-1, targetStation=None, boardIn=None):
        MainBase.Panel_IoBoard_Base.__init__(self, window.frame)
        self.viewCtrl = viewCtrlIn
        self.targetStation = targetStation
        self.onEditBoard = boardIn
        self.editListItem = editListItemIn
        self.window = window
        self.buildBoardTypeChoice()
        self.onLoadUpdate()

    def onLoadUpdate(self):

        if self.onEditBoard:
            boardId = self.onEditBoard.boardId
            boardType = self.onEditBoard.boardType
            self.boardId_text.SetValue(str(boardId))
            for index in range(self.boardType_choice.GetCount()):
                if boardType == self.boardType_choice.GetClientData(index):
                    self.boardType_choice.SetSelection(index)

    def buildBoardTypeChoice(self):
        self.boardType_choice.Clear()

        index = DeviceIoBoard.BOARD_TYPE_INPUT
        self.boardType_choice.Insert(DeviceIoBoard.board_type_choices[index], 0, index)
        self.boardType_choice.SetSelection(0)

        index = DeviceIoBoard.BOARD_TYPE_OUTPUT
        self.boardType_choice.Insert(DeviceIoBoard.board_type_choices[index], 1, index)

    def createIoBoard(self, boardType, boardId):
        board = DeviceIoBoard()
        board.boardId = boardId
        board.boardType = boardType

        return board

    def onIoBoardTypeChoice(self, event):

        print "onIoBoardTypeChoice"
        self.boardType = event.GetInt()

    def onApply(self, evt):
        boardId = int(self.boardId_text.GetValue())
        selIndex = self.boardType_choice.GetSelection()
        boardType = int(self.boardType_choice.GetClientData(selIndex))

        if self.onEditBoard is not None:
            self.onEditBoard.boardId = boardId
            self.onEditBoard.boardType = boardType

            self.viewCtrl.updateBoardListView(self.editListItem, self.onEditBoard)
        else:
            newBoard = self.createIoBoard(boardType, boardId)
            self.targetStation.addNewIoBoard(newBoard)
            self.viewCtrl.appendBoardListView(newBoard)

        #self.viewCtrl.updateBoardList(self.targetStation, False)
        self.window.closeWindow()
        return

    def onCancel(self, evt):
        self.window.closeWindow()
        return
