from pygame import image
from pygame.sprite import Sprite


class Object(Sprite):
    """ Represents any visual object in game """

    def __init__(self, object_image):
        super().__init__()

        # Attributes required for Sprite
        self.image = image.load(object_image)
        self.rect = self.image.get_rect()
