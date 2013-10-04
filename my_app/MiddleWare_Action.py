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
from MyAction import *
import pickle
from MyGlobal import *
from MiddleWare_Edit_IO import *

class ActionGroupViewControl():
    def __init__(self, parentEditor):
        self.parentEditor = parentEditor
        self.actionGrpCfgList = None
        self.viewCtrl = self.parentEditor.getActionGroupViewTree()
        self.setupActionGroupTreeView()
        self.updateToolStatus(0)
        self.getActionGroupCfg()

    def updateToolStatus(self, isEnable):
        if isEnable:
            self.parentEditor.actionGrp_toolbar.EnableTool(MainBase.actionGrp_edit, 1)
            self.parentEditor.actionGrp_toolbar.EnableTool(MainBase.actionGrp_del, 1)
        else:
            self.parentEditor.actionGrp_toolbar.EnableTool(MainBase.actionGrp_edit, 0)
            self.parentEditor.actionGrp_toolbar.EnableTool(MainBase.actionGrp_del, 0)

    def setupActionGroupTreeView(self):
        viewCtrl = self.viewCtrl

        #viewCtrl.SetSingleStyle(wx.LC_EDIT_LABELS, True)
        viewCtrl.InsertColumn(0, "#", wx.LIST_FORMAT_LEFT)
        viewCtrl.InsertColumn(1, LABEL_ACTION_GROUP_NAME)
        viewCtrl.InsertColumn(2, LABEL_ACTION_GROUP_DESC)

        viewCtrl.SetColumnWidth(0, wx.LIST_AUTOSIZE)
        viewCtrl.SetColumnWidth(1, 100)
        viewCtrl.SetColumnWidth(2, 100)

    def clearAllItem(self):
        tree = self.viewCtrl
        tree.DeleteAllItems()

    def appendActionGroupList(self, actionGrp):
        self.actionGrpCfgList.append(actionGrp)

    def setDefaultSelect(self):
        tree = self.viewCtrl
        listCnt = tree.GetItemCount()

        if listCnt > 0:
            tree.Select(0)

    def appendActionGroupListView(self, actionGrp):
        tree = self.viewCtrl
        listCnt = tree.GetItemCount()

        if listCnt == 0:
            index = tree.InsertStringItem(sys.maxint, str(listCnt + 1))
        else:
            index = tree.InsertStringItem(listCnt, str(listCnt + 1))

        tree.SetStringItem(index, 1, actionGrp.name)
        tree.SetStringItem(index, 2, actionGrp.info)
        tree.SetItemPyData(index, actionGrp)

        tree.Select(index)

    def updateActionGrpItem(self, itemIndex, actionGrp):
        tree = self.viewCtrl

        tree.SetStringItem(itemIndex, 0, str(itemIndex + 1))
        tree.SetStringItem(itemIndex, 1, actionGrp.name)
        tree.SetStringItem(itemIndex, 2, actionGrp.info)

    def addNewActionGroup(self):
        window = MyPopupWindow(size=(400, 200), title=WINDOW_TITLE_ADD_ACTION_GROUP)
        Panel_Edit_Action_Group(window, self)
        window.windowPopup()

    def editActionGroup(self):
        window = MyPopupWindow(size=(400, 200), title=WINDOW_TITLE_EDIT_ACTION_GROUP)
        Panel_Edit_Action_Group(window, self, self.viewCtrl.GetFirstSelected())
        window.windowPopup()

    def deleteActionGroup(self):
        itemIndex = self.viewCtrl.GetFirstSelected()

        actGroup = self.getCurrentEditObj()

        dlg = MainBase.ConfirmDIALOG(self.parentEditor.window.frame)
        dlg.SetTitle(WINDOW_TITLE_DEL_ACTION_GROUP)
        dlg.alert_msg_txt.SetLabel(DIALOG_ALERT_DEL_ACTION_GROUP)

        if dlg.ShowModal() == wx.ID_OK:
            if actGroup:
                self.actionGrpCfgList.remove(actGroup)
        dlg.Destroy()

        self.onActionGroupDelUpdate(itemIndex)

    def getActionGroupCfg(self):
        self.actionGrpCfgList = globalGetCfg().getActionGroupCfgList()

    def onActionGroupDelUpdate(self, delIndex):
        self.updateToolStatus(0)

        self.onActionGroupUpdate(False)
        listCnt = self.viewCtrl.GetItemCount()

        if listCnt > 0:
            if delIndex > 0:
                self.viewCtrl.Select(delIndex - 1)
            else:
                self.viewCtrl.Select(0)
        else:
            self.parentEditor.actionViewCtrl.updateActionView(None, True)

    def onActionGroupUpdate(self, isOnLoad):
        actGrpList = self.actionGrpCfgList
        self.clearAllItem()
        for actGrp in actGrpList:
            if actGrp:
                self.appendActionGroupListView(actGrp)

        if isOnLoad:
            self.setDefaultSelect()
        return

    def getCurrentEditObj(self):
        tree = self.viewCtrl
        item = tree.GetFirstSelected()
        if item != -1:
            return tree.GetItemPyData(item)
        return None

    def getActionGroupList(self):
        actionGrpList = []
        listCnt = self.viewCtrl.GetItemCount()

        for index in range(listCnt):
            actGrp = self.viewCtrl.GetItemPyData(index)
            actionGrpList.append(actGrp)

        return actionGrpList

    def onActionGrpToolClicked(self, event):
        eventId = event.GetId()
        ret = {
            MainBase.actionGrp_new: lambda: self.addNewActionGroup(),
            MainBase.actionGrp_edit: lambda: self.editActionGroup(),
            MainBase.actionGrp_del: lambda: self.deleteActionGroup(),
            # MainBase.canStation_up:   lambda: self.moveUpCanStation(),
            # MainBase.canStation_down: lambda: self.moveDownCanStation(),
        }[eventId]()

    #def onCanStationItemSelChanged(self, event):
    def onActionGrpItemSelected(self, event):
        actGrp = self.getCurrentEditObj()
        print "onActionGrpItemSelected"
        self.updateToolStatus(1)

        self.parentEditor.actionViewCtrl.updateActionView(actGrp, True)


