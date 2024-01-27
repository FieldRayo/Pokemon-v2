from designs import *
import funcs
import os, time
import json

def main():
    option = ''
    tutorial_option = ''
    game_option = 1
    
    # Load game
    print(menu_ajust(game_select_menu))
    game_option = input('>>> ')
    time.sleep(1)
    os.system('clear')

    if os.path.exists(f'./saves/save{game_option}.json'):
        player = funcs.load_data(game_option)
    else:
        player = funcs.new_player()
        player.n_game = game_option

        funcs.save_data(player, game_option)
        
    while True:
        funcs.run_menu(player, player.actual_menu)
        os.system('clear')

main_menu_options = {'1': battle_menu,
                     '2': chat_menu}

if __name__ == '__main__':
    main()
