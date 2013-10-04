#!/usr/bin/env python
# -*- coding: utf-8 -*-
import MainBase
from MyGlobal import *
from MiddleWare_Edit_IO import *
from MiddleWare_Action import *


class Panel_ButtonSetting(MainBase.Panel_ButtonSetting_Base):
    def __init__(self, frame, opener, callbackFn):
        MainBase.Panel_ButtonSetting_Base.__init__(self, frame)
        self.frame = frame
        self.opener = opener
        self.operationOn = None
        self.operationOff = None
        self.callbackFn = callbackFn
        self.setApplyBtnEnabled(0)
        self.onLoadUpdate()

    def setApplyBtnEnabled(self, enabled):
        self.applyBtn.Enable(enabled)

    def onLoadUpdate(self):
        self.operationOff = self.opener.operationOff
        self.operationOn = self.opener.operationOn
        self.refreshDisplay()

    def refreshDisplay(self):
        if self.operationOff:
            txt = self.operationOff.genOperationDisplayName()
            self.txt_oprOff.SetValue(txt)

        if self.operationOn:
            txt = self.operationOn.genOperationDisplayName()
            self.txt_oprOn.SetValue(txt)

        if self.operationOn and self.operationOff:
            self.setApplyBtnEnabled(1)

    def getOperationOnSelect(self, opItem):
        print "getOperationOnSelect"
        print opItem
        self.operationOn = opItem
        self.refreshDisplay()
        return

    def getOperationOffSelect(self, opItem):
        print "getOperationOffSelect"
        print opItem

        self.operationOff = opItem
        self.refreshDisplay()
        return

    def onSelectOperationOn(self, event):
        print "onSelectOperationOn"
        window = MyPopupWindow(size=(600, 400), title="setting")
        Panel_Action_Group_Select(window, self, self.getOperationOnSelect)
        window.windowPopup()

    def onSelectOperationOff(self, event):
        print "onSelectOperationOff"
        window = MyPopupWindow(size=(600, 400), title="setting")
        Panel_Action_Group_Select(window, self, self.getOperationOffSelect)
        window.windowPopup()

    def closeWindow(self):
        self.frame.Close()

    def onApply(self, event):
        #callback: onButtonSettingDone
        self.callbackFn(self.operationOn, self.operationOff)
        self.closeWindow()
        return

    def onCancel(self, event):
        print "onCancel"
        self.closeWindow()
        return


class Panel_AnimationCondition_Setting(MainBase.Panel_AnimationCondition_Setting_Base):
    def __init__(self, window, opener, callbackFn):
        MainBase.Panel_AnimationCondition_Setting_Base.__init__(self, window.frame)
        self.window = window
        self.opener = opener
        self.callbackFn = callbackFn
        self.setApplyBtnEnabled(0)
        self.conditionObj = None
        self.condition = None
        self.onLoadUpdate()

    def setApplyBtnEnabled(self, enabled):
        self.applyBtn.Enable(enabled)

    def onLoadUpdate(self):
        self.attribute = self.opener.attribute
        attrCondition = self.opener.attrCondition

        if self.attribute and not attrCondition:
            self.radioTrue.SetValue(False)
            self.radioFalse.SetValue(True)

        self.refreshDisplay()

    def refreshDisplay(self):
        if self.conditionObj:
            txt = self.conditionObj.getNodeNameWithCategory()
            self.txt_attribute.SetValue(txt)
            self.setApplyBtnEnabled(1)

    # def callbackGetAttributeSelect(self, attr):
    #     print "callbackGetAttributeSelect"
    #     print attr
    #     self.attribute = attr
    #     self.refreshDisplay()
    #     return

    def onSelectIoNodeUpdate(self, IoNode):
        print "Panel_AnimationCondition_Setting  onSelectIoNodeUpdate"
        self.conditionObj = IoNode
        self.refreshDisplay()
        return

    def onSelectConditionBind(self, event):
        window = MyPopupWindow(size=(600, 400), title=LABEL_CONDITION_SELECT)
        # Panel_AttributeSelect(window, self, self.callbackGetAttributeSelect)
        Panel_Manage_IO_Node(window, self, Panel_Manage_IO_Node.MODE_SELECT)
        window.windowPopup()

    def getCondition(self):
        #self.radioTrue.GetValue()
        #self.radioFalse.GetValue()
        return self.radioTrue.GetValue()

    def closeWindow(self):
        self.window.closeWindow()

    def onApply(self, event):
        self.callbackFn(self.attribute, self.getCondition())
        self.closeWindow()
        return

    def onCancel(self, event):
        self.closeWindow()
        return