class ActionViewControl():
    def __init__(self, parentEditor):
        self.parentEditor = parentEditor
        self.viewCtrl = self.parentEditor.getActionViewCtrl()
        self.SetupActionList()
        self.updateAddNewToolStatus(0)
        self.updateToolStatus(0)
        return

    def updateAddNewToolStatus(self, isEnable):
        if isEnable:
            self.parentEditor.action_toolbar.EnableTool(MainBase.action_new, 1)
        else:
            self.parentEditor.action_toolbar.EnableTool(MainBase.action_new, 0)
            self.updateToolStatus(0)

    def updateToolStatus(self, isEnable):
        if isEnable:
            self.parentEditor.action_toolbar.EnableTool(MainBase.action_edit, 1)
            self.parentEditor.action_toolbar.EnableTool(MainBase.action_del, 1)
        else:
            self.parentEditor.action_toolbar.EnableTool(MainBase.action_edit, 0)
            self.parentEditor.action_toolbar.EnableTool(MainBase.action_del, 0)

    def SetupActionList(self):
        actionList = self.parentEditor.action_list
        actionList.InsertColumn(0, "#", wx.LIST_FORMAT_LEFT)
        actionList.InsertColumn(1, LABEl_ACTION_TYPE)
        actionList.InsertColumn(2, LABEl_ACTION_DESC)
        actionList.SetColumnWidth(0, 20)
        actionList.SetColumnWidth(1, 100)
        actionList.SetColumnWidth(2, 200)
        #ioBoardList.SetColumnWidth(2, 100)

    def onEditUpdateAction(self, index, actObj):

        self.setActItemView(index, actObj)
        #actionList.Select(index)

        return


    def listInsertAction(self, index, actOgj):
        actionList = self.parentEditor.action_list
        actionCnt = actionList.GetItemCount()

        if index > actionCnt + 1:
            print "error"
            return

        if index == -1:
            if actionCnt == 0:
                index = actionList.InsertStringItem(sys.maxint, str(actionCnt + 1), 0)
            else:
                index = actionList.InsertStringItem(actionCnt, str(actionCnt + 1), 0)
        else:
            index = actionList.InsertStringItem(index, str(index + 1), 0)

        self.setActItemView(index, actOgj)
        actionList.Select(index)

    def getCurrentEditObj(self):
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

    def setActItemView(self, index, actOgj):
        actionList = self.parentEditor.action_list

        actionList.SetStringItem(index, 0, str(index + 1), 0)
        actionList.SetStringItem(index, 1, actOgj.getActionTypeStr(), 0)
        actionList.SetStringItem(index, 2, actOgj.getActionDetail(), 0)
        actionList.SetItemPyData(index, actOgj)

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

    def updateActionList(self, actGrp, isOnLoad):
        self.viewCtrl.DeleteAllItems()

        if actGrp is None:
            return

        for actObj in actGrp.actions:
            self.listInsertAction(-1, actObj)

        if isOnLoad:
            self.setDefaultSelect()

        return

    def onEditActionUpdate(self):
        actionList = self.parentEditor.action_list
        actGrp = self.parentEditor.actGrpCtrl.getCurrentActGrp()
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

    def onAddNewAction(self):
        actGrp = self.getCurrentActionGroup()

        if actGrp is None:
            print "Error: --> onAddNewIoBoard"

        window = MyPopupWindow(size=(600, 400), title=WINDOW_TITLE_ADD_ACTION)
        Panel_EditAction(window, self, targetActGrp=actGrp)
        window.windowPopup()

    def onEditAction(self):
        actGrp = self.getCurrentActionGroup()
        if actGrp is None:
            print "Error: --> onEditAction"

        #actionObj = self.getCurrentEditObj()

        window = MyPopupWindow(size=(600, 400), title=WINDOW_TITLE_EDIT_ACTION)
        Panel_EditAction(window, self, targetActGrp=actGrp, editListItemIn=self.viewCtrl.GetFirstSelected())
        window.windowPopup()

    def onDelAction(self):
        tree = self.viewCtrl
        itemIndex = tree.GetFirstSelected()
        actObj = self.getCurrentEditObj()

        #dlg = MainBase.ConfirmDIALOG(self.canStationEditor.frame)
        dlg = MainBase.ConfirmDIALOG(None)

        dlg.SetTitle(WINDOW_TITLE_DEL_ACTION)
        dlg.alert_msg_txt.SetLabel(DIALOG_ALERT_DEL_ACTION)

        if dlg.ShowModal() == wx.ID_OK:
            if actObj:
                self.getCurrentActionGroup().removeAction(actObj)
                self.onActionDelUpdate(itemIndex)
        dlg.Destroy()



    def getCurrentActionGroup(self):
        return self.parentEditor.actionGrpViewCtrl.getCurrentEditObj()

    def onActionDelUpdate(self, delIndex):
        actGrp = self.getCurrentActionGroup()
        self.updateActionList(actGrp, False)

        tree = self.viewCtrl
        listCnt = tree.GetItemCount()

        if listCnt > 0:
            if delIndex > 0:
                tree.Select(delIndex - 1)
            else:
                tree.Select(0)
                # else:
                #     self.canStationEditor.ioBoardViewCtrl.updateIoBoardView(None)

    def onActionToolClicked(self, event):
        eventId = event.GetId()
        ret = {
            MainBase.action_new: lambda: self.onAddNewAction(),
            MainBase.action_del: lambda: self.onDelAction(),
            MainBase.action_edit: lambda: self.onEditAction(),
            # MainBase.ioBoard_up:   lambda: self.onIoBoardMoveUp(),
            # MainBase.ioBoard_down: lambda: self.onIoBoardMoveDown(),
        }[eventId]()

    def updateActionView(self, actGrp, isOnLoad):
        self.parentEditor.actionViewCtrl.updateAddNewToolStatus(0)

        if actGrp is not None:
            self.parentEditor.actionViewCtrl.updateAddNewToolStatus(1)

        self.updateActionList(actGrp, isOnLoad)

    def onActionItemSelected(self, event):
        board = self.getCurrentEditObj()
        if board is not None:
            self.updateToolStatus(1)
        else:
            self.updateToolStatus(0)

        return


