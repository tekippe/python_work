import pygame
from pygame.sprite import Sprite
import random

class Alien(Sprite):

	def __init__(self, ai_game):
		super().__init__()
		self.screen = ai_game.screen
		self.settings = ai_game.settings
		self.image_urls = ['images/alien01.bmp','images/alien02.bmp','images/alien03.bmp','images/alien04.bmp','images/alien05.bmp','images/alien06.bmp']
		self.image = pygame.image.load(random.choice(self.image_urls))
		self.rect = self.image.get_rect()

		self.rect.x = self.rect.width
		self.rect.y = self.rect.height

		#store alien's h pos
		self.x = float(self.rect.x)

	def check_edges(self):
		screen_rect = self.screen.get_rect()
		if self.rect.right >= screen_rect.right or self.rect.left <= 0:
			return True

	def update(self):
		self.x += (self.settings.alien_speed * self.settings.fleet_direction)
		self.rect.x = self.x


