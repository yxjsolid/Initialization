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

    def setupCanStationTreeView(self):
        tree = self.viewTree

        #tree.AddColumn(LABEL_CAN_STATION_ID)
        tree.AddColumn("#")
        tree.AddColumn(LABEL_CAN_STATION_NAME)
        tree.AddColumn(LABEL_CAN_STATION_ID)
        tree.AddColumn(LABEL_CAN_STATION_DESC)

        tree.SetMainColumn(1)
        #
        #tree.SetColumnWidth(0, 20)

        #tree.SetColumnEditable(0, False)
        tree.SetColumnShown(0, False)
        tree.SetColumnEditable(1, True)
        tree.SetColumnEditable(2, True)
        tree.SetColumnEditable(3, True)

        tree.root = tree.AddRoot("Root Item")

    def addNewCanStation(self):
        tree = self.viewTree
        name = OPERATION_NAME_DEFAULT + str(tree.GetCount()+1)
        station = DeviceCanStation()
        station.name = name
        self.appendCanStationList(station)

    def appendCanStationList(self, station):
        tree = self.viewTree
        listCnt = tree.GetChildrenCount(tree.root)
        child = tree.AppendItem(tree.root, "")

        print "appendCanStationList, id", station.stationId

        #tree.SetItemText(child, str(station.stationId), 0)
        tree.SetItemText(child, str(listCnt + 1), 0)
        tree.SetItemText(child, station.name,       1)
        tree.SetItemText(child, str(station.stationId), 2)
        tree.SetItemText(child, station.info, 3)
        tree.SetItemPyData(child, station)

    def onCanStationUpdate(self):
        canStationList = wx.GetApp().getStationMgmt().getCanStationList()

        for station in canStationList:
            self.appendCanStationList(station)

        return

    def getCurrentCanStation(self):
        tree = self.viewTree
        item = tree.GetSelection()

        if item != tree.GetRootItem():
            print "not root"
            return tree.GetItemPyData(item)
        else:
            print " root"

        if item.IsOk():
            print "ok"
        else:
            print "not ok"

    def setDefaultSelection(self):
        tree = self.viewTree

        #help(tree)
        root = tree.GetRootItem()

        item = tree.GetNext(root)
        if item.IsOk():

            print "get item ok!!!!!!!"
            tree.SelectItem(item)

    def getCanStationList(self):
        stationList = []
        tree = self.viewTree
        item = tree.GetRootItem()
        while True:
            item = tree.GetNext(item)
            if item.IsOk():
                station = tree.GetItemPyData(item)
                stationList.append(station)
                print station.name
            else:
                break
        return stationList

    def setCanStation(self, station, index, txtIn):
        if index is 0:
            station.id = txtIn
        elif index is 1:
            station.name = txtIn
        elif index is 2:
            station.info = txtIn

    def deleteCanStation(self):
        tree = self.viewTree
        item = tree.GetSelection()

        #print "\n\n deleteActGrp"
        if item != tree.GetRootItem():
            prev = tree.GetPrev(item)
            next = tree.GetNext(item)
            tree.Delete(item)
            if prev.IsOk():
                tree.SelectItem(prev)
            elif next.IsOk():
                tree.SelectItem(next)

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
            MainBase.canStation_del:  lambda: self.deleteCanStation(),
            MainBase.canStation_up:   lambda: self.moveUpCanStation(),
            MainBase.canStation_down: lambda: self.moveDownCanStation(),
            }[eventId]()

    def onCanStationItemSelChanged(self, event):
        station = self.getCurrentCanStation()
        print "\n\n onCanStationItemSelChanged:"

        self.canStationEditor.ioBoardViewCtrl.updateIoBoardView(station)

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
        self.ioModuleList = []
        self.SetupIoBoardList()

    ###################################################################
    # action list related

    def SetupIoBoardList(self):
        ioBoardList = self.canStationEditor.ioBoard_list

        ioBoardList.InsertColumn(0, LABEL_IO_BOARD_COLUM_ID, wx.LIST_FORMAT_RIGHT)
        ioBoardList.InsertColumn(1, LABEL_IO_BOARD_COLUM_TYPE)

        #self.list.SetColumnWidth(0, wx.LIST_AUTOSIZE)
        ioBoardList.SetColumnWidth(0, wx.LIST_AUTOSIZE_USEHEADER)
        ioBoardList.SetColumnWidth(1, wx.LIST_AUTOSIZE_USEHEADER)

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
        #actionList.SetStringItem(index, 2, action.moduleFeedback.name, 0)
        #actionList.SetStringItem(index, 3, action.feedbackTimeout, 0)
        #actionList.SetItemData(index, action)

    def listRemoveAction(self, action):
        actionList = self.canStationEditor.action_list
        item = actionList.GetFocusedItem()
        actionList.DeleteItem(item)

    def refreshIoBoardList(self, canStation):
        ioBoardList = self.canStationEditor.ioBoard_list
        ioBoardList.DeleteAllItems()

        if canStation is None:
            return

        for ioBoard in canStation.InputBoardList:
            self.listInsertIoBoard(-1, ioBoard)

        for ioBoard in canStation.OutputBoardList:
            self.listInsertIoBoard(-1, ioBoard)

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

        frame = wx.Frame(None, size=(350, 400))
        Panel_EditIoBoard(frame, self.canStationEditor, targetStation=station)
        frame.CenterOnScreen()
        frame.Show()

    def onDeleteIoBoard(self):
        actionList = self.canStationEditor.action_list
        index = actionList.GetFocusedItem()
        actionList.DeleteItem(index)

        self.onEditActionUpdate()
        actionCount = actionList.GetItemCount()
        if actionCount:
            if index == actionCount:
                actionList.Select(index-1,1)
            else:
                actionList.Select(index,1)
        return

    def onIoBoardMoveUp(self):
        actionList = self.canStationEditor.action_list
        index = actionList.GetFocusedItem()
        if index == -1:
            return

        action = actionList.GetItemData(index)
        actionList.DeleteItem(index)
        if index < 2:
            self.listInsertNewAction(0, action)
            index = 0
        else:
            self.listInsertNewAction(index-1, action)
            index = index-1

        self.onEditActionUpdate()
        actionList.Select(index,1)
        return

    def onIoBoardMoveDown(self):
        actionList = self.canStationEditor.action_list
        index = actionList.GetFocusedItem()
        if index == -1:
            return

        actionCount = actionList.GetItemCount()
        action = actionList.GetItemData(index)
        if actionCount > 1 and index != actionCount-1:
            self.listInsertNewAction(index+2, action)
            actionList.DeleteItem(index)
        else:
            return

        self.onEditActionUpdate()
        actionList.Select(index+1,1)
        return

    def onIoBoardToolClicked(self, event):
        eventId = event.GetId()
        ret = {
            MainBase.ioBoard_new:  lambda: self.onAddNewIoBoard(),
            MainBase.ioBoard_del:  lambda: self.onDeleteIoBoard(),
            MainBase.ioBoard_up:   lambda: self.onIoBoardMoveUp(),
            MainBase.ioBoard_down: lambda: self.onIoBoardMoveDown(),
            }[eventId]()

        print ret

    def updateIoBoardView(self, station):
        if station is None:
            self.canStationEditor.ioBoard_toolbar.EnableTool(MainBase.ioBoard_new, 0)
        else:
            self.canStationEditor.ioBoard_toolbar.EnableTool(MainBase.ioBoard_new, 1)

        self.refreshIoBoardList(station)


