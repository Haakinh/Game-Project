import pygame
import random
import keyboard
import math
import time

pygame.init()
clock = pygame.time.Clock()
infoObject = pygame.display.Info()
screen = pygame.display.set_mode((1080, 300))
# variables
pygame.key.set_repeat(0, 0)
Red = 255, 0, 0
LightGray = 105, 105, 105
Black = 0, 0, 0
DarkGray = 55, 55, 55
LighterGray = 155, 155, 155
Green = 0, 255, 0
Yellow = 255, 255, 0
Blue = 0, 0, 255
dashMulti = 5
dashVel = 20
cooldown1 = 0
cooldown2 = 0
cooldown3 = 0
yvel = 0
y2vel = 0
xvel = 0
x2vel = 0
movement1 = 4
movement2 = 2
movement3 = -5
increment1 = 0.2
increment2 = -0.2
increment3 = 0.2
circletest = 0
setup = 1
setup2 = 1
radius1 = 90
radius2 = 60
angle1 = 0
angle2 = 0
angle3 = 0
levelinc = 1
death = 0
playermovey = 2
playery = 120
playerx = 120
playermovex = 2
creatory = 160
creatorx = 160
rectcreate = 1
rect2create = 1
moverectcreate = 1
collrectcreate = True
keys2d = True
level = 10
coinscollected = 0
windvel = 0
offsetx = 0
offsety = 0
rightarrow = pygame.image.load("rightarrow.png")
rectimg = pygame.image.load("recttexture.png")
fallplatleftedge = pygame.image.load("platformtopleft.png")
fallplatrightedge = pygame.image.load("platformtopright.png")
fallplatmain = pygame.image.load("platformtopmid.png")
playerimg = pygame.image.load("player.png")
collideborderimg = pygame.image.load("colliderectborders.png")
scaledcenter = pygame.image.load("colliderectcenter.png")
coinimg = pygame.image.load("cointext.png")
rectoverlay = pygame.image.load("rectoverlay1-1.png")
arrowrect = pygame.Rect(0, 0, 20, 80)
leftboosters = []
rightboosters = []
upboosters = []
downboosters = []
colliderects = []
collected = False
coins = []
rectrectangles = []
rectrectangles2 = []
collrectrectangles = []
fallplatforms = []
wallplatforms = []
cocoins = []
coinsreq = 0
seed = time.time()
def boostercalc(self, xchange, ychange, fliph, flipv):
    global xvel
    global yvel
    if fliph == 0:
        if self.height % 20 == 0 and self.width > 10:
            arrowrect = pygame.Rect(0, 0, 20, 10)
            arrowimg = pygame.image.load("rightarrow1020.png")
            if self.height % 40 == 0 and self.width > 20:
                arrowrect = pygame.Rect(0, 0, 40, 20)
                arrowimg = pygame.image.load("rightarrow2040.png")
                if self.height % 80 == 0 and self.width > 40:
                    arrowrect = pygame.Rect(0, 0, 80, 40)
                    arrowimg = pygame.image.load("rightarrow.png")
    if fliph == 1:
        if self.width % 20 == 0 and self.height > 10:
            arrowrect = pygame.Rect(0, 0, 20, 10)
            arrowimg = pygame.image.load("rightarrow1020.png")
            if self.width % 40 == 0 and self.height > 20:
                arrowrect = pygame.Rect(0, 0, 40, 20)
                arrowimg = pygame.image.load("rightarrow2040.png")
                if self.width % 80 == 0 and self.height > 40:
                    arrowrect = pygame.Rect(0, 0, 80, 40)
                    arrowimg = pygame.image.load("rightarrow.png")
    if fliph == 1 and flipv == 1:
        arrowimg = pygame.transform.rotate(arrowimg, 90)
    if fliph == 1 and flipv == 0:
        arrowimg = pygame.transform.rotate(arrowimg, 180)
    if fliph == 0 and flipv == 1:
        arrowimg = pygame.transform.rotate(arrowimg, -90)
    if self.height >= arrowrect.height:
        arrowimgtemp = pygame.transform.scale(arrowimg, (arrowrect.width, arrowrect.height))
    if self.height < arrowrect.width:
        arrowimgtemp = pygame.transform.scale(arrowimg, (arrowrect.width, self.height*2))
    surface = pygame.Surface((self.width, self.height))
    surface.blit(arrowimgtemp, (0, 0))
    for x in range(self.left, self.right, arrowrect.width):
        for y in range(self.top, self.bottom, arrowrect.height):
            screen.blit(surface, (x, y))
    if pygame.Rect.colliderect(pygame.Rect(playerx, playery, 20, 20), self):
        xvel += xchange
        yvel += ychange
