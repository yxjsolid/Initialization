# -*- coding: utf-8 -*-

import wx


class DeviceController():
		def __init__(self):
			self.transports = []

			print "init transportList"
			return

		def addTransport(self, device):
			print "addTransport"
			self.transports.append(device)
			return

class Device_Transport():

    def __init__(self, nm="", desc="", pos=""):

        self.name = nm;
        self.desc = desc;
        self.pos = pos;
        self.modules = []

        return

    def dumpDevice(self):
        print "name: ",self.name
        print "desc: ",self.desc
        print "pos : ",self.pos	

    def addModule(self, module):
        self.modules.append(module)

    def getModules(self):
        return self.modules



class DeviceModule():
	def __init__(self, nm="", io="", tp=None):
		self.name = nm
		self.io = io
		self.type = tp

		return

class ModuelControl():
    def __init__(self, nm=''):
        self.name = nm
        self.info = "未定义"







class ModuleAction():
    def __init__(self):
        self.moudleOutput = None
        self.outputValue = 0

        self.moduleFeedback = None
        self.feedbackTimeout = 0

        self.moduleDelay = None
        return





	

class TransporterDevice():
    def __init__(self, parent, id, pos, size, style, log):
    
		self.identifiers = ['id','nm','ds','sv','pr','pl','op','fx','ts']
				
		self.data = [{'id':1,
					  'nm':"皮带机",
		              'ds':"啥啥",
		              'sv':"major",
		              'pr':1,
		              'pl':'MSW',
		              'op':1,
		              'fx':1,
		              'ts':1
		              }]
    
    
    
    
    
    
    
		return	

