import pygame
import keyboard
import math

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
keys2d = True
level = 7
coinscollected = 0
windvel = 0
rightarrow = pygame.image.load("rightarrow.png")
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
cocoins = []
coinsreq = 0
def boostercalc(self, xchange, ychange, fliph, flipv):
    global xvel
    global yvel
    if flipv == 0 and fliph == 0 or 1:
        if self.height % 20 == 0:
            arrowrect = pygame.Rect(0, 0, 20, 10)
            arrowimg = pygame.image.load("rightarrow1020.png")
            if self.height % 40 == 0:
                arrowrect = pygame.Rect(0, 0, 40, 20)
                arrowimg = pygame.image.load("rightarrow2040.png")
                if self.height % 80 == 0:
                    arrowrect = pygame.Rect(0, 0, 80, 40)
                    arrowimg = pygame.image.load("rightarrow.png")
    if flipv == 1 and fliph == 0 or 1:
        if self.width % 20 == 0:
            arrowrect = pygame.Rect(0, 0, 10, 20)
            arrowimg = pygame.image.load("rightarrow1020.png")
            if self.width % 40 == 0:
                arrowrect = pygame.Rect(0, 0, 20, 40)
                arrowimg = pygame.image.load("rightarrow2040.png")
                if self.width % 80 == 0:
                    arrowrect = pygame.Rect(0, 0, 40, 80)
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
    if pygame.Rect.colliderect(pygame.draw.rect(screen, Red, pygame.Rect(playerx, playery, 20, 20)), self):
        xvel += xchange
        yvel += ychange
