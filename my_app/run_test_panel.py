#!/usr/bin/env python
# -*- coding: utf-8 -*- 
import wx
import sys
import MyGlobal as gl
from  MyMiddleWare import *




import  wx.gizmos   as  gizmos

#----------------------------------------------------------------------

class TestPanel(wx.Panel):
    def __init__(self, parent):
        wx.Panel.__init__(self, parent, -1)
        self.Bind(wx.EVT_SIZE, self.OnSize)

        self.tree = gizmos.TreeListCtrl(self, -1, style =
                                        wx.TR_DEFAULT_STYLE
                                        #| wx.TR_HAS_BUTTONS
                                        #| wx.TR_TWIST_BUTTONS
                                        #| wx.TR_ROW_LINES
                                        #| wx.TR_COLUMN_LINES
                                        #| wx.TR_NO_LINES 
                                        | wx.TR_FULL_ROW_HIGHLIGHT
                                        #| wx.TR_EDIT_LABELS
                                        #| wx.LC_EDIT_LABELS
                                   )

     
        # create some columns
        self.tree.AddColumn("Main column")
        self.tree.AddColumn("Column 1")
        self.tree.AddColumn("Column 2")
        self.tree.SetMainColumn(0) # the one with the tree in it...
        self.tree.SetColumnWidth(0, 175)


        self.tree.SetColumnEditable(0, True)
        self.tree.SetColumnEditable(1, True)
        self.tree.SetColumnEditable(2, True)
       # self.tree.SetColumnEditable(3, True)
        
        self.root = self.tree.AddRoot("The Root Item")
        self.tree.SetItemText(self.root, "col 1 root", 1)
        self.tree.SetItemText(self.root, "col 2 root", 2)
       

        for x in range(15):
            txt = "Item %d" % x
            child = self.tree.AppendItem(self.root, txt)
            self.tree.SetItemText(child, txt + "(c1)", 1)
            self.tree.SetItemText(child, txt + "(c2)", 2)
    
    def OnSize(self, evt):
        self.tree.SetSize(self.GetSize())


class testPanel1 ( wx.Panel ):
	
	def __init__( self, parent ):
		wx.Panel.__init__ ( self, parent, id = wx.ID_ANY, pos = wx.DefaultPosition, size = wx.Size( 500,300 ), style = wx.TAB_TRAVERSAL )
		
		bSizer17 = wx.BoxSizer( wx.VERTICAL )
		
		self.m_listbook4 = wx.Treebook( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LB_DEFAULT )
		self.m_panel53 = wx.Panel( self.m_listbook4, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		self.m_listbook4.AddPage( self.m_panel53, "a pageaaaaaaaaaaaaa", False )
		self.m_panel54 = wx.Panel( self.m_listbook4, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		self.m_listbook4.AddPage( self.m_panel54, "a page", False )
		
		bSizer17.Add( self.m_listbook4, 1, wx.EXPAND |wx.ALL, 5 )
		
		
		self.SetSizer( bSizer17 )
		self.Layout()
	
	def __del__( self ):
		pass

class mytestPanel(MainBase.testPanel):
    def __init__(self, parent):
        MainBase.testPanel.__init__(self,parent)


    def onChoice(self, event):

  #      help(event)
        num = event.GetInt()
        print "getint:", num
        print "GetSelection:", event.GetSelection()
    
       
        if num == 1:
            self.mainSizer.Hide(self.SizerIO)
            self.mainSizer.Show(self.sizeTimeDelay)

        else:
            self.mainSizer.Show(self.SizerIO)
            self.mainSizer.Hide(self.sizeTimeDelay)

        self.mainSizer.Layout()



class MyApp(wx.App):

    def __init__(self, redirect=True, filename=None):
        print "App __init__"
        wx.App.__init__(self, redirect, filename)
		
    def OnInit(self):
        print "OnInit"
        self.frame = wx.Frame(parent=None)
        self.frame.Show()
        self.SetTopWindow(self.frame)
        panel = mytestPanel(self.frame)
        #panel = TestPanel(self.frame)

        #help(panel.m_listbook2.GetListView())

        #help( panel.m_listbook2.ListView)

        #listView = panel.m_listbook2.GetListView()
    

    
        print    sys.stderr, "A pretend error message"
        return True

    def OnExit(self):
        print "OnExit"
    
    def SetAppViewSelectPanel(self, panel):
        self.ViewSelectPanel = panel
        return
    
    def GetAppViewSelectPane(self):
        return self.ViewSelectPanel
    

        

if __name__ == '__main__':
    app = MyApp(redirect=False)
    print "before MainLoop"
    app.MainLoop()
    
    gl.app = app
    print "after MainLoop"
