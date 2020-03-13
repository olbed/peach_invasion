import sys
from random import random
from time import sleep

import pygame

from game_objects.bullet import Bullet
from game_objects.enemy import Enemy
from game_objects.player import Player
from movement.falling_sideways_shacking import FallingSidewaysShacking
from movement.straigt_up import StraightUp
from settings import Settings
from ui.background import Background
from ui.button import Button
from ui.scoreboard import Scoreboard
from ui.sound import Sound
from ui.stats import Stats


class Game:
    """ Manages game assets and logic """

    # movement.snake.Snake or movement.falling_sideways.FallingSidewaysShacking
    enemy_movement_scheme = FallingSidewaysShacking

    bullet_movement_scheme = StraightUp

    def __init__(self):
        self.settings = Settings()
        self.sound = Sound(self.settings)

        pygame.init()
        self.sound.load()

        # Set up the game window
        self.screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
        self.rect = self.screen.get_rect()

        # Statistics and current state
        self.scoreboard = Scoreboard(self.settings, self.screen)
        self.stats = Stats(self.settings, self.scoreboard)

        # Game elements
        self.background = Background(self.settings, self.screen)
        self.player = Player(self.settings, self.screen, self.stats)
        self.bullets = pygame.sprite.Group()
        self.enemies = pygame.sprite.Group()

        # Buttons
        self.play_btn = Button(self.settings, self.screen, "Play")

        # Flags
        self.game_active = False

    def run(self):
        """ The main loop of the game """
        while True:
            self._check_events()

            if self.game_active:
                self._update_elements()

            # Hide mouse when game is active and show if not
            pygame.mouse.set_visible(not self.game_active)

            self._redraw_screen()

    def _check_events(self):
        """ Respond to all keyboard and mouse events """
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                self._handle_keydown(event.key)
            elif event.type == pygame.KEYUP:
                self._handle_keyup(event.key)
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                self._check_play_btn(mouse_pos)

    def _handle_keydown(self, key):
        """ Respond to key press """
        if key == pygame.K_RIGHT:
            self.player.moving_right = True
        elif key == pygame.K_LEFT:
            self.player.moving_left = True
        elif key == pygame.K_SPACE:
            self._fire_bullet()
        elif key == pygame.K_ESCAPE:
            sys.exit()
        elif key == pygame.K_RETURN:
            self._play()

    def _handle_keyup(self, key):
        """ Respond to key release """
        if key == pygame.K_RIGHT:
            self.player.moving_right = False
        elif key == pygame.K_LEFT:
            self.player.moving_left = False

    def _update_elements(self):
        """ Updates all elements position and status """
        self.player.update()
        self._update_bullets()
        self._update_enemies()

    def _redraw_screen(self):
        """ Redraw all elements and flip to the new screen """
        self.background.draw()
        self.enemies.draw(self.screen)
        self.bullets.draw(self.screen)
        self.player.draw()
        self.scoreboard.draw()

        if not self.game_active:
            self.play_btn.draw()

        pygame.display.flip()

    def _fire_bullet(self):
        if self.stats.ammo:
            new_bullet = Bullet(self.settings, self.screen, self.player,
                                self.stats, self.bullet_movement_scheme)
            self.bullets.add(new_bullet)
            self.sound.fire.play()
        else:
            self.sound.no_ammo.play()

    def _update_bullets(self):
        """ Update position of all bullets and get rid of old ones """
        self.bullets.update()

        # Get rid of bullets that are out of screen
        for bullet in self.bullets.copy():
            if bullet.rect.bottom <= 0:
                self.bullets.remove(bullet)

        # After deleting invisible bullets recount ammo
        self.stats.ammo = self.settings.ammo_limit - len(self.bullets)

        self._check_for_bullet_enemy_collisions()

    def _check_for_bullet_enemy_collisions(self):
        """ Check if any bullet hit any enemy """
        collisions = pygame.sprite.groupcollide(self.bullets, self.enemies, True, True)
        if not collisions:
            # No collisions - nothing to do
            return

        self.sound.enemy_death.play()

        # Score up for all killed enemies
        for enemies in collisions.values():
            self.stats.score_up(len(enemies))

        # Create new group of enemies if there is no more left
        if not self.enemies:
            self.sound.victory.play()
            self.stats.level_up()
            self._new_round()

    def _has_enemy_reach_bottom(self):
        """ Checks if eny enemy has reached the bottom of the game screen """
        for enemy in self.enemies:
            if enemy.rect.bottom >= self.rect.bottom:
                return True

    def _round_failed(self):
        """ Respond to the player being hit by an enemy """
        self.stats.player_lost_life()
        self.sound.death.play()

        # Game over scenario
        if self.stats.health == 0:
            self.game_active = False
            return

        sleep(.5)
        self._new_round()

    def _new_round(self):
        self.enemies.empty()
        self.bullets.empty()

        self._create_enemies()
        self.player.center_player()

    def _create_enemies(self):
        """ Create the enemies """
        # Prepare width and height of objects
        enemy_w, enemy_h = Enemy(self.settings, self.screen, self.stats, self.enemy_movement_scheme).rect.size
        screen_w, screen_h = self.rect.size
        player_h = self.player.rect.height
        margin_x, margin_y = enemy_w, enemy_h

        # Count how many enemies fit on the screen horizontally
        available_space_x = screen_w - (2 * margin_x)
        number_enemies_x = available_space_x // (enemy_w + margin_x)

        # Count how many enemies fit on the screen vertically
        available_space_y = (screen_h - player_h) * .8  # 80% of free space
        number_enemies_y = int(available_space_y) // (enemy_h + margin_y)

        # Create enemies
        for enemy_number_y in range(number_enemies_y):
            for enemy_number_x in range(number_enemies_x):
                if random() < self.settings.enemy_density:
                    self._create_enemy(enemy_number_x, enemy_number_y, margin_x, margin_y)

    def _create_enemy(self, enemy_number_x, enemy_number_y, margin_x, margin_y):
        """ Create an enemy and place it """
        enemy = Enemy(self.settings, self.screen, self.stats, self.enemy_movement_scheme)
        enemy_w, enemy_h = enemy.rect.size

        # If enemy movement is set to FallingSidewaysShacking create only one row visible
        # and others are hidden up the screen
        if self.enemy_movement_scheme == FallingSidewaysShacking:
            enemy_number_y *= -1

        x = margin_x + ((enemy_w + margin_x) * enemy_number_x)
        y = (enemy_h + margin_y) * enemy_number_y
        enemy.set_initial_position(x, y)

        self.enemies.add(enemy)

    def _update_enemies(self):
        """ Update all enemies positions """
        self.enemies.update()

        # Check for player-enemy collisions and
        if pygame.sprite.spritecollideany(self.player, self.enemies):
            self._round_failed()

        # Check if enemy has reached the screen bottom
        if self._has_enemy_reach_bottom():
            self._round_failed()

    def _check_play_btn(self, mouse_pos):
        if self.play_btn.rect.collidepoint(mouse_pos):
            self._play()

    def _play(self):
        if self.game_active:
            # If game is already active don't restart
            return

        self._new_round()
        self.stats.reset()
        self.game_active = True


if __name__ == '__main__':
    Game().run()
