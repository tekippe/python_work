import pygame

class Ship:
	"""A class to manage the ship."""

	def __init__(self,ai_game):
		"""initialize the ship and set its starting position"""
		self.screen = ai_game.screen
		self.screen_rect = ai_game.screen.get_rect()

		self.settings = ai_game.settings

		#load the ship image and get its rect
		self.image = pygame.image.load('images/ship01.bmp')
		self.rect = self.image.get_rect()
		#Start each new ship at the bottom center of the screen
		self.rect.midbottom = self.screen_rect.midbottom
		#movement flags
		self.moving_right = False
		self.moving_left = False
		#Store a decimal value for the ship's h pos
		self.x = float(self.rect.x)

	def blitme(self):
		"""Draw the ship at the current location"""
		self.screen.blit(self.image, self.rect)

	def update(self):
		"""Update ship position based on movement flags"""
		if self.moving_right and self.rect.right < self.screen_rect.right:
			self.x += self.settings.ship_speed
		if self.moving_left and self.rect.left > 0 :
			self.x -= self.settings.ship_speed
		self.rect.x = self.x


