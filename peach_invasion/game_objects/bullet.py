from pygame.surface import Surface

from peach_invasion.game_objects.object import Object
from peach_invasion.game_objects.player import Player
from peach_invasion.movement.scheme import Scheme
from peach_invasion.settings import Settings
from peach_invasion.ui.stats import Stats


class Bullet(Object):
    """ Handle bullet firing """

    def __init__(self, settings: Settings, screen: Surface, player: Player, stats: Stats):
        super().__init__(settings.image_absolute_path(settings.bullet_image))

        # Init bullet movement scheme
        self._movement_scheme = Scheme(self.rect, screen.get_rect())
        self._movement_scheme.speed = stats.bullet_speed

        # Set bullet's start position
        x, y = player.rect.midtop
        x -= self.rect.width / 2
        self._movement_scheme.position = x, y

    def update(self):
        """ Move the bullet up the screen """
        self._movement_scheme.move()
