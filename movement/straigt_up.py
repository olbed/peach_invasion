from movement.scheme import Scheme


class StraightUp(Scheme):
    """ Moves object straight up """

    def __init__(self, object_rect, screen_rect, speed):
        super().__init__(object_rect, screen_rect, speed)

        # Set initial direction to upwards
        self._direction = [0, -1]
