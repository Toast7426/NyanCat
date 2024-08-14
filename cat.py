import sys
import pygame
import time
import random
pygame.init()
screen = pygame.display.set_mode((1280,720))
pygame.display.set_caption('Nyan_Cat')

bg = pygame.image.load('res/bg.png').convert()    #ImportFiles
cat = pygame.image.load('res/cat.png').convert_alpha()
catdie = pygame.image.load('res/catdie.png').convert_alpha()
catjump = pygame.image.load('res/catjump.png').convert_alpha()
color = pygame.image.load('res/color.png').convert()
error = pygame.image.load('res/error.png').convert()
dbs = pygame.image.load('res/dbs.png').convert()
die1 = pygame.image.load('res/die1.png').convert()
die2 = pygame.image.load('res/die2.png').convert()
ndpperbg = pygame.image.load('res/ndpperbg.png').convert()
firework1 = pygame.image.load('res/firework1.png').convert()
firework2 = pygame.image.load('res/firework2.png').convert()
firework3 = pygame.image.load('res/firework3.png').convert()
firework4 = pygame.image.load('res/firework4.png').convert()
title1 = pygame.image.load('res/title1.png').convert()
title2 = pygame.image.load('res/title2.png').convert()
title3 = pygame.image.load('res/title3.png').convert()
img = pygame.image.load("res/genshincat.png")
pygame.display.set_icon(img)
pygame.mixer.init()
pygame.mixer.music.load(r'res/Nyan_Cat.mp3')
pygame.mixer.music.play()

y = 640    #CreatVariable
x = 96
key = 0
noerror = 1
righttoleftx = 1280
rnghigh = 0
rngwide = 0
persent = 0
colb = 644
colc = 644
cold = 644
cole = 644
colf = 644
colg = 644
colh = 644
white = 255, 255, 255
font = pygame.font.Font('res/JetBrainsMono-Medium.ttf', 64)
isdead = False
ndp = 0    #NoDiskPersent

def start():
    for a in range(5):    #beginning
        screen.blit(title1,(0,0))
        pygame.display.flip()
        time.sleep(0.5)
    screen.blit(bg,(0,0))
    for b in range(2):    #beginning
        screen.blit(title2,(320,180))
        pygame.display.flip()
        time.sleep(0.5)
    for i in range(2):    #beginning
        screen.blit(title3,(320,180))
        pygame.display.flip()
        time.sleep(0.5)

def quit_X():
    if event.type == pygame.QUIT:
        pygame.quit()
        sys.exit()

def jump(UNumber):
    global y
    UNumber = UNumber + 1
    moveDistance = -4 * UNumber * UNumber + 40 * UNumber - (-4 * (UNumber-1) * (UNumber-1) + 40 * (UNumber-1))
    y = y - moveDistance
    screen.blit(catjump,(x,y))
    return y

def rainbow():
    global colb
    global colc
    global cold
    global cole
    global colf
    global colg
    global colh
    screen.blit(color,(84,cola))
    screen.blit(color,(72,colb))
    screen.blit(color,(60,colc))
    screen.blit(color,(48,cold))
    screen.blit(color,(36,cole))
    screen.blit(color,(24,colf))
    screen.blit(color,(12,colg))
    screen.blit(color,(0,colh))
    colh = colg
    colg = colf
    colf = cole
    cole = cold
    cold = colc
    colc = colb
    colb = cola

def firework():
    rnghigh = random.randint(10,710)
    rngwide = random.randint(50,1230)
    for i in range(64):
        if i // 16 == 0:
            screen.blit(firework1,(rngwide,rnghigh))
        elif i // 16 == 1:
            screen.blit(firework1,(rngwide,rnghigh))
        elif i // 16 == 2:
            screen.blit(firework1,(rngwide,rnghigh))
        elif i // 16 == 3:
            screen.blit(firework1,(rngwide,rnghigh))

start()

clock = pygame.time.Clock()
while True:
    clock.tick(60)    #fps
    if isdead == False and persent < 100:
        for event in pygame.event.get():    #MovingProcessing
            quit_X()
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE and key == 0 and y >= 10:
                key = 1
                for c in range(5):
                    clock.tick(60)
                    screen.blit(bg,(0,0))
                    jump(c)
                    cola = y
                    rainbow()
                    righttoleftx = righttoleftx - 8
                    screen.blit(error,(righttoleftx,rnghigh))
                    screen.blit(per,(1000,100))
                    screen.blit(persign,(1100,100))
                    pygame.display.flip()
            elif event.type == pygame.KEYUP and event.key == pygame.K_SPACE:
                key = 0
        if y <= 640:    #weight
            y = y + 6
        screen.blit(bg,(0,0))    #graphics
        screen.blit(cat,(x,y))
        cola = y + 4
        rainbow()

        if righttoleftx <= 220 and righttoleftx >= -160:    #IfDied
            if y >= rnghigh - 76 and y <= rnghigh + 508:
                isdead = True

        if noerror == 1:    #NewError
            rnghigh = random.randint(-40,364)
            righttoleftx = 1280
            noerror = 0
        screen.blit(error,(righttoleftx,rnghigh))

        righttoleftx = righttoleftx - 8    #ErrorMoving

        if righttoleftx <= -288:    #IfNoError
            noerror = 1
            persent = persent + 5

        per = font.render(str(persent), True, white)    #progress
        persign = font.render('%', True, white)
        screen.blit(per,(1000,100))
        screen.blit(persign,(1100,100))

    elif isdead == True:
        if ndp == 0:
            screen.blit(catdie,(x,y))
            pygame.display.flip()
            time.sleep(0.4)
            screen.blit(dbs,(0,0))
            pygame.display.flip()
            ndp = ndp + 1
        elif ndp < 100 and ndp > 0:
            screen.blit(ndpperbg,(600,500))
            screen.blit(die1,(690,500))
            ndp = ndp + 0.5
            quit_X()
        elif ndp == 100:
            screen.blit(dbs,(0,0))
            screen.blit(ndpper,(600,500))
            screen.blit(die2,(710,500))
            pygame.display.flip()
            time.sleep(1.2)
            pygame.quit()
            sys.exit()
        ndp_int = int(ndp)
        ndpper = font.render(str(ndp_int), True, white)
        screen.blit(ndpper,(600,500))

    elif persent == 100:
        for event in pygame.event.get():    #MovingProcessing
            quit_X()
            if key == 0 and y >= 10 and event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                key = 1
                for c in range(5):
                    clock.tick(60)
                    screen.blit(bg,(0,0))
                    jump(c)
                    cola = y
                    rainbow()
                    screen.blit(ndpper,(1000,100))
                    pygame.display.flip()
            elif event.type == pygame.KEYUP and event.key == pygame.K_SPACE:
                key = 0

        if y <= 640:    #weight
            y = y + 6

        screen.blit(bg,(0,0))    #graphics
        firework()
        screen.blit(cat,(x,y))
        cola = y + 4
        rainbow()
        ndpper = font.render('YouWon', True, white)
        screen.blit(ndpper,(1000,100))

    pygame.display.flip()
