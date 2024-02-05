import time, os
import designs
import json

import inspect
import copy

def print_str_effect(str_, default_time=0.025, end='\n'):
    if '|' in str_:
        process_str = str_.split('|')
        str_ = '|'.join([x for x in str_.split('|') if not x.isdigit()])
        process_str = [int(x) for x in process_str if x.isdigit()]
    
    point_count = 0
    for i in range(len(str_)):
        if str_[i] == '|':
            time.sleep(default_time * process_str[point_count])
            point_count += 1

        elif str_[i] != '|':
            print(str_[i], end='', flush=True)
            time.sleep(default_time)

    print(end, end='')

def to_dict(object_):
    denied_data = (str, int, float, bool, list, tuple)
    
    obj = copy.deepcopy(object_)
    
    if callable(obj):
        return f'{type(obj).__name__}, {obj}'

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
    from init import object_map
    dict_ = copy.deepcopy(dictionary)

    if not isinstance(dict_, dict) or 'object_name' not in dict_:
        return dict_

    obj = object_map[dict_['object_name']]
    
    init_parameters = inspect.signature(obj)
    init_parameters = list(init_parameters.parameters.keys())
    init_parameters = [dict_[p] for p in init_parameters]

    obj = obj(*init_parameters)

    for key, value in dict_.items():
        if isinstance(value, list):
            setattr(obj, key, [to_object(x) for x in value])        
        elif isinstance(dict_[key], dict):
            setattr(obj, key, to_object(value))
        else:
            setattr(obj, key, value)

    return obj


def get_specific_attr(player, addres):
    addres = addres.split('.')
    attribute = player

    for i in range(len(addres)):
        if isinstance(attribute, list):
            attribute = [getattr(x, addres[i]) for x in attribute]
            continue
        
        if attribute:
            attribute = getattr(attribute, addres[i])

    if isinstance(attribute, dict):
        attribute = list(attribute)
    
    return attribute


def flatten_list(lst):
    resultado = []
    for elemento in lst:
        if isinstance(elemento, list):
            resultado.extend(flatten_list(elemento))
        else:
            resultado.append(elemento)
    return resultado

def get_all_players():
    list_dir = os.listdir('./saves')
    all_games_data = []

    with open('./data.json', 'r') as json_file:
        data = json.load(json_file)
    
    actual_game = data['actual_game']

    for i in range(len(list_dir)):
        with open(f'./saves/save{i+1}.json', 'r') as json_file:
            player_data = json.load(json_file)
        
        all_games_data.append(to_object(player_data))

    return all_games_data

def get_saves():
    saves = []

    for i in range(len(os.listdir('./saves'))):
        with open(f'./saves/save{i+1}.json', 'r') as json_file:
            saves.append(json.load(json_file))
    
    return saves

# Dialogue functions

def get_dialogue(name_dialogue):
    dialogue_data = {}

    with open('./resources/dialogues.json', 'r') as json_file:
        dialogue_data = json.load(json_file)

    return dialogue_data[name_dialogue]

def run_dialogue(name_dialogue):
    dialogue_data = get_dialogue(name_dialogue)
    args = {}
    
    for key, value in dialogue_data.items():
        requeriments = value['requeriments']
        is_input = value['input']

        requeriments = [args[x] for x in requeriments]

        if requeriments:
            print_str_effect(value['dialogue'].format(*requeriments))
        else:
            print_str_effect(value['dialogue'])
        
        if is_input:
            input_ = input('>>> ')
            input_ = eval(value['type_input'])(input_)

            args[key] = input_

    return args.values()

# Player

def new_player():
    from init import Player

    exit_option = ''
    dialogue = get_dialogue('introduction')
    args = ()

    while exit_option.lower() != 's':
        os.system('clear')
        args = run_dialogue('introduction')
        name, gender, age, exit_option = args

    player = Player(name, gender, age)
    
    time.sleep(1.5)
    os.system('clear')
    chose_pokemon(player)
    time.sleep(1.5)
    os.system('clear')

    print_str_effect('¿Quieres jugar el tutorial(S/N)?')
    tutorial_option = input('>>> ')

    if tutorial_option.lower() == 's':
        time.sleep(2)
        os.system('clear')
        print(player)
        tutorial(player)
    
    time.sleep(2)
    os.system('clear')

    player.actual_menu = designs.main_menu


    return player

def chose_pokemon(player):
    from objects import init_pokemon_data

    pokemon = 0
    pokemon_option = 0
    exit_option = ''

    pokemon_options = ['Charmander', 'Bulbasaur', 'Squirtle']
    
    while not pokemon and exit_option.lower() != 's':
        pokemon_option, exit_option = run_dialogue('chose_pokemon')

        pokemon = init_pokemon_data.get(pokemon_options[pokemon_option-1], 0)
    
    player.set_init_pokemon(pokemon)

def tutorial(player):
    from objects import pokemon_data, potion_1

    run_dialogue('tutorial')
    opponent_pokemon = pokemon_data['Yalo']
    player.opponent_pokemon = opponent_pokemon
    player.add_object(potion_1)

    player_pokemon = player.principal_pokemon

    player.menu_history.append(designs.battle_menu)
    player.actual_menu = designs.battle_menu

    while not opponent_pokemon.is_down:
        opponent_pokemon.health_bar = health_bar(opponent_pokemon)
        player_pokemon.health_bar = health_bar(player_pokemon)
        actual_menu = player.actual_menu
        
        option = actual_menu.open(player)
        
        if actual_menu.name == 'battle_menu_attack':
            player.attack_pokemon(opponent_pokemon, player_pokemon.skills[option])
            time.sleep(0.25)
            player_pokemon.attack_received(opponent_pokemon, opponent_pokemon.skills[0], False)
        elif actual_menu.name == 'use_item_menu':
            time.sleep(0.25)
            player.objects[option].use(1, player_pokemon)        
# Player interactions

def pokemon_fight(player, pokemon):
    option = ''

    print_str_effect(f'¡Te has encontrado un {pokemon.name}({pokemon.level})! |15|'
                      '¿Quieres luchar contra el(S/N)?')
    option = input('>>> ')

    if option.lower() != 's': return
        
    designs.battle_menu.open(player)


def health_bar(pokemon):
    bar_format = '{0} |{1}| {2}%'
        
    health_percentage = (pokemon.health / pokemon.max_health) * 100
    health_percentage = round(health_percentage, 2)

    bar = '█' * int((health_percentage*0.2)) + '▒' * int(((100 - health_percentage)*0.2))

    bar_format = bar_format.format(pokemon.name, bar, health_percentage)

    return bar_format

# Menu Funcs
def get_menu_data(player, menu):
    menu_requeriments = {}
    with open('./menu_requeriments.json', 'r') as json_file:
        menu_requeriments = json.load(json_file)
        
    key = menu.name
    if key not in menu_requeriments: return
    requeriments = menu_requeriments[key]
    
    attribute_list = []

    if not player:
        all_players = get_all_players()
        player_attr = []

        for p in all_players:
            for addres in requeriments:
                player_attr.append(str(get_specific_attr(p, addres)))
            
            player_attr = ' '.join(player_attr)
            attribute_list.append(player_attr)

            player_attr = []

        return flatten_list(attribute_list)
    
    for addres in requeriments:
        attribute = get_specific_attr(player, addres)

        if not attribute: continue

        if isinstance(attribute, list) and hasattr(attribute[0], 'name'):
            attribute = [a.name for a in attribute]
        elif hasattr(attribute, 'name'):
            attribute = attribute.name

        attribute_list.append(attribute)

    return flatten_list(attribute_list)

