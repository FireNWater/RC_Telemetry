

class TFT_Display(object):
 	"""This class will handle the graphics display"""
 	def __init__(self):
 		import pygame, sys, os
 		from pygame.locals import *
		pygame.init()
 		self.os.environ["SDL_FBDEV"] = "/dev/fb1"	#direct output to TFT screen
		self.TFT_Display_Width  = 320 
		self.TFT_Display_Height = 240
		self.DISPLAYSURF = pygame.display.set_mode((TFT_Display_Width, TFT_Display_Height))
		self.pygame.display.set_caption('Ground Station')

		self.text_color = pygame.Color(0, 0, 0)
		self.bg_color = pygame.Color(0, 255, 255)
		self.GREEN = pygame.Color(0, 255, 0)

		self.wingsLevel = pygame.image.load('WingsLevelSymbol.png')
		self.airplaneSymbol = pygame.image.load('AirplaneSymbol.png')

		self.fontObj = pygame.font.Font('freesansbold.ttf', 16)

	def update_screen(self):

		self.calibrationText = fontObj.render('Calibration Status', True, text_color, GREEN)
		self.DISPLAYSURF.fill(bg_color)
		self.DISPLAYSURF.blit(wingsLevel, (10,110))											#Placeholder for testing
		self.DISPLAYSURF.blit(calibrationText, (20, 20))

		self.pygame.display.update()

	def check_for_quit(self):
		for event in self.pygame.event.get():
		if event.type == QUIT:
			self.pygame.quit()
			return True
		else return False

