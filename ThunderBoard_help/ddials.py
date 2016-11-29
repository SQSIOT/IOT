#!/usr/bin/python

import os
import time
import sys
import dials as dd
import pygame
from pygame.locals import *
#pygame.init()

#class gauageNeed:
    #def __init__(self,data):
    #    self.data = data

os.environ['SDL_VIDEO_WINDOW_POS'] = 'center'
###########**************###########
#pygame.font.init()
pygame.init()
font = pygame.font.SysFont("Free Sans", 20)

drawColor = (255, 255,255)  # White
backColor = (0, 0, 0)  # Black
##########***************###########
size = width, height = 640, 640

#pygame.display.set_caption('K11Consult: %s' % __file__)
pygame.display.set_caption('Guage-Needle')
monitorX = pygame.display.Info().current_w
monitorY = pygame.display.Info().current_h

#surface1FullscreenX = (monitorX / 2) - 650
#surface1FullscreenY = (monitorY / 2) - 360

#surface1WindowedX = (width / 2) - 650
#surface1WindowedY = (height / 2) - 360

#surface1X = surface1WindowedX
#surface1Y = surface1WindowedY

#surface2FullscreenX = (monitorX / 2) - 500
#surface2FullscreenY = (monitorY / 2) - 210

#surface2WindowedX = (width / 2) - 500
#surface2WindowedY = (height / 2) - 210

#surface2X = surface2WindowedX
#surface2Y = surface2WindowedY

#coolent temp
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

#fuel
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

#coolent temp
#surface3FullscreenX = (monitorX / 2) - 310#+ 0
#surface3FullscreenY = (monitorY / 2) + 60#- 240

#surface3WindowedX = (width / 2) - 310#- 0
#surface3WindowedY = (height / 2) + 10#- 290

#surface3X = surface3WindowedX
#surface3Y = surface3WindowedY

#fuel
#surface4FullscreenX = (monitorX / 2) + 10#+ 310
#surface4FullscreenY = (monitorY / 2) + 60#- 240

#surface4WindowedX = (width / 2) + 10#- 310
#surface4WindowedY = (height / 2) + 10#- 290

#surface4X = surface4WindowedX
#surface4Y = surface4WindowedY

#rpm
surface5FullscreenX = (monitorX / 2) + 310#- 310
surface5FullscreenY = (monitorY / 2) - 240#+ 60

surface5WindowedX = (width / 2) - 310#- 310
surface5WindowedY = (height / 2) - 290#+ 10    ##to horizontal

surface5X = surface5WindowedX
surface5Y = surface5WindowedY

#speed
surface6FullscreenX = (monitorX / 2) + 0#+ 10
surface6FullscreenY = (monitorY / 2) - 240#+ 60

surface6WindowedX = (width / 2) - 0#+ 10
surface6WindowedY = (height / 2) - 290#+ 10   ##to horizontal

surface6X = surface6WindowedX
surface6Y = surface6WindowedY

screen = pygame.display.set_mode((size),pygame.HWSURFACE | pygame.DOUBLEBUF)

#surface1 = pygame.Surface((1300,680))
#surface2 = pygame.Surface((1000,600))
surface31 = pygame.Surface((40,40))
surface32 = pygame.Surface((40,40))
surface41 = pygame.Surface((340,340))
surface42 = pygame.Surface((340,340))
surface5 = pygame.Surface((300,300))
surface6 = pygame.Surface((300,300))

#surface1.set_colorkey(0x0000FF)
#surface2.set_colorkey(0x0000FF)
surface31.set_colorkey(0x0000FF)
surface32.set_colorkey(0x0000FF)
surface41.set_colorkey(0x0000FF)
surface42.set_colorkey(0x0000FF)
surface5.set_colorkey(0x0000FF)
surface6.set_colorkey(0x0000FF)

screen.fill(0x000000)

#MPH_Value = 0
#RPM_Value = data
#TEMP_Value = 0
#BATT_Value = 0
#FUEL_Value = 0
#MAF_Value = 0

#while True:

pygame.time.Clock().tick(30)
#pygame.mouse.set_visible(False)

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
surface5.fill(0x0000FF)
surface6.fill(0x0000FF)

#dd.Dials(needleDestination=surface1,
 #       needleValue=MPH_Value,needleLength=648,positionX=650,positionY=650,
  #      fontSize=dd.sixty,maximumValue=10,doubleLine=16,singleLine=8,displayNeedle=False,backgroundColour=(81,0,0),foregroundColour=(255,255,255),displayCircle=True)

#dd.Dials(needleDestination=surface2,
 #       needleValue=RPM_Value,needleLength=488,positionX=500,positionY=500,
  #      fontSize=dd.sixty,maximumValue=500,doubleLine=12,singleLine=6,displayNeedle=False,displayDivision=100,displayCircle=True,foregroundColour=(255,255,255))

#dd.Dials(needleDestination=surface3,
 #       needleValue=MAF_Value,startPosition=-45,endPosition=45,displayDivision=10,
  #      needleLength=150,positionX=170,positionY=170,maximumValue=50,dialType=dd.millivolt,dialLabel="MAF",foregroundColour=(255,255,255))

#dd.Dials(needleDestination=surface4,
 #       needleValue=AAC_Value,startPosition=-45,endPosition=45,
  #      needleLength=150,positionX=170,positionY=170,maximumValue=10,dialType=dd.percent,dialLabel="Fuel",foregroundColour=(255,255,255))
