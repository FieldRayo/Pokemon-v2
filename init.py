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
        self.opponent_pokemon: object = None

        self.pokemon_caught = []
        self.pokemon_team = []
        
        # Object
        self.objects = []
    
    def save(self):
        from funcs import to_dict
        player_data = to_dict(self)
             
        with open(f'./saves/save{self.n_game}.json', 'w') as json_file:
            json.dump(player_data, json_file, indent=4)
                
    def load(self, save_file):
        from funcs import to_object
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
        if object in self.objects:
            self.objects[self.objects.name].amount += 1
            return

        self.objects.append(object_)

    def attack_pokemon(self, opponent_pokemon, attack):
        opponent_pokemon.attack_received(opponent_pokemon, attack)

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

    
    def open(self, player=None):
        from funcs import get_menu_data
        
        option_action = None
        data = get_menu_data(player, self)

        self.set_data(data)
        design = self.load_design(data)
        design = self.menu_ajust(design)
        
        print(design)
        option = int(input('>>> '))
        os.system('clear')
        
        if not player:
            return option
        
        menu_history = player.menu_history
        menu_history = list(set(menu_history))
        
        menu_history.append(self)
        
        if not option and len(menu_history)-1:
            menu_history.pop()
            menu_history[-1].open()
        elif option:
            menu_history[-1].menu_options[option-1]()

    def load_design(self, menu_data):
        size_data = self.size_data
                
        if not menu_data: menu_data = []

        menu_data += ['?'] * (size_data - len(menu_data))
        return self.design.format(*menu_data)
    
    def menu_ajust(self, menu):
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
    
        return menu


class Pokemon:
    def __init__(self, name, type_):
        self.name = name
        self.gender = -1

        self.type_: Type = type_
        self.counter = []
        self.isinit_pokemon = False
        self.is_down = False
        self.health_bar = f'{self.name} |████████████████████| 100%'

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
        self.max_health = 0

        self.health = 0
        self.damage = 0
        self.defense = 0
        self.speed = 0
        self.precision = 0

        self.mean = 0

        self.skills = []
        self.nature: object = None
    
    def get_init_stats(self):
        return self.iv_health, self.iv_damage, self.iv_defense, self.iv_speed, self.iv_precision

    def get_stats(self):
        return self.health, self.damage, self.defense, self.speed, self.precision
    
    def get_xp(self):
        return self.xp
    
    def set_skill(self, skill):
        self.skills.append(skill)

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
        self.health = self.type_.health * (self.level ** 1.5 + self.iv_health) // 12 + 1
        self.damage = self.type_.damage * (self.level ** 1.5 + self.iv_damage) // 12 + 1
        self.defense = self.type_.defense * (self.level ** 1.5 + self.iv_defense) // 12 + 1
        self.speed = self.type_.speed * (self.level ** 1.5 + self.iv_speed) // 12 + 1
        self.precision = self.type_.precision * (self.level * 1.5 + self.iv_precision) // 12 + 1

        self.max_health = self.health

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

    def attack_received(self, pokemon, attack, player_turn=True):
        from funcs import health_bar
        
        if player_turn:
            print(f'{pokemon.name} Ha usado "{attack.name}"')

        self.health -= attack.damage / ((self.defense+1) / 2)

        if self.health <= 0:
            self.is_down = True
            self.health = 0
        
        self.health_bar = health_bar(self)


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


class Object:
    def __init__(self, name, price, description, use):
        self.name = name
        self.price = price
        self.description = description
        
        self.object_info = f'{name} - {price}$'
        
        self.owner = None
        self.pokemon = None

        # Function
        self.use = use

    def set_owner(player):
        player_money = player.money
        price = self.price

        if player_money >= price:
            player.money -= price
            self.owner = player
        else:
            return 0

    def set_pokemon(pokemon):
        self.pokemon = pokemon

 
object_map = {'Player': Player,
              'Menu': Menu,
              'Pokemon': Pokemon,
              'Skill': Skill,
              'Type': Type
              }

