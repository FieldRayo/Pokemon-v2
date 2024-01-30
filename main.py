from designs import *
import data
import funcs, init
import os, time
import json
import threading

# Arregla lo de los diccionarios!!!! porfavor

player: object = None
game_option = 0
saves = []

for i in range(len(os.listdir('./saves'))):
    with open(f'./saves/save{i+1}.json', 'r') as json_file:
        saves.append(json.load(json_file))

def main():
    global player
    global game_option

    option = ''
    tutorial_option = ''
    
    # Load game
    game_option = int(game_select_menu.run_menu())
    player = init.Player(0, 0, 0)

    if os.path.exists(f'./saves/save{game_option}.json'):
        player.load_data(saves[game_option-1])
    else:
        player = funcs.new_player()
        player.n_game = int(game_option)
        
        player.save_data()
        
    player.actual_menu = main_menu
    player.menu_history.append(main_menu)

    player.actual_menu.run_menu(player)
    
def update():
    FPS = 30
    time_elapsed = 0

    while True:
        if player and game_option:
            data.update_data(game_option)
            
        time.sleep(1/FPS)
        time_elapsed += 1/FPS

thread_update = threading.Thread(target=update)
thread_update.daemon = True
thread_update.start()

if __name__ == '__main__':
    data.update_data(0)
    main()
