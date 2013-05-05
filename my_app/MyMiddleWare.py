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


mydata = wxPythonInAction.Chapter_15.data.tree

#mydata = data.tree




class MyFrame( MainBase.FrameBase ):
        def __init__( self, parent ):
                MainBase.FrameBase.__init__( self, parent )
                self.parent = parent
                self.construceFrame()
                
        def construceFrame(self):
            self.panel = testMySplitterPanel(self)
            return
        
        def addDevice(self, event):
            print "add device"
#            self.pane.
            wx.GetApp().GetAppViewSelectPane().AddDeviceNode("tool bar create")

            frame1 = wx.Frame(parent=self.parent, size=(800,400))
            
            Panel_AddDevice(frame1)
            frame1.CenterOnScreen()
            frame1.Show()


            return


     
class testMySplitterPanel( MainBase.SplitterPanelBase ):
    def __init__( self, parent ):
        MainBase.SplitterPanelBase.__init__( self, parent )
        self.parent = parent
        
        self.buildViewSelectPanel()
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
    

        
class Panel_AddDevice(MainBase.Panel_AddDevice_Base):
    def __init__( self, parent ):
        MainBase.Panel_AddDevice_Base.__init__( self, parent )
        self.thisDevice = Device_Transport()
        self.deviceInfoPanelSetup()
        self.moduleListSetup()
        self.setupCtrlModuleTree()
        self.SetupActionList()
        
    def deviceInfoPanelSetup(self):
        self.label_name.SetLabel(ADD_DEVICE_LABEL_NAME)
        self.label_pos.SetLabel(ADD_DEVICE_LABEL_POS)
        self.label_desc.SetLabel(ADD_DEVICE_LABEL_DESC)

    def moduleListSetup(self):
        self.list.InsertColumn(0, "")
        self.list.InsertColumn(1, "Name", wx.LIST_FORMAT_RIGHT)
        self.list.InsertColumn(2, "type")
        self.list.InsertColumn(3, "IO")
        

        #self.list.SetColumnWidth(0, wx.LIST_AUTOSIZE)


        self.list.SetColumnWidth(0, wx.LIST_AUTOSIZE_USEHEADER)
        self.list.SetColumnWidth(1, wx.LIST_AUTOSIZE_USEHEADER)
        self.list.SetColumnWidth(2, wx.LIST_AUTOSIZE_USEHEADER)
        self.list.SetColumnWidth(3, wx.LIST_AUTOSIZE_USEHEADER)

        

    def listInsertNewModule(self, module, key):
        count = self.list.GetItemCount() + 1
        index = self.list.InsertStringItem(sys.maxint, str(count))
        self.list.SetStringItem(index, 1, module.name)
        self.list.SetStringItem(index, 2, module.type[1])
        self.list.SetStringItem(index, 3, module.io)

        self.list.SetItemData(index, key)
    
