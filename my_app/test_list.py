#!/usr/bin/env python
# -*- coding: utf-8 -*- 
#now not use
import sys
import wx
import wx.lib.mixins.listctrl as listmix 
class AbstractList(wx.ListCtrl,  
    listmix.ListCtrlAutoWidthMixin,  
    listmix.ColumnSorterMixin):  
    def __init__(self, parent,columes,editlabel=False):  
        """list �ؼ���װ �ṩ��ͷ�����ܣ�����ʹ��"""  
        wx.ListCtrl.__init__(self, parent, -1, wx.DefaultPosition, wx.DefaultSize, wx.LC_REPORT |
                                                                                   wx.SUNKEN_BORDER)  
        listmix.ListCtrlAutoWidthMixin.__init__(self)  
        listmix.ColumnSorterMixin.__init__(self, len(columes))  
        self.SetColumns(columes)  
        self.ImageList = FileImageList()  
        self.AssignImageList(self.ImageList, wx.IMAGE_LIST_SMALL)  
        if editlabel:  
            self.Bind(wx.EVT_LIST_BEGIN_LABEL_EDIT,self.EvtBeginEditLabel)  
            self.Bind(wx.EVT_LIST_END_LABEL_EDIT,self.EvtEndEditLabel)  
        self.pyData = ListPyData(self)  
        self.itemDataMap = {}  
        self.Bind(wx.EVT_RIGHT_DOWN, self.EvtContextMenu)  
  
    def EvtContextMenu(self,evt):  
        pMenu=self.InitPopuMenu()  
        assert pMenu  
        self.PopupMenu(pMenu)  
        pMenu.Destroy()  
  
    def InitPopuMenu(self):  
        """init poup menu"""  
  
    def EvtEndEditLabel(self,evt):  
        """end edit label"""  
  
    def EvtBeginEditLabel(self,evt):  
        """begein edit label"""  
        evt.Allow()  
  
    def SetColumns(self, columes):  
        """��ӱ�ͷ��Ϣ"""  
        i = 0  
        for name, width in columes:  
            self.InsertColumn(i, name)  
            if width: self.SetColumnWidth(i, width)  
            else: self.setResizeColumn(i)  
            i += 1  
  
    def GetListCtrl(self):  
        """�������ֻ��Ϊ�˱�ͷ����"""  
        return self  
  
    def GetPyData(self,idx):  
        return self.pyData.get(idx)  
  
    def RemovePyData(self,idx):  
        del self.pyData[idx]  
  
    def RawIconAndRow(self, item):  
        """��ʽ��������ӵ�ÿһ����ȥ"""  
        NotImplemented('RawIconAndRow')  
  
    def AddRow(self, item, idx=sys.maxint):  
        icon, row = self.RawIconAndRow(item)  
        idx = self.InsertImageStringItem(idx, row[0], icon)  
        cols_num=len(row)  
        for i in xrange(cols_num):  
            self.SetStringItem(idx, i, row[i])  
        self.pyData[idx] = item  
        self.itemDataMap[idx] = row  
        return idx  
  
########################################################################  
  
  
  
class AbstractControlList(AbstractList):  
    def __init__(self, parent,columes,editlabel=False):  
        AbstractList.__init__(self, parent,columes,editlabel)  
        self.Bind(wx.EVT_PAINT,self.PaintControl)  
        self.Bind(wx.EVT_LIST_COL_DRAGGING, self.PaintControl)  
        self.Bind(wx.EVT_LIST_COL_END_DRAG, self.PaintControl)  
        self.Bind(wx.EVT_SCROLL, self.PaintControl)  
  
    def GetControlColNum(self):  
        NotImplemented('GetControlColNum')  
  
    def GetControlItem(self,item,col):  
        NotImplemented('GetCellControl')  
  
    def RefreshColumText(self,rowidx):  
        """refreshText of the list"""  
  
  
    def PaintControl(self,evt):  
        count=self.GetItemCount()  
        control_cols=self.GetControlColNum()  
        for rowidx in xrange(count):  
            for col in control_cols:  
                item=self.pyData[rowidx]  
                control=self.GetControlItem(item,col)  
                rect=self.GetCellRect(rowidx,col)  
                control.SetDimensions(rect.x + 1, rect.y + 1, rect.width - 2, rect.height - 2)  
                control.Update()  
            self.RefreshColumText(rowidx)  
  
    def DeleteItem(self, idx):  
        control_cols=self.GetControlColNum()  
        pyData=self.GetPyData(idx)  
        assert pyData  
        for col in control_cols:  
            control=self.GetControlItem(pyData,col)  
            control.Hide()  
            control=None  
        self.RemovePyData(idx)  
        AbstractList.DeleteItem(self,idx)  
  
  
    def DeleteAllItems(self):  
        control_cols=self.GetControlColNum()  
        for pyData in self.pyData.values():  
            for col in control_cols:  
                control=self.GetControlItem(pyData,col)  
                control.Destory()  
        self.pyData.clear()  
        AbstractList.DeleteAllItems(self)  
  
  
    def RawIconAndRow(self, item):  
        """��ʽ��������ӵ�ÿһ����ȥ"""  
        NotImplemented('RawIconAndRow')  
  
    def AddRow(self, item, idx=sys.maxint):  
        icon, row = self.RawIconAndRow(item)  
        idx = self.InsertImageStringItem(idx, row[0], icon)  
        row_cout=len(row)  
        control_cols=self.GetControlColNum()  
        for i in xrange(row_cout):  
            if i in control_cols:  
                row[i]=''  
            else:  
                self.SetStringItem(idx, i, row[i])  
        self.pyData[idx] = item  
        self.itemDataMap[idx] = row  
        return idx  
  
    def _GetColumnWidthExtent(self, col):  
        col_locs,loc = [0],0  
        num_cols = min(col+1, self.GetColumnCount())  
        for n in xrange(num_cols):  
            loc += self.GetColumnWidth(n)  
            col_locs.append(loc)  
        x0 = col_locs[col]  
        x1 = col_locs[col+1] - 1  
        return x0, x1  
  
    def GetColumnRect(self, col):  
        x0, x1 = self._GetColumnWidthExtent(col)  
        r = self.GetItemRect(0)  
        y0 = r.y  
        y1 = self.GetClientSize()[1]  
        x_scroll = self.GetScrollPos(wx.HORIZONTAL)  
        return wx.RectPP(wx.Point(x0 - x_scroll, y0),wx.Point(x1 - x_scroll, y1))  
  
  
    def GetCellRect(self, row, col):  
        x0, x1 = self._GetColumnWidthExtent(col)  
        r = self.GetItemRect(row)  
        y0 = r.y  
        y1 = r.GetBottom()  
        x_scroll = self.GetScrollPos(wx.HORIZONTAL)  
        return wx.RectPP(wx.Point(x0 - x_scroll, y0),wx.Point(x1 - x_scroll, y1))  


