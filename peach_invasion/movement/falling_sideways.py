from peach_invasion.movement.scheme import Scheme


class FallingSideways(Scheme):
    """ Moves object down and sideways """

    def __init__(self, object_rect, screen_rect):
        super().__init__(object_rect, screen_rect)

    def move(self):
        # Check if it's time to change direction and change if it is
        self._check_direction()

        super().move()

    def _check_direction(self):
        if self._is_at_right_screen_edge() or self._is_at_left_screen_edge():
            self.reverse_x_speed()
