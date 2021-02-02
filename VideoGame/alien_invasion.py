import sys

import pygame

from settings import Settings
from ship import Ship
from bullet import Bullet
from alien import Alien

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
		self.bullets = pygame.sprite.Group()
		self.aliens = pygame.sprite.Group()
		self._create_fleet()
		

	def run_game(self):
		"""Start the main loop of the game"""
		while True:
			self._check_events()
			self.ship.update()
			self.bullets.update()
			self._update_bullets()
			self._update_aliens()
			self._update_screen()

	def _check_events(self):
		"""respond to keypress and mouse events"""
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				sys.exit()
			elif event.type == pygame.KEYDOWN:
				self._check_keydown_events(event)
			elif event.type == pygame.KEYUP:
				self._check_keyup_events(event)
			
	def _check_keydown_events(self, event):
		if event.type == pygame.KEYDOWN:	
			if event.key == pygame.K_RIGHT:
					#move ship to the right
					self.ship.moving_right = True
			elif event.key == pygame.K_LEFT:
					self.ship.moving_left = True
			elif event.key == pygame.K_q:
				sys.exit()
			elif event.key == pygame.K_SPACE:
				self._fire_bullet()

	def _check_keyup_events(self, event):
		if event.type == pygame.KEYUP:
				if event.key == pygame.K_RIGHT:
					self.ship.moving_right = False
				elif event.key == pygame.K_LEFT:
					self.ship.moving_left = False			

	def update(self):
		if self.moving_right:
			self.ship.rect.x += 1
		elif self.moving_left:
			self.ship.rect.x -= 1

	def _update_bullets(self):
		#update bullets positions
		self.bullets.update()
		#get rid of bullets that are off-screen
		for bullet in self.bullets.copy():
				if bullet.rect.bottom <= 0:
					self.bullets.remove(bullet)
		collisions = pygame.sprite.groupcollide(self.bullets, self.aliens,True,True)

		if not self.aliens:
			#Destroy existing bullets and create a new fleet
			self.bullets.empty()
			self._create_fleet()
			#print(len(self.bullets))

	def _update_aliens(self):
		"""Update positions of all aliens in the fleet"""
		self._check_fleet_edges()
		self.aliens.update()

	def _create_fleet(self):
		#make an alien
		alien = Alien(self)	
		alien_width, alien_height = alien.rect.size
		ship_height = self.ship.rect.height
		available_space_x = self.settings.screen_width - (2*alien_width)
		available_space_y = (self.settings.screen_height - 
					(3 *alien_height) - ship_height)
		number_rows = available_space_y//(2*alien_height)
		number_aliens_x = available_space_x//(2*alien_width)
		print(number_aliens_x)
		#Create Fleet of Alien Ships
		for row_number in range(number_rows):
			for alien_number in range(number_aliens_x):
				self._create_alien(alien_number, row_number)

	def _check_fleet_edges(self):
		"""Respond if any aliens have reached an edge"""
		for alien in self.aliens.sprites():
			if alien.check_edges():
				self._change_fleet_direction()
				break

	def _change_fleet_direction(self):
		"""Drop the entire fleet and change the fleet's direction"""
		for alien in self.aliens.sprites():
			alien.rect.y += self.settings.fleet_drop_speed
		self.settings.fleet_direction *= -1
			

	def _create_alien(self, alien_number, row_number):
		alien = Alien(self)	
		alien_width = alien.rect.width
		alien.x = alien_width+2*alien_width*alien_number
		alien.rect.x = alien.x
		alien.rect.y = alien.rect.height +2*alien.rect.height*row_number
		self.aliens.add(alien)

	def _update_screen(self):
		"""Update images on the screen and flip to a new screen"""
		self.screen.fill(self.settings.bg_color)
		self.ship.blitme()
		for bullet in self.bullets.sprites():
			bullet.draw_bullet()
		self.aliens.draw(self.screen)


		pygame.display.flip()


	def _fire_bullet(self):
		if len(self.bullets) < self.settings.bullets_allowed:
			new_bullet = Bullet(self)
			self.bullets.add(new_bullet)


if __name__ == '__main__':
	#make a game instance and run the game
	ai = AlienInvasion()
	ai.run_game()
