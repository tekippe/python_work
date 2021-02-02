class Settings:
	"""A Class to store all settings for Alien Invasion"""

	def __init__(self):
		"""inistialize game's settings"""
		# Screen Settings
		self.screen_width = 1200
		self.screen_height = 800
		self.bg_color = (0, 0, 0)
		self.ship_speed = 1.5

		#Bullet Settings
		self.bullet_speed = 1.0
		self.bullet_width = 3
		self.bullet_height = 15
		self.bullet_color = (255,0,170)
		self.bullets_allowed = 3

		#alien settings
		self.alien_speed = 1.0
		self.fleet_drop_speed = 10
		self.fleet_direction = 1