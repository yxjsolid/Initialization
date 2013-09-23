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
from ViewSelectPanel import *
import pickle



class CanStationViewControl():
    def __init__(self, canStationEditor):
        self.canStationEditor = canStationEditor
        self.viewTree = self.canStationEditor.getOperationViewTree()
        self.ioModuleList = []
        self.setupCanStationTreeView()

    def setupCanStationTreeView(self):
        tree = self.viewTree



        tree.AddColumn(LABEL_CAN_STATION_ID)
        tree.AddColumn(LABEL_CAN_STATION_NAME)
        tree.AddColumn(LABEL_CAN_STATION_DESC)

        tree.SetMainColumn(0) # the one with the tree in it...
        tree.SetColumnWidth(0, 150)

        tree.SetColumnEditable(0, True)
        tree.SetColumnEditable(1, True)
        tree.SetColumnEditable(2, True)

        tree.root = tree.AddRoot("Root Item")

    def addNewCanStation(self):
        tree = self.viewTree
        name = OPERATION_NAME_DEFAULT + str(tree.GetCount()+1)
        ctrl = DeviceOperation(self.canStationEditor.thisDevice, name)
        self.appendActGrp(ctrl)

    def appendActGrp(self, ctrl):
        tree = self.viewTree
        child = tree.AppendItem(tree.root, ctrl.name)
        tree.SetItemText(child, ctrl.info,1)
        tree.SetItemPyData(child, ctrl)

    def onCanStationUpdate(self):
        for ctrl in self.canStationEditor.thisDevice.operations:
            self.appendActGrp(ctrl)

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

    def getActionGroupList(self):
        ActGrps = []
        tree = self.viewTree
        item = tree.GetRootItem()
        while True:
            item = tree.GetNext(item)
            if item.IsOk():
                ActGrp = tree.GetItemPyData(item)
                ActGrps.append(ActGrp)
                print ActGrp.name
            else:
                break
        return ActGrps

    def setActGrp(self, ctrl,index, txtIn):
        if index is 0:
            ctrl.name = txtIn
        elif index is 1:
            ctrl.info = txtIn

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
            tree.SetItemText(newItem, station.info,1)
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

        self.canStationEditor.stationBoardViewCtrl.updateIoBoardView(station)


    def onCanStationItemBeginEdit(self, event):
        print "\n\n onCanStationItemBeginEdit"
        tree = self.viewTree
        tree.editColumn =  event.GetInt()

    def onCanStationItemEndEdit(self, event):
        tree = self.viewTree
        item = event.GetItem()
        ctrl = tree.GetItemPyData(item)
        newLable =  event.GetLabel()
        self.setActGrp(ctrl, tree.editColumn, newLable)
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

class StationBoardViewControl():
    def __init__(self, canStationEditor):
        self.canStationEditor = canStationEditor
        self.ioModuleList = []
        self.SetupStationBoardList()

    ###################################################################
    # action list related

    def SetupStationBoardList(self):
        ioBoardList = self.canStationEditor.ioBoard_list

        ioBoardList.InsertColumn(0, "")
        #actionList.InsertColumn(1, ACTION_COL_ACT, wx.LIST_FORMAT_RIGHT)
        ioBoardList.InsertColumn(1, ACTION_COL_ACT, wx.LIST_FORMAT_RIGHT)
        ioBoardList.InsertColumn(2, ACTION_COL_FEEDBACK)
        ioBoardList.InsertColumn(3, ACTION_COL_FEEDBACK_TIMEOUT)

        #self.list.SetColumnWidth(0, wx.LIST_AUTOSIZE)

        ioBoardList.SetColumnWidth(0, wx.LIST_AUTOSIZE_USEHEADER)
        ioBoardList.SetColumnWidth(1, wx.LIST_AUTOSIZE_USEHEADER)
        ioBoardList.SetColumnWidth(2, wx.LIST_AUTOSIZE_USEHEADER)
        ioBoardList.SetColumnWidth(3, wx.LIST_AUTOSIZE_USEHEADER)


    def listInsertNewAction(self, index, action):
        actionList = self.canStationEditor.action_list

        """ ref SetStringItem """
        actionCount = actionList.GetItemCount()

        if index > actionCount+1:
            print "error"
            return

        if index == -1:
            if actionCount == 0:
                index = actionList.InsertStringItem(sys.maxint, str(actionCount+1),0)
            else:
                index = actionList.InsertStringItem(actionCount, str(actionCount+1),0)
        else:
            index = actionList.InsertStringItem(index, str(actionCount+1),0)

        actionList.SetStringItem(index, 1, action.getName(), 0)
        #actionList.SetStringItem(index, 2, action.moduleFeedback.name, 0)
        #actionList.SetStringItem(index, 3, action.feedbackTimeout, 0)
        #actionList.SetItemData(index, action)

    def listRemoveAction(self, action):
        actionList = self.canStationEditor.action_list

        item = actionList.GetFocusedItem()

        actionList.DeleteItem(item)

    def refreshIoBoardList(self, ctrlModule):
        ioBoardList = self.canStationEditor.ioBoard_list
        ioBoardList.DeleteAllItems()

        for action in ctrlModule.actions:
            self.listInsertNewAction(-1, action)

        return

    def dumpAction(self, action):
        print "dumpAction"
        print action.moduleOutput.name
        print action.moduleFeedback.name

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

        frame = wx.Frame(None, size=(350,400))
        Panel_EditIoBoard(frame, self.canStationEditor, targetObj=station)
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


