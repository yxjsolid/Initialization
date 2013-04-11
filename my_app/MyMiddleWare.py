from MyFrameBase import *
from MyPanelBase import *



class MyFrame( MyFrameBase ):
		def __init__( self, parent ):
				MyFrameBase.__init__( self, parent )
				self.panel = MyPanel(self)
				
				
class MyPanel( MyPanelBase ):
	def __init__( self, parent ):
		MyPanelBase.__init__( self, parent )