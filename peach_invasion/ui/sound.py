from random import choice
from typing import Tuple

from pygame import mixer
from pygame.mixer import SoundType

from peach_invasion.settings import Settings


class Sound:
    """ Handles game sounds """
    fire: SoundType
    no_ammo: SoundType
    death: SoundType
    victory: SoundType
    _enemy_death: Tuple[SoundType]

    def __init__(self, settings: Settings):
        self._settings = settings

        # mixer.pre_init should be called before pygame.init
        # and mixer.init should be called after pygame.init
        # such order helps lower sound delay
        mixer.pre_init(44100, -16, 2, 256)

        # Shortcut
        self.abs_path = self._settings.audio_absolute_path

    def load(self):
        mixer.init()
        bg_music = self._new_sound(self._settings.sound_background_music)
        bg_music.play(-1)

        self.fire = self._new_sound(self._settings.sound_fire)
        self.no_ammo = self._new_sound(self._settings.sound_no_ammo)
        self.death = self._new_sound(self._settings.sound_death)
        self.victory = self._new_sound(self._settings.sound_victory)
        self._enemy_death = tuple(map(lambda f: self._new_sound(f), self._settings.sound_set_enemy_death))

    @property
    def enemy_death(self):
        return choice(self._enemy_death)

    def _new_sound(self, rel_path):
        absolute_path = self._settings.audio_absolute_path(rel_path)
        return mixer.Sound(absolute_path)
