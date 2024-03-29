from . import character, mob, data
from ask_sdk_core.response_helper import get_plain_text_content, get_rich_text_content
from ask_sdk_model.interfaces.display import (
    ImageInstance, Image, RenderTemplateDirective, ListTemplate1,
    BackButtonBehavior, ListItem)
import copy


class Battle:
    def __init__(self, player, mob):
        self.player = copy.deepcopy(player)
        self.player_max_hp = self.player.hp
        self.mob = copy.deepcopy(mob)
        self.mob_max_hp = self.mob.hp
        self.tp = Timer('you')
        self.tm = Timer('the monster')

        self.log_info = []
        self.log_vec = []
        self.seq = 0

    def tick(self):
        player_log = self.tp.tick()
        mob_log = self.tm.tick()
        if player_log:
            self.log(player_log)
        if mob_log:
            self.log(mob_log)

    def normal_attack(self, is_player=True):
        if is_player:  # if it is the player to move
            self.tp.attack_gauge = 0
            amount = max(self.player.attack - self.mob.defense, 0)
            self.mob.hp -= amount

            self.log('You hit the monster, which gives it {} damage, HP {} left'
                     .format(amount, max(0, self.mob.hp)))

            # take effect
            if 'Bleeding' in self.tp.effects:
                # lose 10% HP every time NA
                self.player.hp -= self.player_max_hp * .1
                self.log('You bleed {} when hitting the monster.'.format(
                    self.player_max_hp * .1))

            self.log_move(True, self.player.hp, self.mob.hp, 'HIT',
                          amount, self.tp.effects, self.tm.effects)

        else:
            self.tm.attack_gauge = 0
            amount = max(self.mob.attack - self.player.defense, 0)
            self.player.hp -= amount

            self.log(
                'The monster hit you, which gives you {} damage, HP {} left'
                .format(amount, max(0, self.player.hp)))

            # take effect
            if 'Bleeding' in self.tm.effects:
                # lose 10% HP every time NA
                self.mob.hp -= self.mob_max_hp * .1
                self.log('The monster bleeds {} when hitting you.'.format(
                    self.mob_max_hp * .1))

            self.log_move(False, self.player.hp, self.mob.hp, 'HIT',
                          amount, self.tp.effects, self.tm.effects)

    def use_skill(self, move, is_player=True):
        if is_player:
            if self.player.mp >= move['mp']:
                self.player.mp -= move['mp']
                self.tp.cast_gauge -= int(move['cast']
                                          * 100 / self.player.cast_speed)
                damage = int(
                    max(self.player.attack-self.mob.defense, 0)*move['rate']/100)
                self.mob.hp -= damage

                # set effect on timer
                if move['effect'] == 'Frozen':
                    self.tm.add_effect('Frozen', 400)
                elif move['effect'] == 'Bleeding':
                    self.tm.add_effect('Bleeding', 200)

                self.log('You use {}, which gives the monster {} damage, HP {} left'.format(
                    move['name'], damage, max(0, self.mob.hp)))
                self.log_move(True, self.player.hp, self.mob.hp, move['name'],
                              damage, self.tp.effects, self.tm.effects)
            else:
                self.log(
                    'You don\'t have enough mana to cast {}'.format(move['name']))
        else:
            self.tm.cast_gauge -= int(move['cast']
                                      * 100 / self.mob.cast_speed)
            damage = int(
                max(self.mob.attack-self.player.defense, 0)*move['rate']/100)
            self.player.hp -= damage

            # set effect on timer
            if move['effect'] == 'Frozen':
                self.tp.add_effect('Frozen', 400)
            elif move['effect'] == 'Bleeding':
                self.tp.add_effect('Bleeding', 200)

            self.log('The monster use {}, which gives you {} damage, HP {} left'.format(
                move['name'], damage, max(0, self.player.hp)))

            self.log_move(False, self.player.hp, self.mob.hp, move['name'],
                          damage, self.tp.effects, self.tm.effects)

    def check_death(self):
        if self.player.hp <= 0:
            return 'player'
        elif self.mob.hp <= 0:
            return 'monster'
        else:
            return False

    def log(self, info):
        self.log_info.append(info)

    def log_move(self, is_player, p_hp, m_hp, move, dmg, p_st, m_st):
        ret = ListItem(token=self.seq)
        self.seq += 1
        if is_player:
            ret.image = Image(sources=[ImageInstance(url=data.PLAYER_AVATAR)])

        else:
            ret.image = Image(sources=[ImageInstance(
                url=data.MONSTER_AVATAR[self.mob.name.lower()])])

        p_st = [data.EMOJI_STATUS[x] for x in p_st]
        m_st = [data.EMOJI_STATUS[x] for x in m_st]

        primary_text = "<div align='center'><font size='5'>{} DMG: {}</font></div>".format(
            move, str(dmg))
        secondary_text = "<div align='center'>Your HP:{} {}".format(p_hp, ''.join(
            p_st)) + "Monster HP:{} {}</div>".format(m_hp, ''.join(m_st))

        ret.text_content = get_rich_text_content(primary_text=primary_text,
                                                 secondary_text=secondary_text)
        self.log_vec.append(ret)

    def fight(self):
        while not self.check_death():
            self.tick()

            # player normal attack check
            if self.tp.attack_gauge >= 100 / (self.player.speed / 100):
                self.normal_attack(True)
            if self.check_death():
                break

            # player skill check
            player_skill = self.player.cur_skill
            if player_skill:
                player_skill = data.SKILL_INFO[player_skill]
                if self.tp.cast_gauge >= player_skill['cast'] / (self.player.cast_speed / 100):
                    self.use_skill(player_skill, True)
                if self.check_death():
                    break

            # mob normal attack check
            if self.tm.attack_gauge >= 100 / (self.mob.speed / 100):
                self.normal_attack(False)
            if self.check_death():
                break

            # mob skill check
            mob_skill = self.mob.cur_skill
            if mob_skill:
                mob_skill = data.SKILL_INFO[mob_skill]
                if self.tm.cast_gauge >= mob_skill['cast'] / (self.mob.cast_speed / 100):
                    self.use_skill(mob_skill, False)
                if self.check_death():
                    break

        ret = self.check_death() == 'monster'
        if ret:
            self.log('The monster is dead.')
        else:
            self.log('You died.')
        return ret


class Timer:
    def __init__(self, name):
        self.attack_gauge = 0
        self.cast_gauge = 0
        self.effects = {}
        self.name = name

    def tick(self):
        self.attack_gauge += 1
        self.cast_gauge += 1
        log = ''
        if 'Frozen' in self.effects:
            self.effects['Frozen'] -= 1
            if self.effects['Frozen'] % 2 == 0:
                self.attack_gauge -= 1
            if self.effects['Frozen'] == 1:
                del (self.effects['Frozen'])
                log += self.name+'recovered from Frozen'
        if 'Bleeding' in self.effects:
            self.effects['Bleeding'] -= 1
            if self.effects['Bleeding'] == 1:
                del (self.effects['Bleeding'])
                log += self.name+'recovered from Bleeding'

        return log

    def add_effect(self, effect, time):
        self.effects[effect] = time
