import time, os
from init import init_pokemon_data, Player, Pokemon
import designs
import json

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

def object_to_dic(obj):
    allowed_data = (str, int, float, bool, list, tuple)
    
    if not isinstance(obj, allowed_data) and obj:
        dic = vars(obj) if not isinstance(obj, dict) else obj
        for key, value in dic.items():
            dic[key] = object_to_dic(value)
    
        return dic

    return obj

def save_data(player, n_game):
    player_data = {}

    for attr_name, attr_value in vars(player).items():
        if isinstance(attr_value, (str, int, float, bool, list, tuple, dict)) and not attr_value:
            player_data[attr_name] = attr_value
        else:
            player_data[attr_name] = object_to_dic(attr_value)

    with open(f'./saves/save{n_game}.json', 'w') as json_file:
        json.dump(player_data, json_file, indent=4)

def load_data(n_game):
    with open(f'./saves/save{n_game}.json', 'r') as json_file:
        player_data = json.load(json_file)

    player = Player(0, 0, 0)
    
    for attr_name in vars(player):
        try:
            setattr(player, attr_name, player_data[attr_name])
        except KeyError:
            continue
    
    return player

def new_player():
    exit_option = ''

    while exit_option.lower() != 's':
        os.system('clear')

        print_str_effect('Bienvenido!,|15| dime,|15| como te llamas?: ')
        name = input('>>> ')
        
        print_str_effect(f'Excelente nombre {name}!|10| ahora dime tu genero\n1: Chico\n2: Chica')
        gender = int(input('>>> ')) - 1
        
        print_str_effect(f'Para finalizar|15| ¿porque no me dices tu edad?')
        age = int(input('>>> '))

        exit_option = input('Confirmas tus datos(S/N)? : ')

    print_str_effect('Perfecto, ahora podras empezar a jugar!')
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
        tutorial(player)
    
    time.sleep(2)
    os.system('clear')

    player.actual_menu = designs.main_menu


    return player


def chose_pokemon(player):
    pokemon = 0
    pokemon_option = 0
    exit_option = ''

    pokemon_options = ['Charmander', 'Bulbasaur', 'Squirtle']
    
    while not pokemon and exit_option.lower() != 's':
        print_str_effect('Elije un pokemon entre las siguientes opciones: ')
        print('''
        1 -> Charmander
        2 -> Bulbasaur
        3 -> Squirtle
              ''')
        pokemon_option = int(input('>>> '))

        print_str_effect('Estas segur{0} de tu eleccion(S/N)?'.format('a' if player.gender else 'o'))
        exit_option = input('>>> ')

        pokemon = init_pokemon_data.get(pokemon_options[pokemon_option-1], 0)

    player.set_init_pokemon(pokemon)

def tutorial(player):
    continue_option = ''
    
    print_str_effect('Bienvenido a este mundo de pokemon,|15| antes de iniciar con tu aventura'
                     'te dare las instrucciones para que puedas tener una correcta experiencia|15|'
                     '\n¿estas listo(S/N)?')
    continue_option = input('>>> ')
        
    while continue_option.lower() != 's':
        print_str_effect('.|65|.|65|.|65| ¿listo(S/N)?')
        continue_option = input('>>> ')
    
    print_str_effect('A continuacion tendras tu primera batalla pokémon!|20| ¿No es emocionante?|20|'
                     '¡Claro que lo es!|15|, Tu primera batalla sera contra "Yalo"|15| un pokemon'
                     ' de tipo electrico')
    
    option = ''

    player.actual_menu = designs.battle_menu
    while True:
        print(player.actual_menu)
        option = input('>>> ')


