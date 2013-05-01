import wx
from wx.lib.mixins.listctrl import CheckListCtrlMixin

class CheckListCtrl(wx.ListCtrl, CheckListCtrlMixin):
    def __init__(self, parent, id, pos, size, style):
        wx.ListCtrl.__init__(self, parent, -1, style=wx.LC_REPORT)
        CheckListCtrlMixin.__init__(self)
        self.Bind(wx.EVT_LIST_ITEM_ACTIVATED, self.OnItemActivated)


    def OnItemActivated(self, evt):
        self.ToggleItem(evt.m_itemIndex)


    # this is called by the base class when an item is checked/unchecked
    def OnCheckItem(self, index, flag):
        #data = self.GetItemData(index)
       
        if flag:
            what = "checked"
        else:
            what = "unchecked"

        print what

