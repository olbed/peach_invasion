from typing import Type

from pygame.surface import Surface

from game_objects.object import Object
from game_objects.player import Player
from movement.scheme import Scheme
from settings import Settings
from ui.stats import Stats


class Bullet(Object):
    """ Handle bullet firing """

    def __init__(self, settings: Settings, screen: Surface, player: Player,
                 stats: Stats, movement_scheme: Type[Scheme]):
        super().__init__(settings.bullet_image)

        # Init bullet movement scheme
        self._movement_scheme = movement_scheme(self.rect, screen.get_rect(), stats.bullet_speed)

        # Set bullet's start position
        x, y = player.rect.midtop
        x -= self.rect.width / 2
        self._movement_scheme.position = x, y

    def update(self):
        """ Move the bullet up the screen """
        self._movement_scheme.move()
