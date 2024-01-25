import time, os
from init import init_pokemon_data, Player

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

def tutorial():
    continue_option = ''
    
    print_str_effect('Bienvenido a este mundo de pokemon,|15| antes de iniciar con tu aventura'
                     'te dare las instrucciones para que puedas tener una correcta experiencia|15|'
                     '\n¿estas listo(S/N)?')
    continue_option = input('>>> ')
        
    while continue_option.lower() != 's':
        print_str_effect('.|65|.|65|.|65| ¿listo(S/N)?')
        continue_option = input('>>> ')

    

#p1 = new_player()
#chose_pokemon(p1)
tutorial()
