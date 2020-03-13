from pygame import Surface

from game_object import GameObject
from game_stats import GameStats
from settings import Settings


class Enemy(GameObject):
    """ Handles single enemy """

    def __init__(self, settings: Settings, screen: Surface, stats: GameStats, movement_scheme):
        super().__init__(settings.enemy_image)

        self._movement_scheme = movement_scheme(self.rect, screen.get_rect(), stats.enemy_speed)

    def set_initial_position(self, x, y):
        """ Sets position where enemy will start moving """
        self._movement_scheme.position = (x, y)

    def update(self):
        self._movement_scheme.check()
        self._movement_scheme.move()
