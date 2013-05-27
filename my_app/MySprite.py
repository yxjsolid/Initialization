import cStringIO, base64
import pygame
from pygame.locals import *
from math import pi
from PIL import Image
# from MyMiddleWare import *
from MyGlobal import *
import MyMiddleWare


pygame.font.init()
try:
    regular_font_file = os.path.join(os.path.dirname(__file__), "Vera.ttf")
    bold_font_file = os.path.join(os.path.dirname(__file__), "VeraBd.ttf")

    # Check for cx_Freeze
    #
    if "frozen" in sys.__dict__.keys() and sys.frozen:

        regular_font_file = os.path.join(sys.path[1], "Vera.ttf")
        bold_font_file = os.path.join(sys.path[1], "VeraBd.ttf")

    BIG_FONT = pygame.font.Font(regular_font_file, 30)
    SMALL_FONT = pygame.font.Font(regular_font_file, 12)
    BOLD_FONT = pygame.font.Font(bold_font_file, 12)

except:
    # TODO: log used font: pygame.font.get_default_font()
    #print("Could not load {0}".format(os.path.join(os.path.dirname(__file__), "Vera.ttf")))
    BIG_FONT = pygame.font.Font(None, 40)
    SMALL_FONT = BOLD_FONT = pygame.font.Font(None, 20)
 

#help( SMALL_FONT)
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)
yellow = (255, 255, 0)
white = (255, 255, 255)


BLACK = (  0,   0,   0)
WHITE = (255, 255, 255)
BLUE =  (  0,   0, 255)
GREEN = (  0, 255,   0)
RED =   (255,   0,   0)




class specialSprite_transport(pygame.sprite.LayeredUpdates):
    def __init__(self, color, initial_position, width, height,speed, border):
        pygame.sprite.LayeredUpdates.__init__(self)
        self.initPos = initial_position
        self.width = width
        self.height = height
        self.color = color

        self.addComponent()
       

    def addComponent(self):

        x,y = self.initPos
        r = self.height/2
        center1 = (x+r, y+r)
        center2 = (x+self.width-r, y+r)

        print center1, center2

        rect = pygame.Rect(x + r, y, self.width - r*2, self.height)
        
        comp1 = AnimateMotorSprite("comp1",BLUE, center1, r, 1)
        comp2 = StaticRectSprite("comp2",red, rect)   
        comp3 = AnimateMotorSprite("comp3",WHITE, center2, r, 1)
        #comp4 = StaticLineSprite("comp4",WHITE, rect)    
        
        self.add(comp1,layer=2)
        self.add(comp2,layer=1)
        self.add(comp3,layer=2)
        #self.add(comp4,layer=2)   
       
  
        for item in  self.sprites():
            print item.name
        
        #self.move_to_front(comp1)
        #self.move_to_front(comp2)
        #self.move_to_front(comp3)


        print "comp1",self.get_layer_of_sprite(comp1)
        print "comp2",self.get_layer_of_sprite(comp2)
        print "comp3",self.get_layer_of_sprite(comp3)

        return
class StaticLineSprite(pygame.sprite.Sprite):
    def __init__(self, name, color, rect):
        pygame.sprite.Sprite.__init__(self)
        self.name = name
        self.rect = rect
        self.image = self.drawSelf(color, rect)
        self.imageOrig = self.image
        self.layer = 0

    def drawSelf(self, color, rect):        

        image = pygame.Surface((200, 200), pygame.SRCALPHA, 32)
        #pygame.draw.rect(image,color, netRect,0)

        rect = pygame.draw.line(image, color, (0,0), (200,200), 10)
        
        image = drawBoader(image, rect)

        return image


  
