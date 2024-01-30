import time, os
from pokemon import init_pokemon_data
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
        pokemon_option, exit_option = run_dialogue('chose_pokemon')

        pokemon = init_pokemon_data.get(pokemon_options[pokemon_option-1], 0)
    
    player.set_init_pokemon(pokemon)

def tutorial(player):
    run_dialogue('tutorial')
    
def pokemon_fight(player, pokemon):
    option = ''

    print_str_effect(f'¡Te has encontrado un {pokemon.name}({pokemon.level})! |15|'
                      '¿Quieres luchar contra el(S/N)?')
    option = input('>>> ')

    if option.lower() != 's': return
        
    designs.battle_menu.run_menu(player)
