### PYGAME IN WX ###
# A simple test of embedding Pygame in a wxPython frame
#
# By David Barker (aka Animatinator), 14/07/2010
# Patch for cross-platform support by Sean McKean, 16/07/2010
# Patch to fix redrawing issue by David Barker, 20/07/2010
# Second window demo added by David Barker, 21/07/2010
 
 
import wx, sys, os, pygame
from MySprite import *
import random


pygame.Rect
pygame.init()
class myFileSave():
    direc = r"D:\workspace\myGitProj\init\my_app\image\test1\\"
    def __init__(self):
        self.index = 0

    def save(self,screen, name):
        filename = self.direc + name + str(self.index) +".jpg"
      
        print filename
         
            
        pygame.image.save(screen, filename)
        self.index +=1
#saver = myFileSave()

class PygameDisplay(wx.Window):
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
 
        self.linespacing = 5
        self.addSprite()
        self.previous_time = 0
        self.Bind(wx.EVT_MOUSE_EVENTS, self.OnMouse)

        self.selectedSprite = None
 
    def addSprite(self):
        for color, location, speed in [([255, 0, 0], [50, 50], [2,3]),
                    ([0, 255, 0], [100, 100], [3,2]),
                    ([0, 0, 255], [150, 150], [4,3])]:
            self.rootSpriteGroup.add(MoveBall(color, location, speed, (350, 350)))

        self.rootSpriteGroup.add(test_Drag_Sprite([0, 0, 0], [150, 150], [5,6], (350, 350)))
        self.rootSpriteGroup.add(test_Drag_Sprite([100, 100, 100], [200, 200], [5,6], (350, 350)))

        self.rootSpriteGroup.add(Sprite_Button([200, 200, 200], [300, 400], [5,6], (350, 350)))
        #self.rootSpriteGroup.add(Sprite_Animate([200, 200, 200], [600, 600], [5,6], (350, 350)))
        
        #self.rootSpriteGroup.add(mySelfTestSprite([200, 200, 200], [600, 600], [5,6], (350, 350)))

        trans =  specialSprite_transport([200, 200, 200], (100,100), 500,50,1,1)
        trans1 = AnimateTansporterSprite([200, 200, 200], (150,150), 150,40,500,1)
               
        self.rootSpriteGroup.add(trans)
        self.rootSpriteGroup.add(trans1)
        
        btn = SwitchButtonSprite([200, 200, 200], (250,150), 50,50,500,1)
        self.rootSpriteGroup.add(btn)

        #self.addTestSprite()
        
    def addTestSprite(self):
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
        return
 
    def Redraw(self):
       # print "select page is pygame", self.GetParent().GetCurrentPage() is self
       # print "isEnabled", self.IsEnabled()
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
        img = wx.ImageFromData(self.size[0], self.size[1], s)  # Load this string into a wx image

        if img.IsOk() is not True:
            return

        bmp = wx.BitmapFromImage(img)  # Get the image in bitmap form
        dc = wx.ClientDC(self)  # Device context for drawing the bitmap
        dc.DrawBitmap(bmp, 0, 0, 1)  # Blit the bitmap image to the display
        del dc
    

    def checkCollide(self, event):

        x , y = (event.GetX(),event.GetY())

        mousePoint = pygame.sprite.Sprite()
        mousePoint.rect = pygame.Rect(x, y, 1, 1)

        copoint = pygame.sprite.spritecollideany(mousePoint, self.rootSpriteGroup)
        
        if copoint:
           copoint.setSelect(1)

        
        #print "copoint", copoint
        
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
            print "reight do",(event.GetX(),event.GetY())
            self.removeSelectedSprite()   


        elif event.Dragging():
            print "left drag", (event.GetX(),event.GetY())
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
        self.Unbind(event = wx.EVT_PAINT, handler = self.OnPaint)
        self.Unbind(event = wx.EVT_TIMER, handler = self.Update, source = self.timer)
 
 