class Panel_CanStation(MainBase.Panel_Edit_Can_Station_Base):
    def __init__( self, frame , device=None):
        MainBase.Panel_Edit_Can_Station_Base.__init__( self, frame )
        print "Panel_EditIOStation  1111"

        self.frame = frame
        self.canStationViewCtrl = CanStationViewControl(self)
        self.ioBoardViewCtrl = IoBoardViewControl(self)
        self.onLoadUpdate()

        # self.deviceInfoPanelSetup()
        #
        #
        # self.moduleIoViewCtrl = ModuleIoListControl(self)
        # self.attrCtrl = AttributeViewControl(self)
        # self.actionListCtrl = ActionViewControl(self)
        # self.actGrpCtrl = ActionGroupViewControl(self)
        # self.onLoadUpdate()

    def onIoBoardToolClicked(self, event):
        self.ioBoardViewCtrl.onIoBoardToolClicked(event)

    def onLoadUpdate(self):
        self.canStationViewCtrl.onCanStationUpdate()
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

    def getCanStationViewTree(self):
        return self.canStationTree

    def onCanStationToolClicked(self, event):
        self.canStationViewCtrl.onCanStationToolClicked(event)

    def onCanStationItemSelChanged(self, event):
        self.canStationViewCtrl.onCanStationItemSelChanged(event)

    def onCanStationItemBeginEdit(self, event):
        self.canStationViewCtrl.onCanStationItemBeginEdit(event)

    def onCanStationItemEndEdit(self, event):
        self.canStationViewCtrl.onCanStationItemEndEdit(event)

    def onCanStationItemDelete(self, event):
        self.canStationViewCtrl.onCanStationItemDelete(event)

    ######################################################
    ######################################################


