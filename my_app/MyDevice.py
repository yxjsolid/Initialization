# -*- coding: utf-8 -*-

import wx
from MyGlobal import *


class DeviceController():
    def __init__(self):
        self.transports = []
        print "init transportList"
        return

    def getDevices(self):
        return self.transports

    def addTransport(self, device):
        print "addTransport"
        self.transports.append(device)
        return

class Device_Transport():
    def __init__(self, nm="", info="", location=""):

        self.name = nm
        self.info = info
        self.location = location
        self.io_modules = []
        self.operations = []
        self.attrList = []
        return

    def dumpDevice(self):
        print "name: ",self.name
        print "desc: ",self.desc
        print "pos : ",self.pos	

    def addModule(self, io_module):
        self.io_modules.append(io_module)

    def getIoModules(self):
        return self.io_modules

    def setModules(self, io_modules):
        self.io_modules = io_modules

    def setControls(self, operations):
        self.operations = operations

    def getAttrList(self):
        return self.attrList

class DeviceModule():
    def __init__(self, nm="", io="", tp=None):
        self.name = nm
        self.io = io
        self.type = tp
        return

class DeviceOperation():
    def __init__(self, parent, name=OPERATION_NAME_DEFAULT, info=OPERATION_DESC_DEFAULT):
        self.parent = parent
        self.name = name
        self.info = info
        self.actions = []
    
    def addNewAction(self, action):
        self.actions.append(action)

    def setActions(self, actions):
        self.actions = actions

    def genOperationDisplayName(self):
        txt = self.parent.name + "\\" + self.name
        return txt

    def processOperation(self):
        txt = u"操作:"

        txt += " " + self.genOperationDisplayName()
        print "processOperation:", txt



        LogWriter.writeLog(txt)


        for act in self.actions:
            act.doAction()



class DeviceAttribute():
    def __init__(self):
        self.name = ""
        self.desc = ""
        self.value = 0
        self.parent = None #link to device
        return

    def genAttributeDisplayName(self):
        txt = self.parent.name + "\\" + self.name
        return txt

    def actionYell(self, value):
        txt = self.genAttributeDisplayName()
        txt += " set value to %d"%value
        print txt

    def setAttrValue(self, value):
        print "setAttrValue", value


        self.actionYell(value)
        self.value = value

class DeviceAction():
    def __init__(self):

        return

class DeviceActionIO(DeviceAction):
    def __init__(self):
        DeviceAction.__init__(self)
        self.moduleOutput = None
        self.outputValue = 0

        self.moduleFeedback = None
        self.feedbackTimeout = 0

        self.moduleDelay = None
        return

class DeviceActionAttrSet(DeviceAction):
    def __init__(self):
        DeviceAction.__init__(self)
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


class DeviceActionDelay(DeviceAction):
    def __init__(self):
        DeviceAction.__init__(self)
        self.moduleOutput = None
        self.outputValue = 0

        self.moduleFeedback = None
        self.feedbackTimeout = 0

        self.moduleDelay = None
        return


