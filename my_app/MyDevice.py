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



class DeviceModule():
	def __init__(self, nm="", io="", tp=None):
		self.name = nm
		self.io = io
		self.type = tp

		return

	

class TransporterDevice():
    def __init__(self, parent, id, pos, size, style, log):
    
		self.identifiers = ['id','nm','ds','sv','pr','pl','op','fx','ts']
				
		self.data = [{'id':1,
					  'nm':"Æ¤´ø»ú",
		              'ds':"É¶É¶",
		              'sv':"major",
		              'pr':1,
		              'pl':'MSW',
		              'op':1,
		              'fx':1,
		              'ts':1
		              }]
    
    
    
    
    
    
    
		return	