class Panel_Manage_Action(MainBase.Panel_Manage_Action_Base):
    def __init__(self, window):
        MainBase.Panel_Manage_Action_Base.__init__(self, window.frame)
        self.window = window
        self.actionGrpViewCtrl = ActionGroupViewControl(self)
        self.actionViewCtrl = ActionViewControl(self)
        self.onLoadUpdate()

    def onActionToolClicked(self, event):
        self.actionViewCtrl.onActionToolClicked(event)

    def onLoadUpdate(self):
        self.actionGrpViewCtrl.onActionGroupUpdate(True)
        #self.canStationViewCtrl.setDefaultSelection()
        return

    def closeWindow(self):
        self.window.closeWindow()

    def onApply(self, event):
        canStationList = self.actionGrpViewCtrl.getActionGroupList()
        globalGetCfg().setActionGroupCfg(canStationList)
        self.closeWindow()

    def onCancel(self, event):
        print "my onCancel"

    def getActionViewCtrl(self):
        return self.action_list

    def getActionGroupViewTree(self):
        return self.actionGrpList

    def onActionGrpToolClicked(self, event):
        self.actionGrpViewCtrl.onActionGrpToolClicked(event)

    def onActionGrpItemSelected(self, event):
        self.actionGrpViewCtrl.onActionGrpItemSelected(event)

    def onActionItemSelected(self, event):
        self.actionViewCtrl.onActionItemSelected(event)
        ######################################################
        ######################################################


