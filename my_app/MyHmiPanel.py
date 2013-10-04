#!/usr/bin/env python
# -*- coding: utf-8 -*-
import wx
import wx.lib.buttons as buttons
from MyGlobal import *
import wx.lib.resizewidget as rw
from MySprite import *
from MyWidgetLibrary import *
from MyStatusDisplay import *


RW_THICKNESS = 4
RW_LENGTH = 12

# colors for the handle
RW_PEN   = 'black'
RW_FILL  = '#A0A0A0'
RW_FILL2 = '#E0E0E0'

def testRSizedWidget(parent):
    rw1 = rw.ResizeWidget(parent)
    rw1 = MyResizeWidget(parent)
    # This one we will reparent to the ResizeWidget...
    # tst = wx.Panel(parent)
    # tst.SetBackgroundColour('pink')
    # wx.StaticText(tst, -1, "a panel,\nwith limits")
    # tst.SetMinSize((80,35))
    # tst.SetMaxSize((200,100))

    #tst = Panel_Status_Display(rw1)

    #rw1.SetManagedChild(tst)

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
        # self.addTestSprite()
        self.previous_time = 0
        self.Bind(wx.EVT_MOUSE_EVENTS, self.OnMouse)
        self.Bind(wx.EVT_CONTEXT_MENU, self.OnContextMenu)

        self.selectedSprite = None
        #self.SetDoubleBuffered(True)
        testRSizedWidget(self)

    def addSpriteToPanel(self, sprite):
        sprite.parent = self
        self.rootSpriteGroup.add(sprite, layer=12)

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

        # while cur <= h:
        #     pygame.draw.aaline(self.screen, (255, 255, 255), (0, h - cur), (cur, 0))
        #     cur += self.linespacing

        current_time = pygame.time.get_ticks()
        #print current_time
        #print "current_time - previous_time = ", current_time - self.previous_time

        self.previous_time = current_time
        self.rootSpriteGroup.update(current_time)
        self.rootSpriteGroup.draw(self.screen)

        s = pygame.image.tostring(self.screen, 'RGB')  # Convert the surface to an RGB string
        img = wx.ImageFromData(self.size[0], self.size[1], s)  # Load this string into a wx image

        #if img.IsOk() is not True:
           # return
        bmp = wx.BitmapFromImage(img)  # Get the image in bitmap form
        dc = wx.ClientDC(self)  # Device context for drawing the bitmap
        dc = wx.BufferedDC( dc)
        dc.DrawBitmap(bmp, 0, 0, 1)  # Blit the bitmap image to the display

        if hasattr(self, 'testBtn'):
            #dddc = self.testBtn.OnDrawBtn()
            pass

            # (width, height) = self.GetClientSizeTuple()
            # (x,y) = self.testBtn.GetPositionTuple()
            #
            # dc.Blit(x,y,width,height, dddc, 0,0, useMask=True)

    def checkCollide(self, event):
        x , y = (event.GetX(),event.GetY())

        mousePoint = pygame.sprite.Sprite()
        mousePoint.rect = pygame.Rect(x, y, 1, 1)
        #copoint = pygame.sprite.spritecollideany(mousePoint, self.rootSpriteGroup)
        copoint = pygame.sprite.spritecollide(mousePoint, self.rootSpriteGroup, None)

        if copoint:
            copoint = copoint[-1]

        return copoint

    def removeSelectedSprite(self):
        if self.selectedSprite:
            self.selectedSprite.setSelect(0)
            self.selectedSprite = None

    def setNewSelectedSprite(self, sprite):
        self.removeSelectedSprite()
        sprite.setSelect(1)
        self.selectedSprite = sprite

    def onSelectSprite(self, event, onMouseObj):
        if onMouseObj:
            if self.selectedSprite:
                if onMouseObj != self.selectedSprite:
                    self.setNewSelectedSprite(onMouseObj)
            else:
                self.setNewSelectedSprite(onMouseObj)

            self.selectedSprite.setLastPos((event.GetX(),event.GetY()))
        else:
            self.removeSelectedSprite()


    def OnMouse(self, event):
        mousePos = (event.GetX(),event.GetY())
        onMouseObj = self.checkCollide(event)
        #print "MyHmiPanel Mouse Event:", event
        event.Skip()

        if onMouseObj:
            onMouseObj.OnMouseHandler(event)


        #print "event.GetSkipped()", event.GetSkipped()

        if not event.GetSkipped():

            print "event dropped "
            return

        if event.LeftDown():
            #print "LeftDown",(event.GetX(),event.GetY())
            self.onSelectSprite(event, onMouseObj)
        elif event.LeftUp():
            #print "left up"
            pass

        elif event.RightUp():
            #print "RightUp"
            self.onSelectSprite(event, onMouseObj)
        elif event.RightDown():
            #print "RightDown",(event.GetX(),event.GetY())
            self.onSelectSprite(event, onMouseObj)

        elif event.Dragging() and event.LeftIsDown():
            #print "left Dragging", (event.GetX(),event.GetY())

            if self.selectedSprite:
                self.selectedSprite.move((event.GetX(),event.GetY()))

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
        self.Unbind(event=wx.EVT_PAINT, handler=self.OnPaint)
        self.Unbind(event=wx.EVT_TIMER, handler=self.Update, source=self.timer)

    def OnContextMenu(self, event):
     # only do this part the first time so the events are only bound once
     #
     # Yet another anternate way to do IDs. Some prefer them up top to
     # avoid clutter, some prefer them close to the object of interest
     # for clarity.
        screenPos = event.GetPosition()
        panelPos = self.GetScreenPosition()
        self.popupPosition = wx.Point(screenPos.x - panelPos.x, screenPos.y - panelPos.y)

        if not hasattr(self, "popupID1"):
            self.popupID1 = wx.NewId()
            self.popUpAddHmi = wx.NewId()
            self.popUpAddStatuaDisp = wx.NewId()

            self.Bind(wx.EVT_MENU, self.OnPopupOne, id=self.popupID1)

            self.Bind(wx.EVT_MENU, self.onAddHmiWidget, id=self.popUpAddHmi)
            self.Bind(wx.EVT_MENU, self.onAddStatusDisp, id=self.popUpAddStatuaDisp)

        # make a menu
        menu = wx.Menu()
        # Show how to put an icon in the menu
        item = wx.MenuItem(menu, self.popupID1,"One")

        menu.AppendItem(item)
        # add some other items
        menu.Append(self.popUpAddHmi, HMI_POPUP_MENU_ADD_OBJ)
        menu.Append(self.popUpAddStatuaDisp, HMI_POPUP_MENU_ADD_STATUS_DISP)

        self.PopupMenu(menu)
        menu.Destroy()

    def onAddHmiWidget(self, event):
        popupAddHmiWindow(self, self.popupPosition)

    def onAddStatusDisp(self, event):
