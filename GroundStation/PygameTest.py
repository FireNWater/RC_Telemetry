import pygame, sys, os
from pygame.locals import *
import serial
 
os.environ["SDL_FBDEV"] = "/dev/fb1"											#direct output to TFT screen
dataPackage = serial.Serial('/dev/ttyUSB0', 9600, timeout = 1)		#Collect incoming xBee data from USB port

TFT_Display_Width, TFT_Display_Height = 320, 240

pygame.init()
DISPLAYSURF = pygame.display.set_mode((TFT_Display_Width, TFT_Display_Height))

text_color = pygame.Color(0, 0, 0)
bg_color = pygame.Color(0, 255, 255)
GREEN = pygame.Color(0, 255, 0)

wingsLevel = pygame.image.load('WingsLevelSymbol.png')
airplaneSymbol = pygame.image.load('AirplaneSymbol.png')

fontObj = pygame.font.Font('freesansbold.ttf', 16)
calibrationText = fontObj.render('Calibration Status', True, text_color, GREEN)

pygame.display.set_caption('Hello World!')

DISPLAYSURF.fill(bg_color)
DISPLAYSURF.blit(wingsLevel, (10,110))											#Placeholder for testing
DISPLAYSURF.blit(calibrationText, (20, 20))

while True: # main game loop

	for event in pygame.event.get():
		if event.type == QUIT:
			pygame.quit()
			sys.exit()
	
	data = dataPackage.readline()
	
	if (len(data) > 0):
		dataText = fontObj.render(data, True, text_color, GREEN)
		DISPLAYSURF.blit(dataText, (20, 50))
	
	pygame.display.update()
