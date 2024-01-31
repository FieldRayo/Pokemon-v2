import random, math, time
import json, os

class Player:
    def __init__(self, name, gender, age):
        self.name = name
        self.gender = gender
        self.age = age
        self.id = random.randint(10000000, 99999999)
        self.money = 0
        self.n_game = 1
        
        # Menu
        self.actual_menu: object = None
        self.menu_history = []

        #Menu - Chat
        self.messages = {}
        self.n_messages = sum([len(value) for key, value in self.messages.items()])
        self.friends = []
        
        # Pokemon
        self.init_pokemon: object = None
        self.principal_pokemon: object = None

        self.pokemon_caught = []
        self.pokemon_team = []
        
        # Object
        self.objects = []
    
    def save(self):
        player_data = to_dict(self)
             
        with open(f'./saves/save{self.n_game}.json', 'w') as json_file:
            json.dump(player_data, json_file, indent=4)
                
    def load(self, save_file):
        save_file = to_object(save_file)

        for key in vars(self):
            attr = getattr(save_file, key)
            setattr(self, key, attr)

    def set_init_pokemon(self, init_pokemon):
        if not self.init_pokemon and init_pokemon.isinit_pokemon:
            self.init_pokemon = init_pokemon
        
        self.caught(init_pokemon)
        self.add_team(init_pokemon)
        self.set_principal_pokemon(init_pokemon)
    
    def set_principal_pokemon(self, pokemon):
        self.principal_pokemon = pokemon

    def caught(self, pokemon):
        self.pokemon_caught.append(pokemon)

    def add_team(self, pokemon):
        self.pokemon_team.append(pokemon)

    def add_object(self, object_):
        if object.name in self.objects:
            self.objects[self.objects.name].amount += 1
            return

        self.objects[object_.name] = object_
        self.objects_data[object_.name] = {}

        for attr_name, attr_value in vars(object_).items():
            self.objects_data[object_.name][attr_name] = attr_value


class Menu:
    def __init__(self, name, design, static_menu=False):
        self.name = name
        self.design = design

        self.menu_options = {}
        self.menu_data = []

        self.size_data = design.count('{')
        self.static_menu = static_menu

    def set_options(self, options):
        self.menu_options = options

    def set_data(self, data):
        self.menu_data = data

    def run_menu(self, player=0):
        from designs import load_menu_options, get_menu_data
    
        option = 0
    
        data = get_menu_data(player, self)
        self.set_data(data)
        
        self.print_data()

        self.menu_ajust()

        print(self.design)
        option = input('>>> ')
        os.system('clear')

        if option == '0' and len(player.menu_history)-1:
            player.menu_history.pop()
        if not self.static_menu and option != '0':
            load_menu_options(self)
            player.menu_history.append(self.menu_options[option])
        elif option != '0':
            return option

        player.actual_menu = player.menu_history[-1]
        player.actual_menu.run_menu(player)
    
    def print_data(self):
        menu_data = self.menu_data
        size_data = self.size_data
                
        if not menu_data: menu_data = []

        menu_data += ['?'] * (size_data - len(menu_data))
        self.design = self.design.format(*menu_data)
    
    def menu_ajust(self):
        menu = self.design

        side_count = 0
        size_menu = 0
    
        target_side = 2
        target_distance = 0
        
        i = 0
        while i < len(menu):
            if menu[i] == '║':
                if not size_menu: size_menu = i-1
                side_count += 1

            if side_count == target_side*2:
                target_distance = size_menu - (i-1 - size_menu*(target_side+1)+2)
                menu = menu[:i] + ' '*target_distance + menu[i:]

                side_count -= 1
                target_side += 1
                    
            i += 1
    
        self.design = menu


class Pokemon:
    def __init__(self, name, type_):
        self.name = name
        self.gender = -1

        self.type_: Type = type_
        self.counter = []
        self.isinit_pokemon = False

        self.xp = 0
        self.xp_need = 1
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

        self.skills: dict = {}
        self.nature: object = None
    
    def get_init_stats(self):
        return self.iv_health, self.iv_damage, self.iv_defense, self.iv_speed, self.iv_precision

    def get_stats(self):
        return self.health, self.damage, self.defense, self.speed, self.precision
    
    def get_xp(self):
        return self.xp
    
    def set_skill(self, skill):
        self.skills[skill.name] = skill

    def set_type(self, type_):
        self.type_ = type_

    def set_init_stats(self, args):
        self.iv_health = args[0]
        self.iv_damage = args[1]
        self.iv_defense = args[2]
        self.iv_speed = args[3]
        self.iv_precision = args[4]

        self.iv_mean = sum(args) / 5

    def set_standard_stats(self):
        self.health = self.type_.health * (self.level ** 1.5 + self.iv_health) // 10
        self.damage = self.type_.damage * (self.level ** 1.5 + self.iv_damage) // 10
        self.defense = self.type_.defense * (self.level ** 1.5 + self.iv_defense) // 10
        self.speed = self.type_.speed * (self.level ** 1.5 + self.iv_speed) // 10
        self.precision = self.type_.precision * (self.level * 1.5 + self.iv_precision) // 10

        self.mean = sum([self.health, self.damage, self.defense, self.speed, self.precision])

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


import inspect
import copy

def to_dict(object_):
    denied_data = (str, int, float, bool, list, tuple)
    obj = copy.deepcopy(object_)

    if not isinstance(obj, denied_data) and obj:
        if isinstance(obj, dict):
            dict_ = obj
        else:
            dict_ = vars(obj)
            dict_['object_name'] = type(obj).__name__
        
        for key, value in dict_.items():
            dict_[key] = to_dict(value)

        return dict_
    
    if isinstance(obj, list):
        for i in range(len(obj)):
            obj[i] = to_dict(obj[i])

    return obj

def to_object(dictionary):
    dict_ = copy.deepcopy(dictionary)

    if not isinstance(dict_, dict) or 'object_name' not in dict_:
        return dict_

    obj = object_map[dict_['object_name']]
    
    init_parameters = inspect.signature(obj)
    init_parameters = list(init_parameters.parameters.keys())
    init_parameters = [dict_[p] for p in init_parameters]

    obj = obj(*init_parameters)

    for key, value in dict_.items():
        if isinstance(dict_[key], list):
            setattr(obj, key, [to_object(x) for x in dict_[key]])        
        elif isinstance(dict_[key], dict):
            setattr(obj, key, to_object(dict_[key]))
        else:
            setattr(obj, key, value)

    return obj

def on_key(key):
    return key.name

object_map = {'Player': Player,
              'Menu': Menu,
              'Pokemon': Pokemon,
              'Skill': Skill,
              'Type': Type
              }
