import wx
import images
from MyFrameBase import *
from MyPanelBase import *
from MyMyPanel2 import *
from MyEmptyPanel import *
from wxPythonInAction.Chapter_15 import *
import wxPythonInAction.Chapter_15.data
from MainBase import *

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

			frame1 = wx.Frame(parent=self.parent)
			
			Panel_AddDevice(frame1)
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

		





#---------------------------------------------------------------------------

