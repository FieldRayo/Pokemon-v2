import json, os

def update_data(actual_game=None, games=None):
    list_saves = os.listdir('./saves')

    data = {}
    
    if actual_game and games:
        data['n_games'] = len(list_saves)
        data['actual_game'] = int(actual_game['n_game'])

        for n, g in enumerate(games):
            data[f'game_{n}'] = g['id']
    else:
        data = {'n_games': 0,
                'actual_game': 0
                }

    with open('./data.json', 'w') as json_file:
        json.dump(data, json_file, indent=4)


