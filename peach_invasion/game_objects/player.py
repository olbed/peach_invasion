from pygame import Surface

from peach_invasion.game_objects.object import Object
from peach_invasion.settings import Settings
from peach_invasion.ui.stats import Stats


class Player(Object):
    """ Represents player """

    def __init__(self, settings: Settings, screen: Surface, stats: Stats):
        super().__init__(settings.image_absolute_path(settings.player_image))

        self._stats = stats
        self._screen = screen
        self._screen_rect = self._screen.get_rect()

        # Set starting position
        self.center_player()

        # Store a float value of horizontal position to be more precise
        self._x = float(self.rect.x)

        # Movement flags
        self.moving_right = False
        self.moving_left = False

    def update(self):
        """ Moves player horizontally based on movement flags """
        if self.moving_right and self.rect.right < self._screen_rect.right:
            self._x += self._stats.player_speed

        # Separate if conditions to properly handle both keys pressed at same time
        if self.moving_left and self.rect.left > self._screen_rect.left:
            self._x -= self._stats.player_speed

        self.rect.x = self._x

    def draw(self):
        self._screen.blit(self.image, self.rect)

    def center_player(self):
        self.rect.midbottom = self._screen_rect.midbottom
        self._x = float(self.rect.x)
