from random import random
from typing import Type

from pygame import Surface

from peach_invasion.game_objects.object import Object
from peach_invasion.movement.scheme import Scheme
from peach_invasion.settings import Settings
from peach_invasion.ui.stats import Stats


class Enemy(Object):
    """ Handles single enemy """

    def __init__(self, settings: Settings, screen: Surface, stats: Stats,
                 movement_scheme: Type[Scheme]):
        super().__init__(settings.image_absolute_path(settings.enemy_image))

        # Init enemy movement scheme
        self._movement_scheme = movement_scheme(self.rect, screen.get_rect())
        self._movement_scheme.speed = stats.enemy_speed

    def update(self):
        """ Moves enemy as described by movement scheme """
        self._movement_scheme.move()

    def set_xy_position(self, x, y):
        """ Sets position of the enemy by its x,y coordinates """
        self._movement_scheme.position = (x, y)

    def set_col_row_position(self, col, row):
        """ Sets position of the enemy by its row and col number """
        enemy_w, enemy_h = self.rect.size
        x = enemy_w + (2 * enemy_w * col)
        y = -2 * enemy_h * row
        self.set_xy_position(x, y)

    @staticmethod
    def create_all(settings: Settings, screen: Surface, stats: Stats, movement_scheme: Type[Scheme]):
        """ Create the number of enemies that fits on the screen """
        # Prepare width and height of objects
        enemy_w, enemy_h = Enemy(settings, screen, stats, movement_scheme).rect.size
        screen_w, screen_h = screen.get_rect().size

        # Count how many enemies fit on the screen horizontally
        available_space_x = screen_w - (2 * enemy_w)
        cols = available_space_x // (2 * enemy_w)

        # Count how many enemies fit on the screen vertically
        available_space_y = screen_h * settings.enemy_vertical_space_occupied
        rows = int(available_space_y) // (2 * enemy_h)

        # Create enemies
        for row in range(rows):
            for col in range(cols):
                if random() < settings.enemy_density:
                    enemy = Enemy(settings, screen, stats, movement_scheme)
                    enemy.set_col_row_position(col, row)
                    yield enemy
