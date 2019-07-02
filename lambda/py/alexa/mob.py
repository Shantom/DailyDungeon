from . import data


class Mob:
    def __init__(self, name=None):
        if not name:
            name = 'Awakened Shrub'
        self.name = name
        self.from_dict(name)
        self.attack_gauge = 100
        self.cast_gauge = 1000

    def from_dict(self, name):
        mob_data = data.MOB_INFO[name]
        self.attack = mob_data['attack']
        self.defense = mob_data['defense']
        self.hp = mob_data['hp']
        self.mp = mob_data['mp']
        self.cur_skill = mob_data['skill']
        self.speed = mob_data['speed']
        self.cast_speed = mob_data['cast_speed']
