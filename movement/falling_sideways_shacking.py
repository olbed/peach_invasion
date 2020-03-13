from random import random

from movement.scheme import Scheme


class FallingSidewaysShacking(Scheme):
    """ Moves object down and sideways and make it shacking """

    # Chances that object will go wrong way, it makes it shaking
    chance_to_go_wrong_direction_horizontally = .18
    chance_to_go_wrong_direction_vertically = .43

    def __init__(self, object_rect, screen_rect, speed):
        super().__init__(object_rect, screen_rect, speed)

        # Set initial direction to right and down
        self._direction = [1, 1]

        # Tracks if object is going the wrong way to be able to recover
        self._is_going_wrong_horizontally = False

    def move(self):
        # Check if it's time to change direction and change if it is
        self._check_direction()

        super().move()

    def _check_direction(self):
        self._apply_chances_to_go_wrong()

        if self._is_at_right_screen_edge():
            self.direction = (-1, None)
        elif self._is_at_left_screen_edge():
            self.direction = (1, None)

    def _apply_chances_to_go_wrong(self):
        if random() < self.chance_to_go_wrong_direction_horizontally:
            if not self._is_going_wrong_horizontally:
                x, y = self.direction
                self.direction = (-x, None)
                self._is_going_wrong_horizontally = True
        elif self._is_going_wrong_horizontally:
            x, y = self.direction
            self.direction = (-x, None)
            self._is_going_wrong_horizontally = False

        if random() < self.chance_to_go_wrong_direction_vertically:
            self.direction = (None, -1)
        else:
            self.direction = (None, 1)
