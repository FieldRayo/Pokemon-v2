import random
import math


class Player:
    def __init__(self, name, gender, age):
        self.name = name
        self.gender = gender
        self.age = age

        self.init_pokemon: object = None

        self.team = []

    def set_init_pokemon(self, init_pokemon):
        if not self.init_pokemon and init_pokemon.name in init_pokemon_data:
            self.init_pokemon = init_pokemon


class Pokemon:
    def __init__(self, name, gender, type_):
        self.name = ''
        self.gender = 0

        self.type: object = None
        self.counter = []

        self.xp = 0
        self.xp_need = 0
        self.level = 0

        # Init_stat
        self.iv_health = 0
        self.iv_damage = 0
        self.iv_defense = 0
        self.iv_speed = 0
        self.iv_precision = 0

        self.iv_mean = 0

        # Stats
        self.health = 0
        self.damage = 0
        self.defense = 0
        self.speed = 0
        self.precision = 0

        self.mean = 0

        self.skills = {'Placaje': skills_data['Placaje']}
        self.nature: object = None
    
    def get_init_stats(self):
        return self.iv_health, self.iv_damage, self.iv_defense, self.iv_speed, self.iv_precision

    def get_stats(self):
        return self.health, self.damage, self.defense, self.speed, self.precision
    
    def get_xp(self):
        return self.xp

    def set_type(self, type_):
        self.type = type_

    def set_init_stats(self, args):
        self.iv_health = args[0]
        self.iv_damage = args[1]
        self.iv_defense = args[2]
        self.iv_speed = args[3]
        self.iv_precision = args[4]

        self.iv_mean = sum(args) / 5

    def set_standard_stats(self):
        self.health = self.type.health * (self.level ** 1.5 + self.iv_health) // 10
        self.damage = self.type.damage * (self.level ** 1.5 + self.iv_damage) // 10
        self.defense = self.type.defense * (self.level ** 1.5 + self.iv_defense) // 10
        self.speed = self.type.speed * (self.level ** 1.5 + self.iv_speed) // 10
        self.precision = self.type.precision * (self.level * 1.5 + self.iv_precision) // 10

    def set_stats(self, args):
        self.health = args[0]
        self.damage = args[1]
        self.defense = args[2]
        self.speed = args[3]
        self.precision = args[4]

        self.mean = sum(args) / 5
    
    def set_xp(self, xp):
        self.xp = xp

    def set_counter(self, type_):
        self.counter = type_.counter

    def level_up(self):
        while self.xp >= self.xp_need:
            self.level += 1
            self.xp -= self.xp_need
            self.xp_need *= 2.5 * math.sin(self.level)
            self.set_standard_stats()


class Skill:
    def __init__(self, name, damage, counter):
        self.name = name
        self.damage = damage
        self.counter = counter
        self.level = 0
        self.pp = 0

    def set_counter(self, counter):
        self.counter = counter

    def use(self, pokemon):
        if self.pp > 0:
            if self.counter in pokemon.counter:
                pokemon.health -= self.damage * 2
            else:
                pokemon.health += self.damage


class Type:
    def __init__(self, name):
        self.name = ''
        self.counter = []

        self.health = 0
        self.damage = 0
        self.defense = 0
        self.speed = 0
        self.precision = 0

    def set_stats(self, args):
        self.health = args[0]
        self.damage = args[1]
        self.defense = args[2]
        self.speed = args[3]
        self.precision = args[4]

    def set_counter(self, counter):
        self.counter = counter


# Skills
placaje = Skill('Placaje', 3, None)
skills_data = {'Placaje': placaje}

# Types - fire
fire = Type('fire')
fire.set_stats([1.5, 2, 0.8, 1.2, 0.6])
fire.set_counter(['water', 'stone', 'electric', 'ice'])

# Pokemon - charmander
charmander = Pokemon('Charmander', 0, fire)
charmander.set_type(fire)
charmander.set_counter(fire)

charmander.set_init_stats(random.sample(range(0, 100), 5))
charmander.set_standard_stats()

charmander.xp_need = 1

# Pokemon - Data
init_pokemon_data = {'Charmander': charmander,
                     'Bulbasaur': 1,
                     'Squirtle': 1}
pokemon_data = {'Charmander': charmander,
                'Bulbasaur': 1,
                'Squirtle': 1}