class Panel_Edit_Action_Group(MainBase.Panel_Edit_Action_Group_Base):
    def __init__(self, window, viewCtrl, editListItemIn=-1):
        MainBase.Panel_Edit_Action_Group_Base.__init__(self, window.frame)
        self.viewCtrl = viewCtrl
        self.editListItem = editListItemIn
        self.onEditObj = None
        self.window = window
        if editListItemIn != -1:
            self.onEditObj = viewCtrl.getCurrentEditObj()

        self.onLoadUpdate()

        return

    def onLoadUpdate(self):

        if self.onEditObj is not None:
            actionName = self.onEditObj.name
            actionDesc = self.onEditObj.info
        else:
            actionName = ACTION_GRP_DEFAULT_NAME
            actionDesc = ACTION_GRP_DEFAULT_DESC

        self.actGrpName_txt.SetValue(actionName)
        self.actDesc_txt.SetValue(actionDesc)

        return

    def onApply(self, evt):
        actionName = self.actGrpName_txt.GetValue()
        actionDesc = self.actDesc_txt.GetValue()

        if self.onEditObj is None:
            actionGrp = ActionGroup()
            actionGrp.name = actionName
            actionGrp.info = actionDesc
            self.viewCtrl.appendActionGroupList(actionGrp)
            self.viewCtrl.appendActionGroupListView(actionGrp)
        else:
            actionGrp = self.onEditObj
            actionGrp.name = actionName
            actionGrp.info = actionDesc
            self.viewCtrl.updateActionGrpItem(self.editListItem, actionGrp)

        #self.canStationViewCtrl.onCanStationUpdate()
        self.window.closeWindow()
        return

    def onCancel(self, evt):
        self.window.closeWindow()
        return


