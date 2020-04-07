from pygame.font import SysFont
from pygame.rect import Rect
from pygame.surface import Surface

from peach_invasion.settings import Settings


class Button:
    """ A button at the center of the screen """

    def __init__(self, settings: Settings, screen: Surface, msg):
        self._screen = screen
        self._settings = settings

        self._width, self._height = settings.btn_size
        self._font = SysFont(None, settings.btn_font_size)

        self.rect = Rect(0, 0, self._width, self._height)
        self.rect.center = screen.get_rect().center

        self._render_msg(msg)

    def _render_msg(self, msg):
        self._msg_image = self._font.render(msg, True, self._settings.btn_txt_color)
        self._msg_image_rect = self._msg_image.get_rect()
        self._msg_image_rect.center = self.rect.center

    def draw(self):
        self._screen.fill(self._settings.btn_color, self.rect)
        self._screen.blit(self._msg_image, self._msg_image_rect)