running = True
while running:
    rectangles = []
    rectanglestype2 = []
    colliderects = []
    fallplatforms = []
    wallplatforms = []
    killermovers = []
    winpos = []
    leftboosters = []
    rightboosters = []
    upboosters = []
    downboosters = []
    if level == 256:
        rectangles = []
        rectanglestype2 = []
        colliderects = []
        fallplatforms = []
        wallplatforms = []
        killermovers = []
        winpos = []
        leftboosters = []
        rightboosters = []
        upboosters = []
        downboosters = []
    if level == 0:
        if setup == 1:
            playerx = 350
            playery = 150
            setup = 0
            dash = 0
        screen.fill(Black)
        rectangles = [pygame.Rect(0, 0, 10, 300), pygame.Rect(0, 0, 1080, 10), pygame.Rect(1070, 0, 10, 300), pygame.Rect(0, 290, 1070, 10)]
        rectanglestype2 = []
        winpos = []
        pygame.draw.rect(screen, Green, pygame.Rect(100, 10, 50, 30))
        pygame.draw.rect(screen, Green, pygame.Rect(170, 10, 50, 30))
        pygame.draw.rect(screen, Green, pygame.Rect(240, 10, 50, 30))
        if pygame.Rect.colliderect(pygame.Rect(playerx, playery, 20, 20), pygame.Rect(100, 10, 50, 30)):
            level = 1
            screen.fill(Black)
            playerx = 120
            playery = 120
            cooldown3 = -40
            setup = 1
        if pygame.Rect.colliderect(pygame.Rect(playerx, playery, 20, 20), pygame.Rect(170, 10, 50, 30)):
            level = 2
            screen.fill(Black)
            playerx = 20
            playery = 20
            cooldown3 = -40
            setup = 1
        if pygame.Rect.colliderect(pygame.Rect(playerx, playery, 20, 20), pygame.Rect(240, 10, 50, 30)):
            level = 3
            screen.fill(Black)
            playerx = 50
            playery = 50
            cooldown3 = -40
            setup = 1
    if level == 1:
        if setup == 1:
            angle1 = 0
            playerx = 40
            playery = 200
            dash = 1
            setup = 0
            screen.fill(Black)
            coins.clear()
            coins = []
            setup = 0
        if playerx > 500 and playerx < 520 and xvel <= 5:
            setup = 1
        rectangles = [pygame.Rect(0, 0, 420, 170), pygame.Rect(0, 250, 420, 50), pygame.Rect(430, 0, 350, 170), pygame.Rect(430, 250, 350, 50),
                      pygame.Rect(790, 0, 290, 170), pygame.Rect(1020, 170, 60, 80), pygame.Rect(790, 250, 290, 50), ]
        rectanglestype2 = [pygame.Rect(20, 20, 10, 20), pygame.Rect(30, 40, 10, 20), pygame.Rect(40, 60, 10, 10), pygame.Rect(50, 40, 10, 20),
                           pygame.Rect(60, 20, 10, 20), pygame.Rect(70, 40, 10, 20), pygame.Rect(80, 60, 10, 10), pygame.Rect(90, 40, 10, 20), pygame.Rect(100, 20, 10, 20),
                           pygame.Rect(120, 60, 10, 10), pygame.Rect(120, 50, 10, 10), pygame.Rect(130, 30, 10, 20), pygame.Rect(140, 20, 10, 10),
                           pygame.Rect(150, 30, 10, 20), pygame.Rect(160, 50, 10, 20), pygame.Rect(130, 50, 30, 10), pygame.Rect(180, 30, 10, 10),
                           pygame.Rect(190, 40, 20, 10), pygame.Rect(210, 50, 10, 10), pygame.Rect(180, 60, 30, 10), pygame.Rect(190, 20, 30, 10),
                           pygame.Rect(230, 20, 10, 50), pygame.Rect(240, 20, 20, 10), pygame.Rect(260, 30, 10, 30), pygame.Rect(240, 60, 20, 10),
                           pygame.Rect(40, 80, 60, 10), pygame.Rect(60, 90, 10, 40), pygame.Rect(30, 80, 10, 10), pygame.Rect(110, 90, 10, 30),
                           pygame.Rect(120, 120, 20, 10), pygame.Rect(140, 90, 10, 30), pygame.Rect(120, 80, 20, 10), pygame.Rect(170, 80, 10, 50),
                           pygame.Rect(180, 80, 10, 10), pygame.Rect(190, 90, 10, 20), pygame.Rect(200, 110, 10, 20), pygame.Rect(210, 90, 10, 20),
                           pygame.Rect(220, 80, 20, 10), pygame.Rect(230, 90, 10, 40), pygame.Rect(250, 90, 10, 30), pygame.Rect(260, 120, 20, 10),
                           pygame.Rect(280, 90, 10, 30), pygame.Rect(260, 80, 20, 10), pygame.Rect(300, 80, 10, 20), pygame.Rect(310, 100, 10, 20),
                           pygame.Rect(320, 120, 10, 10), pygame.Rect(330, 100, 10, 20), pygame.Rect(340, 80, 10, 20), pygame.Rect(360, 80, 10, 50),
                           pygame.Rect(370, 120, 20, 10), pygame.Rect(370, 100, 20, 10), pygame.Rect(370, 80, 20, 10), pygame.Rect(440, 20, 10, 60),
                           pygame.Rect(450, 20, 10, 10), pygame.Rect(460, 30, 10, 40), pygame.Rect(450, 70, 10, 10), pygame.Rect(490, 20, 10, 10), pygame.Rect(480, 30, 10, 50),
                           pygame.Rect(500, 30, 10, 50), pygame.Rect(490, 50, 10, 10), pygame.Rect(530, 20, 20, 10), pygame.Rect(520, 30, 10, 10),
                           pygame.Rect(530, 40, 20, 10), pygame.Rect(550, 50, 10, 10), pygame.Rect(520, 60, 30, 10), pygame.Rect(570, 20, 10, 60),
                           pygame.Rect(580, 40, 20, 10), pygame.Rect(600, 20, 10, 60), pygame.Rect(630, 10, 10, 50), pygame.Rect(630, 70, 10, 10),
                           pygame.Rect(480, 170, 20, 80), pygame.Rect(510, 200, 30, 10), pygame.Rect(520, 180, 10, 10), pygame.Rect(530, 190, 10, 10),
                           pygame.Rect(540, 200, 10, 10), pygame.Rect(530, 210, 10, 10), pygame.Rect(520, 220, 10, 10), pygame.Rect(600, 170, 20, 80),
                           pygame.Rect(500, 100, 10, 50), pygame.Rect(510, 100, 30, 10), pygame.Rect(510, 120, 20, 10),
                           pygame.Rect(850, 40, 20, 20), pygame.Rect(850, 90, 20, 20), pygame.Rect(870, 110, 70, 20), pygame.Rect(940, 90, 20, 20),
                           pygame.Rect(940, 40, 20, 20), pygame.Rect(840, 200, 100, 20), pygame.Rect(900, 170, 10, 10), pygame.Rect(910, 180, 10, 10),
                           pygame.Rect(920, 190, 10, 10), pygame.Rect(920, 220, 10, 10), pygame.Rect(910, 230, 10, 10), pygame.Rect(900, 240, 10, 10),]
        winpos = [pygame.Rect(950, 170, 70, 80)]
    if level == 2:
        if setup == 1:
            playerx = 40
            playery = 250
            yvel = 0
            xvel = 0
            x2vel = 0
            y2vel = 0
            dash = 1
            coins.clear()
            coins = []
            rectoverlay = pygame.image.load('rectoverlay1-1.png')
        screen.fill(Black)
        setup = 0
        rectangles = [pygame.Rect(100, 0, 100, 120),
                      pygame.Rect(100, 150, 100, 150), pygame.Rect(290, 0, 200, 250), pygame.Rect(290, 280, 200, 20), pygame.Rect(490, 60, 70, 180), pygame.Rect(600, 60, 70, 180),
                      pygame.Rect(670, 0, 70, 300), pygame.Rect(700, 0, 470, 300)]
        rectanglestype2 = [pygame.Rect(290, 250, 200, 30)]
        killermovers = []
        winpos = [pygame.Rect(640, 0, 30, 60)]
        pygame.draw.rect(screen, Green, pygame.Rect(10, 10, 30, 10))
        if pygame.Rect.colliderect(pygame.Rect(playerx, playery, 20, 20), pygame.Rect(10, 10, 30, 10)):
            level = 0
            playerx = 350
            playery = 150
            cooldown3 = -40
            setup = 1
    if level == 3:
        if setup == 1:
            playerx = 20
            playery = 20
            setup = 0
            dash = 1
            coins.clear()
        screen.fill(Black)
        rectangles = [pygame.Rect(60, 0, 50, 180),
                      pygame.Rect(190, 170, 220, 130), pygame.Rect(410, 50, 90, 250), pygame.Rect(560, 0, 80, 160), pygame.Rect(500, 210, 140, 100),
                      pygame.Rect(630, 0, 50, 160), pygame.Rect(670, 110, 40, 50), pygame.Rect(630, 210, 230, 90), pygame.Rect(810, 110, 70, 235),
                      pygame.Rect(830, 70, 50, 230), pygame.Rect(880, 70, 190, 230), pygame.Rect(910, 0, 170, 300)]
        rectanglestype2 = [pygame.Rect(500, 50, 60, 105), pygame.Rect(560, 155, 75, 55)]
        killermovers = [pygame.Rect(75, (15 * movement1) + 230, 30, 30), pygame.Rect((-30 * movement1) + 240, 130, 40, 40), pygame.Rect((30 * movement1) + 240, 90, 40, 40),
                        pygame.Rect((-30 * movement1) + 240, 50, 40, 40), pygame.Rect((30 * movement1) + 240, 10, 40, 40),
                        pygame.Rect((740 + radius1 * math.cos(math.radians(angle1 + 20)), (40 + radius2 * math.sin(math.radians(angle1 + 20))), 40, 40)),
                        pygame.Rect((740 + radius1 * math.cos(math.radians(angle1 + 40)), (40 + radius2 * math.sin(math.radians(angle1 + 40))), 40, 40)),
                        pygame.Rect((740 + radius1 * math.cos(math.radians(angle1 + 60)), (40 + radius2 * math.sin(math.radians(angle1 + 60))), 40, 40)),
                        pygame.Rect((740 + radius1 * math.cos(math.radians(angle1 + 80)), (40 + radius2 * math.sin(math.radians(angle1 + 80))), 40, 40)),
                        pygame.Rect((740 + radius1 * math.cos(math.radians(angle1 + 100)), (40 + radius2 * math.sin(math.radians(angle1 + 100))), 40, 40))]
        winpos = [pygame.Rect(880, 10, 30, 60)]
    if level == 4:
        if setup == 1:
            playerx = 20
            playery = 200
            dash = 0
            setup = 0
            coins.clear()
            coins = [pygame.Rect(220, 200, 10, 10), pygame.Rect(260, 200, 10, 10), pygame.Rect(300, 200, 10, 10), pygame.Rect(340, 200, 10, 10),
                     pygame.Rect(380, 200, 10, 10), pygame.Rect(420, 200, 10, 10), pygame.Rect(460, 200, 10, 10), pygame.Rect(500, 200, 10, 10),]
        rectangles = [pygame.Rect(0, 280, 620, 20), pygame.Rect(0, 0, 620, 130), pygame.Rect(620, 0, 460, 300), ]
        rectanglestype2 = [pygame.Rect(90, 200, 50, 10), pygame.Rect(90, 180, 70, 20), pygame.Rect(90, 210, 70, 20), pygame.Rect(160, 220, 30, 10),
                           pygame.Rect(160, 180, 30, 10), pygame.Rect(100, 160, 110, 20), pygame.Rect(110, 150, 90, 10), pygame.Rect(130, 140, 50, 10),
                           pygame.Rect(100, 230, 90, 20), pygame.Rect(190, 230, 20, 20), pygame.Rect(110, 250, 90, 10), pygame.Rect(130, 260, 50, 10)]
        winpos = [pygame.Rect(530, 130, 90, 150),
]
    if level == 5:
        if setup == 1:
            playerx = 20
            playery = 20
            dash = 0
            setup = 0
            coins.clear()
            coins = [pygame.Rect(290, 30, 10, 10), pygame.Rect(390, 120, 10, 10), pygame.Rect(490, 260, 10, 10), pygame.Rect(750, 60, 10, 10),
                     pygame.Rect(750, 70, 10, 10), pygame.Rect(760, 70, 10, 10), pygame.Rect(760, 60, 10, 10), pygame.Rect(760, 150, 10, 10),
                     pygame.Rect(750, 150, 10, 10), pygame.Rect(750, 160, 10, 10), pygame.Rect(760, 160, 10, 10), pygame.Rect(760, 240, 10, 10),
                     pygame.Rect(750, 240, 10, 10), pygame.Rect(750, 250, 10, 10), pygame.Rect(760, 250, 10, 10)]
        screen.fill(Black)
        rectangles = [pygame.Rect(0, 50, 190, 40), pygame.Rect(230, 0, 40, 130), pygame.Rect(50, 130, 220, 120), pygame.Rect(0, 290, 270, 80),
                      pygame.Rect(310, 210, 60, 80), pygame.Rect(310, 100, 60, 80), pygame.Rect(310, 40, 150, 60), pygame.Rect(410, 140, 70, 110),
                      pygame.Rect(490, 40, 40, 60), pygame.Rect(520, 100, 60, 190), pygame.Rect(530, 40, 50, 60), pygame.Rect(630, 0, 50, 140),
                      pygame.Rect(630, 180, 50, 110), pygame.Rect(730, 90, 50, 50), pygame.Rect(730, 180, 50, 50), pygame.Rect(680, 0, 100, 50),
                      pygame.Rect(680, 270, 100, 20), pygame.Rect(780, 110, 100, 90), pygame.Rect(920, 50, 80, 80), pygame.Rect(780, 0, 220, 50),
                      pygame.Rect(920, 170, 80, 100), pygame.Rect(780, 270, 220, 20), pygame.Rect(850, 250, 70, 20), pygame.Rect(850, 50, 70, 20),
                      pygame.Rect(1000, 0, 70, 130), pygame.Rect(1000, 170, 70, 120)]
        rectanglestype2 = [pygame.Rect(270, 60, 40, 120), pygame.Rect(310, 180, 60, 30), pygame.Rect(330, 10, 120, 30), pygame.Rect(630, 140, 50, 40),
                           pygame.Rect(920, 130, 80, 40)]
        killermovers = [pygame.Rect(75, (30 * movement1) + 140, 30, 30), pygame.Rect(115, (30 * movement2) + 140, 30, 30), pygame.Rect(155, (30 * movement3) + 140, 30, 30),
                        pygame.Rect(-50 + (12 * movement1), 210, 30, 30), pygame.Rect(150 + (12 * movement1), 55, 30, 30)]
        winpos = [pygame.Rect(1000, 130, 70, 40)]
    if level == 6:
        if setup == 1:
            radius1 = 60
            radius2 = 120
            angle1 = 0
            playerx = 20
            playery = 20
            dash = 1
            setup = 0
            screen.fill(Black)
            coins.clear()
            coins = [pygame.Rect(10, 240, 10, 10), pygame.Rect(10, 250, 10, 10), pygame.Rect(20, 250, 10, 10), pygame.Rect(20, 240, 10, 10),
                     pygame.Rect(330, 130, 10, 10), pygame.Rect(330, 120, 10, 10), pygame.Rect(340, 120, 10, 10), pygame.Rect(340, 130, 10, 10),
                     pygame.Rect(900, 110, 10, 10), pygame.Rect(900, 120, 10, 10), pygame.Rect(910, 120, 10, 10), pygame.Rect(910, 110, 10, 10),
                     pygame.Rect(910, 130, 10, 10), pygame.Rect(900, 130, 10, 10), pygame.Rect(900, 140, 10, 10), pygame.Rect(910, 140, 10, 10)]
        rectangles = [pygame.Rect(0, 0, 10, 300), pygame.Rect(0, 0, 1080, 10), pygame.Rect(1070, 0, 10, 300), pygame.Rect(0, 290, 1070, 10),
                      pygame.Rect(60, 0, 40, 130), pygame.Rect(0, 170, 100, 30), pygame.Rect(50, 240, 50, 20), pygame.Rect(170, 130, 60, 170),
                      pygame.Rect(170, 100, 60, 30), pygame.Rect(100, 0, 130, 50), pygame.Rect(280, 50, 60, 50), pygame.Rect(300, 100, 20, 60),
                      pygame.Rect(280, 160, 60, 50), pygame.Rect(380, 180, 90, 110), pygame.Rect(230, 260, 240, 40), pygame.Rect(380, 0, 90, 80),
                      pygame.Rect(410, 110, 60, 30), pygame.Rect(390, 120, 30, 10), pygame.Rect(390, 130, 20, 10), pygame.Rect(410, 140, 60, 10),
                      pygame.Rect(470, 110, 50, 40), pygame.Rect(530, 190, 50, 40), pygame.Rect(530, 30, 50, 40), pygame.Rect(560, 70, 40, 120),
                      pygame.Rect(640, 0, 40, 40), pygame.Rect(640, 220, 40, 40), pygame.Rect(660, 150, 40, 70), pygame.Rect(660, 40, 40, 70),
                      pygame.Rect(470, 260, 240, 50), pygame.Rect(740, 60, 50, 130), pygame.Rect(730, 230, 70, 70), pygame.Rect(680, 220, 20, 40),
                      pygame.Rect(700, 230, 30, 70), pygame.Rect(680, 0, 120, 30), pygame.Rect(680, 30, 20, 10), pygame.Rect(800, 0, 130, 30),
                      pygame.Rect(840, 30, 40, 50), pygame.Rect(840, 120, 40, 20), pygame.Rect(840, 180, 40, 50), pygame.Rect(800, 230, 130, 70),
                      pygame.Rect(930, 170, 150, 130), pygame.Rect(930, 0, 150, 90), pygame.Rect(470, 10, 170, 30), pygame.Rect(470, 40, 190, 30),
                      pygame.Rect(470, 70, 190, 10)]
        rectanglestype2 = [pygame.Rect(660, 110, 40, 40)]
        killermovers = []
        winpos = [pygame.Rect(970, 90, 120, 80)]
    if level == 7:
        if setup == 1:
            radius1 = 60
            radius2 = 120
            angle1 = 0
            playerx = 20
            playery = 140
            dash = 1
            setup = 0
            screen.fill(Black)
            coins.clear()
            coins = []
        rectangles = [pygame.Rect(0, 0, 10, 300), pygame.Rect(0, 0, 1080, 10), pygame.Rect(1070, 0, 10, 300), pygame.Rect(0, 290, 1070, 10), pygame.Rect(0, 0, 410, 110),
                      pygame.Rect(0, 190, 400, 110), pygame.Rect(400, 190, 10, 110), pygame.Rect(410, 170, 160, 10), pygame.Rect(410, 180, 160, 120),
                      pygame.Rect(410, 0, 160, 130), pygame.Rect(570, 0, 510, 130), pygame.Rect(570, 170, 510, 130)]
        rectanglestype2 = [pygame.Rect(370, 10, 20, 80), pygame.Rect(390, 10, 20, 20), pygame.Rect(390, 70, 20, 20), pygame.Rect(410, 30, 20, 40),
                           pygame.Rect(440, 30, 20, 60), pygame.Rect(460, 10, 20, 20), pygame.Rect(480, 30, 20, 60), pygame.Rect(460, 50, 20, 20),
                           pygame.Rect(540, 10, 40, 20), pygame.Rect(520, 30, 20, 10), pygame.Rect(540, 40, 20, 20), pygame.Rect(560, 60, 20, 10),
                           pygame.Rect(540, 70, 20, 20), pygame.Rect(520, 70, 20, 20), pygame.Rect(600, 10, 20, 80), pygame.Rect(620, 40, 20, 20),
                           pygame.Rect(640, 10, 20, 80), pygame.Rect(680, 10, 20, 50), pygame.Rect(680, 70, 20, 20),]
        killermovers = []
        winpos = [pygame.Rect(600, 130, 60, 40)]
    if level == 8:
        if setup == 1:
            angle1 = 0
            playerx = 20
            playery = 100
            dash = 1
            setup = 0
            screen.fill(Black)
            coins.clear()
            coins = []
        rectangles = [pygame.Rect(0, 0, 10, 300), pygame.Rect(0, 0, 1080, 10), pygame.Rect(1070, 0, 10, 300), pygame.Rect(0, 290, 1070, 10),
                      pygame.Rect(0, 0, 80, 90), pygame.Rect(0, 130, 80, 170), pygame.Rect(80, 150, 10, 40), pygame.Rect(80, 190, 20, 40),
                      pygame.Rect(80, 230, 30, 40), pygame.Rect(80, 270, 40, 30), pygame.Rect(90, 180, 10, 10), pygame.Rect(100, 220, 10, 10),
                      pygame.Rect(110, 260, 10, 10), pygame.Rect(80, 0, 30, 90), pygame.Rect(110, 90, 10, 20), pygame.Rect(120, 110, 10, 30),
                      pygame.Rect(130, 140, 10, 30), pygame.Rect(140, 170, 10, 30), pygame.Rect(150, 200, 10, 20), pygame.Rect(150, 170, 20, 30),
                      pygame.Rect(140, 140, 40, 30), pygame.Rect(130, 110, 60, 30), pygame.Rect(120, 90, 80, 20), pygame.Rect(110, 10, 220, 80),
                      pygame.Rect(200, 260, 10, 30), pygame.Rect(210, 230, 10, 30), pygame.Rect(220, 200, 10, 30), pygame.Rect(230, 170, 10, 30),
                      pygame.Rect(240, 140, 20, 30), pygame.Rect(260, 140, 70, 30), pygame.Rect(210, 260, 110, 30), pygame.Rect(220, 230, 100, 30),
                      pygame.Rect(230, 200, 90, 30), pygame.Rect(240, 170, 80, 30), pygame.Rect(320, 150, 20, 140), pygame.Rect(340, 160, 10, 130),
                      pygame.Rect(350, 170, 10, 120), pygame.Rect(360, 180, 10, 110), pygame.Rect(370, 190, 10, 100), pygame.Rect(380, 200, 10, 90),
                      pygame.Rect(390, 210, 20, 80), pygame.Rect(410, 220, 30, 70), pygame.Rect(330, 10, 20, 90), pygame.Rect(350, 10, 10, 100),
                      pygame.Rect(360, 10, 20, 110), pygame.Rect(380, 10, 10, 120), pygame.Rect(390, 10, 20, 130), pygame.Rect(410, 10, 30, 140),
                      pygame.Rect(440, 10, 10, 140), pygame.Rect(460, 200, 20, 100), pygame.Rect(450, 10, 20, 130), pygame.Rect(470, 10, 10, 120),
                      pygame.Rect(480, 10, 20, 110), pygame.Rect(500, 10, 10, 100), pygame.Rect(480, 190, 10, 110), pygame.Rect(490, 180, 20, 120),
                      pygame.Rect(510, 170, 10, 130), pygame.Rect(240, 170, 80, 30), pygame.Rect(440, 210, 20, 80), pygame.Rect(510, 10, 460, 100),
                      pygame.Rect(520, 170, 450, 120), pygame.Rect(970, 10, 100, 100), pygame.Rect(970, 170, 100, 120)]
        rectanglestype2 = [pygame.Rect(260, 90, 10, 50)]
        killermovers = []
        winpos = [pygame.Rect(1020, 110, 50, 60)]
    if level == 9:
        if setup == 1:
            angle1 = 0
            playerx = 20
            playery = 100
            dash = 1
            setup = 0
            screen.fill(Black)
            coins.clear()
            coins = []
        rectangles = [pygame.Rect(0, 0, 10, 300), pygame.Rect(10, 290, 1070, 10), pygame.Rect(1070, 0, 10, 290), pygame.Rect(10, 0, 1060, 10),
                      pygame.Rect(90, 160, 150, 10), pygame.Rect(90, 120, 80, 40), pygame.Rect(90, 80, 40, 40), pygame.Rect(170, 10, 40, 40),
                      pygame.Rect(210, 10, 30, 80), pygame.Rect(90, 170, 150, 120), pygame.Rect(240, 180, 20, 110), pygame.Rect(260, 180, 50, 30),
                      pygame.Rect(310, 60, 10, 120), pygame.Rect(320, 150, 80, 10), pygame.Rect(320, 100, 40, 50), pygame.Rect(360, 10, 40, 20),
                      pygame.Rect(400, 10, 40, 60), pygame.Rect(440, 10, 20, 180), pygame.Rect(260, 210, 20, 80), pygame.Rect(310, 160, 50, 30),
                      pygame.Rect(390, 220, 50, 10), pygame.Rect(440, 190, 20, 40), pygame.Rect(340, 280, 50, 10), pygame.Rect(540, 80, 40, 40),
                      pygame.Rect(540, 120, 80, 40), pygame.Rect(540, 160, 120, 40), pygame.Rect(540, 200, 160, 40), pygame.Rect(540, 240, 210, 20),
                      pygame.Rect(540, 260, 260, 30), pygame.Rect(620, 10, 40, 40), pygame.Rect(660, 10, 40, 80), pygame.Rect(700, 10, 50, 110),
                      pygame.Rect(750, 10, 50, 140), pygame.Rect(800, 10, 60, 160), pygame.Rect(860, 10, 210, 280)]
        rectanglestype2 = []
        colliderects = [pygame.Rect(240, 170, 70, 10), pygame.Rect(500, 40, 40, 250)]
        fallplatforms = [pygame.Rect(240, 170, 70, 10), pygame.Rect(240, 100, 70, 10), pygame.Rect(240, 40, 70, 10), pygame.Rect(280, 270, 60, 20),
                         pygame.Rect(390, 270, 110, 20), pygame.Rect(50, 40, 40, 10)]
        wallplatforms = []
        killermovers = []
        winpos = [pygame.Rect(800, 270, 60, 20)]
        leftboosters = []
        rightboosters = []
        upboosters = [pygame.Rect(10, 30, 20, 260), pygame.Rect(460, 35, 40, 220)]
        downboosters = []
    if level == 10:
        if setup == 1:
            angle1 = 0
            playerx = 20
            playery = 260
            dash = 1
            setup = 0
            screen.fill(Black)
            coins.clear()
            coins = []
        rectangles = [pygame.Rect(0, 0, 10, 300), pygame.Rect(0, 0, 1080, 10), pygame.Rect(1070, 0, 10, 300), pygame.Rect(0, 290, 1070, 10), pygame.Rect(10, 10, 70, 240),
                      pygame.Rect(820, 10, 260, 280)]
        rectanglestype2 = []
        colliderects = []
        fallplatforms = []
        wallplatforms = []
        killermovers = []
        winpos = [pygame.Rect(770, 210, 50, 60)]
        leftboosters = []
        rightboosters = []
        upboosters = []
        downboosters = [pygame.Rect(60, 10, 60, 240), pygame.Rect(170, 130, 60, 160), pygame.Rect(120, 10, 90, 80), pygame.Rect(200, 10, 100, 80),
                        pygame.Rect(300, 230, 60, 20), pygame.Rect(340, 10, 40, 240), pygame.Rect(230, 130, 40, 40), pygame.Rect(270, 130, 20, 40),
                        pygame.Rect(380, 10, 140, 80), pygame.Rect(520, 170, 40, 120), pygame.Rect(380, 10, 300, 80), pygame.Rect(580, 90, 90, 40),
                        pygame.Rect(640, 10, 80, 180), pygame.Rect(440, 140, 80, 160), pygame.Rect(560, 240, 40, 60), pygame.Rect(700, 10, 100, 200),
                        pygame.Rect(600, 270, 220, 20),]
    if level == 11:
        if setup == 1:
            angle1 = 0
            playerx = 20
            playery = 260
            dash = 1
            setup = 0
            screen.fill(Black)
            coins.clear()
            coins = []
        rectangles = []
        rectanglestype2 = []
        colliderects = [pygame.Rect(100, 30, 600, 60), pygame.Rect(260, 160, 80, 80), pygame.Rect(410, 170, 60, 100),
                        pygame.Rect(550, 260, 60, 40), pygame.Rect(100, 190, 50, 60), pygame.Rect(150, 130, 60, 60),
                        pygame.Rect(150, 250, 60, 40), pygame.Rect(150, 190, 60, 60), pygame.Rect(100, 120, 50, 70)]
        fallplatforms = []
        wallplatforms = []
        killermovers = []
        winpos = []
        leftboosters = []
        rightboosters = []
        upboosters = []
        downboosters = []
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            print("pygame.Rect", str(rectrectangles)[1:-1], ",", sep="")
            print("pygame.Rect", str(rectrectangles2)[1:-1], ",", sep="")
            print("pygame.Rect", str(cocoins)[1:-1], ",", sep="")
            running = False
    keys = pygame.key.get_pressed()
    # Player Movement
    if running:
        if keys[pygame.K_a] and cooldown3 >= 0:
            playerx -= playermovex
        if keys[pygame.K_d] and cooldown3 >= 0:
            playerx += playermovex
        if keys[pygame.K_w] and cooldown3 >= 0:
            playery -= playermovey
        if keys[pygame.K_s] and cooldown3 >= 0:
            playery += playermovey
        if keys[pygame.K_SPACE]:
            print(playerx, playery)

    # Level Creator
    if running:
        if keys[pygame.K_LEFT] and cooldown2 >= 0:
            creatory -= 10
            cooldown2 = -5
        if keys[pygame.K_RIGHT] and cooldown2 >= 0:
            creatory += 10
            cooldown2 = -5
        if keys[pygame.K_UP] and cooldown2 >= 0:
            creatorx -= 10
            cooldown2 = -5
        if keys[pygame.K_DOWN] and cooldown2 >= 0:
            creatorx += 10
            cooldown2 = -5
        if keys[pygame.K_RCTRL] and cooldown2 >= 0:
            if rectcreate:
                rectposy1 = creatory
                rectposx1 = creatorx
                print(rectposx1, rectposy1, rectcreate)
                cooldown2 = -20
            if not rectcreate:
                rectposy2 = creatory
                rectposx2 = creatorx
                print("pygame.Rect", (rectposy1, rectposx1, (abs(rectposy1 - rectposy2)), (abs(rectposx1 - rectposx2))))
                rectrectangle = (rectposy1, rectposx1, (abs(rectposy1 - rectposy2)), (abs(rectposx1 - rectposx2)))
                rectrectangles += [rectrectangle]
                cooldown2 = -20
            rectcreate = not rectcreate
        if keys[pygame.K_RSHIFT] and cooldown2 >= 0:
            rectrectangles.remove((rectposy1, rectposx1, (abs(rectposy1 - rectposy2)), (abs(rectposx1 - rectposx2))))
            pygame.draw.rect(screen, Black, (rectposy1, rectposx1, (abs(rectposy1 - rectposy2)), (abs(rectposx1 - rectposx2))))
            cooldown2 = -20
        if keys[pygame.K_PERIOD] and cooldown2 >= 0:
            if rect2create:
                rect2posy1 = creatory
                rect2posx1 = creatorx
                print(rect2posx1, rect2posy1, rect2create)
                cooldown2 = -20
            if not rect2create:
                rect2posy2 = creatory
                rect2posx2 = creatorx
                print("pygame.Rect", (rect2posy1, rect2posx1, (abs(rect2posy1 - rect2posy2)), (abs(rect2posx1 - rect2posx2))))
                rectrectangle2 = (rect2posy1, rect2posx1, (abs(rect2posy1 - rect2posy2)), (abs(rect2posx1 - rect2posx2)))
                rectrectangles2 += [rectrectangle2]
                cooldown2 = -20
            rect2create = not rect2create
        if keys[pygame.K_COMMA] and cooldown2 >= 0:
            rectrectangles2.remove((rect2posy1, rect2posx1, (abs(rect2posy1 - rect2posy2)), (abs(rect2posx1 - rect2posx2))))
            pygame.draw.rect(screen, Black, (rect2posy1, rect2posx1, (abs(rect2posy1 - rect2posy2)), (abs(rect2posx1 - rect2posx2))))
            cooldown2 = -20
        if keys[pygame.K_LEFTBRACKET] and cooldown2 >= 0:
            coinposy = creatory
            coinposx = creatorx
            print(coinposx, coinposy)
            print("pygame.Rect", (coinposy, coinposx, 10, 10))
            cocoin = (coinposy, coinposx, 10, 10)
            cocoins += [cocoin]
            cooldown2 = -20
        if keys[pygame.K_RIGHTBRACKET] and cooldown2 >= 0:
            cocoins.remove((coinposy, coinposx, 10, 10))
            pygame.draw.rect(screen, Black, (coinposy, coinposx, 10, 10))
            cooldown2 = -20
        if keys[pygame.K_MINUS] and cooldown2 >= 0:
            if moverectcreate:
                moverect1posy1 = creatory
                moverect1posx1 = creatorx
                print(moverect1posx1, moverect1posy1, moverectcreate)
                cooldown2 = -20
                moverectcreate = False
            if not moverectcreate:
                moverect1posy2 = creatory
                moverect1posx2 = creatorx
                print("pygame.Rect", (moverect1posy1, moverect1posx1, (abs(moverect1posy1 - moverect1posy2)), (abs(moverect1posx1 - moverect1posx2))))
                moverectrectangle = (moverect1posy1, moverect1posx1, (abs(moverect1posy1 - moverect1posy2)), (abs(moverect1posx1 - moverect1posx2)))
                print(moverectrectangle)
                cooldown2 = -20
                moverect2create = True
            if moverect2create:
                moverect2posy1 = creatory
                moverect2posx1 = creatorx
                print(moverect2posx1, moverect2posy1, moverect2create)
                cooldown2 = -20
                moverect2create = False
            if not moverect2create:
                moverect2posy2 = creatory
                moverect2posx2 = creatorx
                print("pygame.Rect", (moverect2posy1, moverect2posx1, (abs(moverect2posy1 - moverect2posy2)), (abs(moverect2posx1 - moverect2posx2))))
                moverectrectangle2 = (moverect2posy1, moverect2posx1, (abs(moverect2posy1 - moverect2posy2)), (abs(moverect2posx1 - moverect2posx2)))
                print(moverectrectangle2)
                cooldown2 = -20
                moverectcreatefinal = True
            if moverectcreatefinal:
                if keys[pygame.K_0]:
                    print("pygame.Rect", ((((moverect1posy1 - moverect1posy2) / 2) + moverect1posy1), "movement1" * ((moverect1posx1 - moverect1posx2) / 15)))
                if keys[pygame.K_9]:
                    print("pygame.Rect", (("movement1" * ((moverect1posy1 - moverect1posy2) / 15)), ((moverect1posx2 - moverect1posx2) + moverect1posy1)))
        if keys[pygame.K_BACKSLASH] and cooldown2 >= 0:
            for rectangle in rectangles:
                if pygame.Rect.colliderect(pygame.draw.rect(screen, Green, pygame.Rect(creatory, creatorx, 10, 10)), rectangle):
                    print(rectangle)
            cooldown2 = -10
        if keys[pygame.K_1] and cooldown2 >= 0:
            if collrectcreate:
                collrectposy1 = creatory
                collrectposx1 = creatorx
                print(collrectposx1, collrectposy1, collrectcreate)
                collrectcreate = False
            if not collrectcreate:
                collrectposy2 = creatory
                collrectposx2 = creatorx
                print("pygame.Rect", (collrectposy1, collrectposx1, (abs(collrectposy1 - collrectposy2)), (abs(collrectposx1 - collrectposx2))))
                collrectrectangle = "pygame.Rect", (collrectposy1, collrectposx1, (abs(collrectposy1 - collrectposy2)), (abs(collrectposx1 - collrectposx2)))
                colliderects += [collrectrectangle]
                collrectcreate = True
            cooldown2 = -20
        if keys[pygame.K_LSHIFT] and keys[pygame.K_1] and cooldown2 >= 0:
            collrectrectangles.remove((collrectposy1, collrectposx1, (abs(collrectposy1 - collrectposy2)), (abs(collrectposx1 - collrectposx2))))
            pygame.draw.rect(screen, Black, (collrectposy1, collrectposx1, (abs(collrectposy1 - collrectposy2)), (abs(collrectposx1 - collrectposx2))))
            cooldown2 = -20

    # Velocity calculation
    if running:
        playery -= y2vel
        if yvel >= 3:
            yvel -= 2
        if yvel <= 3:
            yvel = 0
        if y2vel >= 3:
            y2vel -= 2
        if y2vel <= 3:
            y2vel = 0
        playerx -= x2vel
        if xvel >= 3:
            xvel -= 2
        if xvel <= 3:
            xvel = 0
        if x2vel >= 3:
            x2vel -= 2
        if x2vel <= 3:
            x2vel = 0

    #schmoovement
    if running:
        if level == 9:
            downboostervel = 2.5
            upboostervel = 3
        if level == 10:
            downboostervel = 10
            upboostervel = 10
            rightboostervel = 10
            leftboostervel = 10
        for rightbooster in rightboosters:
            boostercalc(rightbooster, rightboostervel, 0, 0, 0)
        for leftbooster in leftboosters:
            boostercalc(leftbooster, -leftboostervel, 0, 1, 0)
        for upbooster in upboosters:
            boostercalc(upbooster, 0, -upboostervel, 1, 1)
        for downbooster in downboosters:
            boostercalc(downbooster, 0, downboostervel, 0, 1)

    # Wind
    if running:
        if level == 7 and playerx > 0:
            xvel -= ((playerx - 10)/200)
        if level == 8:
            if playerx > 12:
                windvel = -1.2
                xvel += windvel
            if playerx > 270:
                windvel = 1.7
                xvel += windvel
            if playerx > 510:
                windvel = 4
                xvel += windvel
        if level == 9:
            windvel = 1.5
            yvel += windvel
    # Dash
    if keys[pygame.K_f] and cooldown1 >= 0 and dash == 1:
        cooldown1 = -20
        if keys[pygame.K_a]:
            x2vel = dashVel
        if keys[pygame.K_d]:
            xvel = dashVel
        if keys[pygame.K_w]:
            y2vel = dashVel
        if keys[pygame.K_s]:
            yvel = dashVel
    # killing / winning / drawing
    for colliderect in colliderects:
        colliderect.height = int(colliderect.height)
        colliderect.y = int(colliderect.y)
        for x in range(colliderect.x - colliderect.width + 10, colliderect.right - colliderect.width - 10, 10):
            #top side
            surface = pygame.Surface((colliderect.width, colliderect.height))
            border_rect = pygame.Rect(10, 0, 10, 10)
            bordersurface = pygame.Surface((10, 10))
            #if pygame.Rect.colliderect(pygame.Rect(colliderect.top, colliderect.y, 20, 20), colliderect):
            #    bordersurface.blit(collideborderimg, (0, 0), pygame.Rect(10, 10, 10, 10))
            #else:
            bordersurface.blit(collideborderimg, (0, 0), pygame.Rect(10, 0, 10, 10))
            screen.blit(bordersurface, (colliderect.width + x, colliderect.y))
            #bottom side
            #if pygame.Rect.colliderect(pygame.Rect(colliderect.x, colliderect.top + colliderect.height, 20, 20), colliderect):
            #    bordersurface.blit(collideborderimg, (0, 0), pygame.Rect(10, 10, 10, 10))
            #else:
            bordersurface.blit(collideborderimg, (0, 0), pygame.Rect(10, 20, 10, 10))
            screen.blit(bordersurface, (colliderect.width + x, colliderect.y + colliderect.height - 10))
        for y in range(colliderect.top + 10, colliderect.bottom - 10, 10):
            # Left side
            bordersurface.blit(collideborderimg, (0, 0), pygame.Rect(0, 10, 10, 10))
            screen.blit(bordersurface, (colliderect.x, y))
            # Right side
            bordersurface.blit(collideborderimg, (0, 0), pygame.Rect(20, 10, 10, 10))
            surface.blit(bordersurface, (colliderect.width - 10, 0))
            screen.blit(bordersurface, (colliderect.x + colliderect.width - 10, y))
        #corners
        if running:
            #top left corner
            surface = pygame.Surface((colliderect.width, colliderect.height))
            bordersurface.blit(collideborderimg, (0, 0), pygame.Rect(0, 0, 10, 10))
            screen.blit(bordersurface, (colliderect.x, colliderect.y))
            # top right corner
            bordersurface.blit(collideborderimg, (0, 0), pygame.Rect(20, 0, 10, 10))
            screen.blit(bordersurface, (colliderect.width + colliderect.left - 10, colliderect.y))
            # bottom left corner
            bordersurface.blit(collideborderimg, (0, 0), pygame.Rect(0, 20, 10, 10))
            screen.blit(bordersurface, (colliderect.x, colliderect.height + colliderect.top - 10))
            # bottom right corner
            bordersurface.blit(collideborderimg, (0, 0), pygame.Rect(20, 20, 10, 10))
            surface.blit(bordersurface, (colliderect.x, colliderect.y))
            screen.blit(bordersurface, (colliderect.width + colliderect.left - 10, colliderect.y + colliderect.height - 10))
        #center
        if running:
            for y in range(colliderect.y + 10, colliderect.y + colliderect.height - 10, 10):
                for x in range(colliderect.x + 10, colliderect.x + colliderect.width - 10, 10):
                    scaledcenter = pygame.transform.scale(scaledcenter, (colliderect.width, colliderect.height))
                    bordersurface.blit(scaledcenter, (0, 0))
                    surface.blit(bordersurface, (colliderect.width + 10, colliderect.height + 10))
                    screen.blit(bordersurface, (x, y))
        if pygame.Rect.colliderect(pygame.Rect(playerx, playery, 20, 20), colliderect):
            # top side collision
            if colliderect.top <= pygame.Rect(playerx, playery, 20, 20).bottom and colliderect.top + 4 >= pygame.Rect(playerx, playery, 20, 20).top:
                if yvel > 0:
                    yvel = -yvel + windvel
                else:
                    yvel = 0
                if pygame.Rect(playerx, playery, 20, 20).bottom > colliderect.top + 5 and playerx > colliderect.left - 10 and playerx < colliderect.right + 10:
                    playery -= 5
                elif pygame.Rect(playerx, playery, 20, 20).bottom > colliderect.top + 3 and playerx > colliderect.left - 10 and playerx < colliderect.right + 10:
                    playery -= windvel - 1
                if keys[pygame.K_s]:
                    playery -= playermovey
            # bottom side collision
            elif colliderect.bottom >= pygame.Rect(playerx, playery, 20, 20).top and colliderect.bottom - 2 <= pygame.Rect(playerx, playery, 20, 20).bottom:
                if y2vel < windvel:
                    y2vel = -y2vel - 2
                else:
                    y2vel = 0
                if pygame.Rect(playerx, playery, 20, 20).top < colliderect.bottom - 5 and playerx > colliderect.left - 10 and playerx < colliderect.right + 10:
                    playery += 5
                elif pygame.Rect(playerx, playery, 20, 20).top < colliderect.bottom and playerx > colliderect.left - 10 and playerx < colliderect.right + 10:
                    playery += windvel + 1
                if keys[pygame.K_w]:
                    playery += playermovey
            #left side collision (working)
            if colliderect.left <= pygame.Rect(playerx, playery, 20, 20).right and colliderect.left >= pygame.Rect(playerx, playery, 20, 20).left and playery + 15 >= colliderect.top and playery - 15 <= colliderect.bottom:
                if xvel > windvel:
                    xvel = -xvel
                else:
                    xvel = 0
                if pygame.Rect(playerx, playery, 20, 20).right > colliderect.left + 5 and playery > colliderect.top + 5 and playery < colliderect.bottom - 5:
                    playerx -= 5
                if pygame.Rect(playerx, playery, 20, 20).right > colliderect.left and playery > colliderect.top + 5 and playery < colliderect.bottom - 5:
                    playerx -= windvel
                if keys[pygame.K_d]:
                    playerx -= playermovex
            # right side collision (working)
            if colliderect.right >= pygame.Rect(playerx, playery, 20, 20).left and colliderect.right <= pygame.Rect(playerx, playery, 20, 20).right and playery + 15 >= colliderect.top and playery - 15 <= colliderect.bottom:
                if x2vel < 0:
                    x2vel = -x2vel - 2
                else:
                    x2vel = 0
                if pygame.Rect(playerx, playery, 20, 20).left < colliderect.right - 5 and playery > colliderect.top - 5 and playery < colliderect.bottom + 5:
                    playerx += 5
                if pygame.Rect(playerx, playery, 20, 20).left < colliderect.right and playery > colliderect.top + 5 and playery < colliderect.bottom - 5:
                    playerx += windvel
                if keys[pygame.K_a]:
                    playerx += playermovex
    for fallplatform in fallplatforms:
        surface = pygame.Surface((fallplatform.width, fallplatform.height))
        surface.blit(fallplatleftedge, (0, 0))
        surface.blit(fallplatrightedge, (fallplatform.width - 10, 0))
        for x in range(fallplatform.left + 10, fallplatform.right - 10, 10):
            surface.blit(fallplatmain, (x - fallplatform.left, 0))
        screen.blit(surface, (fallplatform.left, fallplatform.top))
        if pygame.Rect.colliderect(pygame.Rect(playerx, playery, 20, 20), fallplatform):
            if fallplatform.top <= pygame.Rect(playerx, playery, 20, 20).bottom and fallplatform.top + 4 >= pygame.Rect(playerx, playery, 20, 20).top:
                if yvel > 0:
                    yvel = -yvel + windvel
                else:
                    yvel = 0
                if pygame.Rect(playerx, playery, 20, 20).bottom > fallplatform.top + 5:
                    playery -= 5
                if pygame.Rect(playerx, playery, 20, 20).bottom > fallplatform.top:
                    playery -= windvel
                if keys[pygame.K_s]:
                    playery -= playermovey
    for wallplatform in wallplatforms:
        pygame.draw.rect(screen, Yellow, wallplatform)
        # left side collision (working)
        if wallplatform.left <= pygame.Rect(playerx, playery, 20, 20).right and wallplatform.left >= pygame.Rect(playerx, playery, 20, 20).left and playery > wallplatform.top and playery < wallplatform.bottom:
            if xvel > windvel:
                xvel = -xvel
            else:
                xvel = 0
            if keys[pygame.K_d]:
                playerx -= playermovex
        # right side collision (working)
        if wallplatform.right >= pygame.Rect(playerx, playery, 20, 20).left and wallplatform.right - 2 <= pygame.Rect(playerx, playery, 20, 20).right and playery > wallplatform.top and playery < wallplatform.bottom:
            if x2vel < windvel:
                x2vel = -x2vel - 2
            else:
                x2vel = 0
            if keys[pygame.K_a]:
                playerx += playermovex
    for rectangle in rectangles:
        pygame.draw.rect(screen, LightGray, pygame.Rect(rectangle))
        #rectsurface = pygame.Surface((1080, 300))
        #rectsurface.blit(rectoverlay, (0, 0), rectangle)
        #screen.blit(rectsurface, (rectangle.x, rectangle.y))
        if pygame.Rect.colliderect(pygame.Rect(playerx, playery, 20, 20), rectangle):
            pygame.draw.rect(screen, Black, pygame.Rect((playerx - 60), (playery - 60), 120, 120))
            death += 1
            setup = 1
            coinscollected = 0
    for killermover in killermovers:
        pygame.draw.rect(screen, LightGray, killermover)
        if pygame.Rect.colliderect(pygame.Rect(playerx, playery, 20, 20), killermover):
            death += 1
            setup = 1
            coinscollected = 0
    for winposition in winpos:
        pygame.draw.rect(screen, Yellow, winposition)
    for coin in coins:
        surface = pygame.Surface((coin.width, coin.height))
        coin_rect = pygame.Rect(10, 10, 10, 10)
        coinsurface = pygame.Surface((coin.width, coin.height))
        coinsurface.blit(coinimg, (0, 0), pygame.Rect(0, 0, 10, 10))
        screen.blit(coinsurface, (coin.x, coin.y))
        if pygame.Rect.colliderect(pygame.Rect(playerx, playery, 20, 20), coin):
            coinscollected += 1
            print(coins)
            print(coinscollected)
            coins.remove(coin)
    if level == 3 or level == 5:
        if movement1 >= 5:
            increment1 = -0.05 * (0.5 * abs(movement1))
        if movement1 <= -5:
            increment1 = 0.05 * (0.5 * abs(movement1))
        if movement2 >= 5:
            increment2 = -0.05 * (0.5 * abs(movement2))
        if movement2 <= -5:
            increment2 = 0.05 * (0.5 * abs(movement2))
        if movement3 >= 5:
            increment3 = -0.05 * (0.5 * abs(movement3))
        if movement3 <= -5:
            increment3 = 0.05 * (0.5 * abs(movement3))
        movement1 += increment1
        movement2 += increment2
        movement3 += increment3

    # Drawing levelcreator objects
    if running:
        for rectrectangle in rectrectangles:
            pygame.draw.rect(screen, LightGray, rectrectangle)
        for rectrectangle2 in rectrectangles2:
            pygame.draw.rect(screen, LighterGray, rectrectangle2)
        for cocoin in cocoins:
            pygame.draw.rect(screen, Yellow, cocoin)

    # angle values
    if running:
        if level == 3:
            angle1 += 5

    # coins checking
    if running:
        if coinsreq <= coinscollected:
            for winposition in winpos:
                if pygame.Rect.colliderect(pygame.Rect(playerx, playery, 20, 20), winposition):
                    level += levelinc
                    setup = 1
                    yvel = 0
                    xvel = 0
                    y2vel = 0
                    x2vel = 0
                    print(death)
                    coins.clear()
                    coinsreq = 0
                    coinscollected = 0
    cooldown1 += 1
    cooldown2 += 1
    cooldown3 += 1
    playerrect = pygame.Rect(playerx, playery, 20, 20)
    surface = pygame.Surface((playerrect.width, playerrect.height))
    surface.blit(playerimg, (0, 0))
    screen.blit(surface, (playerx, playery))
    for rectangletype2 in rectanglestype2:
        pygame.draw.rect(screen, LighterGray, rectangletype2)
    pygame.draw.rect(screen, Green, pygame.Rect(creatory, creatorx, 10, 10))
    playery += yvel
    playerx += xvel
    if 0 > playery or 280 < playery or 0 > playerx or 1060 < playerx:
        setup = 1
    clock.tick(60)
    pygame.display.flip()
    pygame.draw.rect(screen, Black, pygame.Rect((playerx - 60), (playery - 60), 120, 120))
    pygame.draw.rect(screen, Black, pygame.Rect(creatory, creatorx, 30, 30))