####################################################################
# control module related  
    def setupCtrlModuleTree(self):
        tree = self.ctrl_tree

        tree.AddColumn("名称")
        tree.AddColumn("描述")
        
        tree.SetMainColumn(0) # the one with the tree in it...
        tree.SetColumnWidth(0, 150)

        tree.SetColumnEditable(0, True)
        tree.SetColumnEditable(1, True)  
        tree.root = tree.AddRoot("Root Item")

    def addNewCtrlModule(self):
        tree = self.ctrl_tree
        name = "未命名" + str(tree.GetCount()+1) 
        ctrl = ModuelControl(name)

        child = tree.AppendItem(tree.root, ctrl.name)
        tree.SetItemText(child, ctrl.info,1)        
        tree.SetItemPyData(child, ctrl)
    
    def getCurrentCtrlModule(self):
        tree = self.ctrl_tree
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
        

    def setCtrlModule(self, ctrl,index, txtIn):
        if index is 0:
            ctrl.name = txtIn
        elif index is 1:
            ctrl.info = txtIn
        
    def deleteCtrlModule(self):
        tree = self.ctrl_tree
        item = tree.GetSelection()
       
        #print "\n\n deleteCtrlModule"
        if item != tree.GetRootItem():
            prev = tree.GetPrev(item)
            next = tree.GetNext(item)
            tree.Delete(item)
            if prev.IsOk():
                tree.SelectItem(prev)
            elif next.IsOk():
                tree.SelectItem(next)

    def moveUpCtrlModule(self):
        tree = self.ctrl_tree
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

    def moveDownCtrlModule(self):
        tree = self.ctrl_tree
        item = tree.GetSelection()
        next = tree.GetNext(item)
        ctrl = tree.GetItemPyData(item)

        if next.IsOk():
            newItem = tree.InsertItem(tree.GetRootItem(), next, ctrl.name)
            tree.SetItemText(newItem, ctrl.info,1)
            tree.SetItemPyData(newItem, ctrl)

            tree.Delete(item)
            tree.SelectItem(newItem)   
  
    def onCtrlToolClicked(self, event):
        eventId = event.GetId()
        #print "onCtrlToolClicked:", eventId

        ret = {
            MainBase.ctrl_new:  lambda: self.addNewCtrlModule(),
            MainBase.ctrl_del:  lambda: self.deleteCtrlModule(),
            MainBase.ctrl_up:   lambda: self.moveUpCtrlModule(),
            MainBase.ctrl_down: lambda: self.moveDownCtrlModule(),
        }[eventId]()

    def onCtrlSelChanged(self, event):

        ctrlModule = self.getCurrentCtrlModule()
        print "\n\n onCtrlSelChanged:"

        if ctrlModule:
            self.action_toolbar.EnableTool(MainBase.action_new, 1)
        else:
            self.action_toolbar.EnableTool(MainBase.action_new, 0)
            

    def onCtrlItemBeginEdit(self, event):
        print "\n\n onCtrlItemBeginEdit"
        self.ctrl_tree.editColumn =  event.GetInt()
        
  
    def onCtrlItemEndEdit(self, event):
        tree = self.ctrl_tree
        item = event.GetItem()
        ctrl = tree.GetItemPyData(item)
        newLable =  event.GetLabel()
        self.setCtrlModule(ctrl, tree.editColumn, newLable)
    def onCtrlItemDelete(self, event):
        print "onCtrlItemDelete"


