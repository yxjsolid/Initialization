# vim: et sw=4 ts=4 ai sm fo-=ro 


import wx
import wx.lib.agw.hypertreelist as HTL

import sys, os

#try:
#    dirName = os.path.dirname(os.path.abspath(__file__))
#except:
#    dirName = os.path.dirname(os.path.abspath(sys.argv[0]))

#sys.path.append(os.path.split(dirName)[0])

#from agw import hypertreelist as HTL
    
class MyFrame(wx.Frame):
    def __init__(self):
        wx.Frame.__init__(self, None, -1, 
                        "Main Menu", size=(1050,490))

        # set up tree structure
        #self.tree=wx.gizmos.TreeListCtrl(self, # style=wx.TR_HAS_BUTTONS|wx.TR_EDIT_LABELS)
        #        style=wx.TR_DEFAULT_STYLE|wx.TR_FULL_ROW_HIGHLIGHT|wx.TR_ROW_LINES|wx.TR_COLUMN_LINES)

        self.tree=HTL.HyperTreeList(self, style=wx.TR_HAS_BUTTONS|wx.TR_EDIT_LABELS|wx.TR_HAS_VARIABLE_ROW_HEIGHT)
#                style=wx.TR_DEFAULT_STYLE|wx.TR_FULL_ROW_HIGHLIGHT)


        self.tree.AddColumn("zero", width=200)
        self.tree.AddColumn("one", width=200)
        self.tree.AddColumn("two", width=100)
        self.tree.AddColumn("three", width=100)

        self.tree.SetColumnEditable(0, False)
        self.tree.SetColumnEditable(1, True)
        self.tree.SetColumnEditable(2, True)
        self.tree.SetColumnEditable(3, True)

        parent=self.tree.AddRoot("root")

        # note: ct_type=1 causes a checkbox to be attached to the cell in 
        # column 0.  It also messes up editing in columns 1,2,&3 :(
        item=self.tree.AppendItem(parent, "A", ct_type=1)
        self.tree.SetItemText(item, "A1" , 1)
        self.tree.SetItemText(item, "A2" , 2)
        self.tree.SetItemText(item, "A3" , 3)

        item=self.tree.AppendItem(parent, "B")
        self.tree.SetItemText(item, "B1" , 1)
        self.tree.SetItemText(item, "B2" , 2)
        self.tree.SetItemText(item, "B3" , 3)

        # Show how to add a window to an item
        sampleList = ['zero', 'one', 'two', 'three', 'four', 'five',
                      'six', 'seven', 'eight']

        choice = wx.Choice(self.tree.GetMainWindow(), -1, choices=sampleList)
        choice.Bind(wx.EVT_CHOICE, self.OnChoice)
        self.tree.SetItemWindow(item, choice, 1)
        
        self.tree.Bind(wx.EVT_TREE_END_LABEL_EDIT, self.OnEndLabelEdit)
        self.tree.Bind(HTL.EVT_TREE_ITEM_CHECKED, self.OnItemChecked)
        self.tree.ExpandAll()


    def OnEndLabelEdit(self, evt):
        print "OnEndLabelEdit"
        if evt.IsEditCancelled():
            print "Edit Cancelled"
            return
        textCtrl = self.tree.GetEditControl()
        column = textCtrl.column()
        label=evt.GetLabel()
        print "column, label=", column, label

        
    def OnItemChecked(self, evt):
        item = evt.GetItem()
        # the following is backwards: 0->checked, 1->not checked :(
        print "OnItemChecked, checkbox state=", item.IsChecked()


    def OnChoice(self, event):

        print "OnChoice", event.GetEventObject().GetStringSelection()
        

if __name__=='__main__':
    app = wx.PySimpleApp()
    frame=MyFrame()
    frame.Show()
    app.MainLoop()
