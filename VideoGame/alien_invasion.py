import sys

import pygame

class AlienInvasion:
	"""Overall class to manage game assets and behavior"""

	def __init__(self):
		"""initialize the game and create game resources."""
		pygame.init()

		self.sreen = pygame.display.set_mode((1200, 800))
		pygame.display.set_caption("Alien Invasion")
		#set bg color
		self.bg_color = (230, 230, 230)

	def run_game(self):
		"""Start the main loop of the game"""
		while True:
			#Watch for keyboard and mouse events
			for event in pygame.event.get():
					if event.type == pygame.QUIT:
						sys.exit()
			#redraw the screen on each pass through the loop
			self.screen.fill(self.bg_color)
			#render most recently drawn screen
			pygame.display.flip()

if __name__ == '__main__':
	#make a game instance and run the game
	ai = AlienInvasion()
	ai.run_game()
