from pygame.font import SysFont
from pygame.rect import Rect
from pygame.sprite import Group
from pygame.surface import Surface

from peach_invasion.game_objects.object import Object
from peach_invasion.settings import Settings


class Scoreboard:
    """ Handle displaying game statistics on the screen """
    _score_image: Surface
    _high_score_image: Surface
    _level_image: Surface
    _score_rect: Rect
    _high_score_rect: Rect
    _level_rect: Rect
    _ammo: Group
    _health: Group

    def __init__(self, settings: Settings, screen: Surface):
        self._settings = settings
        self._screen = screen
        self._screen_rect = screen.get_rect()
        self._font = SysFont(None, settings.scoreboard_font_size)
        self._margin = settings.scoreboard_margin

        self.render_all(0, 0, 1, settings.health_limit, settings.ammo_limit)

    def render_all(self, score, high_score, level, health, ammo):
        # Renders all statistics indicators
        self.render_score(score)
        self.render_high_score(high_score)
        self.render_level(level)
        self.render_health(health)
        self.render_ammo(ammo)

    def render_score(self, score):
        self._score_image = self._font.render(f'${score:,}', True, self._settings.scoreboard_txt_color)
        self._score_rect = self._score_image.get_rect()

        # Position
        self._score_rect.right = self._screen_rect.right - self._margin
        self._score_rect.top = self._margin

    def render_high_score(self, high_score):
        self._high_score_image = self._font.render(f'${high_score:,}', True, self._settings.scoreboard_txt_color)
        self._high_score_rect = self._high_score_image.get_rect()

        # Position
        self._high_score_rect.centerx = self._screen_rect.centerx
        self._high_score_rect.top = self._margin

    def render_level(self, level):
        self._level_image = self._font.render(f'Level {level}', True, self._settings.scoreboard_txt_color)
        self._level_rect = self._level_image.get_rect()

        # Position
        self._level_rect.left = self._margin
        self._level_rect.top = self._margin

    def render_ammo(self, ammo):
        self._ammo = Group()
        for i in range(ammo):
            ammo = Object(self._settings.image_absolute_path(self._settings.ammo_image))
            ammo.rect.right = (self._screen_rect.right - self._margin) - i * (ammo.rect.width + self._margin)
            ammo.rect.bottom = self._screen_rect.bottom - self._margin
            self._ammo.add(ammo)

    def render_health(self, health):
        self._health = Group()
        for i in range(health):
            health = Object(self._settings.image_absolute_path(self._settings.health_image))
            health.rect.left = self._margin
            health.rect.bottom = (self._screen_rect.bottom - self._margin) - i * (health.rect.height + self._margin)
            self._health.add(health)

    def draw(self):
        """ Draws last renders of all stat indicators """
        self._screen.blit(self._score_image, self._score_rect)
        self._screen.blit(self._high_score_image, self._high_score_rect)
        self._screen.blit(self._level_image, self._level_rect)
        self._health.draw(self._screen)
        self._ammo.draw(self._screen)
