import wx
from wx.lib.mixins.listctrl import CheckListCtrlMixin
from wx.lib.agw import ultimatelistctrl as ULC
from wx.lib.agw import customtreectrl as CTL

class UlcListCtrl(ULC.UltimateListCtrl):
    def __init__(self, parent, id, pos, size, style=0):
        ULC.UltimateListCtrl.__init__(self, parent, -1, agwStyle=wx.LC_REPORT
                                                    |wx.LC_SINGLE_SEL
                                                    |wx.LC_HRULES
                                                    |wx.LC_VRULES
                                                    |ULC.ULC_SHOW_TOOLTIPS)
        return

#
# class MyCustomTreeCtrl()
#
# customtreectrl( self.m_panel80, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TR_DEFAULT_STYLE|wx.TR_LINES_AT_ROOT )


class CheckListCtrl(wx.ListCtrl, CheckListCtrlMixin):
    def __init__(self, parent, id, pos, size, style):
        wx.ListCtrl.__init__(self, parent, -1, style=wx.LC_REPORT)
        CheckListCtrlMixin.__init__(self)
        self.Bind(wx.EVT_LIST_ITEM_ACTIVATED, self.OnItemActivated)
        self.Bind( wx.EVT_LIST_ITEM_SELECTED, self.onListItemSelected )
        self.checkList = []

    def OnItemActivated(self, evt):
        self.ToggleItem(evt.m_itemIndex)


    # this is called by the base class when an item is checked/unchecked
    def OnCheckItem(self, index, flag):
        #data = self.GetItemData(index)
        #key is the module index in module list
        key = self.GetItemData(index)

        print "\n\n oncheckitem flag = ", flag
        if flag:
            print "check"
            if key in self.checkList:
                print "Error: key alreay in list"
            self.checkList.append(key)
        else:
            print "uncheck"
            self.checkList.remove(key)

   

    def onListItemSelected(self, evt):
        #help(evt)
        print evt.getItem()


