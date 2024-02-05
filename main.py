import data
import funcs, init
import os, time
import json
import threading

from designs import main_menu, game_select_menu, load_menu

player: object = None
selected_game = 0
saves = funcs.get_saves()

def main():
    global player
    global selected_game
    global saves

    selected_game = int(game_select_menu.open())
    player = init.Player(0, 0, 0)

    if os.path.exists(f'./saves/save{selected_game}.json'):
           player.load(saves[selected_game-1])
    else:
        player = funcs.new_player()
        player.n_game = int(selected_game)

        player.save()
        saves = funcs.get_saves()
    
    data.update_data(saves[selected_game-1], saves)
        
    player.actual_menu = main_menu
    player.menu_history = [main_menu]

    while True:
        option = player.actual_menu.open(player)

        if player.actual_menu.name == 'battle_menu_attack':
            player.attack_pokemon(player.opponent_pokemon, player.principal_pokemon.skills[option-1])

def update():
    FPS = 50
    time_elapsed = 0

    while True:
        if os.path.exists(f'./saves/save{selected_game}.json'):
            # Automatic save every second
            if not time_elapsed % 1:
                player.save()
            
            load_menu(player)
 
         # It is rounded to 2 decimal places to avoid loss of precision.
        time_elapsed = round(time_elapsed + 1/FPS, 2)
        time.sleep(1/FPS)
        
thread_update = threading.Thread(target=update)
thread_update.daemon = True
thread_update.start()

if __name__ == '__main__':
    data.update_data()
    main()