# wx.CommandEvent
        popupAddStatusDisplay(self, self.popupPosition)

    def OnPopupOne(self, event):
        self.log.WriteText("Popup one\n")


class MyResizeWidget(wx.PyPanel):
    def __init__(self, *args, **kw):
        wx.PyPanel.__init__(self, *args, **kw)
        self._init()

        self.Bind(wx.EVT_LEFT_DOWN, self.OnLeftDown)
        self.Bind(wx.EVT_LEFT_UP, self.OnLeftUp)
        self.Bind(wx.EVT_MOTION,  self.OnMouseMove)
        self.Bind(wx.EVT_LEAVE_WINDOW, self.OnMouseLeave)

        self.Bind(wx.EVT_SIZE, self.OnSize)
        self.Bind(wx.EVT_PAINT, self.OnPaint)


    def _init(self):
        self._managedChild = None
        self._bestSize = wx.Size(100,25)
        self._resizeCursor = False
        self._dragPos = None
        self._resizeEnabled = True
        self._reparenting = False


    def SetManagedChild(self, child):
        self._reparenting = True
        child.Reparent(self)  # This calls AddChild, so do the rest of the init there
        self._reparenting = False
        self.AdjustToChild()

    def GetManagedChild(self):
        return self._managedChild

    ManagedChild = property(GetManagedChild, SetManagedChild)


    def AdjustToChild(self):
        self.AdjustToSize(self._managedChild.GetEffectiveMinSize())


    def AdjustToSize(self, size):
        size = wx.Size(*size)
        self._bestSize = size + (RW_THICKNESS, RW_THICKNESS)
        self.SetSize(self._bestSize)


    def EnableResize(self, enable=True):
        self._resizeEnabled = enable
        self.Refresh(False)


    def IsResizeEnabled(self):
        return self._resizeEnabled


    #=== Event handler methods ===
    def OnLeftDown(self, evt):
        if self._hitTest(evt.GetPosition()) and self._resizeEnabled:
            self.CaptureMouse()
            self._dragPos = evt.GetPosition()


    def OnLeftUp(self, evt):
        if self.HasCapture():
            self.ReleaseMouse()
        self._dragPos = None


    def OnMouseMove(self, evt):
        # set or reset the drag cursor
        pos = evt.GetPosition()
        if self._hitTest(pos) and self._resizeEnabled:
            if not self._resizeCursor:
                self.SetCursor(wx.StockCursor(wx.CURSOR_SIZENWSE))
                self._resizeCursor = True
        else:
            if self._resizeCursor:
                self.SetCursor(wx.StockCursor(wx.CURSOR_ARROW))
                self._resizeCursor = False

        # determine if a new size is needed
        if evt.Dragging() and self._dragPos is not None:
            delta = self._dragPos - pos
            newSize = self.GetSize() - delta.Get()
            self._adjustNewSize(newSize)
            if newSize != self.GetSize():
                self.SetSize(newSize)
                self._dragPos = pos
                self._bestSize = newSize
                self._sendEvent()


    def _sendEvent(self):
        #event = _RWLayoutNeededEvent(self.GetId())
       # event.SetEventObject(self)
        #self.GetEventHandler().ProcessEvent(event)
        pass


    def _adjustNewSize(self, newSize):
        if newSize.width < RW_LENGTH:
            newSize.width = RW_LENGTH
        if newSize.height < RW_LENGTH:
            newSize.height = RW_LENGTH

        if self._managedChild:
            minsize = self._managedChild.GetMinSize()
            if minsize.width != -1 and newSize.width - RW_THICKNESS < minsize.width:
                newSize.width = minsize.width + RW_THICKNESS
            if minsize.height != -1 and newSize.height - RW_THICKNESS < minsize.height:
                newSize.height = minsize.height + RW_THICKNESS
            maxsize = self._managedChild.GetMaxSize()
            if maxsize.width != -1 and newSize.width - RW_THICKNESS > maxsize.width:
                newSize.width = maxsize.width + RW_THICKNESS
            if maxsize.height != -1 and newSize.height - RW_THICKNESS > maxsize.height:
                newSize.height = maxsize.height + RW_THICKNESS


    def OnMouseLeave(self, evt):
        if self._resizeCursor:
            self.SetCursor(wx.StockCursor(wx.CURSOR_ARROW))
            self._resizeCursor = False


    def OnSize(self, evt):
        if not self._managedChild:
            return
        sz = self.GetSize()
        self._managedChild.SetRect(
            wx.RectPS((0,0), sz - (RW_THICKNESS, RW_THICKNESS)))
        r = wx.Rect(sz.width - RW_LENGTH,
                    sz.height - RW_LENGTH,
                    RW_LENGTH, RW_LENGTH)
        r.Inflate(2,2)
        self.RefreshRect(r)


    def OnPaint(self, evt):
    # draw the resize handle
        dc = wx.PaintDC(self)
        w,h = self.GetSize()
        points = [ (w - 1,            h - RW_LENGTH),
                   (w - RW_THICKNESS, h - RW_LENGTH),
                   (w - RW_THICKNESS, h - RW_THICKNESS),
                   (w - RW_LENGTH,    h - RW_THICKNESS),
                   (w - RW_LENGTH,    h - 1),
                   (w - 1,            h - 1),
                   (w - 1,            h - RW_LENGTH),
                   ]
        dc.SetPen(wx.Pen(RW_PEN, 1))
        if self._resizeEnabled:
            fill = RW_FILL
        else:
            fill = RW_FILL2
        dc.SetBrush(wx.Brush(fill))
        dc.DrawPolygon(points)


    def _hitTest(self, pos):
        # is the position in the area to be used for the resize handle?
        w, h = self.GetSize()
        if ( w - RW_THICKNESS <= pos.x <= w
             and h - RW_LENGTH <= pos.y <= h ):
            return True
        if ( w - RW_LENGTH <= pos.x <= w
             and h - RW_THICKNESS <= pos.y <= h ):
            return True
        return False


    #=== Overriden virtuals from the base class ===
    def AddChild(self, child):
        assert self._managedChild is None, "Already managing a child widget, can only do one"
        self._managedChild = child
        wx.PyPanel.AddChild(self, child)

        # This little hack is needed because if this AddChild was called when
        # the widget was first created, then the OOR values will get reset
        # after this function call, and so the Python proxy object saved in
        # the window may be different than the child object we have now, so we
        # need to reset which proxy object we're using.  Look for it by ID.
        def _doAfterAddChild(self, id):
            if not self:
                return
            child = self.FindWindowById(id)
            self._managedChild = child
            self.AdjustToChild()
            self._sendEvent()
        if self._reparenting:
            _doAfterAddChild(self, child.GetId())
        else:
            wx.CallAfter(_doAfterAddChild, self, child.GetId())

    def RemoveChild(self, child):
        self._init()
        wx.PyPanel.RemoveChild(self, child)


    def DoGetBestSize(self):
        return self._bestSize



