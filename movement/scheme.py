class Scheme:
    """ Defines how object moves on the screen """

    def __init__(self, object_rect, screen_rect):
        self._object_rect = object_rect
        self._screen_rect = screen_rect

        # Store a float values of object position for higher accuracy when updating
        self._position = [0.0, 0.0]

        # Horizontal and vertical speed, shows how many pixels object moves in one step
        self._speed = [0.0, 0.0]

    def _is_at_right_screen_edge(self):
        return self._object_rect.right >= self._screen_rect.right

    def _is_at_left_screen_edge(self):
        return self._object_rect.left <= 0

    def move(self):
        """ Moves object 1 step in current direction with current speed """
        x, y = self.position
        x_path, y_path = self._speed
        self.position = x + x_path, y + y_path
        return x_path, y_path

    @property
    def position(self):
        return self._position

    @position.setter
    def position(self, xy):
        x, y = xy
        if x is not None:
            self._position[0] = float(x)
            self._object_rect.x = self._position[0]
        if y is not None:
            self._position[1] = float(y)
            self._object_rect.y = self._position[1]

    @property
    def speed(self):
        return self._speed

    @speed.setter
    def speed(self, xy):
        x, y = xy
        if x is not None:
            self._speed[0] = x
        if y is not None:
            self._speed[1] = y

    def reverse_x_speed(self):
        self._speed[0] *= -1

    def reverse_y_speed(self):
        self._speed[1] *= -1