class Panel_EditAction(MainBase.Panel_EditAction_Base):
    def __init__(self, window, viewCtrlIn, targetActGrp=None, editListItemIn=-1):
        MainBase.Panel_EditAction_Base.__init__(self, window.frame)
        self.window = window
        self.viewCtrl = viewCtrlIn
        self.onEditActGrp = targetActGrp
        self.onEditObj = None

        self.outputObj = None
        self.feedbackObj = None
        self.internalObj = None
        self.onSelectCfg = None

        self.editListItem = editListItemIn
        if editListItemIn != -1:
            self.onEditObj = self.viewCtrl.getCurrentEditObj()

        self.buildActionChoice()
        self.selectActionType(ActionBase.ACTION_TYPE_OUTPUT)

        self.onLoadUpdate()

    def updateActionOutPutView(self, actObj):
        self.outputObj = actObj.outputObj
        self.feedbackObj = actObj.feedbackObj

        self.output_txt.SetValue(actObj.outputObj.getNodeNameWithCategory())
        self.outVal_txt.SetValue(str(actObj.outputValue))

        if actObj.needFeedback:
            self.needFeedback_cb.SetValue(1)
            self.feedback_txt.SetValue(actObj.feedbackObj.getNodeNameWithCategory())
            self.feedbackTimeout_txt.SetValue(str(actObj.feedbackTimeout))

        return

    def updateActionDelayView(self, actObj):
        self.delayTime_txt.SetValue(str(actObj.delayTime))
        return

    def updateActionSetInternalView(self, actObj):

        return

    def onLoadUpdate(self):
        if self.onEditObj:
            actObj = self.onEditObj
            actionType = actObj.type
            self.selectActionType(actionType)

            if actionType == ActionBase.ACTION_TYPE_OUTPUT:
                self.updateActionOutPutView(actObj)
            elif actionType == ActionBase.ACTION_TYPE_DELAY:
                self.updateActionDelayView(actObj)
            elif actionType == ActionBase.ACTION_TYPE_SET_INTERNAL:
                self.updateActionSetInternalView(actObj)
        return

    def buildActionChoice(self):
        self.actionType_choice.Clear()

        for actType in ActionBase.ACTION_TYPE:
            self.actionType_choice.Insert(ActionBase.ACTION_TYPE_STR[actType], actType)

        self.actionType_choice.Select(ActionBase.ACTION_TYPE_OUTPUT)

    def selectActionType(self, actionType):
        self.actionType = actionType
        self.actionType_choice.Select(actionType)

        #0: IO , 1:delay, 2:attr

        self.mainSizer.Hide(self.SizerIO)
        self.mainSizer.Hide(self.sizeTimeDelay)
        self.mainSizer.Hide(self.SizerAttr)

        if actionType == ActionBase.ACTION_TYPE_OUTPUT:
            self.mainSizer.Show(self.SizerIO)
        elif actionType == ActionBase.ACTION_TYPE_DELAY:
            self.mainSizer.Show(self.sizeTimeDelay)
        elif actionType == ActionBase.ACTION_TYPE_SET_INTERNAL:
            self.mainSizer.Show(self.SizerAttr)

        self.mainSizer.Layout()

        # def editActionUpdate(self):
        #self.buildChoiceList()
    def getPrevSelected(self, choiceObj):
        sel = choiceObj.GetSelection()
        if sel == wx.NOT_FOUND:
            return None

        return choiceObj.GetClientData(sel)

    def createOutputAction(self):
        actObj = ActionOutput()
        outputValue = self.outVal_txt.GetValue()
        actObj.outputObj = self.outputObj
        actObj.outputValue = int(outputValue)

        if self.needFeedback_cb.IsChecked():
            feedbackTimeout = self.feedbackTimeout_txt.GetValue()

            actObj.needFeedback = 1
            actObj.feedbackObj = self.feedbackObj
            actObj.feedbackTimeout = int(feedbackTimeout)

        return actObj

    def createSetInternalAction(self):
        actObj = ActionInternalSet()
        outputValue = self.outVal_txt.GetValue()

        sel = self.choice_attr.GetSelection()
        if sel != wx.NOT_FOUND:
            attrObj = self.choice_attr.GetClientData(sel)
        else:
            attrObj = None

        newActionObj.attribute = attrObj
        newActionObj.valueToSet = int(self.text_valuSet.GetValue())

        return newActionObj

    def createTimeDelayAction(self):
        newActionObj = ActionTimeDelay()
        delay = self.delayTime_txt.GetValue()
        newActionObj.delayTime = int(delay)

        return newActionObj

    def createNewAction(self, actionType):
        obj = None
        if actionType == ActionBase.ACTION_TYPE_OUTPUT:
            obj = self.createOutputAction()
        elif actionType == ActionBase.ACTION_TYPE_DELAY:
            obj = self.createTimeDelayAction()
        elif actionType == ActionBase.ACTION_TYPE_SET_INTERNAL:
            obj = self.createSetInternalAction()

        return obj

    def onEditUpdate(self, targetObj=None):
        print "Panel_NewAction -> onEditUpdate"
        self.buildOutputChoiceList()
        self.buildFeedbackChoiceList()

        print "targetObj.GetCount()", targetObj.GetCount()
        targetObj.SetSelection(targetObj.GetCount() - 1)
        self.deviceEditor.onEditUpdate()

    def onChoice(self, event):
        print "onChoice"
        type = event.GetInt()
        self.selectActionType(type)

    def updateView(self):
        if self.outputObj:
            infoStr = self.outputObj.getNodeNameWithCategory()
            self.output_txt.SetValue(infoStr)

        if self.feedbackObj:
            infoStr = self.feedbackObj.getNodeNameWithCategory()
            self.feedback_txt.SetValue(infoStr)

        if self.internalObj:
            infoStr = self.internalObj.getNodeNameWithCategory()
            self.internalVal_txt.SetValue(infoStr)

    def onSelectIoNodeUpdate(self, nodeObj):
        onCfg = self.onSelectCfg
        if onCfg == 1:
            self.outputObj = nodeObj
        elif onCfg == 2:
            self.feedbackObj = nodeObj
        elif onCfg == 3:
            self.internalObj = nodeObj

        self.updateView()
        return

    def onSelectOutput(self, event):
        self.onSelectCfg = 1
        self.openIoNodeSelWindow()
        return

    def onSelectInput(self, event):
        self.onSelectCfg = 2
        self.openIoNodeSelWindow()
        return

    def onSelectInternal(self, event):
        self.onSelectCfg = 3
        self.openIoNodeSelWindow()
        return

    def openIoNodeSelWindow(self):
        window = MyPopupWindow(parent=self, size=(600, 400), title=WINDOW_TITLE_SELECT_IO_NODE)
        panel = Panel_Manage_IO_Node(window, self, Panel_Manage_IO_Node.MODE_SELECT)
        panel.disableToolBar()
        window.windowPopup()

    def refreshDisplay(self):
        if self.attribute:
            txt = self.attribute.genAttributeDisplayName()
            self.txt_attribute.SetValue(txt)
            self.setApplyBtnEnabled(1)

    def closeWindow(self):
        self.window.closeWindow()

    def onApply(self, evt):

        if self.editListItem == -1:
            newAction = self.createNewAction(self.actionType)
            self.onEditActGrp.addNewAction(newAction)
            self.viewCtrl.listInsertAction(-1, newAction)
        else:
            newAction = self.createNewAction(self.actionType)
            self.onEditActGrp.replaceAction(self.editListItem, newAction)
            self.viewCtrl.onEditUpdateAction(self.editListItem, newAction)

            # tests = []
            # tests.append()
            # tests.


        self.closeWindow()
        return

    def onCancel(self, evt):
        self.closeWindow()
        return