class Panel_EditIOStation(MainBase.Panel_Edit_IO_Station_base):
    def __init__( self, frame , device=None):
        MainBase.Panel_Edit_IO_Station_base.__init__( self, frame )


        print "Panel_AddDevice  1111"

        if device is None:
            self.thisDevice = Device_Transport()
        else:
            self.thisDevice = device
        self.frame = frame

        self.canStationViewCtrl = CanStationViewControl(self)
        self.stationBoardViewCtrl = StationBoardViewControl(self)


        # self.deviceInfoPanelSetup()
        #
        #
        # self.moduleIoViewCtrl = ModuleIoListControl(self)
        # self.attrCtrl = AttributeViewControl(self)
        # self.actionListCtrl = ActionViewControl(self)
        # self.actGrpCtrl = ActionGroupViewControl(self)
        # self.onLoadUpdate()

    def deviceInfoPanelSetup(self):
        self.label_name.SetLabel(ADD_DEVICE_LABEL_NAME)
        self.label_pos.SetLabel(ADD_DEVICE_LABEL_POS)
        self.label_desc.SetLabel(ADD_DEVICE_LABEL_DESC)

    def setupDeviceInfo(self, device):
        self.text_name.SetValue(device.name)
        self.text_pos.SetValue(device.info)
        self.text_desc.SetValue(device.location)

    def onIoBoardToolClicked(self, event):
        self.stationBoardViewCtrl.onIoBoardToolClicked(event)

    def onLoadUpdate(self):
        self.setupDeviceInfo(self.thisDevice)
        self.moduleIoViewCtrl.onModuleIOListUpdate()
        self.actGrpCtrl.onActGrpUpdate()
        self.attrCtrl.onAttrListUpdate()
        return

    def onEditUpdate(self, targetObj=None):
        self.editDeviceUpdate()

    def editDeviceUpdate(self):
        self.getModuleIoViewControl().onModuleIOListUpdate()
        return


    """
    Attribute list control
    """
    def onAddAttribute(self, event):
        print "onAddAttribute"
        #self.attrCtrl.onAddNewAttribute()
        self.attrCtrl.popupAttrEditWnd()
        return

    def onEditAttribute(self, event):
        print "onEditAttribute"
        return

    def onDeleteAttribute(self, event):
        print "onDeleteAttribute"
        return

    """
    # main
    """
    def closeWindow(self):
        self.frame.Close()
    def onApply(self, event):
        print "my onApply"

        name = self.text_name.GetValue()
        info = self.text_pos.GetValue()
        location = self.text_desc.GetValue()
        actGrpList = self.actGrpCtrl.getActionGroupList()

        self.thisDevice.name = name
        self.thisDevice.info = info
        self.thisDevice.location = location

        self.thisDevice.setControls(actGrpList)
        #self.thisDevice.attrList = self.attrCtrl.attrObjList
        wx.GetApp().deviceController.addTransport(self.thisDevice)
        self.closeWindow()

        """ViewSelectPanel.onEditUpdate()"""
        wx.GetApp().viewPanel_sub.onEditUpdate()

    def onCancel(self, event):
        print "my onCancel"


    """
    Operation related
    """
    def getOperationViewTree(self):
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
    def onAddModuleIO(self, event):
        print "onAddModuleIO"
        #frame1 = wx.Frame(parent=self.parent, size=(800,400))
        frame1 = wx.Frame(parent=None, size=(800,400))
        Panel_EditModuleIO(frame1, self, self)
        frame1.CenterOnScreen()
        frame1.Show()

    def onDeleteModuleIO(self, event):
        print "onDeleteModuleIO"
        ioViewCtrl = self.getModuleIoViewControl()
        ioViewCtrl.deleteIoModule()
        ioViewCtrl.onModuleIOListUpdate()

    def getModuleIoViewList(self):
        return self.moudleIo_list
    def getModuleIoViewControl(self):
        return self.moduleIoViewCtrl