def ddial_temp(data):
    TEMP_Value = data
    dd.Dials(needleDestination=surface3,
                needleValue=TEMP_Value,startPosition=-45,endPosition=45,
                maximumValue=40,dialType=dd.degree,dialLabel="Coolant Temp",backgroundColour=(0,0,81),displayCircle=True,foregroundColour=(255,255,255))
    screen.blit(surface3,(surface3X,surface3Y))
    pygame.display.update()
    return

def ddial_fuel(data):
    dd.Dials(needleDestination=surface4,
                needleValue=data,startPosition=-45,endPosition=45,maximumValue=40,
                dialType=dd.degree,dialLabel="Intake Air Temp",backgroundColour=(0,0,81),displayCircle=True,foregroundColour=(255,255,255))
    screen.blit(surface4,(surface4X,surface4Y))
    pygame.display.update()
    return
    
def ddial_rpm(data):
    RPM_Value = data
    dd.Dials(needleDestination=surface5,
                needleValue=RPM_Value,startPosition=-45,endPosition=45,
                maximumValue=10,dialType=dd.rpm,dialLabel="RPM",backgroundColour=(0,0,81),displayCircle=True,foregroundColour=(255,255,255))
    screen.blit(surface5,(surface5X,surface5Y))
    pygame.display.update()
    return
    
def ddial_mph(data):
        dd.Dials(needleDestination=surface6,
                needleValue=data,startPosition=-45,endPosition=45,maximumValue=1,
                dialType=dd.volt,dialLabel="Speed",backgroundColour=(0,0,81),displayCircle=True,foregroundColour=(255,255,255))
        screen.blit(surface6,(surface6X,surface6Y))
        pygame.display.update()
        return

def dtext(data):
        surface31 = font.render(data, True, drawColor)
        screen.blit(surface31, (surface31X,surface31Y))#[280, 175])
        pygame.display.update()
        return


def dtext1(data,x,y,l,b):
        BLUE = (0,0,30)
        surface32 = font.render(data, True, drawColor)
        pygame.draw.rect(screen, BLUE ,[x, y, l, b])# [264, 360], 40)
        #delay(1)
        screen.blit(surface32, [x,y])#(surface32X,surface32Y))#[280, 175])
        pygame.display.flip()
        #surface32 = font.render(data, True, backcolor)
        #screen.blit(surface32, (surface32X,surface32Y))
        #pygame.display.update()
        return
        
def dtext2(data,h,t):
        surface41 = font.render(data, True, drawColor)
        screen.blit(surface41, [h,t])#(surface41X,surface41Y))#[280, 175])
        pygame.display.update()
        return

def dtext3(data):
        BLUE = (136,196,255)
        surface42 = font.render(data, True, drawColor)
        pygame.draw.rect(screen, BLUE ,[234, 375, 88, 30])# [264, 360], 40)
        screen.blit(surface42, [234,380])#[280, 175])
        pygame.display.flip()
        return
def dtext_temp(data):
        surface41 = font.render(data, True, drawColor)
        screen.blit(surface41, [100,380])#(surface41X,surface41Y))#[280, 175])
        pygame.display.update()
        return
def dtext3(data):
        BLUE = (136,196,255)
        surface42 = font.render(data, True, drawColor)
        pygame.draw.rect(screen, BLUE ,[234, 375, 88, 30])# [264, 360], 40)
        screen.blit(surface42, [234,380])#[280, 175])
        pygame.display.flip()
        return
def dtext_hum(data):
        surface41 = font.render(data, True, drawColor)
        screen.blit(surface41, [100,380])#(surface41X,surface41Y))#[280, 175])
        pygame.display.update()
        return
def dtext3(data):
        BLUE = (136,196,255)
        surface42 = font.render(data, True, drawColor)
        pygame.draw.rect(screen, BLUE ,[234, 375, 88, 30])# [264, 360], 40)
        screen.blit(surface42, [234,380])#[280, 175])
        pygame.display.flip()
        return

###screen.blit(surface1,(surface1X,surface1Y))
###screen.blit(surface2,(surface2X,surface2Y))
#screen.blit(surface3,(surface3X,surface3Y))
#screen.blit(surface4,(surface4X,surface4Y))
#screen.blit(surface5,(surface5X,surface5Y))
#screen.blit(surface6,(surface6X,surface6Y))

#time.sleep(0.02)

#if MPH_Value < 351:
#        MPH_Value = MPH_Value + 1
#else:
#        MPH_Value = 1

#if RPM_Value <= data:#5000
#        RPM_Value = RPM_Value + 30
#else:
#        RPM_Value = RPM_Value-30#10

#if TEMP_Value < 140:
#        TEMP_Value = TEMP_Value + 1
#else:
#        TEMP_Value = 1

#if FUEL_Value < 100:
#        FUEL_Value = FUEL_Value + 1
#else:
#        FUEL_Value = 1


#if MAF_Value < 100:
 #   MAF_Value = MAF_Value + 1.5
#else:
 #   MAF_Value = 1



#if BATT_Value < 18:
 #   BATT_Value = BATT_Value + 0.2
#else:
 #   BATT_Value = 12


#pygame.display.update()
#return 
