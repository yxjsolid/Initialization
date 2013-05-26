#!/usr/bin/env python
# -*- coding: utf-8 -*-
import wx
import wx.lib.buttons as buttons
from MyGlobal import *
import wx.lib.resizewidget as rw
from MySprite import *
from MyWidgetLibrary import *

def testRSizedWidget(parent):
    rw1 = rw.ResizeWidget(parent)

    # This one we will reparent to the ResizeWidget...
    tst = wx.Panel(parent)
    tst.SetBackgroundColour('pink')
    wx.StaticText(tst, -1, "a panel,\nwith limits")
    tst.SetMinSize((80,35))
    tst.SetMaxSize((200,100))
    rw1.SetManagedChild(tst)

class MyHmiPanel(wx.Panel):
    def __init__(self, parent, ID):
        wx.Window.__init__(self, parent, ID)
        self.parent = parent
        self.hwnd = self.GetHandle()

        self.size = self.GetSizeTuple()
        self.size_dirty = True

        self.rootSpriteGroup = pygame.sprite.LayeredUpdates()

        self.timer = wx.Timer(self)
        self.Bind(wx.EVT_PAINT, self.OnPaint)
        self.Bind(wx.EVT_TIMER, self.Update, self.timer)
        self.Bind(wx.EVT_SIZE, self.OnSize)

        self.fps = 60.0
        self.timespacing = 1000.0 / self.fps
        self.timer.Start(self.timespacing, False)
        #self.timer.Start(5000, False)

        self.linespacing = 5
        self.addTestSprite()
        self.previous_time = 0
        self.Bind(wx.EVT_MOUSE_EVENTS, self.OnMouse)
        self.Bind(wx.EVT_CONTEXT_MENU, self.OnContextMenu)

        self.selectedSprite = None
        #self.SetDoubleBuffered(True)
        testRSizedWidget(self)


    def addSpriteToPanel(self, sprite):
        self.rootSpriteGroup.add(sprite)


    def addTestSprite(self):
        for color, location, speed in [([255, 0, 0], [50, 50], [2,3]),
                                       ([0, 255, 0], [100, 100], [3,2]),
                                       ([0, 0, 255], [150, 150], [4,3])]:
            self.rootSpriteGroup.add(MoveBall(color, location, speed, (350, 350)))


        self.rootSpriteGroup.add(test_Drag_Sprite([100, 100, 100], [200, 200], [5,6], (350, 350)))

        self.rootSpriteGroup.add(Sprite_Button([200, 200, 200], [300, 400], [5,6], (350, 350)))
        self.rootSpriteGroup.add(AnimateTansporterSprite([200, 200, 200], (150,150), 150,40,500,1))
        self.rootSpriteGroup.add(SwitchButtonSprite([200, 200, 200], (250,150), 50,50,500,1))

        #self.rootSpriteGroup.add(specialSprite_transport([200, 200, 200], (100,100), 500,50,1,1))



        #self.addTestSprite()

    def addSpritePerformanceTest(self):
        rowMax = 10
        colMax = 10
        x_i = 100
        y_i = 100

        width = 150
        height = 50

        for i in range(0,rowMax):
            for j in range(colMax):
                updateInterval = random.randint(300,2000)
                trans1 = AnimateTansporterSprite([200, 200, 200], (x_i + i*width +20, y_i + j*width), width,height,updateInterval,1)
                self.rootSpriteGroup.add(trans1)

    def Update(self, event):
        # Any update tasks would go here (moving sprites, advancing animation frames etc.)

        #return

        # if hasattr(self, 'testBtn'):
        #     #self.testBtn.Update()
        #     #self.testBtn.OnPaint(event)
        #     self.testBtn.Refresh()
        #     pass
        #return
        self.Redraw()

        if hasattr(self, 'testBtn'):
                #self.testBtn.Update()
            #self.testBtn.OnPaint(event)
            #self.testBtn.Update()
            #self.testBtn.Refresh()
            pass
        return

    def Redraw(self):
        #print "select page is HIM", self.GetParent().GetCurrentPage() is self
        #print "isEnabled", self.IsEnabled()
        #print "MyHmiPanel, Redraw"
        # return

        if  self.size[0] == 0  or  self.size[1] == 0:
            print "MyHmiPanel.Redraw", self.size
            return

        if self.size_dirty:
            self.screen = pygame.Surface(self.size, 0, 32)
            self.size_dirty = False

        self.screen.fill((0,0,0))

        cur = 0
        w, h = self.screen.get_size()

        while cur <= h:
        #for i in range(0, 3):
            pygame.draw.aaline(self.screen, (255, 255, 255), (0, h - cur), (cur, 0))
            cur += self.linespacing

        current_time = pygame.time.get_ticks()
        #print current_time
        #print "current_time - previous_time = ", current_time - self.previous_time

        self.previous_time = current_time

        self.rootSpriteGroup.update(current_time)
        self.rootSpriteGroup.draw(self.screen)

        #saver.save(self.screen, "test")
        s = pygame.image.tostring(self.screen, 'RGB')  # Convert the surface to an RGB string

        #print "hmisize ",self.size
        img = wx.ImageFromData(self.size[0], self.size[1], s)  # Load this string into a wx image

        #if img.IsOk() is not True:
           # return
        bmp = wx.BitmapFromImage(img)  # Get the image in bitmap form
        dc = wx.ClientDC(self)  # Device context for drawing the bitmap
        #dc = wx.PaintDC(self)
        dc = wx.BufferedDC( dc)

        #print "MyHmiPanel repaint"
        dc.DrawBitmap(bmp, 0, 0, 1)  # Blit the bitmap image to the display


        if hasattr(self, 'testBtn'):
            #dddc = self.testBtn.OnDrawBtn()
            pass

            # (width, height) = self.GetClientSizeTuple()
            # (x,y) = self.testBtn.GetPositionTuple()
            #
            # dc.Blit(x,y,width,height, dddc, 0,0, useMask=True)

     #del dc
     #self.Refresh()


    def checkCollide(self, event):
        x , y = (event.GetX(),event.GetY())

        mousePoint = pygame.sprite.Sprite()
        mousePoint.rect = pygame.Rect(x, y, 1, 1)
        copoint = pygame.sprite.spritecollideany(mousePoint, self.rootSpriteGroup)

        if copoint:
            copoint.setSelect(1)

        return copoint

    def removeSelectedSprite(self):
        if self.selectedSprite:
            self.selectedSprite.setSelect(0)
            self.selectedSprite = None

    def setNewSelectedSprite(self, sprite):
        self.removeSelectedSprite()
        sprite.setSelect(1)
        self.selectedSprite = sprite

    def OnMouse(self, event):
        if event.LeftDown():

            print "left",(event.GetX(),event.GetY())

            selected = self.checkCollide(event)

            if selected:
                if self.selectedSprite:
                    if selected != self.selectedSprite:
                        self.setNewSelectedSprite(selected)
                else:
                    self.setNewSelectedSprite(selected)

                self.selectedSprite.setLastPos((event.GetX(),event.GetY()))
            else:
                self.removeSelectedSprite()

        elif event.LeftUp():
            print "left up"
        elif event.RightDown():
            print "RightDown",(event.GetX(),event.GetY())
            self.removeSelectedSprite()


        elif event.Dragging():
            print "left drag", (event.GetX(),event.GetY())
            if self.selectedSprite:
                self.selectedSprite.move((event.GetX(),event.GetY()))

        event.Skip()



    def OnPaint(self, event):
        self.Redraw()
        event.Skip()  # Make sure the parent frame gets told to redraw as well

    def OnSize(self, event):
        self.size = self.GetSizeTuple()
        self.size_dirty = True

    def Kill(self, event):
        # Make sure Pygame can't be asked to redraw /before/ quitting by unbinding all methods which
        # call the Redraw() method
        # (Otherwise wx seems to call Draw between quitting Pygame and destroying the frame)
        # This may or may not be necessary now that Pygame is just drawing to surfaces
        self.Unbind(event = wx.EVT_PAINT, handler = self.OnPaint)
        self.Unbind(event = wx.EVT_TIMER, handler = self.Update, source = self.timer)

    def OnContextMenu(self, event):
     # only do this part the first time so the events are only bound once
     #
     # Yet another anternate way to do IDs. Some prefer them up top to
     # avoid clutter, some prefer them close to the object of interest
     # for clarity.
        if not hasattr(self, "popupID1"):
            self.popupID1 = wx.NewId()
            self.popupID2 = wx.NewId()
            self.popupID3 = wx.NewId()
            self.popupID4 = wx.NewId()
            self.popupID5 = wx.NewId()
            self.popupID6 = wx.NewId()
            self.popupID7 = wx.NewId()
            self.popupID8 = wx.NewId()
            self.popupID9 = wx.NewId()
            self.popUpAddHmi = wx.NewId()


            self.Bind(wx.EVT_MENU, self.OnPopupOne, id=self.popupID1)
            self.Bind(wx.EVT_MENU, self.OnPopupTwo, id=self.popupID2)
            self.Bind(wx.EVT_MENU, self.OnPopupThree, id=self.popupID3)
            self.Bind(wx.EVT_MENU, self.OnPopupFour, id=self.popupID4)
            self.Bind(wx.EVT_MENU, self.OnPopupFive, id=self.popupID5)
            self.Bind(wx.EVT_MENU, self.OnPopupSix, id=self.popupID6)
            self.Bind(wx.EVT_MENU, self.OnPopupSeven, id=self.popupID7)
            self.Bind(wx.EVT_MENU, self.OnPopupEight, id=self.popupID8)
            self.Bind(wx.EVT_MENU, self.OnPopupNine, id=self.popupID9)

            self.Bind(wx.EVT_MENU, self.onAddHmiWidget, id=self.popUpAddHmi)

        # make a menu
        menu = wx.Menu()
        # Show how to put an icon in the menu
        item = wx.MenuItem(menu, self.popupID1,"One")

        menu.AppendItem(item)
        # add some other items
        menu.Append(self.popUpAddHmi, u"添加控件")
        menu.Append(self.popupID2, "Two")
        menu.Append(self.popupID3, "Three")
        menu.Append(self.popupID4, "Four")
        menu.Append(self.popupID5, "Five")
        menu.Append(self.popupID6, "Six")
        # make a submenu
        sm = wx.Menu()
        sm.Append(self.popupID8, "sub item 1")
        sm.Append(self.popupID9, "sub item 1")
        menu.AppendMenu(self.popupID7, "Test Submenu", sm)


        # Popup the menu.  If an item is selected then its handler
        # will be called before PopupMenu returns.
        self.PopupMenu(menu)

        menu.Destroy()


    def onAddHmiWidget(self, event):
     popupAddHmiWindow(self)

    def OnPopupOne(self, event):
     self.log.WriteText("Popup one\n")

    def OnPopupTwo(self, event):
     self.log.WriteText("Popup two\n")

    def OnPopupThree(self, event):
     self.log.WriteText("Popup three\n")

    def OnPopupFour(self, event):
     self.log.WriteText("Popup four\n")

    def OnPopupFive(self, event):
     self.log.WriteText("Popup five\n")

    def OnPopupSix(self, event):
     self.log.WriteText("Popup six\n")

    def OnPopupSeven(self, event):
     self.log.WriteText("Popup seven\n")

    def OnPopupEight(self, event):
     self.log.WriteText("Popup eight\n")

    def OnPopupNine(self, event):
     self.log.WriteText("Popup nine\n")
