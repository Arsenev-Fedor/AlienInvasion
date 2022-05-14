import pygame

class Triger():
	def __init__(self, ai_game):
		super().__init__()
		self.settings = ai_game.settings
		self.screen = ai_game.screen

		self.screen_rect = ai_game.screen.get_rect()
		self.image = pygame.image.load('images/triger.bmp')
		self.image = pygame.transform.scale(self.image,(self.screen_rect.width // 12, self.screen_rect.height // 12))
		self.rect = self.image.get_rect()
		self.x = float(self.rect.x)
		self.y = float(self.rect.y)


	def update(self, rect):
		self.ship_position_x = rect.x
		self.ship_position_y = rect.y

		self.x += self.settings.triger_speed
		self.rect.x = self.x


	def blitme(self):
		self.screen.blit(self.image, self.rect)