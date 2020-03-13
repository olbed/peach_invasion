from typing import Type

from pygame import Surface

from game_objects.object import Object
from movement.scheme import Scheme
from settings import Settings
from ui.stats import Stats


class Enemy(Object):
    """ Handles single enemy """

    def __init__(self, settings: Settings, screen: Surface, stats: Stats,
                 movement_scheme: Type[Scheme]):
        super().__init__(settings.enemy_image)

        # Init enemy movement scheme
        self._movement_scheme = movement_scheme(self.rect, screen.get_rect(), stats.enemy_speed)

    def set_initial_position(self, x, y):
        """ Sets position where enemy will start moving """
        self._movement_scheme.position = (x, y)

    def update(self):
        """ Moves enemy as described by movement scheme """
        self._movement_scheme.move()