class mySelfTestSprite(pygame.sprite.Sprite):
    def __init__(self, color, initial_position, speed, border):
        pygame.sprite.Sprite.__init__(self)
       
        #self.image = self.drawMyPic(color)

        R = 1000
        self.image = self.drawMyPic()
        self.imageOrig = self.image
        self.lastUpdate = 0
        self.angle = 0
        #self.image.fill(WHITE)

        #self.drawMyPic(self.image)
        #self.rect = pygame.Rect(0,0,R,R)
        self.rect = self.image.get_rect()
        self.rect.topleft = (300,300)
        print "self.rect", self.rect
        self.rectOrig = self.rect

    def update(self, current_time):
        
        if current_time - self.lastUpdate > 50:
            self.lastUpdate = current_time
        else:
            return
         
        #print "update"

        self.angle += 10 

        if self.angle > 360:
            self.angel = 0
        
        center = self.rectOrig.center

        self.image = pygame.transform.rotate(self.imageOrig, self.angle)
        self.image = drawBoader(self.image, self.image.get_rect())

        self.rect = self.image.get_rect()
        self.rect.center = center

        #print center,self.rect.topleft

    def drawMyPic(self):

        r = 40
        w = 2*r

        rect = pygame.Rect(0,0,w,w)

        image = pygame.Surface((w,w), pygame.SRCALPHA, 32)


        x = rect.center[0]
        y = rect.center[1]
       
        p0 = [x,y]
        p1 = [x-r, y-r]
        p2 = [x, y-r]
        p3 = [x+r, y-r]
        p4 = [x+r, y]
        p5 = [x+r, y+r]
        p6 = [x, y+r]
        p7 = [x-r, y+r]
        p8 = [x-r, y]
  
        pygame.draw.circle(image, BLUE, p0, r)

        yellow = (255, 255, 0,0)
        pointlist = [p0 ,p2 ,p3 ]
        pygame.draw.polygon(image, yellow, pointlist, 0)

        pointlist = [p0 ,p1 ,p8 ]
        pygame.draw.polygon(image, yellow, pointlist, 0)

        pointlist = [p0 ,p7 ,p6 ]
        pygame.draw.polygon(image, yellow, pointlist, 0)

        pointlist = [p0 ,p4 ,p5 ]
        pygame.draw.polygon(image, yellow, pointlist, 0)
        
        pygame.draw.circle(image, BLUE, p0, r,2)
        #return image

        self.drawTextAtPos(image,rect)

        return image

        #pygame.Surface.blit(screen, image, rect)

        
    def drawTextAtPos(self, screen, rect):
        
        for index in range(1,5):

            if index is 1:
                centered_rect,fontsurf = self.drawSomeText(str(index))
                centered_rect.topleft = rect.topleft
            elif index is 2:
                centered_rect,fontsurf = self.drawSomeText(str(index))
                centered_rect.topright = rect.topright
            elif index is 3:
                centered_rect,fontsurf = self.drawSomeText(str(index))
                centered_rect.bottomright = rect.bottomright
            elif index is 4:
                centered_rect,fontsurf = self.drawSomeText(str(index))
                centered_rect.bottomleft = rect.bottomleft

            screen.blit(fontsurf, centered_rect)
    
    def drawSomeText(self, txt):
        fontsurf = SMALL_FONT.render(txt, True, (0, 0, 0), (255, 255, 0))
        centered_rect = fontsurf.get_rect()
        return centered_rect, fontsurf

    def drawOther(self, screen):
        screen.fill(WHITE)

# Draw on the screen a GREEN line from (0,0) to (50.75) 
# 5 pixels wide.
        pygame.draw.line(screen, GREEN, [0, 0], [50,30], 5)

# Draw on the screen a GREEN line from (0,0) to (50.75) 
# 5 pixels wide.
        pygame.draw.lines(screen, BLACK, False, [[0, 80], [50, 90], [200, 80], [220, 30]], 5)

# Draw on the screen a GREEN line from (0,0) to (50.75) 
# 5 pixels wide.
        pygame.draw.aaline(screen, GREEN, [0, 50],[50, 80], True)

# Draw a rectangle outline
        pygame.draw.rect(screen, BLACK, [75, 10, 50, 20], 2)

# Draw a solid rectangle
        pygame.draw.rect(screen, BLACK, [150, 10, 50, 20])

# Draw an ellipse outline, using a rectangle as the outside boundaries
        pygame.draw.ellipse(screen, RED, [225, 10, 50, 20], 2) 

# Draw an solid ellipse, using a rectangle as the outside boundaries
        pygame.draw.ellipse(screen, RED, [300, 10, 50, 20]) 

# This draws a triangle using the polygon command
        pygame.draw.polygon(screen, BLACK, [[100, 100], [0, 200], [200, 200]], 5)

# Draw an arc as part of an ellipse. 
# Use radians to determine what angle to draw.
        
        pygame.draw.rect(screen, BLACK, [210, 75, 150, 150])
        R = 2
        
        rect = pygame.Rect(210, 75, 150, 150)
        center = rect.center

        while R < 150:
            ww = 2
            R += ww

            newRect = pygame.Rect(0, 0, R, R)
            newRect.center = center
            pygame.draw.arc(screen, BLACK,newRect, 0, pi/2, 1)
            pygame.draw.arc(screen, GREEN,newRect, pi/2, pi, 1)
            pygame.draw.arc(screen, BLUE, newRect, pi,3*pi/2, 1)
            pygame.draw.arc(screen, RED,  newRect, 3*pi/2, 2*pi, 1)

# Draw a circle
        pygame.draw.circle(screen, BLUE, [60, 250], 40)

