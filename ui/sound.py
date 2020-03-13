from pygame import mixer
from pygame.mixer import SoundType

from settings import Settings


class Sound:
    """ Handles game sounds """
    enemy_death: SoundType
    death: SoundType
    no_ammo: SoundType
    fire: SoundType

    def __init__(self, settings: Settings):
        self._settings = settings

        # mixer.pre_init should be called before pygame.init
        # and mixer.init should be called after pygame.init
        # such order helps lower sound delay
        mixer.pre_init(44100, -16, 2, 256)

    def load(self):
        mixer.init()
        mixer.Sound(self._settings.sound_background_music).play(-1)

        self.fire = mixer.Sound(self._settings.sound_fire)
        self.no_ammo = mixer.Sound(self._settings.sound_no_ammo)
        self.death = mixer.Sound(self._settings.sound_death)
        self.enemy_death = mixer.Sound(self._settings.sound_enemy_death)
