class MovementScheme:
    def __init__(self, object_rect, screen_rect, speed):
        self._object_rect = object_rect
        self._screen_rect = screen_rect
        self._speed = speed

        # Store a float values of object position for higher accuracy when updating
        self._position = [0.0, 0.0]

        # First number corresponds for horizontal movement: 1 = right, -1 = left, 0 = not moving
        # Second number corresponds for vertical movement: 1 = down, -1 = up, 0 = not moving
        self._direction = [0, 0]

    def _is_at_right_screen_edge(self):
        return self._object_rect.right >= self._screen_rect.right

    def _is_at_left_screen_edge(self):
        return self._object_rect.left <= 0

    def move(self):
        """ Moves object 1 step in current direction with current speed """
        x, y = self.position
        x_path, y_path = map(lambda direction: direction * self._speed, self.direction)
        self.position = x + x_path, y + y_path
        return x_path, y_path

    @property
    def position(self):
        return self._position

    @position.setter
    def position(self, pos):
        x, y = pos
        if x is not None:
            self._position[0] = float(x)
            self._object_rect.x = self._position[0]
        if y is not None:
            self._position[1] = float(y)
            self._object_rect.y = self._position[1]

    @property
    def direction(self):
        return self._direction

    @direction.setter
    def direction(self, pos):
        x, y = pos
        if x is not None:
            self._direction[0] = x
        if y is not None:
            self._direction[1] = y
