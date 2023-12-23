import time, os
from init import init_pokemon_data, Player

def print_str_effect(str_, end='\n'):
    default_time = 0.025

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

def new_player():
    opt = ''

    while opt.lower() != 's':
        print_str_effect('Bienvenido!,|15| dime,|15| como te llamas?: ')
        name = input('>>> ')
        print_str_effect(f'Excelente nombre {name}!|10| ahora dime tu genero\n1: Chico\n2: Chica')
        gender = input('>>> ')

        opt = input('Confirmas tus datos(S/N)? : ')
    
    print_str_effect('Perfecto, ahora podras empezar a jugar!')
    player = Player(name, gender)

    return player


def chose_pokemon(player):
    pokemon = 0
    opt = 0
    pokemon_options = ['Charmander', 'Bulbasaur', 'Squirtle']
    
    while not pokemon:
        print_str_effect('Elije un pokemon entre las siguientes opciones: ')
        print('''
        1 -> Charmander
        2 -> Bulbasaur
        3 -> Squirtle
              ''')
        opt = int(input('>>> '))
        pokemon = init_pokemon_data.get(pokemon_options[opt-1], 0)
    
    player.set_init_pokemon(pokemon)

new_player()
