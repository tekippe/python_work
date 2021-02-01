import sys

import pygame

from settings import Settings
from ship import Ship

class AlienInvasion:
	"""Overall class to manage game assets and behavior"""

	def __init__(self):
		"""initialize the game and create game resources."""
		pygame.init()
		self.settings = Settings()

		self.screen = pygame.display.set_mode(
			(self.settings.screen_width, self.settings.screen_height))

		#self.sreen = pygame.display.set_mode((1200, 800))
		pygame.display.set_caption("Alien Invasion")

		self.ship = Ship(self)
		

	def run_game(self):
		"""Start the main loop of the game"""
		while True:
			self._check_events()
			self.ship.update()
			self._update_screen()

	def _check_events(self):
		"""respond to keypress and mouse events"""
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				sys.exit()
			elif event.type == pygame.KEYDOWN:
				if event.key == pygame.K_RIGHT:
					#move ship to the right
					self.ship.moving_right = True
				elif event.key == pygame.K_LEFT:
					self.ship.moving_left = True
			elif event.type == pygame.KEYUP:
				if event.key == pygame.K_RIGHT:
					self.ship.moving_right = False
				elif event.key == pygame.K_LEFT:
					self.ship.moving_left = False
		
					

	def update(self):
		if self.moving_right:
			self.ship.rect.x += 1
		elif self.moving_left:
			self.ship.rect.x -= 1

	def _update_screen(self):
		"""Update images on the screen and flip to a new screen"""
		self.screen.fill(self.settings.bg_color)
		self.ship.blitme()

		pygame.display.flip()


if __name__ == '__main__':
	#make a game instance and run the game
	ai = AlienInvasion()
	ai.run_game()
