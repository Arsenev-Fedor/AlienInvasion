import pygame


class Images_transforming():
		def __init__(self):
			self.bg_image = pygame.image.load("images/space2.bmp")
			self.bg_image = pygame.transform.scale(self.bg_image, (self.settings.screen_width, self.settings.screen_height))