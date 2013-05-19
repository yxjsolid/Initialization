#!/usr/bin/env python
# -*- coding: gb2312 -*-

import sys
import  wx
import  wx.lib.mixins.listctrl  as  listmix
#----------------------------------------------------------------------------

class TestListCtrl(wx.ListCtrl, listmix.ListCtrlAutoWidthMixin):
    def __init__(self, parent, ID, pos=wx.DefaultPosition,
                 size=wx.Size(800, 600), style=wx.LC_REPORT):
        wx.ListCtrl.__init__(self, parent, ID, pos, size, style=wx.LC_REPORT)
        listmix.ListCtrlAutoWidthMixin.__init__(self)
       
class NodeListCtrl(wx.Panel, listmix.ColumnSorterMixin):
    def __init__(self, parent):
        wx.Panel.__init__(self, parent, -1,size=wx.Size(800, 600), pos=wx.Point(16, 16), style=wx.LC_REPORT|wx.WANTS_CHARS)
        tID = wx.NewId()
        self.list = TestListCtrl(self, tID,
                                 style=wx.LC_REPORT
                                 #| wx.BORDER_SUNKEN
                                 | wx.BORDER_NONE
                                 | wx.LC_SORT_ASCENDING
                                 #| wx.LC_NO_HEADER
                                 #| wx.LC_VRULES
                                 #| wx.LC_HRULES
                                 #| wx.LC_SINGLE_SEL
                                 )
       
        self.InitPopulateList()

        # Now that the list exists we can init the other base class,
        # see wx/lib/mixins/listctrl.py
        #print musicdata
        listmix.ColumnSorterMixin.__init__(self, 11)
        #self.SortListItems(10, True)
    def InitPopulateList(self):#添加表头信息
        colnum = [ "仪器编号","网络","节点",  "信号强度", "电压(V)", "温度(℃)","通信"," 数据","   数据采集时间"]
            # for normal, simple columns, you can add them like this:
        for i in range(9):
            self.list.InsertColumn(i, colnum[i])
        col_width = [65,    45,     45,     70,       60,  65,   45,   50,  130]
                #序号, 网络号,节点号, 信号强度,   电压,温度, 通信, 数据, 时间

        #print sum(col_width)
        for i in range(9):
            self.list.SetColumnWidth(i, col_width[i])
    def PopulateList(self,dict):   #eg:  dict={1:"1","3","","",....},# 创建数据映射
        self.itemDataMap = dict
        items = dict.items()
        for key, data in items:
            index = self.list.InsertStringItem(sys.maxint, str(data[0]))
            #print "key=%s,index=%s"%(key,index)
            for i in range(9):
                self.list.SetStringItem(index, i, str(data[i]))
                self.list.SetItemData(index, key)
        self.SortListItems(9, True)   #这个表示默认以第九列为排序依据
       
    def AddOneRow(self,data):#改变一行信息
        if data[0] not in Dict.keys():
            return
        index = self.list.FindItem(-1, str(data[0])) #这个地方注意,要先找出该节点在列表中所在的位置,才能更新
        #print 'index = ' ,index
        for i in range(9):
            self.list.SetStringItem( index,col=i, label=str(data[i]))
        self.list.SetItemData(index, data[0])
        return
       
    def SetBackgroundGreen(self,index):
        item = self.list.GetItem(index)
        item.SetBackgroundColour(wx.GREEN)
        self.list.SetItem(item)
        event.Skip()   
    def SetTextRED(self,index):
        item = self.list.GetItem(index)
        item.SetTextColour(wx.RED)
        self.list.SetItem(item)
        event.Skip()
    def GetListCtrl(self):

#扩展自ColumnSorterMixin 的类（这里是DemoFrame）必须有一个名为
#GetListCtrl()的方法，它返回实际要被排序的列表控件。该方法被这个mixin
#用来得到控件的一个索引。
        #print self.list
        return self.list

