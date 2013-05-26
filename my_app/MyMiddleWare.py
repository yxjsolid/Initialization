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

mydata = wxPythonInAction.Chapter_15.data.tree

def dumpModuleObj(module, pad=0):
    return
    if pad:
        print
    print "name", module.name, sys.getrefcount(module)
#---------------------------------------------------------------------------


class MyFrame( MainBase.FrameBase ):
    def __init__( self, parent ):
        MainBase.FrameBase.__init__( self, parent )
        self.parent = parent
        self.construceFrame()
        self.saveFileName = r".\save.txt"
            
    def construceFrame(self):
        self.panel = testMySplitterPanel(self)
        self.viewPanel_sub = self.panel.viewPanel_sub
        return

    def addDevice(self):
        print "add device"

        frame1 = wx.Frame(parent=self.parent, size=(800,400))
        Panel_AddDevice(frame1)
        frame1.CenterOnScreen()
        frame1.Show()
        return

    def editDevice(self):
        print "editDevice device"
        item = self.viewPanel_sub.tree.GetSelection()
        isDevice = 0

        if item.IsOk():
            print "ok"
            obj = self.viewPanel_sub.tree.GetItemPyData(item)
            if obj:
                isDevice = isinstance(obj, Device_Transport)
        else:
            print "not ok"

        if isDevice:
            print "isdevice"
        else:
            print "not device"

        frame1 = wx.Frame(parent=self.parent, size=(800,400))
        Panel_AddDevice(frame1, obj)
        frame1.CenterOnScreen()
        frame1.Show()
        return

    def onSave(self):
        print "onSave"
        saveFile = open(self.saveFileName, "w")

        deviceController = wx.GetApp().deviceController
        pickle.dump(deviceController, saveFile)
        saveFile.close()
        return

    def onLoad(self):
        print "onLoad"
        saveFile = open(self.saveFileName, "r")
        deviceController = pickle.load(saveFile)
        wx.GetApp().deviceController = deviceController
        for device in deviceController.transports:
            print device.name

        self.viewPanel_sub.onEditUpdate()

    def onMenuBtnClicked(self, event):
        eventId = event.GetId()
        ret = {
        MainBase.ID_MENU_SAVE:          lambda: self.onSave(),
        MainBase.ID_MENU_LOAD:          lambda: self.onLoad(),
        MainBase.ID_MENU_ADD_DEVICE:    lambda: self.addDevice(),
        MainBase.ID_MENU_EDIT_DEVICE:   lambda: self.editDevice(),
        MainBase.ID_MENU_DELETE_DEVICE: lambda: self.addDevice(),
        }[eventId]()
        return

class testMySplitterPanel( MainBase.SplitterPanelBase ):
    def __init__( self, parent ):
        MainBase.SplitterPanelBase.__init__( self, parent )
        self.parent = parent
        self.buildViewSelectPanel()
        self.viewPanel_sub = self.viewPanel_sub
        #self.ViewPanelSetDsp()
    
    def buildViewSelectPanel(self):
        container = self.viewSelectPanel
        sizer = wx.BoxSizer( wx.VERTICAL )
        
