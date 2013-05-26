#!/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import division
import wx
import wx.lib.buttons as buttons
from MyGlobal import *
import wx.lib.resizewidget as rw
from MySprite import *
from MyButton import *


class MyWidgetLibraryPanel ( wx.Panel ):

    def __init__( self, parent ):
        wx.Panel.__init__ ( self, parent, id = wx.ID_ANY, pos = wx.DefaultPosition, size = wx.Size( 518,300 ), style = wx.TAB_TRAVERSAL )

        mainWinSizer = wx.BoxSizer( wx.VERTICAL )

        self.scrolledWindow = wx.ScrolledWindow( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.HSCROLL|wx.VSCROLL )
        self.scrolledWindow.SetScrollRate( 5, 5 )
        # boxSizer = wx.StaticBoxSizer( wx.StaticBox( self.scrolledWindow, wx.ID_ANY, _(u"label") ), wx.VERTICAL )
        boxSizer = wx.StaticBoxSizer( wx.StaticBox( self.scrolledWindow, wx.ID_ANY, u"label" ), wx.VERTICAL )

        libSizer = wx.FlexGridSizer( 10, 5, 0, 0 )
        libSizer.SetFlexibleDirection( wx.BOTH )
        libSizer.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

        boxSizer.Add( libSizer, 1, wx.EXPAND, 5 )
        self.scrolledWindow.SetSizer( boxSizer )
        self.scrolledWindow.Layout()
        boxSizer.Fit( self.scrolledWindow )
        mainWinSizer.Add( self.scrolledWindow, 1, wx.EXPAND |wx.ALL, 5 )
        self.SetSizer( mainWinSizer )

        self.boxSizer = boxSizer
        self.libSizer = libSizer

        self.Layout()

        self.loadDefaultWidgetLib()


    def __del__( self ):
        pass

    def loadDefaultWidgetLib(self):
        self.libs = MyDefaultLibrary((100,100))

        for widget in self.libs.widgetList:
            self.addWidgetToLibrary(widget)

    def addWidgetToLibrary(self, widget):
        iconBmp = widget.getIconBmp(self.libs.defaultSize)
        btn = wx.BitmapButton( self.scrolledWindow, wx.ID_ANY, iconBmp, wx.DefaultPosition, iconBmp.GetSize(), wx.BU_AUTODRAW)
        #btn = wx.BitmapButton( self.scrolledWindow, wx.ID_ANY, iconBmp, wx.DefaultPosition, iconBmp.GetSize(), wx.BU_AUTODRAW | wx.TRANSPARENT_WINDOW)
        btn.Bind( wx.EVT_LEFT_DCLICK, self.addSpriteWidgetToPanel )
        btn.widget = widget
        self.libSizer.Add( btn, 0, wx.ALL, 5 )

    def addWidgetToPanel11(self, event):

        print "addWidgetToPanel"
        testBtn1 =  MyGenBitmapToggleButton(self.targetPanel, -1,  pos = (100,100), style =  wx.BORDER_NONE|wx.TRANSPARENT_WINDOW)
        testBtn1.loadImageLabel(btn_on)
        testBtn1.loadImageSelected(btn_off)
        testBtn1.setSizeFitImage()

    def addWidgetToPanel(self, event):
        print "addWidgetToPanel"
        #m_button16 = wx.Button( self.targetPanel, wx.ID_ANY, u"MyButton", pos = (100,100), (100,100), 0)
        m_button16 = btn1( self.targetPanel, wx.ID_ANY, u"MyButton", (100,200), (100,100), wx.TRANSPARENT_WINDOW )

        btnuu = wx.BitmapButton( self.targetPanel, wx.ID_ANY, wx.ArtProvider.GetBitmap( wx.ART_ADD_BOOKMARK, wx.ART_BUTTON ), (250,300), (100,100), wx.TRANSPARENT_WINDOW )

        self.testBtn1 =  MyGenBitmapToggleButton(self.targetPanel, -1,  pos = (100,250), style =  wx.BORDER_NONE |  wx.TRANSPARENT_WINDOW )
        self.testBtn1.Raise()
        self.testBtn1.SetDoubleBuffered(0)

        self.testBtn1.loadImageLabel(circle_btn_on)
        self.testBtn1.loadImageSelected(circle_btn_off)

        self.targetPanel.testBtn =   self.testBtn1

    def addSpriteWidgetToPanel(self, event):
        btn =  event.GetEventObject()
        widget = btn.widget
        sprite = widget.createNewSprite()
        self.targetPanel.addSpriteToPanel(sprite)
        return
"""
class btn1(wx.Button):
    def __init__(self, parent,  id=-1,  label="",
                                                     pos=wx.DefaultPosition,  size=wx.DefaultSize,
                                                     style=0,  validator=wx.DefaultValidator,
                                                     name=""):
        wx.Button.__init__( self, parent, id, label, pos,size, style, validator,  name)
        self.SetDoubleBuffered(1)

    def OnPaint(self,event):
        print "btn1 onpaint"

    def Redraw(self):
        print "btn1 redraw"
"""


