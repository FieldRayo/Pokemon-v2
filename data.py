import json, os

def update_data(actual_game):
    list_saves = os.listdir('./saves')

    data = {}
    
    data['n_games'] = len(list_saves)
    data['actual_game'] = int(actual_game)

    for a, n in enumerate(list_saves):
        with open(f'./saves/{n}', 'r') as json_file:
            data[f'game_{a}'] = json.load(json_file)['id']

    with open('./data.json', 'w') as json_file:
        json.dump(data, json_file, indent=4)


