import pygame

class Ship():
	def __init__(self, ai_game):
		self.screen = ai_game.screen
		self.screen_rect = ai_game.screen.get_rect()
		self.image = pygame.image.load("images/ship.bmp")
		self.image = pygame.transform.scale(self.image,(self.screen_rect.width // 12, self.screen_rect.height // 12))
		self.rect = self.image.get_rect()

		self.rect.midbottom = self.screen_rect.midbottom
		self.moving_right = False
		self.moving_left = False
		self.moving_up = False
		self.moving_down = False

		self.x = float(self.rect.x)
		self.y = float(self.rect.y)

		self.speed = ai_game.settings.ship_speed


	def update(self):
		if self.moving_right:
			if self.rect.right < self.screen_rect.width:
				self.x += self.speed
				self.rect.x = self.x
		if self.moving_left:
			if self.rect.left > 0:
				self.x -= self.speed
				self.rect.x = self.x
		if self.moving_up:
			if self.rect.top > 0:
				self.y -= self.speed
				self.rect.y = self.y
		if self.moving_down:
			if self.rect.bottom < self.screen_rect.height :
				self.y += self.speed
				self.rect.y = self.y



	def blitme(self):
		self.screen.blit(self.image, self.rect)

	def center_ship(self):
		self.rect.midright = self.screen_rect.midright
		self.x = float(self.rect.x)
		self.y = float(self.rect.y)
		