from designs import *
import data
import funcs
import os, time
import json
import threading

player: object = None
game_option = 0

def main():
    global player
    global game_option

    option = ''
    tutorial_option = ''
    
    # Load game
    game_option = game_select_menu.run_menu()

    if os.path.exists(f'./saves/save{game_option}.json'):
        player = funcs.load_data(game_option)
    else:
        player = funcs.new_player()
        player.n_game = int(game_option)

        funcs.save_data(player, game_option)

    player.actual_menu = main_menu
    player.menu_history.append(main_menu)
    
    player.actual_menu.run_menu(player)

def update():
    fps = 30
    while True:
        if player and game_option:
            data.update_data(game_option)
        
        time.sleep(1/fps)

thread_update = threading.Thread(target=update)
thread_update.daemon = True
thread_update.start()

if __name__ == '__main__':
    data.update_data(0)
    main()
