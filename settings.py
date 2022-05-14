import random

class Settings():

	def __init__(self):
		self.screen_width = 800
		self.screen_height = 600

		self.bullet_h_speed = 1.05
		self.bullet_width = 15
		self.bullet_height = 6
		self.bullet_color = (88, 0, 0)

		self.drop_speed = 10
		self.number_rows = 4

		self.ship_limit = 2

		self.button_width = 200
		self.button_height = 50
		self.button_color = (0, 255, 0)
		self.button_text_color = (255, 255, 255)

		self.speedup_scale = 1.3
		self.initialize_dynamic_settings()

		self.triger_speed = 1
		self.ship_speed = 0.2
		self.bullet_speed = 1.0
		self.alien_points_increase = 5


	def initialize_dynamic_settings(self):
		self.alien_speed_factor = 0.09
		self.fleet_direction = 1
		self.alien_points = 50


	def increase_speed(self):
		self.alien_speed_factor *= self.speedup_scale
		self.alien_points += self.alien_points_increase



	
	  