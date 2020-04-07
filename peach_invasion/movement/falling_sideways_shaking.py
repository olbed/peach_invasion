from random import random

from peach_invasion.movement.falling_sideways import FallingSideways


class FallingSidewaysShaking(FallingSideways):
    """ Moves object down and sideways and make it shacking """

    # Chances that object will go wrong way, it makes it shaking
    chance_to_go_wrong_direction_x = .25
    chance_to_go_wrong_direction_y = .1

    def __init__(self, object_rect, screen_rect):
        super().__init__(object_rect, screen_rect)

        # Tracks if object is going the wrong way to be able to recover
        self._must_be_positive_x = True
        self._must_be_positive_y = True

    def _check_direction(self):
        if self._is_at_right_screen_edge() or self._is_at_left_screen_edge():
            self.reverse_x_speed()
            self._must_be_positive_x = not self._must_be_positive_x
            return

        is_moving_wrong_x, is_moving_wrong_y = self._is_moving_wrong()

        must_go_wrong_x = random() < self.chance_to_go_wrong_direction_x
        must_go_wrong_y = random() < self.chance_to_go_wrong_direction_y

        if is_moving_wrong_x != must_go_wrong_x:
            self.reverse_x_speed()
        if is_moving_wrong_y != must_go_wrong_y:
            self.reverse_y_speed()

    def _is_moving_wrong(self):
        x, y = self.speed
        is_x_positive, is_y_positive = x > 0, y > 0
        return is_x_positive != self._must_be_positive_x, \
               is_y_positive != self._must_be_positive_y
