# -*- coding: utf-8 -*-

import wx


class DeviceAttribute():
    def __init__(self):
        self.name = ""
        self.desc = ""
        return


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
        self.modules = []
        self.controls = []

        return

    def dumpDevice(self):
        print "name: ",self.name
        print "desc: ",self.desc
        print "pos : ",self.pos	

    def addModule(self, module):
        self.modules.append(module)

    def getModules(self):
        return self.modules

    def setModules(self, moduels):
        self.modules = modules

    def setControls(self, controls):
        self.controls = controls

class DeviceModule():
	def __init__(self, nm="", io="", tp=None):
		self.name = nm
		self.io = io
		self.type = tp

		return

class ActionGroup():
    def __init__(self, nm=''):
        self.name = nm
        self.info = "δ����"
        self.actions = []
    
    def addNewAction(self, action):
        self.actions.append(action)

    def setActions(self, actions):
        self.actions = actions





class ModuleAction():
    def __init__(self):
        self.moduleOutput = None
        self.outputValue = 0

        self.moduleFeedback = None
        self.feedbackTimeout = 0

        self.moduleDelay = None
        return





	

class TransporterDevice():
    def __init__(self, parent, id, pos, size, style, log):
    
		self.identifiers = ['id','nm','ds','sv','pr','pl','op','fx','ts']
				
		self.data = [{'id':1,
					  'nm':"Ƥ���",
		              'ds':"ɶɶ",
		              'sv':"major",
		              'pr':1,
		              'pl':'MSW',
		              'op':1,
		              'fx':1,
		              'ts':1
		              }]
    
    
    
    
    
    
    
		return	