class MyWidgetObj():
    TYPE_SPRITE, TYPE_WXPYTHON = range(2)

    def __init__(self, type):

        self.dict = {"Button":self.createNewBtnSprite, "Sprite":self.getSpriteIconBmp}
        self.type = type
        self.Sprite = None

        if not self.dict.has_key(type):
            raise "error"

    # def getIconBmp(self, size):
    #     from PIL import Image
    #     print "self.btnOn,", self.btnOn
    #     print "size", size
    #
    #     im = Image.open(self.btnOn)
    #     #im.thumbnail(size, Image.ANTIALIAS)
    #     #im.save(r".\image\tttt", "JPEG")
    #     #s = im.tostring()
    #     img = ImageOps.fit(im, size, Image.ANTIALIAS)
    #     img.save(r".\image\tttt", "JPEG")
    #     #img = wx.ImageFromData(size[0], size[1], s)  # Load this string into a wx image
    #
    #     return img.ConvertToBitmap()

    def getIconBmp(self, size):
        # getIconFn = self.dict[self.type]
        # return getIconFn(size)

        return self.getSpriteIconBmp(size)

    def fitIconBmp(self, img, size):
        imgSize = img.GetSize()

        imgSizeMax = max(imgSize[0], imgSize[1])
        scale = size[0]/imgSizeMax   #suppose size[0]==size[1]

        x = imgSize[0]*scale
        y = imgSize[1]*scale
        px = size[0] - x
        py = size[1] - y

        img = img.Scale(x,y,quality=wx.IMAGE_QUALITY_HIGH)
        img = img.Size((100,100), (px/2,py/2))

        return img

    def getBtnIconBmp(self, size):
        #from PIL import Image
        img = wx.Image(self.btnOn)
        img = self.fitIconBmp(img, size)

        return img.ConvertToBitmap()

    def getSpriteIconBmp1(self, size):
        s = pygame.image.tostring(self.Sprite.image, 'RGBA', False)  # Convert the surface to an RGB string
        imgSize = self.Sprite.image.get_size()

        alpha_data = s[3::4]
        rgb_data = ""
        for i in range(0, len(s), 4):
            rgb_data += s[i:i+3]

        #img = wx.ImageFromData(imgSize[0], imgSize[1], rgb_data)  # Load this string into a wx image
        img = wx.ImageFromDataWithAlpha(imgSize[0], imgSize[1], rgb_data, alpha_data)  # Load this string into a wx image
        img = self.fitIconBmp(img, size)
        return img.ConvertToBitmap()

    def getSpriteIconBmp(self, size):
        s = pygame.image.tostring(self.Sprite.image, 'RGBA', False)  # Convert the surface to an RGB string
        imgSize = self.Sprite.image.get_size()

        print "sprint size", imgSize

#        scale(Surface, (width, height), DestSurface = None) -> Surface

        alpha_data = s[3::4]
        rgb_data = ""
        for i in range(0, len(s), 4):
            rgb_data += s[i:i+3]

        #img = wx.ImageFromData(imgSize[0], imgSize[1], rgb_data)  # Load this string into a wx image
        img = wx.ImageFromDataWithAlpha(imgSize[0], imgSize[1], rgb_data, alpha_data)  # Load this string into a wx image
        img = self.fitIconBmp(img, size)
        return img.ConvertToBitmap()

    def createNewSprite(self):
        fn = self.dict[self.type]
        return fn()


    def createNewBtnSprite(self):
        print "createNewBtnSprite"

        dicList = []
        dic = self.Sprite.imageResource
        for key in dic:
            dicList.append((key, dic[key][0]))

        sprite = ButtonSprite(initPos=(100,250), dicts=dicList)
        return sprite

class MyDefaultLibrary():
    def __init__(self, size):
        self.defaultSize = size
        self.widgetList = []
        self.buildDefaultLibray()

    def buildDefaultLibray(self):
        self.addSpriteBtn(btn_on, btn_off)
        self.addSpriteBtn(btn_red_up, btn_red_down)
        self.addSpriteBtn(btn_green_up, btn_green_down)
        self.addSpriteBtn(circle_btn_on, circle_btn_off)
        self.addDefaultSprite()

    def addDefaultBtn(self, btnOn, btnOff):
        obj = MyWidgetObj("Button")
        obj.btnOn = btnOn
        obj.btnOff = btnOff
        self.widgetList.append(obj)

    def addSpriteBtn(self, on, off):
        x = self.defaultSize[0]
        y = self.defaultSize[1]

        obj = MyWidgetObj("Button")
        obj.Sprite = ButtonSprite(initPos=(0,0), width=x, height=y, dicts= [('on',on),('off',off)])
        self.widgetList.append(obj)

    def addDefaultSprite(self):
        x = self.defaultSize[0]
        y = self.defaultSize[1]

        obj = MyWidgetObj("Sprite")
        obj.Sprite = AnimateTansporterSprite(width=200, height=60)
        self.widgetList.append(obj)


def popupAddHmiWindow(targetPanel):
    frame1 = wx.Frame(parent=None, size=(800,400))
    panel = MyWidgetLibraryPanel(frame1)
    panel.targetPanel = targetPanel

    frame1.CenterOnScreen()
    frame1.Show()


if __name__ == '__main__':
    app = MyTestApplication()
    app.setFrame()
    #app.setDialog()

    panel = MyWidgetLibraryPanel(app.window)
    app.launchApp()