class Ball(pygame.sprite.Sprite):
    def __init__(self, color, initial_position):
        pygame.sprite.Sprite.__init__(self)
        ball_file = cStringIO.StringIO(base64.decodestring(
"""iVBORw0KGgoAAAANSUhEUgAAABkAAAAZCAYAAADE6YVjAAAAGXRFWHRTb2Z0d2FyZQBBZG9iZSBJ
bWFnZVJlYWR5ccllPAAABBJJREFUeNqsVj2PG1UUvfPp8XictXfHa+9mlyJCNEQRWiToqACJAgGC
LqJNlQZR0IFEj8RPSJkGGooUpEWJkGhR0tAAElI2tsfjjxnPjIdz7oyDF2wSUK72yN43793z7rkf
Y8N2HFmbbVliGIYiyzIpy1Isy3oHeMswzLOyXJ2tVit9VhTFAxz5Cfge+A7IZIcZmySObQudwIE0
veanraB1w/O8l5x6D9eXy6UkSaJYLBa6BvsNuAV8uY3sCQlvX4LANM0Xw/Dgdhj2Xm02m+K6LqPR
PXmeS5qmMp/PZTabyXQ6lclkosS1/QJcB+5vkthrAkoAuc4uHx//0B8MvCAIxG/5jEg0kpIkmcwX
icTxBIhlHWEURXoedgW4B3wIfHuBJM9yMQ3j5PTk5N7g6MjtdrrS3e9Ku90GUUvc2hkdMYJx5Ivn
NRC19UReRlRLR/sGeB34UUkMJBcJlcHg6K4SdDvS7/el1+tJp7MnQdCWRqMhDGWZLmWCCFog9rBm
GBYc50rOKON4uqkSC+IQSC3moeX7N09PX/i4AwLkAoQDxeFhHziU8CCUzt6e+EFLc2QaJi4mFQHy
kQLZMpME+WJF1sabdYA7Nq4jQbv9OZPs+75cgkSMYH9/X6PhJ9dpTLjruFLkBRyjACBd1BoLzzY8
T3O0IRntJvCZDXsTTnq262CzrzmgRHu4+QEIQhAxNzRWU1mTxfjOwvBIAOlIYNnWtja5bqM33mN/
sBEdx9bNPOQ1PWlqZJdAFKoMrEI6R+9gj6t7cUl1zjKnjFvsfaybr1Uqlv94ypXSKCud+aefpezs
7O3LL9s4c5U65gCrhGDDpUkqyWIuU1STweNlJRe7nAlmA+ZaVbnmiD4KFNEWC+3VqjB5YImDdMA+
YKONx2OVgxefojRL8CzmCxkOhxLhWYy+mGIvz6RKmv096X91PErP4Byazapbs3vZB45bVQqTzBzQ
kjQBQSTnjx7JcDTCRSLkKNY9SbKACsttHKZdrIqHILnGCNhoDU0qG83U5mNUVTOKShRPYo3m8fAc
nT/S/3mWFy2KrXKNOFbuI+Rr1FvLsB731Ho2m2pU7I1Sx8pSHTLaESIZjob6nfso2w77mSR3IMsN
zh4mmLOIBAkO6fjAgESdV1MYiV4kiUZHRDjD3E0Qza580D+rjsUdAQEj4fRl8wUkqBttPeo5RlJI
uB71jIASc8D+i4W8IoX8CviC5cuI+JlgpLsgcF1ng6RQyaoX1oWX1i67DTxe9w+9/EHW9VOrngCW
ZfNFpmvVWOfUzZ/mfG0HwHBz4ZV1kz8nvLuL+YPnRPDJ00J8A/j9fzrnW+sjeUbjbP8amDyj86z+
tXL5PwzOC4njj4K3gavA8cazczYacLd+p/+6y8mfAgwAsRuLfp/zVLMAAAAASUVORK5CYII="""))

#        screen = pygame.display.set_mode([350, 350])
        
        image = pygame.image.load(ball_file, 'file')



        print "aaaaaaaaaaaaaaa", image
        
        print image.get_size()


        self.imagestr = pygame.image.tostring(image, "RGBA")
        

        self.image = pygame.image.fromstring(self.imagestr, (25, 25), "RGBA")


        #self.image = pygame.image.load(ball_file, 'file').convert_alpha()
       # 
        #print self.image

        self.rect = self.image.fill(color, None, BLEND_ADD)
        self.rect.topleft = initial_position

        print "self.rect", self.rect
       


class MoveBall(Ball):
    def __init__(self, color, initial_position, speed, border):
        super(MoveBall, self).__init__(color, initial_position)
        self.speed = speed
        self.border = border
        self.update_time = 0
        
 
    def update(self, current_time):
        #print "update"
        if self.update_time < current_time:
            if self.rect.left < 0 or self.rect.left > self.border[0] - self.rect.w:
                self.speed[0] *= -1
            if self.rect.top < 0 or self.rect.top > self.border[1] - self.rect.h:
                self.speed[1] *= -1
 
            self.rect.x, self.rect.y = self.rect.x + self.speed[0], self.rect.y + self.speed[1]
            self.update_time = current_time + 10



