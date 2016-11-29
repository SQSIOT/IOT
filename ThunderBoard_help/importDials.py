#!/usr/bin/python

import os
import time
import sys
import dials as dd
import pygame
from pygame.locals import *

#class gauageNeed()
def ddial():

    os.environ['SDL_VIDEO_WINDOW_POS'] = 'center'

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
    surface3FullscreenX = (monitorX / 2) + 0
    surface3FullscreenY = (monitorY / 2) - 240

    surface3WindowedX = (width / 2) - 0
    surface3WindowedY = (height / 2) - 290

    surface3X = surface3WindowedX
    surface3Y = surface3WindowedY

    #fuel
    surface4FullscreenX = (monitorX / 2) + 310
    surface4FullscreenY = (monitorY / 2) - 240

    surface4WindowedX = (width / 2) - 310
    surface4WindowedY = (height / 2) - 290

    surface4X = surface4WindowedX
    surface4Y = surface4WindowedY

    #rpm
    surface5FullscreenX = (monitorX / 2) - 310
    surface5FullscreenY = (monitorY / 2) + 60

    surface5WindowedX = (width / 2) - 310
    surface5WindowedY = (height / 2) + 10    ##to horizontal

    surface5X = surface5WindowedX
    surface5Y = surface5WindowedY

    #speed
    surface6FullscreenX = (monitorX / 2) + 10
    surface6FullscreenY = (monitorY / 2) + 60

    surface6WindowedX = (width / 2) + 10
    surface6WindowedY = (height / 2) + 10   ##to horizontal

    surface6X = surface6WindowedX
    surface6Y = surface6WindowedY

    screen = pygame.display.set_mode((size),pygame.HWSURFACE | pygame.DOUBLEBUF)

    #surface1 = pygame.Surface((1300,680))
    #surface2 = pygame.Surface((1000,600))
    surface3 = pygame.Surface((340,340))
    surface4 = pygame.Surface((340,340))
    surface5 = pygame.Surface((300,300))
    surface6 = pygame.Surface((300,300))

    #surface1.set_colorkey(0x0000FF)
    #surface2.set_colorkey(0x0000FF)
    surface3.set_colorkey(0x0000FF)
    surface4.set_colorkey(0x0000FF)
    surface5.set_colorkey(0x0000FF)
    surface6.set_colorkey(0x0000FF)

    screen.fill(0x000000)

    MPH_Value = 0
    RPM_Value = 0
    TEMP_Value = 0
    #BATT_Value = 0
    FUEL_Value = 0
    #MAF_Value = 0

    while True:

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
            surface3.fill(0x0000FF)
            surface4.fill(0x0000FF)
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
            dd.Dials(needleDestination=surface3,
                            needleValue=TEMP_Value,startPosition=-45,endPosition=45,
                            maximumValue=14,dialType=dd.degree,dialLabel="Coolant Temp",backgroundColour=(0,0,81),displayCircle=True,foregroundColour=(255,255,255))

            dd.Dials(needleDestination=surface4,
                            needleValue=FUEL_Value,startPosition=-45,endPosition=45,maximumValue=10,
                            dialType=dd.percent,dialLabel="Fuel",backgroundColour=(0,0,81),displayCircle=True,foregroundColour=(255,255,255))


            dd.Dials(needleDestination=surface5,
                            needleValue=RPM_Value,startPosition=-45,endPosition=45,
                            maximumValue=500,dialType=dd.rpm,dialLabel="RPM",backgroundColour=(0,0,81),displayCircle=True,foregroundColour=(255,255,255))

            dd.Dials(needleDestination=surface6,
                            needleValue=MPH_Value,startPosition=-45,endPosition=45,maximumValue=40,
                            dialType=dd.volt,dialLabel="Speed",backgroundColour=(0,0,81),displayCircle=True,foregroundColour=(255,255,255))


            #screen.blit(surface1,(surface1X,surface1Y))
            #screen.blit(surface2,(surface2X,surface2Y))
            screen.blit(surface3,(surface3X,surface3Y))
            screen.blit(surface4,(surface4X,surface4Y))
            screen.blit(surface5,(surface5X,surface5Y))
            screen.blit(surface6,(surface6X,surface6Y))

            #time.sleep(0.02)

            if MPH_Value < 351:
                    MPH_Value = MPH_Value + 1
            else:
                    MPH_Value = 1

            if RPM_Value < 5000:
                    RPM_Value = RPM_Value + 30
            else:
                    RPM_Value = 10

            if TEMP_Value < 140:
                    TEMP_Value = TEMP_Value + 1
            else:
                    TEMP_Value = 1

            if FUEL_Value < 100:
                    FUEL_Value = FUEL_Value + 1
            else:
                    FUEL_Value = 1


            #if MAF_Value < 100:
             #   MAF_Value = MAF_Value + 1.5
            #else:
             #   MAF_Value = 1

            

            #if BATT_Value < 18:
             #   BATT_Value = BATT_Value + 0.2
            #else:
             #   BATT_Value = 12

            
            pygame.display.update()

    return None
