from peach_invasion.settings import Settings
from peach_invasion.ui.scoreboard import Scoreboard


class Stats:
    """ Track gaming statistics """

    def __init__(self, settings: Settings, scoreboard: Scoreboard):
        self._settings = settings
        self._scoreboard = scoreboard

        # High score never resets throughout the game
        self._high_score = 0

        self._set_initial_values()

    def reset(self):
        self._set_initial_values()

    def _set_initial_values(self):
        self._score = 0
        self._level = 1
        self._health = self._settings.health_limit
        self._ammo = self._settings.ammo_limit

        # Rerender all displaying statistics after it has been changed
        self._scoreboard.render_all(self._score, self._high_score, self._level, self._health, self._ammo)

    @property
    def score(self):
        return self._score

    @property
    def high_score(self):
        return self._high_score

    def score_up(self, kills):
        """ Adds user scores based on the number of kills and the level """
        self._score += kills * self._level * 2
        self._scoreboard.render_score(self._score)

        # Update high score
        if self._score > self._high_score:
            self._high_score = self._score
            self._scoreboard.render_high_score(self._high_score)

    @property
    def health(self):
        return self._health

    def player_lost_life(self):
        self._health -= 1
        self._scoreboard.render_health(self._health)

    @property
    def level(self):
        return self._level

    def level_up(self):
        self._level += 1
        self._scoreboard.render_level(self._level)

    @property
    def player_speed(self):
        return self._settings.player_speed * self._game_speed

    @property
    def enemy_speed(self):
        return self._settings.enemy_x_speed * self._game_speed, \
               self._settings.enemy_y_speed * self._game_speed

    @property
    def bullet_speed(self):
        return 0, -self._settings.bullet_speed * self._game_speed

    @property
    def _game_speed(self):
        return self._settings.speedup_rate ** self._level

    @property
    def ammo(self):
        return self._ammo

    @ammo.setter
    def ammo(self, ammo):
        if ammo != self._ammo:
            self._scoreboard.render_ammo(ammo)
        self._ammo = ammo