class test_Drag_Sprite(pygame.sprite.Sprite):
    def __init__(self, color, initial_position, speed, border):
        pygame.sprite.Sprite.__init__(self)
        ball_file = cStringIO.StringIO(base64.decodestring(
"""iVBORw0KGgoAAAANSUhEUgAAABkAAAAZCAYAAADE6YVjAAAAGXRFWHRTb2Z0d2FyZQBBZG9iZSBJ
bWFnZVJlYWR5ccllPAAABBJJREFUeNqsVj2PG1UUvfPp8XictXfHa+9mlyJCNEQRWiToqACJAgGC
LqJNlQZR0IFEj8RPSJkGGooUpEWJkGhR0tAAElI2tsfjjxnPjIdz7oyDF2wSUK72yN43793z7rkf
Y8N2HFmbbVliGIYiyzIpy1Isy3oHeMswzLOyXJ2tVit9VhTFAxz5Cfge+A7IZIcZmySObQudwIE0
veanraB1w/O8l5x6D9eXy6UkSaJYLBa6BvsNuAV8uY3sCQlvX4LANM0Xw/Dgdhj2Xm02m+K6LqPR
PXmeS5qmMp/PZTabyXQ6lclkosS1/QJcB+5vkthrAkoAuc4uHx//0B8MvCAIxG/5jEg0kpIkmcwX
icTxBIhlHWEURXoedgW4B3wIfHuBJM9yMQ3j5PTk5N7g6MjtdrrS3e9Ku90GUUvc2hkdMYJx5Ivn
NRC19UReRlRLR/sGeB34UUkMJBcJlcHg6K4SdDvS7/el1+tJp7MnQdCWRqMhDGWZLmWCCFog9rBm
GBYc50rOKON4uqkSC+IQSC3moeX7N09PX/i4AwLkAoQDxeFhHziU8CCUzt6e+EFLc2QaJi4mFQHy
kQLZMpME+WJF1sabdYA7Nq4jQbv9OZPs+75cgkSMYH9/X6PhJ9dpTLjruFLkBRyjACBd1BoLzzY8
T3O0IRntJvCZDXsTTnq262CzrzmgRHu4+QEIQhAxNzRWU1mTxfjOwvBIAOlIYNnWtja5bqM33mN/
sBEdx9bNPOQ1PWlqZJdAFKoMrEI6R+9gj6t7cUl1zjKnjFvsfaybr1Uqlv94ypXSKCud+aefpezs
7O3LL9s4c5U65gCrhGDDpUkqyWIuU1STweNlJRe7nAlmA+ZaVbnmiD4KFNEWC+3VqjB5YImDdMA+
YKONx2OVgxefojRL8CzmCxkOhxLhWYy+mGIvz6RKmv096X91PErP4Byazapbs3vZB45bVQqTzBzQ
kjQBQSTnjx7JcDTCRSLkKNY9SbKACsttHKZdrIqHILnGCNhoDU0qG83U5mNUVTOKShRPYo3m8fAc
nT/S/3mWFy2KrXKNOFbuI+Rr1FvLsB731Ho2m2pU7I1Sx8pSHTLaESIZjob6nfso2w77mSR3IMsN
zh4mmLOIBAkO6fjAgESdV1MYiV4kiUZHRDjD3E0Qza580D+rjsUdAQEj4fRl8wUkqBttPeo5RlJI
uB71jIASc8D+i4W8IoX8CviC5cuI+JlgpLsgcF1ng6RQyaoX1oWX1i67DTxe9w+9/EHW9VOrngCW
ZfNFpmvVWOfUzZ/mfG0HwHBz4ZV1kz8nvLuL+YPnRPDJ00J8A/j9fzrnW+sjeUbjbP8amDyj86z+
tXL5PwzOC4njj4K3gavA8cazczYacLd+p/+6y8mfAgwAsRuLfp/zVLMAAAAASUVORK5CYII="""))


        #image = pygame.image.load(ball_file, 'file')
        image = pygame.image.load(image_fish)
        self.imagestr = pygame.image.tostring(image, "RGBA")

        x,y = image.get_size()
        self.image = pygame.image.fromstring(self.imagestr,(x,y) , "RGBA")

        #self.image = pygame.image.fromstring(self.imagestr, (25, 25), "RGBA")
        self.rect = self.image.fill(color, None, BLEND_ADD)
        self.rect.topleft = initial_position
        self.is_select = 0
        self.lastPos = 0

        self.imageOrig = self.image
        self.rectOrig = self.rect

    def setLastPos(self, pos):
        self.lastPos = pos

    def move(self, pos):
        dx = pos[0] - self.lastPos[0]
        dy = pos[1] - self.lastPos[1]
        self.lastPos = pos
        center = (self.rect.center[0] + dx, self.rect.center[1] + dy)      
        self.rect.center = center

        return

    def setSelect(self, is_select):
       # print self.image.get_rect() 
        pad = 8
        center = self.rect.center

        if is_select:
            if not self.is_select:
                self.is_select = 1
                W,H = (self.rect.width, self.rect.height)
                W += pad
                H += pad
                self.image = pygame.Surface((W,H), pygame.SRCALPHA, 32)
                yellow = (255, 255, 0)
                
                pygame.draw.rect(self.image, yellow, (0,0,W-1,H-1), 2)
                pygame.Surface.blit(self.image, self.imageOrig, (pad/2,pad/2,W-pad,H-pad))

                self.rect =  pygame.Rect(0,0,W,H)
                self.rect.center = center

        else:
            self.is_select = 0
            self.recovery()
            


    def recovery(self):
        self.image = self.imageOrig
        center = self.rect.center
        self.rect = self.rectOrig
        self.rect.center = center

    def update(self, current_time):

        return
        #print "update"
        if self.update_time < current_time:
            if self.rect.left < 0 or self.rect.left > self.border[0] - self.rect.w:
                self.speed[0] *= -1
            if self.rect.top < 0 or self.rect.top > self.border[1] - self.rect.h:
                self.speed[1] *= -1
 
            self.rect.x, self.rect.y = self.rect.x + self.speed[0], self.rect.y + self.speed[1]
            self.update_time = current_time + 10




