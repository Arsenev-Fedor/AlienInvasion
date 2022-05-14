import pygame.font

class Button():
	def __init__(self, ai_game, msg):
		self.screen = ai_game.screen
		self.settings = ai_game.settings
		self.screen_rect = self.screen.get_rect()

		self.width = self.settings.button_width
		self.height = self.settings.button_height
		self.button_color = self.settings.button_color
		self.text_color = self.settings.button_text_color

		self.font = pygame.font.SysFont(None, 48)
		self.rect = pygame.Rect(0, 0, self.width, self.height)
		self.rect.center = self.screen_rect.center
		self._prep_msg(msg)

	def _prep_msg(self, msg):
		self.msg_image = self.font.render(msg, True, self.text_color, self.button_color)
		self.msg_image_rect = self.msg_image.get_rect()
		self.msg_image_rect.center = self.rect.center

	def draw_button(self):
		self.screen.fill(self.button_color, self.rect)
		self.screen.blit(self.msg_image, self.msg_image_rect)