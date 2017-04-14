#!/usr/bin/python

import os
import time
import sys
import dials as dd
import pygame
from pygame.locals import *

os.environ['SDL_VIDEO_WINDOW_POS'] = 'center'
###########**************###########
pygame.init()
font = pygame.font.SysFont("Free Sans", 20)

drawColor = (255, 255,255)  # White
backColor = (0, 0, 0)  # Black
##########***************###########
size = width, height = 1277, 726


pygame.display.set_caption('OBDII Gauge Panel')
monitorX = pygame.display.Info().current_w
monitorY = pygame.display.Info().current_h

#text
surface31FullscreenX = (monitorX / 2) - 310#+ 0
surface31FullscreenY = (monitorY / 2) + 60#- 240

surface31WindowedX = (width / 2) - 220#- 0
surface31WindowedY = (height / 2) + 30#- 290

surface31X = surface31WindowedX
surface31Y = surface31WindowedY
##
surface32FullscreenX = (monitorX / 2) -180#+ 0
surface32FullscreenY = (monitorY / 2) + 60#- 240

surface32WindowedX = (width / 2) -150#- 0
surface32WindowedY = (height / 2) + 40#- 290

surface32X = surface32WindowedX
surface32Y = surface32WindowedY

#text
surface41FullscreenX = (monitorX / 2) - 310#+ 310
surface41FullscreenY = (monitorY / 2) + 60#- 240

surface41WindowedX = (width / 2) - 240#- 310
surface41WindowedY = (height / 2) + 80#- 290

surface41X = surface41WindowedX
surface41Y = surface41WindowedY
##
surface42FullscreenX = (monitorX / 2) + 10#+ 310
surface42FullscreenY = (monitorY / 2) + 60#- 240

surface42WindowedX = (width / 2) + 10#- 310
surface42WindowedY = (height / 2) + 10#- 290

surface42X = surface42WindowedX
surface42Y = surface42WindowedY

#Throttle Position
surface3FullscreenX = (monitorX / 2) - 310#+ 0
surface3FullscreenY = (monitorY / 2) + 60#- 240

surface3WindowedX = (width / 2) - 600#- 0
surface3WindowedY = (height / 2) + 20#- 290

surface3X = surface3WindowedX
surface3Y = surface3WindowedY

#Acceleration
surface4FullscreenX = (monitorX / 2) + 10#+ 310
surface4FullscreenY = (monitorY / 2) + 60#- 240

surface4WindowedX = (width / 2) -220#- 310
surface4WindowedY = (height / 2) + 20#- 290

surface4X = surface4WindowedX
surface4Y = surface4WindowedY

#rpm
surface5FullscreenX = (monitorX / 2) + 310#- 310
surface5FullscreenY = (monitorY / 2) - 240#+ 60

surface5WindowedX = (width / 2) - 600#- 310
surface5WindowedY = (height / 2) - 330#+ 10    ##to horizontal

surface5X = surface5WindowedX
surface5Y = surface5WindowedY

#speed
surface6FullscreenX = (monitorX / 2) + 0#+ 10
surface6FullscreenY = (monitorY / 2) - 240#+ 60

surface6WindowedX = (width / 2) - 220#+ 10
surface6WindowedY = (height / 2) - 330#+ 10   ##to horizontal

surface6X = surface6WindowedX
surface6Y = surface6WindowedY

screen = pygame.display.set_mode((size),pygame.HWSURFACE | pygame.DOUBLEBUF)

#surface1 = pygame.Surface((1300,680))
#surface2 = pygame.Surface((1000,600))
surface31 = pygame.Surface((40,40))
surface32 = pygame.Surface((40,40))
surface41 = pygame.Surface((340,340))
surface42 = pygame.Surface((340,340))
surface3 = pygame.Surface((300,300))
surface4 = pygame.Surface((300,300))
surface5 = pygame.Surface((300,300))
surface6 = pygame.Surface((300,300))

#surface1.set_colorkey(0x0000FF)
#surface2.set_colorkey(0x0000FF)
surface31.set_colorkey(0x0000FF)
surface32.set_colorkey(0x0000FF)
surface41.set_colorkey(0x0000FF)
surface42.set_colorkey(0x0000FF)
surface3.set_colorkey(0x0000FF)
surface4.set_colorkey(0x0000FF)
surface5.set_colorkey(0x0000FF)
surface6.set_colorkey(0x0000FF)

screen.fill(0x000000)

pygame.time.Clock().tick(30)

