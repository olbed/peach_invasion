from movement.scheme import Scheme


class Snake(Scheme):
    """ Moves object in a snake way, right-down-left-down and so on"""

    def __init__(self, object_rect, screen_rect, speed):
        super().__init__(object_rect, screen_rect, speed)

        # Set initial direction to right
        self._direction = [1, 0]

        # How many pixels left to go down before changing direction
        self._to_go_down = 0.0

    def move(self):
        # Check if it's time to change direction and change if it is
        self._check_direction()

        # Moving and getting path object passed
        x_path, y_path = super().move()

        # Lower 'go down' counter by the distance object passed downwards
        self._to_go_down -= y_path

    def _check_direction(self):
        if not self._is_at_right_screen_edge() and not self._is_at_left_screen_edge():
            # No need to check direction if object is not on the screen edge yet
            return

        if self.direction[0] != 0:
            # Object moves horizontally but is now on the screen edge, let's turn downwards
            self.direction = (0, 1)
            self._to_go_down = float(self._object_rect.height)

        elif self._to_go_down <= 0:
            # Object moves down and went enough, let's turn sideways
            x_dir = 1 if self._is_at_left_screen_edge() else -1
            self.direction = (x_dir, 0)
