# -*- coding: utf-8 -*-
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


LABEL_CAN_STATION_NAME = "Name"
LABEL_CAN_STATION_ID = "ID"
LABEL_CAN_STATION_DESC = "desc"

LABEL_IO_BOARD_COLUM_ID = u"子板号"
LABEL_IO_BOARD_COLUM_TYPE = u"子板类型"


LABEL_IO_BOARD_OUTPUT = u"信号量输出"
LABEL_IO_BOARD_INPUT = u"信号量输入"

LABEL_STATION_NAME = u"子板"
LABEL_STATION_INFO = u"未定义"

MENU_ITEM_BUTTON_SETTING = u"动作属性"

DEVICE_ITEM_SETTING = u"属性设置"

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


# %a 本地简化星期名称
# %A 本地完整星期名称
# %b 本地简化的月份名称
# %B 本地完整的月份名称
# %c 本地相应的日期表示和时间表示
# %j 年内的一天（001-366）
# %p 本地A.M.或P.M.的等价符
# %U 一年中的星期数（00-53）星期天为星期的开始
# %w 星期（0-6），星期天为星期的开始
# %W 一年中的星期数（00-53）星期一为星期的开始
# %x 本地相应的日期表示
# %X 本地相应的时间表示
# %Z 当前时区的名称
# %% %号本身


class MyLogWriter():
    def __init__(self):
        self.txt = None
        return

    def writeLog(self, log):
        import time
        tmstr =  time.strftime("%Y-%m-%d %X \t", time.localtime())
        self.txt.WriteText(tmstr)
        self.txt.WriteText(log)
        self.txt.WriteText("\n")
        return


LogWriter = MyLogWriter()