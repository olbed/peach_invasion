from game_objects.object import Object
from game_objects.player import Player
from settings import Settings
from ui.stats import Stats


class Bullet(Object):
    """ Handle bullet firing """

    def __init__(self, settings: Settings, player: Player, stats: Stats):
        super().__init__(settings.bullet_image)

        self._stats = stats

        # Set bullet's start position
        self.rect.midtop = player.rect.midtop

        # Store a float value for higher accuracy updating
        self._y = float(self.rect.y)

    def update(self):
        """ Move the bullet up the screen """
        self._y -= self._stats.bullet_speed
        self.rect.y = self._y
