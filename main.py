from designs import *
import funcs
import os, time
import json

def main():
    option = ''
    tutorial_option = ''
    game_option = 1
    
    # Load game
    game_option = game_select_menu.run_menu()

    if os.path.exists(f'./saves/save{game_option}.json'):
        player = funcs.load_data(game_option)
    else:
        player = funcs.new_player()
        player.n_game = game_option

        funcs.save_data(player, game_option)

    player.actual_menu = main_menu
    player.menu_history.append(main_menu)
    while True:
        player.actual_menu.run_menu(player)

main_menu_options = {'1': battle_menu,
                     '2': chat_menu}

if __name__ == '__main__':
    main()
