import os, sys
import pygame, sys, os
from pygame.locals import *
import xbeedata as xb

telemetry = xb.XbeeData()

os.environ["SDL_FBDEV"] = "/dev/fb1"	#direct output to TFT screen

pygame.init()

TFT_Display_Width, TFT_Display_Height = 320, 240

screenCenter = (TFT_Display_Width / 2, TFT_Display_Height / 2)
compassCenter = (260,45)

DISPLAYSURF = pygame.display.set_mode((TFT_Display_Width, TFT_Display_Height))

text_color = pygame.Color(0, 0, 0)
bg_color = pygame.Color(0, 255, 255)
GREEN = pygame.Color(0, 255, 0)

wingsLevel = pygame.image.load('WingsLevelSymbol.png').convert_alpha()
wingSymbol = [] 
for rotation in range(90, -90, -1):
	wingSymbol.append(pygame.transform.rotate(wingsLevel, rotation))

airplaneSymbol = pygame.image.load('AirplaneSymbol.png').convert_alpha()
compassSymbol = []
for rotation in range(360, 0, -1):
	compassSymbol.append(pygame.transform.rotate(airplaneSymbol, rotation))

fontObj = pygame.font.Font('freesansbold.ttf', 16)

telemetry.update_data()		#Fill data buffer
telemetry.update_data()		#Fill data buffer

while True: # main game loop
	
	for event in pygame.event.get():
			if (event.type == QUIT):
				pygame.quit()
				sys.exit()
	
	DISPLAYSURF.fill(bg_color)

	rollText = fontObj.render("Roll: " + telemetry.roll, True, text_color, bg_color)			
	DISPLAYSURF.blit(rollText, (20, 5))
	pitchText = fontObj.render("Pitch: " + telemetry.pitch, True, text_color, bg_color)			
	DISPLAYSURF.blit(pitchText, (20, 25))
	headingText = fontObj.render("Mag Hdg: " + telemetry.magnetic_heading, True, text_color, bg_color)			
	DISPLAYSURF.blit(headingText, (20, 45))

	latitudeText = fontObj.render("Lat: " + telemetry.latitude, True, text_color, bg_color)			
	DISPLAYSURF.blit(latitudeText, (20, 220))
	longitudeText = fontObj.render("Long: " + telemetry.longitude, True, text_color, bg_color)			
	DISPLAYSURF.blit(longitudeText, (150, 220))

	calibrationText = fontObj.render("Calibration: " + telemetry.calibration_system, True, text_color, bg_color)			
	DISPLAYSURF.blit(calibrationText, (20, 200))

	wingRectObject = wingSymbol[int(float(telemetry.roll)) + 90].get_rect()
	wingRectObject.center = screenCenter
	DISPLAYSURF.blit(wingSymbol[int(float(telemetry.roll)) + 90], wingRectObject)
	pygame.draw.line(DISPLAYSURF, text_color, (0, screenCenter[1]), (TFT_Display_Width, screenCenter[1]), 2)

	compassRectObj = compassSymbol[int(float(telemetry.magnetic_heading))].get_rect()
	compassRectObj.center = compassCenter
	DISPLAYSURF.blit(compassSymbol[int(float(telemetry.magnetic_heading))], compassRectObj)
	pygame.draw.circle(DISPLAYSURF, text_color, compassCenter, 20, 2)
	compassNText = fontObj.render("N", True, text_color, bg_color)			
	DISPLAYSURF.blit(compassNText, (compassCenter[0]-5, compassCenter[1]-35))

	pygame.display.update()
	telemetry.update_data()