class Sprite_Button(test_Drag_Sprite):
    def __init__(self, color, initial_position, speed, border):
        test_Drag_Sprite.__init__(self, color, initial_position, speed, border)
        self.imageResource = []

        self.loadImgResource(btn_red_up)
        self.loadImgResource(btn_red_down)
        self.setCurrentResource(0)

    def loadImgResource(self, file):
        image_file = pygame.image.load(file)
        imagedata = pygame.image.tostring(image_file, "RGBA")
        imageSurface = pygame.image.fromstring(imagedata, image_file.get_size() , "RGBA")
        #imageS1.fill(color, None, BLEND_ADD)
        
        self.imageResource.append(imageSurface)

    def setCurrentResource(self, index):
        self.imageOrig = self.imageResource[index]
        self.image = self.imageOrig
        self.rect = self.image.get_rect()
        self.rectOrig = self.rect


    def switchResource(self, index):
        self.setCurrentResource(index)


class Sprite_Animate(test_Drag_Sprite):
    def __init__(self, color, initial_position, speed, border):
        test_Drag_Sprite.__init__(self, color, initial_position, speed, border)
        self.imageResource = []
        self.resouceIndex = 0
        #self.loadImgResource(image_btn1)
        #self.loadImgResource(image_btn2)
        self.loadImgResource(image_device1)
        self.loadImgResource(image_device2)
        self.setCurrentResource(0)
        self.lastUpdate = 0

    def saveFile(self,image,file):

        rect = image.get_rect()

        W = 1640
        H = 360
        newrect = pygame.Rect((0,0,W, H))
        x = rect.center[0]
        y = rect.center[1]

        newrect.center = (x+60, y-40)
        print "rect", rect

 
        newfile = image.subsurface(image.get_rect())

        black = (0, 0, 0)
        yellow = (255, 255, 0)
        #W,H = (self.rect.width, self.rect.height)        

        width = image.get_width()
        hight = image.get_height()


        pygame.draw.aaline(newfile, black, (0,0), (width,hight))
        pygame.draw.aaline(newfile, black, (width,0), (0,hight))
        #pygame.draw.rect(newfile, yellow, (0,0,W,H), 2)
            


        #pygame.image.save(newfile, file)

    def loadImgResource(self, file):
        image_file = pygame.image.load(file)
        imagedata = pygame.image.tostring(image_file, "RGBA")
        imageSurface = pygame.image.fromstring(imagedata, image_file.get_size() , "RGBA")
        #imageS1.fill(color, None, BLEND_ADD)

        print file, image_file.get_size()
            
        
        self.saveFile(imageSurface, file+"1.png")
        self.imageResource.append(imageSurface)

    def setCurrentResource(self, index):
        self.imageOrig = self.imageResource[index]
        self.image = self.imageOrig
        self.rect = self.image.get_rect()
        self.rectOrig = self.rect


    def switchResource(self, index):
        self.setCurrentResource(index)

    def update(self, current_time):
        
        if current_time - self.lastUpdate > 500:
            self.lastUpdate = current_time
        else:
            return


        if self.resouceIndex < len(self.imageResource) - 1:
            self.resouceIndex += 1
        else:
            self.resouceIndex = 0
        #print "index", self.resouceIndex
        self.switchResource(self.resouceIndex)
        
"""
##############################################################################################################################
##############################################################################################################################
##############################################################################################################################
##############################################################################################################################
##############################################################################################################################
##############################################################################################################################
##############################################################################################################################
##############################################################################################################################
##############################################################################################################################
##############################################################################################################################
##############################################################################################################################
##############################################################################################################################
##############################################################################################################################
##############################################################################################################################
##############################################################################################################################
"""

class __MouseMixin:

    def onLeftUp(self, event):
        print "onLeftUp"
        pass

    def onLeftDown(self, event):
        print "onLeftDown"
        pass

    def onLeftDClick(self, event):
        print "onLeftDClick"
        pass

    def onRightUp(self, event):
        print "onRightUp"
        pass

    def onRightDown(self, event):
        print "onRightDown"
        pass

    def onDragging(self, event):
        print "onDragging"
        pass

    def onMouseEnter(self, event):
        print "onMouseEnter"
        pass

    def OnMouseHandler(self, event):
        #print "OnMouseHandler"
        event.Skip()

        if event.LeftUp():
            self.onLeftUp(event)
        elif event.LeftDown():
            self.onLeftDown(event)
        elif event.LeftDClick():
            self.onLeftDClick(event)
        elif event.RightUp():
            self.onRightUp(event)
        elif event.RightDown():
            self.onRightDown(event)
        elif event.Dragging() and event.LeftIsDown():
            self.onDragging(event)

        pass