class FoolDisplay(PygameDisplay):
    def __init__(self, parent, id):
        PygameDisplay.__init__(self, parent, id)
        pygame.font.init()
        self.mainfont = pygame.font.Font(None, 40)
        self.text = self.mainfont.render("FOOOOOOL! NOW WE ARE ALL DAMNED!", True, (255, 0, 0))
        self.borw = True  # True = draw a black background, False = draw a white background
        self.points = []  # A list of points to draw
       
        self.Bind(wx.EVT_LEFT_DOWN, self.OnClick)
   
    def Update(self, event):
        PygameDisplay.Update(self, event)
        self.borw = not self.borw  # Alternate the background colour
       
        for i, point in enumerate(self.points):  # Slide all the points down and slightly to the right
            self.points[i] = (point[0] + 0.1, point[1] + 1)
   
    def Redraw(self):
        # If the size has changed, create a new surface to match it
        if self.size_dirty:
            self.screen = pygame.Surface(self.size, 0, 32)
            self.size_dirty = False
       
        # Draw the background
        if self.borw:
            self.screen.fill((0, 0, 0))
        else:
            self.screen.fill((255, 255, 255))
       
        self.screen.blit(self.text, (0, 0))
       
        # Draw circles at all the stored points
        for point in self.points:
            pygame.draw.circle(self.screen, (0, 255, 0), (int(point[0]), int(point[1])), 5)
       
        s = pygame.image.tostring(self.screen, 'RGB')  # Convert the surface to an RGB string
        img = wx.ImageFromData(self.size[0], self.size[1], s)  # Load this string into a wx image
        bmp = wx.BitmapFromImage(img)  # Get the image in bitmap form
        dc = wx.ClientDC(self)  # Device context for drawing the bitmap
        dc.DrawBitmap(bmp, 0, 0, False)  # Blit the bitmap image to the display
        del dc
   
    def OnClick(self, event):
        self.points.append(event.GetPositionTuple())  # Add a new point at the mouse position
 
 
class FoolFrame(wx.Frame):
    def __init__(self, parent):
        wx.Frame.__init__(self, parent, -1, size = (600, 300), style = wx.CAPTION | wx.SYSTEM_MENU | wx.CLOSE_BOX)
       
        self.display = FoolDisplay(self, -1)
       
        self.SetTitle("NOOOOOOOO!")
 
 
class Frame(wx.Frame):
    def __init__(self, parent):
        wx.Frame.__init__(self, parent, -1, size = (600, 600))
       
        self.display = PygameDisplay(self, -1)
       
        self.statusbar = self.CreateStatusBar()
        self.statusbar.SetFieldsCount(3)
        self.statusbar.SetStatusWidths([-3, -4, -2])
        self.statusbar.SetStatusText("wxPython", 0)
        self.statusbar.SetStatusText("Look, it's a nifty status bar!!!", 1)
       
        self.Bind(wx.EVT_SIZE, self.OnSize)
        self.Bind(wx.EVT_CLOSE, self.Kill)
       
        self.curframe = 0
       
        self.SetTitle("Pygame embedded in wxPython")
       
        self.slider = wx.Slider(self, wx.ID_ANY, 5, 1, 10, style = wx.SL_HORIZONTAL | wx.SL_LABELS)
        self.slider.SetTickFreq(0.1, 1)
        self.button = wx.Button(self, -1, "DO NOT PRESS THIS BUTTON")
       
        self.timer = wx.Timer(self)
       
        self.Bind(wx.EVT_SCROLL, self.OnScroll)
        self.Bind(wx.EVT_SIZE, self.OnSize)
        self.Bind(wx.EVT_TIMER, self.Update, self.timer)
        self.Bind(wx.EVT_BUTTON, self.ButtonClick, self.button)
       
        self.timer.Start((1000.0 / self.display.fps))
       
        self.sizer = wx.BoxSizer(wx.VERTICAL)
        self.sizer2 = wx.BoxSizer(wx.HORIZONTAL)
        self.sizer2.Add(self.slider, 1, flag = wx.EXPAND | wx.RIGHT, border = 5)
        self.sizer2.Add(self.button, 0, flag = wx.EXPAND | wx.ALL, border = 5)
        self.sizer.Add(self.sizer2, 0, flag = wx.EXPAND)
        self.sizer.Add(self.display, 1, flag = wx.EXPAND)
       
        self.SetAutoLayout(True)
        self.SetSizer(self.sizer)
        self.Layout()
 
    def Kill(self, event):
        self.display.Kill(event)
        self.Destroy()
 
    def OnSize(self, event):
        self.Layout()
 
    def Update(self, event):
        self.curframe += 1
        self.statusbar.SetStatusText("Frame %i" % self.curframe, 2)
 
    def OnScroll(self, event):
        self.display.linespacing = self.slider.GetValue()
   
    def ButtonClick(self, event):
        # (Commented code replaces the main display with the 'foooool!' display)
        #self.sizer.Detach(self.display)
        #self.display.Destroy()
        #self.display = FoolDisplay(self, -1)
        #self.sizer.Add(self.display, 1, flag = wx.EXPAND)
        #self.Layout()
       
        newframe = FoolFrame(self)
        newframe.Show()
       
        self.button.SetLabel("YOU WERE WARNED!")
        self.Layout()
 
class App(wx.App):
    def __init__(self, redirect=False, filename=None):
        print "App __init__"
        wx.App.__init__(self, redirect, filename)
    def OnInit(self):
        self.frame = Frame(parent = None)
        self.frame.Show()
        self.SetTopWindow(self.frame)
       
        return True
 
if __name__ == "__main__":
    app = App()
    app.MainLoop()