#        self.viewPanel_sub = wx.Panel( self.viewPanel, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
#        sizer.Add( self.viewPanel_sub, 1, wx.EXPAND |wx.ALL, 5 )
        
        self.viewPanel_sub = ViewSelectPanel(self, container, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
        sizer.Add( self.viewPanel_sub, 1, wx.EXPAND |wx.ALL, 5 )
        self.viewPanel_sub.SetBackgroundColour("sky blue")
        container.SetSizer( sizer )
        container.Layout()
        sizer.Fit(container)
        return
    
    def GetViewPanel(self):
        return self.viewPanel
"""















"""
class Panel_AddDevice(MainBase.Panel_AddDevice_Base):
    def __init__( self, frame , device=None):
        MainBase.Panel_AddDevice_Base.__init__( self, frame )

        if device is None:
            self.thisDevice = Device_Transport()
        else:
            self.thisDevice = device
        self.frame = frame
        self.deviceInfoPanelSetup()
        self.moduleListSetup()
        self.attrCtrl = AttributeViewControl(self)

        self.actionListCtrl = ActionViewControl(self)
        self.actGrpCtrl = ActionGroupViewControl(self)
        self.onLoadUpdate()
        
    def deviceInfoPanelSetup(self):
        self.label_name.SetLabel(ADD_DEVICE_LABEL_NAME)
        self.label_pos.SetLabel(ADD_DEVICE_LABEL_POS)
        self.label_desc.SetLabel(ADD_DEVICE_LABEL_DESC)

    def setupDeviceInfo(self, device):
        self.text_name.SetValue(device.name)
        self.text_pos.SetValue(device.info)
        self.text_desc.SetValue(device.location)

    def onActionToolClicked(self, event):
        self.actionListCtrl.onActionToolClicked(event)


#######################################################
# module list related
    def moduleListSetup(self):
        self.io_moudle_list.InsertColumn(0, "")
        self.io_moudle_list.InsertColumn(1, "Name", wx.LIST_FORMAT_RIGHT)
        self.io_moudle_list.InsertColumn(2, "type")
        self.io_moudle_list.InsertColumn(3, "IO")
        
        #self.list.SetColumnWidth(0, wx.LIST_AUTOSIZE)

        self.io_moudle_list.SetColumnWidth(0, wx.LIST_AUTOSIZE_USEHEADER)
        self.io_moudle_list.SetColumnWidth(1, wx.LIST_AUTOSIZE_USEHEADER)
        self.io_moudle_list.SetColumnWidth(2, wx.LIST_AUTOSIZE_USEHEADER)
        self.io_moudle_list.SetColumnWidth(3, wx.LIST_AUTOSIZE_USEHEADER)
        self.io_moudle_list.Bind( wx.EVT_LIST_ITEM_SELECTED, self.onModuleListItemSelected )

    def listInsertNewModule(self, module):
        count = self.io_moudle_list.GetItemCount() + 1
        index = self.io_moudle_list.InsertStringItem(sys.maxint, str(count), 0)
        self.io_moudle_list.SetStringItem(index, 1, module.name, 0)
        self.io_moudle_list.SetStringItem(index, 2, module.type[1], 0)
        self.io_moudle_list.SetStringItem(index, 3, module.io, 0)
        
        print "\n name,", module.name, sys.getrefcount(module)

        self.io_moudle_list.SetItemData(index, module)
        print " name,", module.name, sys.getrefcount(module)

    def addModule(self, module):
        self.thisDevice.addModule(module)

    def getModules(self):
        return self.thisDevice.getModules()

    def deleteModuel(self):
        modules = []
        self.io_moudle_list.checkList

        key = 0
        for item in self.thisDevice.modules:
            if key not in self.io_moudle_list.checkList:
                modules.append(item)
            key += 1
        self.thisDevice.modules = modules

    def onLoadUpdate(self):
        self.setupDeviceInfo(self.thisDevice)
        self.onModuleListUpdate()
        self.actGrpCtrl.onActGrpUpdate()
        return

    def onEditUpdate(self, targetObj=None):
        self.editDeviceUpdate()

    def onModuleListUpdate(self):
        self.io_moudle_list.DeleteAllItems()
        self.io_moudle_list.checkList = []
        
        index = 0
        for item in self.thisDevice.modules:
            self.listInsertNewModule(item) 
            index += 1
        self.io_moudle_list.SetColumnWidth(0, wx.LIST_AUTOSIZE)
        self.io_moudle_list.SetColumnWidth(1, wx.LIST_AUTOSIZE)
        self.io_moudle_list.SetColumnWidth(2, wx.LIST_AUTOSIZE)
        self.io_moudle_list.SetColumnWidth(3, wx.LIST_AUTOSIZE)
        return

    def editDeviceUpdate(self):
        self.onModuleListUpdate()
        return

    def onModuleListItemSelected(self, event):
            
        moduleObj = event.GetData()
        print sys.getrefcount(moduleObj)

        return

#------------------------------------------------------
# module list end
#######################################################
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
        self.thisDevice.attrList = self.attrCtrl.attrObjList
        wx.GetApp().deviceController.addTransport(self.thisDevice)
        self.closeWindow()
        
        """ViewSelectPanel.onEditUpdate()"""
        wx.GetApp().viewPanel_sub.onEditUpdate()

    def onCancel(self, event):
        print "my onCancel"



    def onActGrpToolClicked(self, event):
        self.actGrpCtrl.onActGrpToolClicked(event)

    def onActGrpItemSelChanged(self, event):
        self.actGrpCtrl.onActGrpItemSelChanged(event)

    def onActGrpItemBeginEdit(self, event):
        self.actGrpCtrl.onActGrpItemBeginEdit(event)

    def onActGrpItemEndEdit(self, event):
        self.actGrpCtrl.onActGrpItemEndEdit(event)

    def onActGrpItemDelete(self, event):
        self.actGrpCtrl.onActGrpItemDelete(event)


    def onAddModuleIO(self, event):
        print "onAddModuleIO"
        #frame1 = wx.Frame(parent=self.parent, size=(800,400))
        frame1 = wx.Frame(parent=None, size=(800,400))

        Panel_EditModuleIO(frame1, self, self)
        frame1.CenterOnScreen()
        frame1.Show()

    def onDeleteModuleIO(self, event):
        print "onDeleteModuleIO"
        self.deleteModuel()
        self.onModuleListUpdate()


class Panel_EditModuleIO(MainBase.Panel_EditModuleIO_Base):
    def __init__(self, frame, parent, deviceEditor, targetObj=None):
        MainBase.Panel_EditModuleIO_Base.__init__( self, frame )
        self.moduleTypeChoiceSetup(self.choice)
        self.deviceEditor = deviceEditor
        self.frame = frame
        self.parent = parent
        self.targetObj = targetObj

    def moduleTypeChoiceSetup(self, choice):
        items = MODULE_TYPE_LIST.items()
        for key, data in items:
            index = choice.GetCount()
            choice.Insert(data,index)
            choice.SetClientData(index, (key,data))
        choice.Select(0)

    def createNewModule(self):
        name =  self.text_name.GetValue()
        ioStr =  self.text_io.GetValue()
        type = self.getChoiceData()
        module = DeviceModule(nm=name, io=ioStr, tp=type)
        return module

    def getChoiceObj(self):
        return self.choice

    def getChoiceData(self):
        choice = self.getChoiceObj()
        index = choice.GetSelection()
        return choice.GetClientData(index)

    
    def onChoice(self, event):

        print "onChoice"

        print event.GetString()
        print event.GetClientData()

    def onApply(self, event):
        module = self.createNewModule()
        print "aa name", module.name, sys.getrefcount(module)
        dumpModuleObj(module, pad=1)
        self.deviceEditor.addModule(module)
        print "aa name", module.name, sys.getrefcount(module)
        dumpModuleObj(module)
        self.parent.onEditUpdate(targetObj=self.targetObj)
        dumpModuleObj(module)
        print "aa name", module.name, sys.getrefcount(module)
        self.closeWindow()

    def onCancel(self, event):
        print "onCancel"
        self.closeWindow()

    def closeWindow(self):
        self.frame.Close()


class ActionGroupViewControl():
    def __init__(self, parent):
        self.parent = parent
        self.ioModuleList = []
        self.setupActGrpTreeView()

    def setupActGrpTreeView(self):
        tree = self.parent.actionGroupTree

        tree.AddColumn(ADD_MOUDLE_LABEL_NAME)
        tree.AddColumn(ADD_MOUDLE_LABEL_DESC)

        tree.SetMainColumn(0) # the one with the tree in it...
        tree.SetColumnWidth(0, 150)

        tree.SetColumnEditable(0, True)
        tree.SetColumnEditable(1, True)
        tree.root = tree.AddRoot("Root Item")

    def addNewActGrp(self):
        tree = self.parent.actionGroupTree
        name = MOUDLE_NAME_DEFAULT + str(tree.GetCount()+1)
        ctrl = ActionGroup(name)
        self.appendActGrp(ctrl)

    def appendActGrp(self, ctrl):
        tree = self.parent.actionGroupTree
        child = tree.AppendItem(tree.root, ctrl.name)
        tree.SetItemText(child, ctrl.info,1)
        tree.SetItemPyData(child, ctrl)

    def onActGrpUpdate(self):
        for ctrl in self.parent.thisDevice.controls:
            self.appendActGrp(ctrl)

        return

    def getCurrentActGrp(self):
        tree = self.parent.actionGroupTree
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
        tree = self.parent.actionGroupTree
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

    def deleteActGrp(self):
        tree = self.parent.actionGroupTree
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

    def moveUpActGrp(self):
        tree = self.parent.actionGroupTree
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

    def moveDownActGrp(self):
        tree = self.parent.actionGroupTree
        item = tree.GetSelection()
        next = tree.GetNext(item)
        ctrl = tree.GetItemPyData(item)

        if next.IsOk():
            newItem = tree.InsertItem(tree.GetRootItem(), next, ctrl.name)
            tree.SetItemText(newItem, ctrl.info,1)
            tree.SetItemPyData(newItem, ctrl)

            tree.Delete(item)
            tree.SelectItem(newItem)

    def onActGrpToolClicked(self, event):
        eventId = event.GetId()
        print "onCtrlToolClicked:", eventId
        ret = {
            MainBase.ctrl_new:  lambda: self.addNewActGrp(),
            MainBase.ctrl_del:  lambda: self.deleteActGrp(),
            MainBase.ctrl_up:   lambda: self.moveUpActGrp(),
            MainBase.ctrl_down: lambda: self.moveDownActGrp(),
            }[eventId]()

    def onActGrpItemSelChanged(self, event):
        ActGrp = self.getCurrentActGrp()
        print "\n\n onCtrlSelChanged:"

        if ActGrp is None:
            self.parent.action_toolbar.EnableTool(MainBase.action_new, 0)
        else:
            self.parent.action_toolbar.EnableTool(MainBase.action_new, 1)
            self.parent.actionListCtrl.refreshActionList(ActGrp)

    def onActGrpItemBeginEdit(self, event):
        print "\n\n onActGrpItemBeginEdit"
        tree = self.parent.actionGroupTree
        tree.editColumn =  event.GetInt()

    def onActGrpItemEndEdit(self, event):
        tree = self.parent.actionGroupTree
        item = event.GetItem()
        ctrl = tree.GetItemPyData(item)
        newLable =  event.GetLabel()
        self.setActGrp(ctrl, tree.editColumn, newLable)
    def onActGrpItemDelete(self, event):
        print "onActGrpItemDelete"


    def onAddModule(self, event):
        print "onAddModuel"
        #frame1 = wx.Frame(parent=self.parent, size=(800,400))
        frame1 = wx.Frame(parent=None, size=(800,400))

        Panel_EditActGroup(frame1, self, self)
        frame1.CenterOnScreen()
        frame1.Show()
    #------------------------------------------------------------------

class ActionViewControl():
    def __init__(self, parent):
        self.parent = parent
        self.ioModuleList = []
        self.SetupActionList()

    ###################################################################
    # action list related

    def SetupActionList(self):
        actionList = self.parent.action_list

        actionList.InsertColumn(0, "")
        #actionList.InsertColumn(1, ACTION_COL_ACT, wx.LIST_FORMAT_RIGHT)
        actionList.InsertColumn(1, ACTION_COL_ACT, wx.LIST_FORMAT_RIGHT)
        actionList.InsertColumn(2, ACTION_COL_FEEDBACK)
        actionList.InsertColumn(3, ACTION_COL_FEEDBACK_TIMEOUT)

        #self.list.SetColumnWidth(0, wx.LIST_AUTOSIZE)

        actionList.SetColumnWidth(0, wx.LIST_AUTOSIZE_USEHEADER)
        actionList.SetColumnWidth(1, wx.LIST_AUTOSIZE_USEHEADER)
        actionList.SetColumnWidth(2, wx.LIST_AUTOSIZE_USEHEADER)
        actionList.SetColumnWidth(3, wx.LIST_AUTOSIZE_USEHEADER)


    def listInsertNewAction(self, index, action):
        actionList = self.parent.action_list

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

        actionList.SetStringItem(index, 1, action.moduleOutput.name, 0)
        actionList.SetStringItem(index, 2, action.moduleFeedback.name, 0)
        actionList.SetStringItem(index, 3, action.feedbackTimeout, 0)
        actionList.SetItemData(index, action)

    def listRemoveAction(self, action):
        actionList = self.parent.action_list

        item = actionList.GetFocusedItem()

        actionList.DeleteItem(item)

    def refreshActionList(self, ctrlModule):
        actionList = self.parent.action_list
        actionList.DeleteAllItems()

        for action in ctrlModule.actions:
            self.listInsertNewAction(-1, action)

        return

    def dumpAction(self, action):
        print "dumpAction"
        print action.moduleOutput.name
        print action.moduleFeedback.name

    def onEditActionUpdate(self):
        actionList = self.parent.action_list
        actGrp = self.parent.actGrpCtrl.getCurrentActGrp()
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
        ctrlModule = self.parent.actGrpCtrl.getCurrentActGrp()

        if ctrlModule is None:
            print "Error: --> addNewAction"

        frame = wx.Frame(None, size=(350,400))
        Panel_EditAction(frame, self.parent, targetObj=ctrlModule)
        frame.CenterOnScreen()
        frame.Show()

    def onDeleteAction(self):
        actionList = self.parent.action_list
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

    def onActionMoveUp(self):
        actionList = self.parent.action_list
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

    def onActionMoveDown(self):
        actionList = self.parent.action_list
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

    def onActionToolClicked(self, event):
        eventId = event.GetId()
        ret = {
            MainBase.action_new:  lambda: self.onAddNewAction(),
            MainBase.action_del:  lambda: self.onDeleteAction(),
            MainBase.action_up:   lambda: self.onActionMoveUp(),
            MainBase.action_down: lambda: self.onActionMoveDown(),
            }[eventId]()

        print ret

#----------------------------------------------------------------
# action list end

class Panel_EditAction(MainBase.Panel_EditAction_Base):
    def __init__(self, frame, deviceEditor, targetObj=None):
        MainBase.Panel_EditAction_Base.__init__(self, frame)
        self.deviceEditor = deviceEditor
        self.targetObj = targetObj
        self.frame = frame
        self.setActionType(0)       
        self.buildOutputChoiceList()
        self.buildFeedbackChoiceList()

    def setActionType(self, type):
        self.actionType = type
        #0: IO , 1:delay
        if type == 1:
            self.mainSizer.Hide(self.SizerIO)
            self.mainSizer.Show(self.sizeTimeDelay)

        else:
            self.mainSizer.Show(self.SizerIO)
            self.mainSizer.Hide(self.sizeTimeDelay)

        self.mainSizer.Layout()

   # def editActionUpdate(self):
        #self.buildChoiceList()

    def getPrevSelected(self, choiceObj):
        sel = choiceObj.GetSelection()
        if sel == wx.NOT_FOUND:
            return None

        return choiceObj.GetClientData(sel)
    
    def buildChoiceList(self, choiceObj):
        """select the previous selected item after update"""
        index = 0
        modules = self.deviceEditor.getModules()
        
        prevItem = self.getPrevSelected(choiceObj)
        choiceObj.Clear()
        
        for item in modules:
            print "\n",item.name, sys.getrefcount(item)
            choiceObj.Append(item.name, item)

            if item is prevItem:
                choiceObj.Select(index)
            index += 1
            print item.name, sys.getrefcount(item)


    def buildFeedbackChoiceList(self):
        self.buildChoiceList(self.choice_feedback)
    
    def buildOutputChoiceList(self):
        self.buildChoiceList(self.choice_output)
 
    def createNewAction(self):
        newActionObj = ModuleAction()
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

    def closeWindow(self):
        self.frame.Close()

    def onApply(self, evt):
        newAction = self.createNewAction()
        self.targetObj.addNewAction(newAction)
        self.deviceEditor.actionListCtrl.listInsertNewAction(-1, newAction)

        self.closeWindow()
        return

    def onCancel(self, evt):
        self.closeWindow()
        return


class AttributeViewControl():
    def __init__(self, parent):
        self.parent = parent
        self.attrObjList = []
        self.SetupAttributeList()
        self.addTestObj()

    def addTestObj(self):
        attrObj = DeviceAttribute()
        attrObj.name = "test"
        attrObj.desc = "name"

        self.listInsertNewAttribute(0, attrObj)
        self.listInsertNewAttribute(1, attrObj)

    def SetupAttributeList(self):
        attrList = self.parent.attribute_list
        attrList.InsertColumn(0, "")
        #actionList.InsertColumn(1, ACTION_COL_ACT, wx.LIST_FORMAT_RIGHT)
        attrList.InsertColumn(1, ATTR_COL_NAME)
        attrList.InsertColumn(2, ATTR_COL_DESC)
        attrList.InsertColumn(3, ATTR_COL_OTHER)

        attrList.SetColumnWidth(0, wx.LIST_AUTOSIZE_USEHEADER)
        attrList.SetColumnWidth(1, wx.LIST_AUTOSIZE_USEHEADER)
        attrList.SetColumnWidth(2, wx.LIST_AUTOSIZE_USEHEADER)
        attrList.SetColumnWidth(3, wx.LIST_AUTOSIZE_USEHEADER)

    def popupAttrEditWnd(self):

        # ctrlModule = self.getCurrentCtrlModule()
        # if ctrlModule is None:
        #     print "Error: --> addNewAction"

        frame = wx.Frame(None, size=(350,400))
        Panel_EditAttribute(frame, self, target=self)
        frame.CenterOnScreen()
        frame.Show()

    def addNewAttribute(self, attrObj):
        self.attrObjList.append(attrObj)
        self.listInsertNewAttribute(1, attrObj)
        return

    def listCtrlUpdate(self):
        self.refreshAttributeList()

    def refreshAttributeList(self):
        listCtrl = self.parent.attribute_list
        listCtrl.DeleteAllItems()

        for obj in self.attrObjList:
            self.listInsertNewAttribute(-1, obj)

        return


    def listInsertNewAttribute(self, index, attrObj):
        attrList = self.parent.attribute_list

        """ ref SetStringItem """
        actionCount = attrList.GetItemCount()

        if index > actionCount+1:
            print "error"
            return

        if index == -1:
            if actionCount == 0:
                index = attrList.InsertStringItem(sys.maxint, str(actionCount+1),0)
            else:
                index = attrList.InsertStringItem(actionCount, str(actionCount+1),0)
        else:
            index = attrList.InsertStringItem(index, str(actionCount+1),0)

        attrList.SetStringItem(index, 1, attrObj.name, 0)
        attrList.SetStringItem(index, 2, attrObj.desc, 0)
        attrList.SetStringItem(index, 3, "aaa", 0)
        attrList.SetItemData(index, None)

    #----------------------------------------------------------------
    # action list end

class Panel_EditAttribute(MainBase.Panel_EditAttribute_Base):
    def __init__(self, frame, deviceEditor, target=None):
        MainBase.Panel_EditAttribute_Base.__init__(self, frame)
        self.target = target
        self.frame = frame
        return

    def onApply(self, evt):
        newAttr = self.createNewAttribute()
        self.target.addNewAttribute(newAttr)
        self.target.listCtrlUpdate()
        self.closeWindow()
        return

    def onCancel():
        self.closeWindow()
        return

    def closeWindow(self):
        self.frame.Close()

    def createNewAttribute(self):
        attrObj = DeviceAttribute()

        name = self.text_name.GetValue()
        desc = self.text_desc.GetValue()

        attrObj.name = name
        attrObj.desc = desc
        return attrObj