class DragSprite(__MouseMixin, pygame.sprite.Sprite):
    def __init__(self, parent=None):
        pygame.sprite.Sprite.__init__(self)
        self.is_select = 0
        self.lastPos = 0
        self.lastUpdate = 0
        self.parent = parent

    def setLastPos(self, pos):
        self.lastPos = pos

    def move(self, pos):
        dx = pos[0] - self.lastPos[0]
        dy = pos[1] - self.lastPos[1]
        self.lastPos = pos
        center = (self.rect.center[0] + dx, self.rect.center[1] + dy)      
        self.rect.center = center

        return

    def isSelected(self):
        return self.is_select

    def setSelect(self, is_select):

        self.is_select = is_select
        return
         
        pad = 8
        center = self.rect.center

        if is_select:
            if not self.is_select:
                self.is_select = 1
                W,H = (self.rect.width, self.rect.height)
                W += pad
                H += pad
                self.image = pygame.Surface((W,H), pygame.SRCALPHA, 32)
                yellow = (255, 255, 0)
                
                pygame.draw.rect(self.image, yellow, (0,0,W-1,H-1), 2)
                pygame.Surface.blit(self.image, self.imageOrig, (pad/2,pad/2,W-pad,H-pad))

                self.rect =  pygame.Rect(0,0,W,H)
                self.rect.center = center
        else:
            self.is_select = 0
            self.recovery()
           
    def recovery(self):
        self.image = self.imageOrig.copy()
        center = self.rect.center
        self.rect = self.rectOrig.copy()

    def update(self, current_time):
        return
   
def drawBoader(image, rect):
    #rect = image.get_rect()
    pad = 2
    W,H = (rect.width, rect.height)
    W += pad
    H += pad
    newimage = pygame.Surface((W,H), pygame.SRCALPHA, 32)
    yellow = (255, 255, 0)

    pygame.draw.rect(newimage, yellow, (0,0,W-1,H-1), 2)
    pygame.Surface.blit(newimage, image, (pad/2,pad/2,W-pad,H-pad))

    return newimage

def drawBoader1(image, rect):
    W,H = (rect.width, rect.height)
    yellow = (255, 255, 0)
    pygame.draw.rect(image, yellow, (0,0,W-2,H-2), 2)

def drawSomeTextAt(screen, pos, txt, color):
    fontsurf = SMALL_FONT.render(txt, True, (0, 0, 0), color)
    centered_rect = fontsurf.get_rect()
    centered_rect.center = pos
    screen.blit(fontsurf, centered_rect)

    return centered_rect, fontsurf

class StaticRectSprite(pygame.sprite.Sprite):
    def __init__(self, name, color, rect):
        pygame.sprite.Sprite.__init__(self)
        self.name = name
        self.rect = rect
        self.image = self.drawSelf(color, rect)
        self.imageOrig = self.image
        self.layer = 0

    def drawSelf(self, color, rect):
        #print "drawSelf", rect, rect.x, rect.y
        
        netRect = pygame.Rect(rect)
        netRect.topleft = (0,0)
        image = pygame.Surface((rect.w, rect.h), pygame.SRCALPHA, 32)
        #image.fill((255,0,0,0), netRect)

        startP = (netRect.topleft[0],netRect.topleft[1])
        endP = (netRect.topright[0], netRect.topright[1])
        pygame.draw.line(image, color, startP, endP, 2)
       # pygame.draw.aaline(image, color, startP, endP, 1)
        
        netRect = netRect.inflate(-2,-2)
        netRect.topleft = (0,0)
        startP = (netRect.bottomleft[0],netRect.bottomleft[1])
        endP = (netRect.bottomright[0],netRect.bottomright[1])
        pygame.draw.line(image, color, startP, endP, 2)
        #pygame.draw.aaline(image, color, startP, endP, 1)
        return image


class AnimateMotorSprite(pygame.sprite.Sprite):
    def __init__(self, name, color, center, R, speed):
        pygame.sprite.Sprite.__init__(self)
        self.name = name
        self.color = color
        self.center = center
        self.R = R

        self.image = self.drawSelf(R, center, color)
        self.imageOrig = self.image
        self.lastUpdate = 0
        self.angle = 0

        self.rect = self.image.get_rect()
        self.rect.center = center
        #print "self.rect", self.rect
        self.rectOrig = self.rect
        self.layer = 0

    def update(self, current_time):
        if current_time - self.lastUpdate > 50:
            self.lastUpdate = current_time
        else:
            return
         
        #print "update"
        self.angle += 20
        if self.angle > 360:
            self.angel = 0
        
        center = self.rectOrig.center
        self.image = pygame.transform.rotate(self.imageOrig, self.angle)
        #self.image = drawBoader(self.image)

        self.rect = self.image.get_rect()
        self.rect.center = center
        return self.rect
        #print center,self.rect.topleft

    def drawSelf(self, r, center, color):

        w = 2*r
        rect = pygame.Rect(0,0,w,w)
        image = pygame.Surface((w,w), pygame.SRCALPHA, 32)

        x = rect.center[0]
        y = rect.center[1]
       
        p0 = [x,y]
        p1 = [x-r, y-r]
        p2 = [x, y-r]
        p3 = [x+r, y-r]
        p4 = [x+r, y]
        p5 = [x+r, y+r]
        p6 = [x, y+r]
        p7 = [x-r, y+r]
        p8 = [x-r, y]

        pygame.draw.circle(image, color, p0, r)

        maskColor = (0, 0, 0, 0)
        pointlist = [p0 ,p2 ,p3 ]
        pygame.draw.polygon(image, maskColor, pointlist, 0)

        pointlist = [p0 ,p1 ,p8 ]
        pygame.draw.polygon(image, maskColor, pointlist, 0)

        pointlist = [p0 ,p7 ,p6 ]
        pygame.draw.polygon(image, maskColor, pointlist, 0)

        pointlist = [p0 ,p4 ,p5 ]
        pygame.draw.polygon(image, maskColor, pointlist, 0)
        
        pygame.draw.circle(image, WHITE, p0, r,2)
        #self.drawTextAtPos(image,rect,color)
        return image

    def drawTextAtPos(self, screen, rect, color):
        
        for index in range(1,5):
            if index is 1:
                centered_rect,fontsurf = self.drawSomeText(str(index),color)
                centered_rect.topleft = rect.topleft
            elif index is 2:
                centered_rect,fontsurf = self.drawSomeText(str(index),color)
                centered_rect.topright = rect.topright
            elif index is 3:
                centered_rect,fontsurf = self.drawSomeText(str(index),color)
                centered_rect.bottomright = rect.bottomright
            elif index is 4:
                centered_rect,fontsurf = self.drawSomeText(str(index),color)
                centered_rect.bottomleft = rect.bottomleft

            screen.blit(fontsurf, centered_rect)
    
    def drawSomeText(self, txt, color):
        fontsurf = SMALL_FONT.render(txt, True, (0, 0, 0), color)
        centered_rect = fontsurf.get_rect()
        return centered_rect, fontsurf


