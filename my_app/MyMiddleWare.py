import sys
import wx
import images
from MyFrameBase import *
from MyPanelBase import *
from MyMyPanel2 import *
from MyEmptyPanel import *
from wxPythonInAction.Chapter_15 import *
import wxPythonInAction.Chapter_15.data
from MainBase import *
from MyDevice import *
from ViewSelectPanel import *


mydata = wxPythonInAction.Chapter_15.data.tree

#mydata = data.tree




class MyFrame( MyFrameBase ):
		def __init__( self, parent ):
				MyFrameBase.__init__( self, parent )
				self.parent = parent
				self.construceFrame()
				
		def construceFrame(self):
			self.panel = testMySplitterPanel(self)
			return
		
		def addDevice(self, event):
			print "add device"
#			self.pane.
			wx.GetApp().GetAppViewSelectPane().AddDeviceNode("tool bar create")

			frame1 = wx.Frame(parent=self.parent, size=(800,400))
			
			Panel_AddDevice(frame1)
			frame1.CenterOnScreen()
			frame1.Show()


			return
				
class MySplitterPanel( MainBase.SplitterPanelBase ):
	def __init__( self, parent ):
		MainBase.SplitterPanelBase.__init__( self, parent )	
		self.parent = parent			
				
				
class MyPanel( MyPanelBase ):
	def __init__( self, parent ):
		MyPanelBase.__init__( self, parent )
		
		
		
class MyPanel2( MyMyPanel2 ):
	def __init__( self, parent ):
		MyMyPanel2.__init__( self, parent )

class testMySplitterPanel( MySplitterPanel ):
	def __init__( self, parent ):
		MySplitterPanel.__init__( self, parent )
		self.parent = parent
		
		self.buildViewSelectPanel()
		#self.ViewPanelSetDsp()

	
	def buildViewSelectPanel(self):
		
		container = self.viewSelectPanel
		
		sizer = wx.BoxSizer( wx.VERTICAL )
		
#		self.viewPanel_sub = wx.Panel( self.viewPanel, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
#		sizer.Add( self.viewPanel_sub, 1, wx.EXPAND |wx.ALL, 5 )
		
		self.viewPanel_sub = ViewSelectPanel(self, container, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		sizer.Add( self.viewPanel_sub, 1, wx.EXPAND |wx.ALL, 5 )
		self.viewPanel_sub.SetBackgroundColour("sky blue")
		container.SetSizer( sizer )
		container.Layout()
		sizer.Fit(container)
		return
	
	def GetViewPanel(self):
		return self.viewPanel
	

		
class Panel_AddDevice(Panel_AddDevice_Base):
	def __init__( self, parent ):
		Panel_AddDevice_Base.__init__( self, parent )
		self.thisDevice = Device_Transport()
		self.panelSetup()
		self.listSetup()
		
	def panelSetup(self):
		self.label_name.SetLabel(ADD_DEVICE_LABEL_NAME)
		self.label_pos.SetLabel(ADD_DEVICE_LABEL_POS)
		self.label_desc.SetLabel(ADD_DEVICE_LABEL_DESC)

	def listSetup(self):
		self.list.InsertColumn(0, "Artist")
		self.list.InsertColumn(1, "Title", wx.LIST_FORMAT_RIGHT)
		self.list.InsertColumn(2, "Genre")
		
		#self.list.CheckItem(4)
		#self.list.CheckItem(7)

		index = self.list.InsertStringItem(sys.maxint, "test1")
		self.list.SetStringItem(index, 1, "test2")
		self.list.SetStringItem(index, 2, "test3")
		#self.list.SetItemData(index, key)

		self.list.SetColumnWidth(0, wx.LIST_AUTOSIZE)
		self.list.SetColumnWidth(1, wx.LIST_AUTOSIZE)
		self.list.SetColumnWidth(2, 100)
	

	def showValue(self):
		print self.text_name.GetValue()

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
			
		Panel_AddModule(frame1, self.thisDevice)
		frame1.CenterOnScreen()
		frame1.Show()

	def onDeleteModule(self, event):
		print "onDeleteModule"




class Panel_AddModule(Panel_AddModule_Base):
	def __init__(self, parent, device):
		Panel_AddModule_Base.__init__( self, parent )
		self.moduleTypeChoiceSetup(self.choice)
		self.device = device
		self.parent = parent

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
		print "onApply"
		
		module = self.createNewModule()
		self.device.addModule(module)
		self.closeWindow()

	def onCancel(self, event):
		print "onCancel"
		self.closeWindow()

	def closeWindow(self):
		self.parent.Close()

#---------------------------------------------------------------------------

