#!/usr/bin/env python
# -*- coding: utf-8 -*-

from MyGlobal import *


class ActionGroup():
    def __init__(self, name=ACTION_GRP_DEFAULT_NAME, info=ACTION_GRP_DEFAULT_DESC):
        self.name = name
        self.info = info
        self.actions = []

    def addNewAction(self, action):
        self.actions.append(action)

    def removeAction(self, action):
        self.actions.remove(action)

    def replaceAction(self, index, newAction):
        self.actions.remove(self.actions[index])
        self.actions.insert(index, newAction)
        return

    def setActions(self, actions):
        self.actions = actions

    def genOperationDisplayName(self):
        txt = self.parent.name + "\\" + self.name
        return txt

    def processOperation(self):
        txt = u"操作:"

        txt += " " + self.genOperationDisplayName()
        print "processOperation:", txt
        # LogWriter.writeLog(txt)
        #
        #
        # for act in self.actions:
        #     act.doAction()


class ActionBase():
    ACTION_TYPE_OUTPUT, ACTION_TYPE_SET_INTERNAL, ACTION_TYPE_DELAY = range(3)
    ACTION_TYPE = [ACTION_TYPE_OUTPUT, ACTION_TYPE_SET_INTERNAL, ACTION_TYPE_DELAY]
    ACTION_TYPE_STR = [ACTION_TYPE_OUTPUT_NAME, ACTION_TYPE_SET_INTERNAL_NAME, ACTION_TYPE_DELAY_NAME]

    def __init__(self):
        self.type = None

        return

    def getActionTypeStr(self):
        return ActionBase.ACTION_TYPE_STR[self.type]




class ActionOutput(ActionBase):
    def __init__(self):
        ActionBase.__init__(self)
        self.type = ActionBase.ACTION_TYPE_OUTPUT
        self.outputObj = None
        self.outputValue = 0

        self.needFeedback = 0
        self.feedbackObj = None
        self.feedbackTimeout = 0

        return

    def getActionDetail(self):
        actionDetailFormat = ACTION_DETAIL_STR_FORMAT
        nameStr = self.outputObj.getNodeNameWithCategory()

        return  actionDetailFormat % (nameStr, str(self.outputValue))


class ActionInternalSet(ActionBase):
    def __init__(self):
        ActionBase.__init__(self)
        self.type = ActionBase.ACTION_TYPE_SET_INTERNAL
        self.attribute = None
        self.valueToSet = 0
        return

    def getName(self):
        if self.attribute:
            return self.attribute.name
        else:
            return "N/A"

    def doAction(self):
        if self.attribute:
            self.attribute.setAttrValue(self.valueToSet)

    def getActionDetail(self):
        return

class ActionTimeDelay(ActionBase):
    def __init__(self):
        ActionBase.__init__(self)
        self.type = ActionBase.ACTION_TYPE_DELAY
        self.delayTime = 0
        return

    def getActionDetail(self):

        return u"等待: [%d]秒" % (self.delayTime)