#class AnimateTansporterSprite(pygame.sprite.Sprite):
class AnimateTansporterSprite(DragSprite):
   # def __init__(self, color, initPos, width, height, updateInterval, border):
    def __init__(self, color=(0,0,0), initPos=(0,0), width=0, height=0, updateInterval=0, border=0):
        #pygame.sprite.Sprite.__init__(self)
        DragSprite.__init__(self)

        self.pad = 8
        self.initPos = (initPos[0] ,initPos[1])
        self.width = width 
        self.height = height
        self.color = color
        self.components = []
        self.imageOrig = pygame.Surface((width + self.pad*2, height + self.pad*2), pygame.SRCALPHA, 32)
        self.rect = pygame.Rect(initPos, (width + self.pad*2, height + self.pad*2))

        #self.imageOrig.fill((0,0,0,0), self.rect)

        self.addComponent()
        self.index = 0
        self.rectOrig = self.rect
        self.angle = 0
        self.updateInterval = updateInterval
        self.isActive = 0
        self.drawSelf(0)

    def addComponent(self):
        pad = self.pad
        x,y = (pad, pad)
        width = self.width - pad*2
        height = self.height - pad*2
        width = self.width 
        height = self.height 

        r = height/2
        center1 = (x+r, y+r)
        center2 = (x+width-r, y+r)

        rect = pygame.Rect(x + r, y, width - r*2, height)
        
        comp1 = AnimateMotorSprite("comp1", BLUE, center1, r, 1)
        comp2 = StaticRectSprite("comp2", WHITE, rect)
        comp3 = AnimateMotorSprite("comp3", BLUE, center2, r, 1)
        #comp4 = StaticLineSprite("comp4",WHITE, rect)
       
        self.components.append(comp2)
        self.components.append(comp1)
        self.components.append(comp3)

        return
    
    def setSelect(self, is_select):
        DragSprite.setSelect(self,is_select)
        
        if is_select:
            self.isActive = 0
        else:
            self.isActive = 1    

    def drawSelf(self, current_time):
        self.image = self.imageOrig.copy()
        
        center = self.rect.center        
        for compent in self.components:
            compent.update(current_time)
            self.image.blit(compent.image, compent.rect)        
     

    def animate(self,current_time):

        return
        if self.isActive and current_time - self.lastUpdate > self.updateInterval:
            self.lastUpdate = current_time
            self.angle += 15
        self.image = pygame.transform.rotate(self.image, self.angle)

    def update(self, current_time):

        center = self.rect.center
        self.drawSelf(current_time)    
        self.animate(current_time)

        rect = self.image.get_rect()
        if self.isSelected():
            drawBoader1(self.image, rect)
        
        self.rect = rect
        self.rect.center = center


class SwitchButtonSprite(DragSprite):
    def __init__(self, color, initPos, width, height,speed, border):
        DragSprite.__init__(self)
        self.imageResource = []
        self.status = 0
        self.index = 0

        self.initPos = (initPos[0],initPos[1])
        self.width = width
        self.height = height
        self.rect = pygame.Rect(initPos, (width, height))
        self.loadImgResource(circle_btn_on)
        self.loadImgResource(circle_btn_off)
        self.setCurrentResource(0)

    def loadImgResource1(self, file):
        """
            load image with PIL lib
        """
        im = Image.open(file)
        im = im.resize((self.width, self.height))

        imagedata = im.convert('RGBA').tostring()
        imagesize = im.size

        imageSurface = pygame.image.fromstring(imagedata, imagesize , "RGBA")
        self.imageResource.append(imageSurface)

    def loadImgResource(self, file):
        """
            load image with pygame lib
        """
        image_file = pygame.image.load(file)
        imagedata = pygame.image.tostring(image_file, "RGBA")
        imagesize = image_file.get_size()

        imageSurface = pygame.image.fromstring(imagedata, imagesize , "RGBA")
        #imageS1.fill(color, None, BLEND_ADD)
        imageSurface = pygame.transform.smoothscale(imageSurface,(self.width, self.height))
        self.imageResource.append(imageSurface)

    def setCurrentResource(self, index):
        self.imageOrig = self.imageResource[index]
        self.image = self.imageOrig.copy()
        #self.rect = self.image.get_rect()
        #self.rectOrig = self.rect

    def switchResource(self, index):
        self.setCurrentResource(index)

    def update(self, current_time):
        return
        if current_time - self.lastUpdate > 500:
            self.lastUpdate = current_time
            self.status = ~(self.status)
            self.switchResource(self.status)

        if self.isSelected():
            drawBoader1(self.image, self.image.get_rect())


