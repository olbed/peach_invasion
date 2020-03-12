from pygame import Surface

from game_object import GameObject
from game_stats import GameStats
from settings import Settings


class Enemy(GameObject):
    """ Handles single enemy """

    def __init__(self, settings: Settings, screen: Surface, stats: GameStats):
        super().__init__(settings.enemy_image)

        self._screen = screen
        self._stats = stats

        # Store a float values of enemy position for higher accuracy when updating
        self._x, self._y = 0.0, 0.0

        # 0 - down / 1 - right / 2 - left
        self._direction = 1

        # How many pixels left to go down before changing direction
        self._to_go_down = 0.0

    def update(self):
        # Check if enemy is still moving in right direction and change if not
        self._check_direction()

        # Move
        if self._direction:
            self._go_sideways()
        else:
            self._go_down()

    def _is_at_right_screen_edge(self):
        return self.rect.right >= self._screen.get_rect().right

    def _is_at_left_screen_edge(self):
        return self.rect.left <= 0

    def _go_down(self):
        self.y += self._stats.enemy_speed
        self._to_go_down -= self._stats.enemy_speed

    def _go_sideways(self):
        self.x += self._stats.enemy_speed * self._direction

    def _check_direction(self):
        if not self._is_at_right_screen_edge() and not self._is_at_left_screen_edge():
            # No need to check direction if enemy is not on the screen edge
            return

        if self._direction != 0:
            # Enemy moves sideways but is now on the screen edge, let's turn downwards
            self._direction = 0
            self._to_go_down = float(self.rect.height)

        elif self._to_go_down <= 0:
            # Enemy moves down and went enough, let's turn sideways
            self._direction = 1 if self._is_at_left_screen_edge() else -1

    @property
    def x(self):
        return self._x

    @x.setter
    def x(self, x):
        self._x = float(x)
        self.rect.x = self._x

    @property
    def y(self):
        return self._y

    @y.setter
    def y(self, y):
        self._y = float(y)
        self.rect.y = self._y