running = True
while running:
    if level == 256:
        rectangles = []
        rectanglestype2 = []
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
        rectangles = [pygame.Rect(0, 0, 10, 300), pygame.Rect(0, 0, 1080, 10),
                      pygame.Rect(1070, 0, 10, 300), pygame.Rect(0, 290, 1070, 10)]
        rectanglestype2 = []
        winpos = []
        pygame.draw.rect(screen, Green, pygame.Rect(100, 10, 50, 30))
        pygame.draw.rect(screen, Green, pygame.Rect(170, 10, 50, 30))
        pygame.draw.rect(screen, Green, pygame.Rect(240, 10, 50, 30))
        if pygame.Rect.colliderect(pygame.draw.rect(screen, Red, pygame.Rect(playerx, playery, 20, 20)),
                                   pygame.Rect(100, 10, 50, 30)):
            level = 1
            screen.fill(Black)
            playerx = 120
            playery = 120
            cooldown3 = -40
            setup = 1
        if pygame.Rect.colliderect(pygame.draw.rect(screen, Red, pygame.Rect(playerx, playery, 20, 20)),
                                   pygame.Rect(170, 10, 50, 30)):
            level = 2
            screen.fill(Black)
            playerx = 20
            playery = 20
            cooldown3 = -40
            setup = 1
        if pygame.Rect.colliderect(pygame.draw.rect(screen, Red, pygame.Rect(playerx, playery, 20, 20)),
                                   pygame.Rect(240, 10, 50, 30)):
            level = 3
            screen.fill(Black)
            playerx = 50
            playery = 50
            cooldown3 = -40
            setup = 1
    if level == 1:
        if setup == 1:
            playerx = 40
            playery = 250
            yvel = 0
            xvel = 0
            x2vel = 0
            y2vel = 0
            dash = 1
            coins.clear()
            coins = [pygame.Rect(40, 150, 10, 10)]
        setup = 0
        rectangles = [pygame.Rect(0, 0, 10, 300), pygame.Rect(0, 290, 1080, 10),
                      pygame.Rect(0, 0, 1080, 10), pygame.Rect(1070, 0, 10, 300),
                      pygame.Rect(100, 0, 100, 120), pygame.Rect(100, 150, 100, 150),
                      pygame.Rect(290, 10, 200, 240), pygame.Rect(290, 280, 200, 20),
                      pygame.Rect(490, 60, 70, 180), pygame.Rect(600, 60, 70, 180),
                      pygame.Rect(670, 0, 70, 300), pygame.Rect(700, 0, 470, 300)]
        rectanglestype2 = [pygame.Rect(290, 250, 200, 30)]
        killermovers = []
        winpos = [pygame.Rect(640, 10, 30, 50)]
        coinsreq = 1
        pygame.draw.rect(screen, Green, pygame.Rect(10, 10, 30, 10))
        if pygame.Rect.colliderect(pygame.draw.rect(screen, Red, pygame.Rect(playerx, playery, 20, 20)),
                                   pygame.Rect(10, 10, 30, 10)):
            level = 0
            playerx = 350
            playery = 150
            cooldown3 = -40
            setup = 1
    if level == 2:
        if setup == 1:
            playerx = 20
            playery = 20
            setup = 0
            dash = 1
            coins.clear()
        screen.fill(Black)
        rectangles = [pygame.Rect(0, 0, 10, 300), pygame.Rect(0, 290, 1080, 10),
                      pygame.Rect(0, 0, 1080, 10), pygame.Rect(1070, 0, 10, 300),
                      pygame.Rect(65, 10, 50, 175), pygame.Rect(190, 170, 220, 125),
                      pygame.Rect(410, 50, 90, 240), pygame.Rect(560, 10, 75, 145),
                      pygame.Rect(500, 210, 135, 80), pygame.Rect(630, 10, 50, 145),
                      pygame.Rect(670, 110, 40, 45), pygame.Rect(630, 210, 230, 90),
                      pygame.Rect(810, 110, 70, 235), pygame.Rect(830, 70, 50, 60),
                      pygame.Rect(880, 70, 190, 220), pygame.Rect(910, 10, 160, 70)]
        rectanglestype2 = [pygame.Rect(500, 50, 60, 105), pygame.Rect(560, 155, 75, 55)]
        killermovers = [pygame.Rect(75, (15 * movement1) + 230, 30, 30),
                        pygame.Rect((-30 * movement1) + 240, 130, 40, 40),
                        pygame.Rect((30 * movement1) + 240, 90, 40, 40),
                        pygame.Rect((-30 * movement1) + 240, 50, 40, 40),
                        pygame.Rect((30 * movement1) + 240, 10, 40, 40),
                        pygame.Rect((740 + radius1 * math.cos(math.radians(angle1 + 20)),
                                     (40 + radius2 * math.sin(math.radians(angle1 + 20))), 40, 40)),
                        pygame.Rect((740 + radius1 * math.cos(math.radians(angle1 + 40)),
                                     (40 + radius2 * math.sin(math.radians(angle1 + 40))), 40, 40)),
                        pygame.Rect((740 + radius1 * math.cos(math.radians(angle1 + 60)),
                                     (40 + radius2 * math.sin(math.radians(angle1 + 60))), 40, 40)),
                        pygame.Rect((740 + radius1 * math.cos(math.radians(angle1 + 80)),
                                     (40 + radius2 * math.sin(math.radians(angle1 + 80))), 40, 40)),
                        pygame.Rect((740 + radius1 * math.cos(math.radians(angle1 + 100)),
                                     (40 + radius2 * math.sin(math.radians(angle1 + 100))), 40, 40))]
        winpos = [pygame.Rect(880, 10, 30, 60)]
    if level == 3:
        if setup == 1:
            playerx = 20
            playery = 20
            dash = 0
            setup = 0
            coins.clear()
            coins = [pygame.Rect(290, 30, 10, 10), (390, 120, 10, 10), (490, 260, 10, 10), (750, 60, 10, 10),
                     (750, 70, 10, 10), (760, 70, 10, 10), (760, 60, 10, 10), (760, 150, 10, 10), (750, 150, 10, 10),
                     (750, 160, 10, 10), (760, 160, 10, 10), (760, 240, 10, 10), (750, 240, 10, 10), (750, 250, 10, 10),
                     (760, 250, 10, 10)]
        screen.fill(Black)
        rectangles = [pygame.Rect(0, 0, 10, 300), pygame.Rect(0, 0, 1080, 10),
                      pygame.Rect(1070, 0, 10, 300), pygame.Rect(0, 290, 1070, 10),
                      (10, 50, 180, 40), (230, 10, 40, 120), (50, 130, 220, 120), (10, 290, 260, 80),
                      (310, 210, 60, 80), (310, 100, 60, 80), (310, 40, 150, 60), (410, 140, 70, 110),
                      (490, 40, 40, 60), (520, 100, 60, 190), (530, 40, 50, 60), (630, 10, 50, 130),
                      (630, 180, 50, 110), (730, 90, 50, 50), (730, 180, 50, 50), (680, 10, 100, 40),
                      (680, 270, 100, 20), (780, 110, 100, 90), (920, 50, 80, 80), (780, 10, 220, 40),
                      (920, 170, 80, 100), (780, 270, 220, 20), (850, 250, 70, 20), (850, 50, 70, 20),
                      (1000, 10, 70, 120), (1000, 170, 70, 120)]
        rectanglestype2 = [pygame.Rect(270, 60, 40, 120), (310, 180, 60, 30), pygame.Rect(330, 10, 120, 30),
                           pygame.Rect(630, 140, 50, 40), (920, 130, 80, 40)]
        killermovers = [pygame.Rect(75, (30 * movement1) + 140, 30, 30),
                        pygame.Rect(115, (30 * movement2) + 140, 30, 30),
                        pygame.Rect(155, (30 * movement3) + 140, 30, 30),
                        pygame.Rect(-50 + (12 * movement1), 210, 30, 30),
                        pygame.Rect(150 + (12 * movement1), 55, 30, 30)]
        winpos = [pygame.Rect(1000, 130, 70, 40)]
    if level == 4:
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
            coins = [pygame.Rect(10, 240, 10, 10), (10, 250, 10, 10), (20, 250, 10, 10), (20, 240, 10, 10),
                     (330, 130, 10, 10), (330, 120, 10, 10), (340, 120, 10, 10), (340, 130, 10, 10),
                     (900, 110, 10, 10), (900, 120, 10, 10), (910, 120, 10, 10), (910, 110, 10, 10),
                     (910, 130, 10, 10), (900, 130, 10, 10), (900, 140, 10, 10), (910, 140, 10, 10)]
        rectangles = [pygame.Rect(0, 0, 10, 300), pygame.Rect(0, 0, 1080, 10),
                      pygame.Rect(1070, 0, 10, 300), pygame.Rect(0, 290, 1070, 10),
                      (60, 0, 40, 130), (0, 170, 100, 30), (50, 240, 50, 20), (170, 130, 60, 170),
                      (170, 100, 60, 30), (100, 0, 130, 50), (280, 50, 60, 50), (300, 100, 20, 60), (280, 160, 60, 50),
                      (380, 180, 90, 110), (230, 260, 240, 40), (380, 0, 90, 80), (410, 110, 60, 30),
                      (390, 120, 30, 10), (390, 130, 20, 10), (410, 140, 60, 10), (470, 110, 50, 40),
                      (530, 190, 50, 40), (530, 30, 50, 40), (560, 70, 40, 120), (640, 0, 40, 40), (640, 220, 40, 40),
                      (660, 150, 40, 70), (660, 40, 40, 70), (470, 260, 240, 50), (740, 60, 50, 130),
                      (730, 230, 70, 70), (680, 220, 20, 40), (700, 230, 30, 70), (680, 0, 120, 30), (680, 30, 20, 10),
                      (800, 0, 130, 30), (840, 30, 40, 50), (840, 120, 40, 20), (840, 180, 40, 50), (800, 230, 130, 70),
                      (930, 170, 150, 130), (930, 0, 150, 90), (470, 10, 170, 30), (470, 40, 190, 30),
                      (470, 70, 190, 10)]
        rectanglestype2 = [pygame.Rect(660, 110, 40, 40)]
        killermovers = []
        winpos = [pygame.Rect(970, 90, 120, 80)]
    if level == 5:
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
        rectangles = [pygame.Rect(0, 0, 10, 300), pygame.Rect(0, 0, 1080, 10),
                      pygame.Rect(1070, 0, 10, 300), pygame.Rect(0, 290, 1070, 10),
                      pygame.Rect(0, 0, 410, 110), (0, 190, 400, 110), (400, 190, 10, 110), (410, 170, 160, 10),
                      (410, 180, 160, 120), (410, 0, 160, 130), (570, 0, 510, 130), (570, 170, 510, 130)]
        rectanglestype2 = [pygame.Rect(370, 10, 20, 80), (390, 10, 20, 20), (390, 70, 20, 20), (410, 30, 20, 40),
                           (440, 30, 20, 60), (460, 10, 20, 20), (480, 30, 20, 60), (460, 50, 20, 20),
                           (540, 10, 40, 20), (520, 30, 20, 10), (540, 40, 20, 20), (560, 60, 20, 10),
                           (540, 70, 20, 20), (520, 70, 20, 20), (600, 10, 20, 80), (620, 40, 20, 20),
                           (640, 10, 20, 80), (680, 10, 20, 50), (680, 70, 20, 20),
]
        killermovers = []
        winpos = [pygame.Rect(600, 130, 60, 40)]
    if level == 6:
        if setup == 1:
            angle1 = 0
            playerx = 20
            playery = 100
            dash = 1
            setup = 0
            screen.fill(Black)
            coins.clear()
            coins = []
        rectangles = [pygame.Rect(0, 0, 10, 300), pygame.Rect(0, 0, 1080, 10),
                      pygame.Rect(1070, 0, 10, 300), pygame.Rect(0, 290, 1070, 10),
                      pygame.Rect(0, 0, 80, 90), (0, 130, 80, 170), (80, 150, 10, 40), (80, 190, 20, 40),
                      (80, 230, 30, 40), (80, 270, 40, 30), (90, 180, 10, 10), (100, 220, 10, 10), (110, 260, 10, 10),
                      (80, 0, 30, 90), (110, 90, 10, 20), (120, 110, 10, 30), (130, 140, 10, 30), (140, 170, 10, 30),
                      (150, 200, 10, 20), pygame.Rect(150, 170, 20, 30), (140, 140, 40, 30), (130, 110, 60, 30),
                      (120, 90, 80, 20), (110, 10, 220, 80), (200, 260, 10, 30), (210, 230, 10, 30), (220, 200, 10, 30),
                      (230, 170, 10, 30), (240, 140, 20, 30), (260, 140, 70, 30), (210, 260, 110, 30),
                      (220, 230, 100, 30), (230, 200, 90, 30), (240, 170, 80, 30), (320, 150, 20, 140),
                      (340, 160, 10, 130), (350, 170, 10, 120), (360, 180, 10, 110), (370, 190, 10, 100),
                      (380, 200, 10, 90), (390, 210, 20, 80), (410, 220, 30, 70), (330, 10, 20, 90), (350, 10, 10, 100),
                      (360, 10, 20, 110), (380, 10, 10, 120), (390, 10, 20, 130), (410, 10, 30, 140),
                      (440, 10, 10, 140), (460, 200, 20, 100), (450, 10, 20, 130), (470, 10, 10, 120),
                      (480, 10, 20, 110), (500, 10, 10, 100), (480, 190, 10, 110), (490, 180, 20, 120),
                      (510, 170, 10, 130), (240, 170, 80, 30), (440, 210, 20, 80), (510, 10, 460, 100),
                      (520, 170, 450, 120), (970, 10, 100, 100), (970, 170, 100, 120)]
        rectanglestype2 = [(260, 90, 10, 50)]
        killermovers = []
        winpos = [(1020, 110, 50, 60)]
    if level == 7:
        if setup == 1:
            angle1 = 0
            playerx = 20
            playery = 100
            dash = 1
            setup = 0
            screen.fill(Black)
            coins.clear()
            coins = []
        rectangles = [pygame.Rect(0, 0, 10, 300), (10, 290, 1070, 10), (1070, 0, 10, 290), (10, 0, 1060, 10),]
        rectanglestype2 = []
        colliderects = [pygame.Rect(300, 70, 300, 150)]
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
    pygame.draw.rect(screen, Red, pygame.Rect(playerx, playery, 20, 20))
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
            pygame.draw.rect(screen, Black,
                             (rectposy1, rectposx1, (abs(rectposy1 - rectposy2)), (abs(rectposx1 - rectposx2))))
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
                print("pygame.Rect",
                      (rect2posy1, rect2posx1, (abs(rect2posy1 - rect2posy2)), (abs(rect2posx1 - rect2posx2))))
                rectrectangle2 = (rect2posy1, rect2posx1, (abs(rect2posy1 - rect2posy2)), (abs(rect2posx1 - rect2posx2)))
                rectrectangles2 += [rectrectangle2]
                cooldown2 = -20
            rect2create = not rect2create
        if keys[pygame.K_COMMA] and cooldown2 >= 0:
            rectrectangles2.remove(
                (rect2posy1, rect2posx1, (abs(rect2posy1 - rect2posy2)), (abs(rect2posx1 - rect2posx2))))
            pygame.draw.rect(screen, Black,
                             (rect2posy1, rect2posx1, (abs(rect2posy1 - rect2posy2)), (abs(rect2posx1 - rect2posx2))))
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
            if not moverectcreate:
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
                if pygame.Rect.colliderect(pygame.draw.rect(screen, Green, pygame.Rect(creatory, creatorx, 10, 10)),
                                           rectangle):
                    print(rectangle)
            cooldown2 = -10

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
    if level == 7:
        downboostervel = 2.5
    for rightbooster in rightboosters:
        boostercalc(rightbooster, 2, 0, 0, 0)
    for leftbooster in leftboosters:
        boostercalc(leftbooster, -2, 0, 1, 0)
    for upbooster in upboosters:
        boostercalc(upbooster, 0, -2, 1, 1)
    for downbooster in downboosters:
        boostercalc(downbooster, 0, downboostervel, 0, 1)

    # Wind??
    if running:
        if level == 5 and playerx > 0:
            xvel -= ((playerx - 10)/200)
        if level == 6:
            if playerx > 12:
                windvel = -1.2
                xvel += windvel
            if playerx > 270:
                windvel = 1.7
                xvel += windvel
            if playerx > 510:
                windvel = 4
                xvel += windvel
        if level == 7:
            windvel = 0.2
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
    # killing / winning
    for colliderect in colliderects:
        pygame.draw.rect(screen, Yellow, colliderect)
        if pygame.Rect.colliderect(pygame.draw.rect(screen, Red, pygame.Rect(playerx, playery, 20, 20)), colliderect):
            #left side collision (working)
            if colliderect.left <= pygame.Rect(playerx, playery, 20, 20).right and colliderect.left >= pygame.Rect(playerx, playery, 20, 20).left:
                if xvel > windvel:
                    xvel = -xvel
                else:
                    xvel = 0
                if keys[pygame.K_d]:
                    playerx -= playermovex
            # right side collision (working)
            if colliderect.right >= pygame.Rect(playerx, playery, 20, 20).left and colliderect.right - 2 <= pygame.Rect(playerx, playery, 20, 20).right:
                if x2vel < windvel:
                    x2vel = -x2vel - 2
                else:
                    x2vel = 0
                if keys[pygame.K_a]:
                    playerx += playermovex
            #top side collision

            #bottom side collision
            if colliderect.bottom >= pygame.Rect(playerx, playery + yvel, 20, 20).top and colliderect.bottom <= pygame.Rect(playerx, playery + yvel, 20, 20).bottom:
                if yvel < 0:
                    playery = colliderect.top - 20
                    yvel = 0
                if keys[pygame.K_w]:
                    playery += playermovey
    for rectangle in rectangles:
        pygame.draw.rect(screen, LightGray, rectangle)
        if pygame.Rect.colliderect(pygame.draw.rect(screen, Red, pygame.Rect(playerx, playery, 20, 20)), rectangle):
            pygame.draw.rect(screen, Black, pygame.Rect((playerx - 60), (playery - 60), 120, 120))
            if level == 0:
                playerx = 40
                playery = 250
            if level == 1:
                playerx = 40
                playery = 250
            if level == 2:
                playerx = 20
                playery = 20
            if level == 3:
                playerx = 20
                playery = 20
            death += 1
            setup = 1
            coinscollected = 0
    for killermover in killermovers:
        pygame.draw.rect(screen, LightGray, killermover)
        if pygame.Rect.colliderect(pygame.draw.rect(screen, Red, pygame.Rect(playerx, playery, 20, 20)), killermover):
            if level == 0:
                playerx = 40
                playery = 250
            if level == 1:
                playerx = 40
                playery = 250
            if level == 2:
                playerx = 20
                playery = 20
            if level == 3:
                playerx = 20
                playery = 20
            death += 1
            setup = 1
            coinscollected = 0
    for winposition in winpos:
        pygame.draw.rect(screen, Yellow, winposition)
    for coin in coins:
        pygame.draw.rect(screen, Yellow, pygame.Rect(coin))
        if pygame.Rect.colliderect(pygame.draw.rect(screen, Red, pygame.Rect(playerx, playery, 20, 20)), coin):
            coinscollected += 1
            print(coins)
            print(coinscollected)
            coins.remove(coin)
    if level == 2 or 3:
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
        if level == 2:
            angle1 += 5

    # coins checking
    if running:
        if coinsreq <= coinscollected:
            for winposition in winpos:
                if pygame.Rect.colliderect(pygame.draw.rect(screen, Red, pygame.Rect(playerx, playery, 20, 20)),
                                           winposition):
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
    for rectangletype2 in rectanglestype2:
        pygame.draw.rect(screen, LighterGray, rectangletype2)
    pygame.draw.rect(screen, Green, pygame.Rect(creatory, creatorx, 10, 10))
    playery += yvel
    playerx += xvel
    clock.tick(60)
    pygame.display.flip()
    pygame.draw.rect(screen, Black, pygame.Rect((playerx - 60), (playery - 60), 120, 120))
    pygame.draw.rect(screen, Black, pygame.Rect(creatory, creatorx, 30, 30))
