import time
from . import data
from .battle import Battle
from .mob import Mob


class Character:

    def __init__(self, char_data=None):
        if not char_data:
            self.level = 1
            self.floor = 1
            self.exp = 0
            self.coin = 0
            self.job = 'Novice'
            self.attack = 50
            self.defense = 10
            self.hp = 200
            self.mp = 100
            self.cur_skill_set = ['Double Strafe']
            self.speed = 100
            self.cast_speed = 100
            self.last_offline_time = int(time.time())
            self.sec_per_round = 20
        else:
            self.from_dict(char_data)
        self.attack_gauge = 100
        self.cast_gauge = 1000

    def check_level_up(self):
        while self.exp >= data.EXP_TO_LEVEL_UP[self.level]:
            self.exp -= data.EXP_TO_LEVEL_UP[self.level]
            self.level += 1
            self.attack += 16
            self.defense += 4
            self.hp += 36
            self.mp += 16

    def gain_exp_by_time(self):
        cur_time = int(time.time())
        passing_time = cur_time - self.last_offline_time
        self.exp += (passing_time // self.sec_per_round) * \
            data.EXP_PER_ROUND[int(self.floor)]

    def gain_coin_by_time(self):
        cur_time = int(time.time())
        passing_time = cur_time - self.last_offline_time
        self.coin += (passing_time // self.sec_per_round) * data.COIN_PER_ROUND

    def claim_loot(self):
        self.gain_coin_by_time()
        self.gain_exp_by_time()
        self.check_level_up()
        self.last_offline_time = int(time.time())

    def to_dict(self):
        ret = dict()
        ret['level'] = self.level
        ret['floor'] = self.floor
        ret['exp'] = self.exp
        ret['coin'] = self.coin
        ret['job'] = self.job
        ret['attack'] = self.attack
        ret['defense'] = self.defense
        ret['hp'] = self.hp
        ret['mp'] = self.mp
        ret['cur_skill_set'] = self.cur_skill_set
        ret['speed'] = self.speed
        ret['cast_speed'] = self.cast_speed
        ret['last_offline_time'] = self.last_offline_time
        ret['sec_per_round'] = self.sec_per_round

        return ret

    def from_dict(self, char_data):
        self.level = int(char_data['level'])
        self.floor = int(char_data['floor'])
        self.exp = int(char_data['exp'])
        self.coin = int(char_data['coin'])
        self.job = char_data['job']
        self.attack = int(char_data['attack'])
        self.defense = int(char_data['defense'])
        self.hp = int(char_data['hp'])
        self.mp = int(char_data['mp'])
        self.cur_skill_set = char_data['cur_skill_set']
        self.speed = int(char_data['speed'])
        self.cast_speed = int(char_data['cast_speed'])
        self.last_offline_time = int(char_data['last_offline_time'])
        self.sec_per_round = int(char_data['sec_per_round'])

    def battle_with_boss(self):
        # TODO: a battle here
        bat = Battle(self, Mob('Awakened Shrub'))
        is_win = bat.fight()
        log_battle = bat.log_info
        if is_win:
            self.floor += 1
            return True, log_battle
        else:
            return False, log_battle
