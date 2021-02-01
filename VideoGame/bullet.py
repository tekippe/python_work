import pygame
from pygame.sprite import sprite

class Bullet(Sprite):
	"""A Class to manage bullets fired from the ship"""
	super().__init__()
	self.screen = ai_game.screen
	self.settings = ai_game.settings
	self.color = self.settings.bullet_color

	self.rect = pygame.Rect(0, 0, self.settings.bullet_width. 
		self.settings.bullet_height)
	self.rect.midtop = ai_game.ship.rect.midtop

	#store bullet's pos as a decimal
	self.y = floar(self.rect.y)

	def update(self):
		""" move the bullet up the screen"""
		#Update the decimal position of the bullet
		self.y -= self.settings.bullet_speed
		#Update the rect pos
		self.rect.y = self.y

	def draw bullet(self):
		pygame.draw.rect(self.screen, self.color, self.rect)
		