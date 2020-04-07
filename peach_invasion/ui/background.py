from random import randint

from pygame import Surface
from pygame.sprite import Group

from peach_invasion.game_objects.object import Object
from peach_invasion.settings import Settings


class Background:
    """ Handle game background """

    def __init__(self, settings: Settings, screen: Surface):
        self._settings = settings
        self._screen = screen

        self._grass = Group()

        for _ in range(self._settings.bg_grass_number):
            new_grass = self.Grass(settings, screen.get_rect().size)
            self._grass.add(new_grass)

    def draw(self):
        """ Draws complete background for the game """
        self._screen.fill(self._settings.bg_color)
        self._grass.draw(self._screen)

    class Grass(Object):
        """ Represents one grass object """

        def __init__(self, settings: Settings, screen_size):
            super().__init__(settings.image_absolute_path(settings.bg_grass_image))

            self._screen_size = screen_size
            self.rect = self._get_random_position()

        def _get_random_position(self):
            grass_w, grass_h = self.image.get_rect().size
            screen_w, screen_h = self._screen_size
            max_x = screen_w - grass_w
            max_y = screen_h - grass_h
            return randint(0, max_x), randint(0, max_y)
