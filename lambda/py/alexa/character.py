import time
from . import data

class Character:

    def __init__(self, *args, **kwargs):

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
        self.exp += (passing_time // self.sec_per_round) * data.EXP_PER_ROUND[self.floor]

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