from designs import *
import funcs
import os, time

def main():
    option = ''
    tutorial_option = ''

    player = funcs.new_player()
    time.sleep(2)
    os.system('clear')
    funcs.chose_pokemon(player)
    time.sleep(2)
    os.system('clear')

    funcs.print_str_effect('¿Quieres jugar el tutorial(S/N)?')
    tutorial_option = input('>>> ')

    if tutorial_option.lower() == 's':
        time.sleep(2)
        os.system('clear')
        funcs.tutorial(player)
    
    time.sleep(2)
    os.system('clear')

    player.actual_menu = main_menu
    funcs.save_data(player)

    while True:
        funcs.run_menu(player, player.actual_menu)
        os.system('clear')

main_menu_options = {'1': battle_menu,
                     '2': chat_menu}

if __name__ == '__main__':
    main()
