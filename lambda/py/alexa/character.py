import time
from . import data


class Character:

    def __init__(self, char_data=None):
        if not char_data:
            self.level = 1
            self.floor = 1
            self.exp = 0
            self.coin = 0
            self.job = 'Novice'
            self.attack = 50
            self.defense = 30
            self.hp = 200
            self.mp = 100
            self.cur_skill_set = []
            self.last_offline_time = int(time.time())
            self.sec_per_round = 20
        else:
            self.from_dict(char_data)

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
            data.EXP_PER_ROUND[self.floor]

    def gain_coin_by_time(self):
        cur_time = int(time.time())
        passing_time = cur_time - self.last_offline_time
        self.coin += (passing_time // self.sec_per_round) * data.COIN_PER_ROUND

    def claim_loot(self):
        self.gain_coin_by_time()
        self.gain_exp_by_time()

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
        ret['last_offline_time'] = self.last_offline_time
        ret['sec_per_round'] = self.sec_per_round

        return ret

    def from_dict(self, char_data):
        self.level = char_data['level']
        self.floor = char_data['floor']
        self.exp = char_data['exp']
        self.coin = char_data['coin']
        self.job = char_data['job']
        self.attack = char_data['attack']
        self.defense = char_data['defense']
        self.hp = char_data['hp']
        self.mp = char_data['mp']
        self.cur_skill_set = char_data['cur_skill_set']
        self.last_offline_time = char_data['last_offline_time']
        self.sec_per_round = char_data['sec_per_round']
