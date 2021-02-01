class Settings:
	"""A Class to store all settings for Alien Invasion"""

	def __init__(self):
		"""inistialize game's settings"""
		# Screen Settings
		self.screen_width = 1200
		self.screen_height = 800
		self.bg_color = (230, 230, 230)
		self.ship_speed = 1.5

		#Bullet Settings
		self.bullet_speed = 1.0
		self.bullet_width = 3
		self.bullet_height = 15
		self.bullet_color = (255,0,170)