###################################################################
# action list related


    def SetupActionList(self):
        actionList = self.action_list

        actionList.InsertColumn(0, "")
        #actionList.InsertColumn(1, "动作", wx.LIST_FORMAT_RIGHT)
        actionList.InsertColumn(1, "动作", wx.LIST_FORMAT_RIGHT)
        actionList.InsertColumn(2, "反馈")
        actionList.InsertColumn(3, "反馈超时")
        

        #self.list.SetColumnWidth(0, wx.LIST_AUTOSIZE)


        actionList.SetColumnWidth(0, wx.LIST_AUTOSIZE_USEHEADER)
        actionList.SetColumnWidth(1, wx.LIST_AUTOSIZE_USEHEADER)
        actionList.SetColumnWidth(2, wx.LIST_AUTOSIZE_USEHEADER)
        actionList.SetColumnWidth(3, wx.LIST_AUTOSIZE_USEHEADER)




    def addNewAction(self):
        ctrlModule = self.getCurrentCtrlModule()

        if ctrlModule == None:
            print "Error: --> addNewAction"

        frame = wx.Frame(None, size=(350,400))
        Panel_NewAction(frame, self, targetObj=ctrlModule)
        frame.CenterOnScreen()
        frame.Show()


    def func1(self,id):
        print "a: ", id
        return id


    def onActionToolClicked(self, event):
        eventId = event.GetId()
        
        print "onActionToolClicked ", eventId

        ret = {
            MainBase.action_new: lambda: self.addNewAction(),
            MainBase.action_del: lambda: self.func1(eventId),
            MainBase.action_up: lambda: self.func1(eventId),
            MainBase.action_down: lambda: self.func1(eventId),
        }[eventId]()


        print ret





 #######################################################

    def showValue(self):
        print self.text_name.GetValue()
        
    def addModule(self, module):
        self.thisDevice.addModule(module)

    def getModules(self):
        return self.thisDevice.getModules()

    def deleteModuel(self):
        modules = []
        self.list.checkList

        key = 0
        for item in self.thisDevice.modules:
            if key not in self.list.checkList:
                modules.append(item)
            key += 1
        self.thisDevice.modules = modules


    def onEditUpdate(self, targetObj=None):
        self.editDeviceUpdate()

    def editDeviceUpdate(self):
        self.list.DeleteAllItems()
        self.list.checkList = []
        
        index = 0
        for item in self.thisDevice.modules:
            self.listInsertNewModule(item,index) 
            index += 1
        self.list.SetColumnWidth(0, wx.LIST_AUTOSIZE)
        self.list.SetColumnWidth(1, wx.LIST_AUTOSIZE)
        self.list.SetColumnWidth(2, wx.LIST_AUTOSIZE)
        self.list.SetColumnWidth(3, wx.LIST_AUTOSIZE)
        return

    def onApply(self, event):
        print "my onApply"

        name = self.text_name.GetValue()
        position = self.text_pos.GetValue()
        description = self.text_desc.GetValue()

        device = Device_Transport(nm=name, pos=position,desc=description)
        wx.GetApp().deviceController.addTransport(device)

        self.showValue()
        

    def onCancel(self, event):
        print "my onCancel"


    def onAddModule(self, event):
        print "onAddModuel"
        #frame1 = wx.Frame(parent=self.parent, size=(800,400))
        frame1 = wx.Frame(parent=None, size=(800,400))
            
        Panel_AddModule(frame1, self, self)
        frame1.CenterOnScreen()
        frame1.Show()

    def onDeleteModule(self, event):
        print "onDeleteModule"
        self.deleteModuel()
        self.editDeviceUpdate()
        

        #print event.GetClientData()




class Panel_AddModule(MainBase.Panel_AddModule_Base):
    def __init__(self, frame, parent, deviceEditor, targetObj=None):
        MainBase.Panel_AddModule_Base.__init__( self, frame )
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
        self.deviceEditor.addModule(module)
        self.parent.onEditUpdate(targetObj=self.targetObj)
        self.closeWindow()

    def onCancel(self, event):
        print "onCancel"
        self.closeWindow()

    def closeWindow(self):
        self.frame.Close()

#---------------------------------------------------------------------------

class Panel_NewAction(MainBase.Panel_NewAction_Base):
    def __init__(self, parent, deviceEditor, targetObj=None):
        MainBase.Panel_NewAction_Base.__init__(self, parent)
        self.deviceEditor = deviceEditor
        self.targetObj = targetObj

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

        outputValue = sel.text_output.GetValue()
       
        sel = self.choice_feedback.GetSelection() 
        if sel != wx.NOT_FOUND:
            feedbackObj = self.choice_feedback.GetClientData(sel)

        timeout = sel.text_timeout.GetValue()

        newActionObj.moudleOutput = outObj
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
    
    def onAddModule(self, event):
        print "onAddModuel"


        if self.addOutputBtn is event.GetEventObject():
            targetChoice = self.choice_output
        else:
            targetChoice = self.choice_feedback


        #frame1 = wx.Frame(parent=self.parent, size=(800,400))
        frame1 = wx.Frame(parent=None, size=(800,400))
            
        Panel_AddModule(frame1, self, self.deviceEditor, targetObj=targetChoice)
        frame1.CenterOnScreen()
        frame1.Show()

    def onApply(self, evt):
        self.createNewAction()

        return
    def onCancel():
        
        return