class ButtonSprite(DragSprite):
        def __init__(self, parent=None, initPos=(0,0), width=25, height=50, dicts=None):
            DragSprite.__init__(self, parent)
            self.imageResource = {}
            self.status = 0
            self.index = 0

            self.initPos = (initPos[0],initPos[1])
            self.width = width
            self.height = height
            self.rectOrig = pygame.Rect(initPos, (width, height))
            self.rect = self.rectOrig.copy()

            self.operationOn = None
            self.operationOff = None

            self.operationDic = {"on":self.getOperationOnItem, "off":self.getOperationOffItem}


            for dic in dicts:
                self.loadImgResource(dic)

            self.setCurrentResource("off")

        def getOperationOnItem(self):
            return self.operationOn

        def getOperationOffItem(self):
            return self.operationOff

        def loadImgResource1(self, file):
            """
                load image with PIL lib
            """
            im = Image.open(file)
            im = im.resize((self.width, self.height))
            imagedata = im.convert('RGBA').tostring()
            imagesize = im.size
            imageSurface = pygame.image.fromstring(imagedata, imagesize , "RGBA")

        def loadImgResource2(self, dicKey, file):
            """
                load image with pygame lib
            """
            image_file = pygame.image.load(file)
            imagedata = pygame.image.tostring(image_file, "RGBA")
            imagesize = image_file.get_size()
            imageSurface = pygame.image.fromstring(imagedata, imagesize , "RGBA")
            #imageS1.fill(color, None, BLEND_ADD)
            #imageSurface = pygame.transform.smoothscale(imageSurface,(self.width, self.height))
            #self.imageResource.append(imageSurface)
            self.imageResource[dicKey] = imageSurface

        def loadImgResource(self, dict):
            """
                load image with pygame lib
            """
            key = dict[0]
            file_name = dict[1]

            image_file = pygame.image.load(file_name)
            imagedata = pygame.image.tostring(image_file, "RGBA")
            imagesize = image_file.get_size()
            imageSurface = pygame.image.fromstring(imagedata, imagesize , "RGBA")

            #x = max(imagesize[0], imagesize[1])
            #newImg = pygame.Rect((0,0), (x, x))
            #imageS1.fill(color, None, BLEND_ADD)
            #imageSurface = pygame.transform.smoothscale(imageSurface,(self.width, self.height))
            #self.imageResource.append(imageSurface)
            self.imageResource[key] = (file_name, imageSurface)

        def resizeResource(self, src, size):
            return pygame.transform.smoothscale(src, size)

        def setCurrentResource(self, status):
            self.currentStatus = status

            self.imageOrig = self.resizeResource(self.imageResource[status][1], (self.width, self.height))
            self.image = self.imageOrig.copy()
           # self.rect = self.image.get_rect().copy()

        def switchResource(self, index):
            self.setCurrentResource(index)

        def update(self, current_time):
            # return
            # if current_time - self.lastUpdate > 500:
            #     self.lastUpdate = current_time
            #     self.status = ~(self.status)
            #     self.switchResource(self.status)

            if self.isSelected():
                # print "buttonSprite selected"
                drawBoader1(self.image, self.image.get_rect())
            else:
                self.image = self.imageOrig.copy()

        def onRightUp(self, event):
            print "onRightUp"
            self.PopupButtonSetupMenu()
            event.Skip(False)
            pass

        def PopupButtonSetupMenu(self):
            menu = wx.Menu()
            self.popupID = wx.NewId()
            menu.Append(self.popupID, MENU_ITEM_BUTTON_SETTING)
            menu.Bind(wx.EVT_MENU, self.onBeginButtonSetting, id=self.popupID)

            # wx.EVT_MENU_RANGE(self, DIVISION_MENU_SPLIT_HORIZONTALLY, DIVISION_MENU_EDIT_BOTTOM_EDGE, self.OnMenu)
            self.parent.PopupMenu(menu)

        def onBeginButtonSetting(self, event):
            print "onButtonSetting"
            window = MyPopupWindow(self.parent, size=wx.DefaultSize, title="setting")

            MyMiddleWare.Panel_ButtonSetting(window.frame, self.onButtonSettingDone)
            window.windowPopup()

        def onButtonSettingDone(self, operOn, operOff):
            self.operationOn = operOn
            self.operationOff = operOff
            return

        def onProcessOperation(self):
            getOpItemFn = self.operationDic[self.currentStatus]

            opItem = getOpItemFn()
            if opItem:
                opItem.processOperation()

        def onLeftDClick(self, event):

            if self.currentStatus == "on":
                self.setCurrentResource("off")
            elif self.currentStatus == "off":
                self.setCurrentResource("on")

            self.onProcessOperation()
            return