class Panel_EditIoBoard(MainBase.Panel_IoBoard_Base):

    def __init__(self, frame, canStationEditor, targetStation=None):
        MainBase.Panel_IoBoard_Base.__init__(self, frame)
        self.canStationEditor = canStationEditor
        self.targetStation = targetStation
        self.frame = frame
        self.buildBoardTypeChoice()

    def buildBoardTypeChoice(self):
        self.boardType_choice.Clear()

        index = DeviceIoBoard.BOARD_TYPE_INPUT
        self.boardType_choice.Insert(DeviceIoBoard.board_type_choices[index], 0, index)
        self.boardType_choice.SetSelection(0)

        index = DeviceIoBoard.BOARD_TYPE_OUTPUT
        self.boardType_choice.Insert(DeviceIoBoard.board_type_choices[index], 1, index)

    def selectActionType(self, boardType):
        self.boardType = boardType

    def getPrevSelected(self, choiceObj):
        sel = choiceObj.GetSelection()
        if sel == wx.NOT_FOUND:
            return None

        return choiceObj.GetClientData(sel)

    def buildChoiceList(self, itemList, choiceObj):
        """select the previous selected item after update"""
        index = 0

        prevItem = self.getPrevSelected(choiceObj)
        choiceObj.Clear()

        for item in itemList:
            choiceObj.Append(item.name, item)
            if item is prevItem:
                choiceObj.Select(index)
            index += 1

    def createIoBoard(self, boardType, boardId):
        board = DeviceIoBoard()
        board.boardId = boardId
        board.boardType = boardType

        return board

    def onEditUpdate(self, targetObj=None):
        print "Panel_NewAction -> onEditUpdate"
        self.buildOutputChoiceList()
        self.buildFeedbackChoiceList()

        print "targetObj.GetCount()", targetObj.GetCount()
        targetObj.SetSelection(targetObj.GetCount()-1)
        self.deviceEditor.onEditUpdate()

    def onIoBoardTypeChoice(self, event):

        print "onIoBoardTypeChoice"
        self.boardType = event.GetInt()

    def onAddModuleIO(self, event):
        print "onAddModuleIO"

        if self.addOutputBtn is event.GetEventObject():
            targetChoice = self.choice_output
        else:
            targetChoice = self.choice_feedback

        #frame1 = wx.Frame(parent=self.parent, size=(800,400))
        frame1 = wx.Frame(parent=None, size=(800,400))

        Panel_EditModuleIO(frame1, self, self.deviceEditor, targetObj=targetChoice)
        frame1.CenterOnScreen()
        frame1.Show()

    def refreshDisplay(self):
        if self.attribute:
            txt = self.attribute.genAttributeDisplayName()
            self.txt_attribute.SetValue(txt)
            self.setApplyBtnEnabled(1)

    # def callbackGetAttributeSelect(self, attr):
    #     print "callbackGetAttributeSelect"
    #     print attr
    #     self.attribute = attr
    #     self.refreshDisplay()
    #     return
    #
    # def onSelectAttributeBind( self, event ):
    #     print "onSelectOperationOn"
    #     window = MyPopupWindow(size=(600,400), title="setting")
    #     Panel_AttributeSelect(window.frame, self, self.callbackGetAttributeSelect)
    #     window.windowPopup()

    def closeWindow(self):
        self.frame.Close()

    def onApply(self, evt):
        boardId = self.boardId_text.GetValue()
        selIndex = self.boardType_choice.GetSelection()
        boardType = self.boardType_choice.GetClientData(selIndex)
        newBoard = self.createIoBoard(boardType, boardId)

        self.targetStation.addNewIoBoard(newBoard)
        self.canStationEditor.ioBoardViewCtrl.refreshIoBoardList(self.targetStation)
        self.closeWindow()
        return

    def onCancel(self, evt):
        self.closeWindow()
        return