class Panel_Action_Group_Select(MainBase.Panel_Action_Group_Select_Base):
    def __init__(self, window, opener, callbackFn):
        MainBase.Panel_Action_Group_Select_Base.__init__(self, window.frame)
        self.opener = opener
        self.callbackFn = callbackFn
        self.actionGrpCfgList = None
        self.window = window
        self.getActionGroupCfg()
        self.setupActionGroupTreeView()
        self.onActionGroupUpdate(True)

        return


    def setupActionGroupTreeView(self):
        viewCtrl = self.actionGrpListView

        #viewCtrl.SetSingleStyle(wx.LC_EDIT_LABELS, True)
        viewCtrl.InsertColumn(0, "#", wx.LIST_FORMAT_LEFT)
        viewCtrl.InsertColumn(1, LABEL_ACTION_GROUP_NAME)
        viewCtrl.InsertColumn(2, LABEL_ACTION_GROUP_DESC)

        viewCtrl.SetColumnWidth(0, wx.LIST_AUTOSIZE)
        viewCtrl.SetColumnWidth(1, 100)
        viewCtrl.SetColumnWidth(2, 100)


    def getActionGroupCfg(self):
        self.actionGrpCfgList = globalGetCfg().getActionGroupCfgList()

    def onActionGroupUpdate(self, isOnLoad):
        actGrpList = self.actionGrpCfgList
        # self.clearAllItem()
        for actGrp in actGrpList:
            if actGrp:
                self.appendActionGroupListView(actGrp)

        if isOnLoad:
            self.setDefaultSelect()
        return

    def appendActionGroupListView(self, actionGrp):
        tree = self.actionGrpListView
        listCnt = tree.GetItemCount()

        if listCnt == 0:
            index = tree.InsertStringItem(sys.maxint, str(listCnt + 1))
        else:
            index = tree.InsertStringItem(listCnt, str(listCnt + 1))

        tree.SetStringItem(index, 1, actionGrp.name)
        tree.SetStringItem(index, 2, actionGrp.info)
        tree.SetItemPyData(index, actionGrp)

        tree.Select(index)

    def setDefaultSelect(self):
        tree = self.actionGrpListView
        listCnt = tree.GetItemCount()

        if listCnt > 0:
            tree.Select(0)

    def getCurrentSelectedObj(self):
        tree = self.actionGrpListView
        item = tree.GetFirstSelected()
        if item != -1:
            return tree.GetItemPyData(item)
        return None

    def onApply(self, event):
        opItem = self.getCurrentSelectedObj()
        if opItem is None:
            raise "Panel_OperationSelect error onApply"

        self.callbackFn(opItem)
        self.window.closeWindow()
        return