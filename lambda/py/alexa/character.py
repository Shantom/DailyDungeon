import time
import copy
from . import data
from .battle import Battle
from .mob import Mob


class Character:
    def __init__(self, char_data=None):
        if not char_data:
            self.level = 0
            self.floor = 1
            self.exp = 0
            self.coin = 0
            self.job = 'Novice'
            self.attack = 50
            self.defense = 10
            self.hp = 200
            self.mp = 100
            self.cur_skill = 'Thump'
            self.skills = ['Double Strafe',
                           'Blitz Beat', 'Arrow Shower', 'Thump']
            self.speed = 100
            self.cast_speed = 100
            self.last_offline_time = int(time.time())
            self.sec_per_round = 20
            self.messages = []
        else:
            self.from_dict(char_data)

        self.attack_gauge = 100
        self.cast_gauge = 1000

    def new_msg(self, msg):
        self.messages.append(msg)

    def check_level_up(self):
        while self.exp >= data.EXP_TO_LEVEL_UP[self.level]:
            self.exp -= data.EXP_TO_LEVEL_UP[self.level]
            self.level += 1
            self.attack += 16
            self.defense += 4
            self.hp += 36
            self.mp += 16
            if data.SKILL_ACQUIRE[self.level]:
                self.new_msg('You have acquired a new skill, {}. '.format(
                    data.SKILL_ACQUIRE[self.level]))

    def gain_exp_by_time(self, passing_time):
        loot = (passing_time // self.sec_per_round) * \
            data.EXP_PER_ROUND[int(self.floor)]
        self.exp += loot
        return loot

    def gain_coin_by_time(self, passing_time):
        loot = (passing_time // self.sec_per_round) * data.COIN_PER_ROUND
        self.coin += loot
        return loot

    def claim_loot(self):
        cur_time = int(time.time())
        passing_time = cur_time - self.last_offline_time
        loot_coin = self.gain_coin_by_time(passing_time)
        loot_exp = self.gain_exp_by_time(passing_time)
        self.check_level_up()
        self.last_offline_time = int(time.time())
        return passing_time, loot_coin, loot_exp

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
        ret['cur_skill'] = self.cur_skill
        ret['skills'] = self.skills
        ret['speed'] = self.speed
        ret['cast_speed'] = self.cast_speed
        ret['last_offline_time'] = self.last_offline_time
        ret['sec_per_round'] = self.sec_per_round
        ret['messages'] = self.messages

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
        self.cur_skill = char_data['cur_skill']
        self.skills = char_data['skills']
        self.speed = int(char_data['speed'])
        self.cast_speed = int(char_data['cast_speed'])
        self.last_offline_time = int(char_data['last_offline_time'])
        self.sec_per_round = int(char_data['sec_per_round'])
        self.messages = char_data['messages']

    def battle_with_boss(self, temp_buff):
        # use a temp char to do the battle
        temp_char = temp_buff
        temp_char.attack += self.attack
        temp_char.defense += self.defense
        temp_char.hp += self.hp
        temp_char.mp += self.mp
        temp_char.speed += self.speed
        temp_char.cast_speed += self.cast_speed
        temp_char.cur_skill = self.cur_skill

        bat = Battle(temp_char, Mob(data.BOSS_OF_FLOOR[self.floor-1]))
        is_win = bat.fight()
        log_battle = bat.log_info
        if is_win:
            self.floor += 1
            return True, log_battle
        else:
            return False, log_battle


class TempCharacter:
    def __init__(self, char_data=None):
        if not char_data:
            self.attack = 0
            self.defense = 0
            self.hp = 0
            self.mp = 0
            self.cur_skill = None
            self.speed = 0
            self.cast_speed = 0
            self.attack_gauge = 100
            self.cast_gauge = 100
        else:
            self.from_dict(char_data)

    def to_dict(self):
        ret = dict()
        ret['attack'] = self.attack
        ret['defense'] = self.defense
        ret['hp'] = self.hp
        ret['mp'] = self.mp
        ret['cur_skill'] = self.cur_skill
        ret['speed'] = self.speed
        ret['cast_speed'] = self.cast_speed
        return ret

    def from_dict(self, char_data):
        self.attack = int(char_data['attack'])
        self.defense = int(char_data['defense'])
        self.hp = int(char_data['hp'])
        self.mp = int(char_data['mp'])
        self.cur_skill = char_data['cur_skill']
        self.speed = int(char_data['speed'])
        self.cast_speed = int(char_data['cast_speed'])
        self.attack_gauge = 100
        self.cast_gauge = 100

    def process(self, room_type, cur_char):
        if room_type == 'ATTUP':
            self.attack += int(cur_char.attack * .2)
            return 'You found a good sword, which makes your attack increase by 20 percent. '
        elif room_type == 'HEAL':
            self.hp += int(cur_char.hp * .3)
            return 'You found a mysterious portion and drank it all. Your hp recovered 30 percent. '
        elif room_type == 'POISON':
            self.hp -= int(cur_char.hp * .3)
            return 'You found a mysterious portion and drank it all. Your hp lost 30 percent. '
        elif room_type == 'ATTDOWN':
            self.attack -= int(cur_char.attack * .2)
            return 'You fell into a small puddle and your weapon is damaged a bit. Your attack decreases by 20 percent. '
        elif room_type == 'DEFUP':
            self.defense += int(cur_char.defense * .2)
            return 'You found a good shield, which makes your defense increase by 20 percent. '
        elif room_type == 'DEFDOWN':
            self.defense -= int(cur_char.defense * .2)
            return 'You were attacked by a slime. Your armor saved your life but it was scratched. Your defense decreases by 20 percent. '
        elif room_type == 'VISITED':
            return 'You have been here. There is nothing left.'
        else:
            return 'There is nothing in this room'
