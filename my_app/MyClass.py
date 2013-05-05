import wx
from wx.lib.mixins.listctrl import CheckListCtrlMixin

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
        help(evt)
        print evt.getItem()


