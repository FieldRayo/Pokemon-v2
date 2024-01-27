import main
import json, os

def update():
    data = {'n_games': len(os.listdir('./saves')),
            'actual_game': main.game_option}
    
    for a, n in enumerate(os.listdir('./saves')):
        with open(f'./saves/{n}', 'r') as json_file:
            data[f'game_{a}'] = json.load(json_file)['id']

    with open('./data.json', 'w') as json_file:
        json.dump(data, json_file, indent=4)

if __name__ == '__main__':
    update()
