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


EDIT_IO_NODE_LABEL_OUTPUT = u"开关量输出"
EDIT_IO_NODE_LABEL_INPUT = u"开关量输入"
EDIT_IO_NODE_LABEL_GROUP_DEFAULT = u"默认分组"

EDIT_IO_NODE_LABEL_GROUP_INPUT_NAME = u"新分组名称:"

EDIT_IO_NODE_LABEL_DEL_GROUP_CONFIRM = u"确定删除分组及其所有数据点?"

EDIT_IO_NODE_LABEL_NEW_GROUP = u"新建分组"
EDIT_IO_NODE_LABEL_DEL_GROUP = u"删除分组"
EDIT_IO_NODE_LABEL_RENAME_GROUP = u"重命名分组"
EDIT_IO_NODE_LABEL_EXPAND_GROUP = u"展开分组"
EDIT_IO_NODE_LABEL_COLLAPSE_GROUP = u"闭合分组"


IO_NODE_ADD_NEW = u"添加数据点"
IO_NODE_EDIT = u"编辑数据点"

IO_NODE_LIST_COL_NAME = u"数据点名称"
IO_NODE_LIST_COL_DESC = u"描述"
IO_NODE_LIST_COL_IO = u"I/O连接"
WINDOW_TITLE_DEL_IO_NODE = u"删除数据点"
DIALOG_ALERT_DEL_IO_NODE = u"确定删除数据点？"




CAN_STATION_DEFAULT_NAME = u"默认站点"
CAN_STATION_DEFAULT_DESC = u"未定义"

LABEL_CAN_STATION_NAME = u"站点名称"
LABEL_CAN_STATION_ID = u"站点地址"
LABEL_CAN_STATION_DESC = u"站点描述"
WINDOW_TITLE_ADD_STATION = u"添加站点"
WINDOW_TITLE_EDIT_STATION = u"编辑站点"
WINDOW_TITLE_DEL_STATION = u"删除站点"
DIALOG_ALERT_DEL_STATION = u"确定删除站点及其所有子板？"


LABEL_IO_BOARD_COLUM_ID = u"子板号"
LABEL_IO_BOARD_COLUM_TYPE = u"子板类型"
WINDOW_TITLE_ADD_BOARD = u"添加子板"
WINDOW_TITLE_EDIT_BOARD = u"编辑子板"
WINDOW_TITLE_DEL_BOARD = u"删除子板"
DIALOG_ALERT_DEL_BOARD = u"确定删除子板？"

LABEL_IO_PORT = u"端子"


LABEL_IO_BOARD_TYPE_UNKNOWN = u"子板类型错误"
LABEL_IO_BOARD_OUTPUT = u"信号量输出"
LABEL_IO_BOARD_INPUT = u"信号量输入"


MENU_ITEM_BUTTON_SETTING = u"动作属性"


DEVICE_ITEM_SETTING = u"属性设置"
HMI_POPUP_MENU_ADD_OBJ = u"添加控件"
HMI_POPUP_MENU_ADD_STATUS_DISP = u"添加状态表"


STATUS_DISPLAY_NAME = u"数据点"
STATUS_DISPLAY_STATUS = u"状态"

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


def globalGetCfg():
    cfgObj = wx.GetApp().getConfigure()
    return cfgObj




class MyPopupWindow():
    def __init__(self, parent=None, size=(800, 600), title=None):
        #wx.DEFAULT_FRAME_STYLE
        #self.frame = wx.MiniFrame(parent=None, size=size, style = wx.CAPTION | wx.RESIZE_BORDER)
        self.frame = wx.Frame(parent=None, size=size, title=title)
        self.frame.EnableCloseButton(1)

    def windowPopup(self):
        self.frame.CenterOnScreen()
        self.frame.Show()

    def closeWindow(self):
        self.frame.Close()

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