for event in pygame.event.get():

        if event.type==pygame.QUIT:
                sys.exit()

        if event.type is KEYDOWN and event.key == K_q:
                sys.exit()

        if event.type is KEYDOWN and event.key == K_w:
                pygame.display.set_mode((size),pygame.HWSURFACE | pygame.DOUBLEBUF)
                pygame.mouse.set_visible(True)
                surface1X = surface1WindowedX
                surface1Y = surface1WindowedY
                surface2X = surface2WindowedX
                surface2Y = surface2WindowedY
                surface31X = surface31WindowedX
                surface31Y = surface31WindowedY
                surface32X = surface32WindowedX
                surface32Y = surface32WindowedY
                surface41X = surface41WindowedX
                surface41Y = surface41WindowedY
                surface42X = surface42WindowedX
                surface42Y = surface42WindowedY
                surface3X = surface3WindowedX
                surface3Y = surface3WindowedY
                surface4X = surface4WindowedX
                surface4Y = surface4WindowedY
                surface5X = surface5WindowedX
                surface5Y = surface5WindowedY
                surface6X = surface6WindowedX
                surface6Y = surface6WindowedY
                screen.fill(0x000000)

        if event.type is KEYDOWN and event.key == K_f:
                pygame.display.set_mode((monitorX,monitorY), FULLSCREEN)
                surface1X = surface1FullscreenX
                surface1Y = surface1FullscreenY
                surface2X = surface2FullscreenX
                surface2Y = surface2FullscreenY
                surface31X = surface31FullscreenX
                surface31Y = surface31FullscreenY
                surface32X = surface32FullscreenX
                surface32Y = surface32FullscreenY
                surface41X = surface41FullscreenX
                surface41Y = surface41FullscreenY
                surface42X = surface42FullscreenX
                surface42Y = surface42FullscreenY
                surface3X = surface3FullscreenX
                surface3Y = surface3FullscreenY
                surface4X = surface4FullscreenX
                surface4Y = surface4FullscreenY
                surface5X = surface5FullscreenX
                surface5Y = surface5FullscreenY
                surface6X = surface6FullscreenX
                surface6Y = surface6FullscreenY
                pygame.mouse.set_visible(False)
                screen.fill(0x000000)


#surface1.fill(0x000000)
#surface2.fill(0x0000FF)
surface31.fill(0x0000FF)
surface32.fill(0x0000FF)
surface41.fill(0x0000FF)
surface42.fill(0x0000FF)
surface3.fill(0x0000FF)
surface4.fill(0x0000FF)
surface5.fill(0x0000FF)
surface6.fill(0x0000FF)

def ddial_thro(data):
    THRO_Value = data
    dd.Dials(needleDestination=surface3,
                needleValue=THRO_Value,startPosition=-45,endPosition=45,
                maximumValue=10 ,dialType=dd.percent,dialLabel="Throttle Position",backgroundColour=(0,0,81),displayCircle=True,foregroundColour=(255,255,255))
    screen.blit(surface3,(surface3X,surface3Y))
    pygame.display.update()
    return

def ddial_acce(data):
    ACCE_Value = data
    dd.Dials(needleDestination=surface4,
                needleValue=ACCE_Value, startPosition=-45,endPosition=45,maximumValue=40,
                dialType=dd.accele,dialLabel="Acceleration",backgroundColour=(0,0,81),displayCircle=True,foregroundColour=(255,255,255))
    screen.blit(surface4,(surface4X,surface4Y))
    pygame.display.update()
    return
    
def ddial_rpm(data):
    RPM_Value = data
    dd.Dials(needleDestination=surface5,
                needleValue=RPM_Value,startPosition=-45,endPosition=45,
                maximumValue=500,dialType=dd.rpm,dialLabel="RPM",backgroundColour=(0,0,81),displayCircle=True,foregroundColour=(255,255,255))
    screen.blit(surface5,(surface5X,surface5Y))
    pygame.display.update()
    return
    
def ddial_mph(data):
        MPH_Value = data
        dd.Dials(needleDestination=surface6,
                needleValue=data,startPosition=-45,endPosition=45,maximumValue=10,
                dialType=dd.volt,dialLabel="Speed",backgroundColour=(0,0,81),displayCircle=True,foregroundColour=(255,255,255))
        screen.blit(surface6,(surface6X,surface6Y))
        pygame.display.update()
        return



def dtext1(data,x,y,l,b):
        BLUE = (0,0,30)
        surface32 = font.render(data, True, drawColor)
        pygame.draw.rect(screen, BLUE ,[x, y, l, b])# [264, 360]
        screen.blit(surface32, [x,y])
        pygame.display.flip()
        return
        
