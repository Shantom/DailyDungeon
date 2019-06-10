from . import character, mob, data
import copy


class Battle:
    def __init__(self, player, mob):
        self.player = copy.deepcopy(player)
        self.mob = copy.deepcopy(mob)
        self.player.attack_gauge = 0
        self.mob.attack_gauge = 0
        self.player.cast_gauge = 0
        self.mob.cast_gauge = 0
        self.player_queue = self.player.cur_skill_set[:]
        self.mob_queue = self.mob.cur_skill_set[:]

    def tick(self):
        self.player.attack_gauge += 1
        self.mob.attack_gauge += 1
        self.player.cast_gauge += 1
        self.mob.cast_gauge += 1

    def normal_attack(self, is_player=True):
        if is_player:  # if it is the player to move
            self.player_attack_gauge = 0
            amount = self.player.attack - self.mob.defense
            self.mob.hp -= amount
        else:
            self.mob_attack_gauge = 0
            amount = self.mob.attack - self.player.defense
            self.player.hp -= amount

    def move(self, move, caster, target):
        if caster.mp >= move['mp']:
            caster.mp -= move['mp']
            caster.cast_gauge -= int(move['cast'] * 100 / caster.cast_speed)
            damage = (caster.attack-target.defense)*move['rate']
            target.hp -= damage

    def check_death(self):
        if self.player.hp <= 0:
            return 'player'
        elif self.mob.hp <= 0:
            return 'mob'
        else:
            return False

    def next_skill(self, is_player):
        ret = None
        if is_player:
            if self.player_queue:
                ret = self.player_queue.pop(0)
                self.player_queue.append(ret)
        else:
            if self.mob_queue:
                ret = self.mob_queue.pop(0)
                self.mob_queue.append(ret)
        return ret

    def fight(self):
        while not self.check_death():
            self.tick()

            # player normal attack check
            if self.player.attack_gauge >= 100 / (self.player.speed / 100):
                self.normal_attack(True)
            if self.check_death():
                break

            # player skill check
            player_next = self.next_skill(True)
            if player_next:
                player_next = data.SKILL_INFO[player_next]
                if self.player.cast_gauge >= player_next['cast'] / (self.player.cast_speed / 100):
                    self.move(player_next, self.player, self.mob)
                if self.check_death():
                    break

            # mob normal attack check
            if self.mob.attack_gauge >= 100 / (self.mob.speed / 100):
                self.normal_attack(False)
            if self.check_death():
                break

            # mob skill check
            mob_next = self.next_skill(False)
            if mob_next:
                mob_next = data.SKILL_INFO[mob_next]
                if self.mob.cast_gauge >= mob_next['cast'] / (self.mob.cast_speed / 100):
                    self.move(mob_next, self.mob, self.player)
                if self.check_death():
                    break

        return self.check_death() == 'mob'
