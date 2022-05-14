import sys
import pygame

from settings import Settings
from ship import Ship
from bullet import Bullet
from alien import Alien
from triger import Triger
from statistik import Statistik
from button import Button
from scoreboard import Scoreboard
from asteroid import Asteroid



class AlienInvasion:
	def __init__(self):
		pygame.init()
		self.settings = Settings()

		self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height))
		self.settings.screen_width = self.screen.get_rect().width
		self.settings.screen_height = self.screen.get_rect().height
		pygame.display.set_caption("main")

		self.bg_image = pygame.image.load("images/space2.bmp")
		self.bg_image = pygame.transform.scale(self.bg_image, (self.settings.screen_width, self.settings.screen_height))

		self.statistik = Statistik(self)
		self.ship = Ship(self)
		self.triger = Triger(self)
		self.bullets = pygame.sprite.Group()
		self.aliens = pygame.sprite.Group()
		self.sb = Scoreboard(self)
		self.asteroids = pygame.sprite.Group()
		self.asteroid = Asteroid(self)
		self._create_fleet()
		self._create_asteroid()
		self._create_asteroid()
		self._create_asteroid()

		self.play_button = Button(self, "Play")


	def run_game(self):
		while True:
			self._check_events()
			if self.statistik.game_active:
				self.ship.update()
				self.triger.update(self.ship.rect)
				self.update_aliens()
				self.update_asteroids()
				self._update_bullets()

			self._update_screen()


	def _check_events(self):
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				sys.exit()
			elif event.type == pygame.KEYDOWN:
				self._check_keydown_events(event)
			elif event.type == pygame.KEYUP:
				self._check_keyup_events(event)
			elif event.type == pygame.MOUSEBUTTONDOWN:
				mouse_pos = pygame.mouse.get_pos()
				self._check_play_button(mouse_pos)


	def _update_bullets(self):
		self.bullets.update()
		for bullet in self.bullets.copy():
			if bullet.rect.left <= 0:
				self.bullets.remove(bullet)
		self._check_bullet_alien_collisions()


	def _check_bullet_alien_collisions(self):
		collisions = pygame.sprite.groupcollide(self.bullets, self.aliens, True, True)
		if not self.aliens:
			self.bullets.empty()
			self._create_fleet()
			self.settings.increase_speed()
		if collisions:
			self.statistik.score += self.settings.alien_points
			self.sb.prep_score()
			self.sb.check_high_score()


	def _check_keydown_events(self, event):
		if event.key == pygame.K_d:
			self.ship.moving_right = True
		elif event.key == pygame.K_a:
			self.ship.moving_left = True
		elif event.key == pygame.K_s:
			self.ship.moving_down = True
		elif event.key == pygame.K_w:
			self.ship.moving_up = True
		elif event.key == pygame.K_SPACE:
			self._fire_bullet()
		elif event.key == pygame.K_ESCAPE:
			sys.exit()


	def _check_keyup_events(self, event):
		if event.key == pygame.K_d:
			self.ship.moving_right = False
		elif event.key == pygame.K_a:
			self.ship.moving_left = False
		elif event.key == pygame.K_w:
			self.ship.moving_up = False
		elif event.key == pygame.K_s:
			self.ship.moving_down = False


	def _update_screen(self):
		self.screen.blit(self.bg_image, (0, 0))
		self.asteroids.draw(self.screen)
		self.ship.blitme()
		self.triger.blitme()

		for bullet in self.bullets.sprites():
			bullet.draw_bullet()

		self.aliens.draw(self.screen)
		if not self.statistik.game_active:
			self.play_button.draw_button()
		self.sb.show_score()
		pygame.display.flip()


	def _fire_bullet(self):
		if self.statistik.game_active:
			new_bullet = Bullet(self)
			self.bullets.add(new_bullet)


	def update_aliens(self):
		self._check_fleet_edges()
		self.aliens.update()
		if pygame.sprite.spritecollideany(self.ship, self.aliens):
			self._ship_hit()
		self._check_aliens_bottom()


	def _create_fleet(self):
		alien = Alien(self)
		al_w = alien.rect.width
		al_h = alien.rect.height
		avaible_space_y = self.settings.screen_height - (2 * al_h)
		number_aliens_y = avaible_space_y // (2 * al_h)
		number_rows_2 = self.settings.number_rows
		for row_n in range(number_rows_2):
			for alien_number in range(number_aliens_y):
				self._create_alien(alien_number, row_n)


	def _create_alien(self, alien_number, row_n):
		alien = Alien(self)
		al_w, al_h = alien.rect.size
		alien.y = al_w + 2 * al_w * alien_number
		alien.rect.y = alien.y
		alien.x = al_h + 1.5 * al_h * row_n
		alien.rect.x = alien.x
		self.aliens.add(alien)


	def _check_fleet_edges(self):
		for alien in self.aliens:
			if alien.check_edges():
				self.change_fleet_direction()
				break


	def change_fleet_direction(self):
		for alien in self.aliens:
			alien.rect.x += self.settings.drop_speed
		self.settings.fleet_direction *= -1


	def _ship_hit(self):
		if self.statistik.hp > 0:
			self.statistik.hp -= 1

			self.aliens.empty()
			self.bullets.empty()
			
			self._create_fleet()
			self.ship.center_ship()
		
		else:
			self.statistik.game_active = False
			pygame.mouse.set_visible(True)



	def _check_aliens_bottom(self):
		screen_rect = self.screen.get_rect()
		for alien in self.aliens.sprites():
			if alien.rect.right >= screen_rect.right:
				self._ship_hit()
				break


	def _check_play_button(self, mouse_pos):
		button_clicked = self.play_button.rect.collidepoint(mouse_pos)
		if button_clicked and not self.statistik.game_active:
			self.settings.initialize_dynamic_settings()
			self.statistik.reset_stats()
			self.statistik.game_active = True
			self.aliens.empty()
			self.bullets.empty()

			self._create_fleet()
			self.ship.center_ship()
			pygame.mouse.set_visible(False)

			self.sb.prep_score()


	def update_asteroids(self):
		self.asteroids.update()
		self._position_asteroid_check()


	def _create_asteroid(self):
		self.asteroids.add(self.asteroid)


	def _position_asteroid_check(self):
		for asteroid in self.asteroids.copy():
			if self.asteroid.rect.left <= -100:
				self.asteroids.remove(self.asteroid)
				self._create_asteroid()



if __name__ == '__main__':
	ai = AlienInvasion()
	ai.run_game() 