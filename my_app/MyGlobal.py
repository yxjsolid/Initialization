﻿# -*- coding: utf-8 -*-
from MyTestApp import *


teststr = "测试"

VIEW_OPTION_NAME_MAIN = u"总览"
VIEW_OPTION_NAME_DEVICE = u"设备"
DEVICE_NAME_TRANSPORT = u"皮带机"


ADD_DEVICE_LABEL_NAME = u"名称："
ADD_DEVICE_LABEL_POS = u"位置："
ADD_DEVICE_LABEL_DESC = u"描述："


OPERATION_LIST_LABEL_NAME = u"名称："
OPERATION_LIST_LABEL_POS = u"位置："
OPERATION_LIST_LABEL_DESC = u"描述："
OPERATION_NAME_DEFAULT = u"未命名"
OPERATION_DESC_DEFAULT = u"未定义"


ACTION_COL_ACT = u"动作"
ACTION_COL_FEEDBACK = u"反馈"
ACTION_COL_FEEDBACK_TIMEOUT = u"反馈超时"


ATTR_COL_NAME = u"名称"
ATTR_COL_DESC = u"描述"
ATTR_COL_OTHER = u"其他"



MODULE_TYPE_SIG_IN = 1
MODULE_TYPE_VAL_IN = 2
MODULE_TYPE_SIG_OUT = 3

MODULE_TYPE_LIST = {
MODULE_TYPE_SIG_IN : u"信号量输入",
MODULE_TYPE_VAL_IN : u"数值量输入",
MODULE_TYPE_SIG_OUT : u"信号量输出",
}

MENU_ITEM_BUTTON_SETTING = u"动作绑定"



rescoure_dir = r".\image\\"

btn_red_up = rescoure_dir + r"red_up.png"
btn_red_down = rescoure_dir + "red_down.png"

btn_green_up = rescoure_dir + "green_up.png"
btn_green_down = rescoure_dir + "green_down.png"

btn_on = rescoure_dir + "btn_on.png"
btn_off = rescoure_dir + "btn_off.png"

circle_btn_on = rescoure_dir + "circle_btn_on.png"
circle_btn_off = rescoure_dir + "circle_btn_off.png"

image_fish = rescoure_dir + "fugu.png"

"""
 def addDevice(self):
        print "add device"
#            self.pane.
# wx.GetApp().GetAppViewSelectPane().AddDeviceNode("tool bar create")

        frame1 = wx.Frame(parent=self.parent, size=(800,400))
        Panel_AddDevice(frame1)
        frame1.CenterOnScreen()
        frame1.Show()

"""


class MyPopupWindow():
    def __init__(self, parent=None, size=(800, 600), title=None):
        #wx.DEFAULT_FRAME_STYLE
        #self.frame = wx.MiniFrame(parent=None, size=size, style = wx.CAPTION | wx.RESIZE_BORDER)
        self.frame = wx.Frame(parent=None, size=size, title=title)
        self.frame.EnableCloseButton(1)

    def windowPopup(self):
        self.frame.CenterOnScreen()
        self.frame.Show()

# class Panel_ButtonSetting():
#     def __init__(self, frame):
#         return