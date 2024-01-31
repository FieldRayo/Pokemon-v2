from designs import *
import data
import funcs, init
import os, time
import json
import threading

player: object = None
selected_game = 0

def get_saves():
    saves = []

    for i in range(len(os.listdir('./saves'))):
        with open(f'./saves/save{i+1}.json', 'r') as json_file:
            saves.append(json.load(json_file))
    
    return saves

saves = get_saves()

def main():
    global player
    global selected_game
    global saves

    option = ''
    tutorial_option = ''
    
    selected_game = int(game_select_menu.run_menu())

    player = init.Player(0, 0, 0)

    if os.path.exists(f'./saves/save{selected_game}.json'):
           player.load(saves[selected_game-1])
    else:
        player = funcs.new_player()
        player.n_game = int(selected_game)

        player.save()
        saves = get_saves()

    player.actual_menu = main_menu
    player.menu_history.append(main_menu)

    player.actual_menu.run_menu(player)
    
def update():
    FPS = 30
    time_elapsed = 0

    while True:
        if os.path.exists(f'./saves/save{selected_game}.json'):
            data.update_data(saves[selected_game-1], saves)
        elif not saves:
            data.update_data()
            
        time.sleep(1/FPS)
        time_elapsed += 1/FPS

thread_update = threading.Thread(target=update)
thread_update.daemon = True
thread_update.start()

if __name__ == '__main__':
    data.update_data()
    main()
