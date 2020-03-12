from game_object import GameObject
from game_stats import GameStats
from player import Player
from settings import Settings


class Bullet(GameObject):
    """ Handle bullet firing """

    def __init__(self, settings: Settings, player: Player, stats: GameStats):
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