class Panel_EditIoBoard(MainBase.Panel_IoBoard_Base):
    #0: IO , 1:delay, 2:attr

    ACTION_TYPE_IO, ACTION_TYPE_DELAY, ACTION_TYPE_ATTR = range(3)
    def __init__(self, frame, canStationEditor, targetObj=None):
        MainBase.Panel_IoBoard_Base.__init__(self, frame)
        self.canStationEditor = canStationEditor
        self.targetObj = targetObj
        self.frame = frame
        #self.selectActionType(0)
        #self.buildOutputChoiceList()
        #self.buildFeedbackChoiceList()
        #self.buildAttrChoiceList()

#        print "Panel_EditAction.ACTION_TYPE_IO", Panel_EditAction.ACTION_TYPE_IO

    def selectActionType(self, type):
        self.actionType = type
        #0: IO , 1:delay, 2:attr

        self.mainSizer.Hide(self.SizerIO)
        self.mainSizer.Hide(self.sizeTimeDelay)
        self.mainSizer.Hide(self.SizerAttr)

        if type == Panel_EditAction.ACTION_TYPE_IO:
            self.mainSizer.Show(self.SizerIO)
        elif type == Panel_EditAction.ACTION_TYPE_DELAY:
            self.mainSizer.Show(self.sizeTimeDelay)
        elif type == Panel_EditAction.ACTION_TYPE_ATTR:
            self.mainSizer.Show(self.SizerAttr)

        self.mainSizer.Layout()

        # def editActionUpdate(self):
        #self.buildChoiceList()

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

        #wx.Choice(
        for item in itemList:
            print "\n",item.name, sys.getrefcount(item)
            choiceObj.Append(item.name, item)

            if item is prevItem:
                choiceObj.Select(index)
            index += 1
            print item.name, sys.getrefcount(item)

    def buildFeedbackChoiceList(self):
        io_modules = self.deviceEditor.getModuleIoViewControl().getIoModules()
        self.buildChoiceList(io_modules, self.choice_feedback)

    def buildOutputChoiceList(self):
        io_modules = self.deviceEditor.getModuleIoViewControl().getIoModules()
        self.buildChoiceList(io_modules, self.choice_output)

    def buildAttrChoiceList(self):
        attrList = self.deviceEditor.thisDevice.getAttrList()
        self.buildChoiceList(attrList, self.choice_attr)

    def createIoAction(self):
        newActionObj = DeviceActionIO()
        outObj = None
        feedbackObj = None

        sel = self.choice_output.GetSelection()
        if sel != wx.NOT_FOUND:
            outObj = self.choice_output.GetClientData(sel)

        outputValue = self.text_output.GetValue()

        sel = self.choice_feedback.GetSelection()
        if sel != wx.NOT_FOUND:
            feedbackObj = self.choice_feedback.GetClientData(sel)

        timeout = self.text_timeout.GetValue()
        newActionObj.moduleOutput = outObj
        newActionObj.outputValue = outputValue
        newActionObj.moduleFeedback = feedbackObj
        newActionObj.feedbackTimeout = timeout

        return newActionObj

    def createAttrSetAction(self):
        newActionObj = DeviceActionAttrSet()

        sel = self.choice_attr.GetSelection()
        if sel != wx.NOT_FOUND:
            attrObj = self.choice_attr.GetClientData(sel)
        else:
            attrObj = None

        newActionObj.attribute = attrObj
        newActionObj.valueToSet = int(self.text_valuSet.GetValue())

        return newActionObj

    def createDelayAction(self):
        newActionObj = DeviceActionDelay()


        return newActionObj

    def createNewAction(self, actionType):
        obj = None
        if actionType == Panel_EditAction.ACTION_TYPE_IO:
            obj = self.createIoAction()
        elif actionType == Panel_EditAction.ACTION_TYPE_DELAY:
            obj = self.createDelayAction()
        elif actionType == Panel_EditAction.ACTION_TYPE_ATTR:
            obj = self.createAttrSetAction()

        return obj

    def onEditUpdate(self, targetObj=None):
        print "Panel_NewAction -> onEditUpdate"
        self.buildOutputChoiceList()
        self.buildFeedbackChoiceList()

        print "targetObj.GetCount()", targetObj.GetCount()
        targetObj.SetSelection(targetObj.GetCount()-1)
        self.deviceEditor.onEditUpdate()

    def onChoice(self, event):
        type = event.GetInt()
        self.selectActionType(type)

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
        newAction = self.createNewAction(self.actionType)
        self.targetObj.addNewAction(newAction)
        self.deviceEditor.actionListCtrl.listInsertNewAction(-1, newAction)
        self.closeWindow()
        return

    def onCancel(self, evt):
        self.closeWindow()
        return