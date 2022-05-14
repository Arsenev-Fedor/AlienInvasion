import pygame
from pygame.sprite import Sprite
import random

class Asteroid(Sprite):
	def __init__(self, ai_game):
		super().__init__()
		self.screen = ai_game.screen
		self.screen_rect = self.screen.get_rect()

		self.image = pygame.image.load("images/asteroid.bmp")
		self.image = pygame.transform.scale(self.image,
			(ai_game.settings.screen_width // 8, ai_game.settings.screen_height // 6))
		
		self.rect = self.image.get_rect()

		self.rect.x = self.rect.width
		self.rect.y = self.rect.height

		self.rect.x = 900
		self.rect.y = random.randint(0, 600)

		self.x = float(self.rect.x)
		self.y = float(self.rect.y)
		self.settings = ai_game.settings
		self.speed_asteroid_factor = False


	def update(self):
		self.asteroid_speed_random = random.randint(20, 21) #1, 15
		self.asteroid_speed = self.asteroid_speed_random / 100
		
		self.x -= self.asteroid_speed
		self.rect.x = self.x

