from pathlib import Path


class Settings:
    """ Stores game settings """

    def __init__(self):
        # Player
        self.player_image = 'player.bmp'
        self.player_speed = 4.5

        # Bullets
        self.bullet_image = 'bullet.bmp'
        self.bullet_speed = 6.5

        # Enemy
        self.enemy_image = 'enemy.bmp'
        self.enemy_x_speed = 1.0
        self.enemy_y_speed = .15
        self.enemy_density = .5
        self.enemy_vertical_space_occupied = .5

        # Ammo
        self.ammo_image = 'ammo.bmp'
        self.ammo_limit = 2

        # Health
        self.health_image = 'health.bmp'
        self.health_limit = 3

        # Background
        self.bg_color = (20, 60, 30)
        self.bg_grass_image = 'grass.bmp'
        self.bg_grass_number = 35

        # Scoreboard
        self.scoreboard_txt_color = (210, 240, 220)
        self.scoreboard_font_size = 42
        self.scoreboard_margin = 10

        # Button
        self.btn_size = (250, 70)
        self.btn_color = (210, 240, 220)
        self.btn_txt_color = (20, 60, 30)
        self.btn_font_size = 64

        # Gameplay
        self.speedup_rate = 1.1

        # Sounds
        self.sound_background_music = 'background.wav'
        self.sound_fire = 'fire.wav'
        self.sound_no_ammo = 'no_ammo.wav'
        self.sound_death = 'death.wav'
        self.sound_victory = 'victory.ogg'
        self.sound_set_enemy_death = (
            'enemy_death_1.ogg',
            'enemy_death_2.wav',
            'enemy_death_3.wav',
            'enemy_death_4.wav',
            'enemy_death_5.wav',
        )

        self.static = Path(__file__).parent.absolute().joinpath('static')

    def image_absolute_path(self, rel_path):
        return f'{self.static}/images/{rel_path}'

    def audio_absolute_path(self, rel_path):
        return f'{self.static}/audio/{rel_path}'
