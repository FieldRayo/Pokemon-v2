from init import Menu, to_object
import json, os

# Menu
game_select_menu = Menu('game_select_menu', '''
╔═════════════════════════════════════════════════════════════════════╗
║                             Partidas                                ║
╠═════════════════════════════════════════════════════════════════════╣
║  1 > {0}║
║  2 > {1}║
║  3 > {2}║
║  4 > {3}║
║  5 > Siguiente Pag.║
╚═════════════════════════════════════════════════════════════════════╝

''', static_menu=True
)

# Main menu
main_menu = Menu('main_menu', '''
╔══════════════════╗
║     POKÉMON      ║
╠══════════════════╣
║ 1 > Batalla      ║
║ 2 > Chat         ║
║ 3 > Mapa         ║
║ 4 > Tienda       ║
║ 5 > Pokedex      ║
║ 6 > Bolsa        ║
║ 7 > Ajustes      ║
║ 8 > Guardar      ║
╚══════════════════╝
'''
)

# Battle Menu

battle_menu = Menu('battle_menu', '''
╔═════════════════════════════════════════════════════════════════════╗
║                              BATALLA                                ║
╠═════════════════════════════════════════════════════════════════════╣
║  1 > Atacar           3 > Usar Objeto           5 > Pokémon Actual  ║
║  2 > Cambiar Pokémon  4 > Pokémon Contrincante  6 > Huir            ║
║  0 > Salir                                                          ║
╚═════════════════════════════════════════════════════════════════════╝
'''
)

# Battle Menu Attack (Option 1)

battle_menu_attack = Menu('battle_menu_attack', '''
╔═════════════════════════════════════════════════════════════════════╗
║                           MENÚ DE ATAQUE                            ║
╠═════════════════════════════════════════════════════════════════════╣
║ 1 > {0}    6 > {5}║
║ 2 > {1}    7 > {6}║
║ 3 > {3}    8 > {7}║
║ 4 > {3}    9 > {8}║
║ 5 > {4}    10 > {9}║
║ 0 > Salir                                                           ║
╚═════════════════════════════════════════════════════════════════════╝
'''
)

# Change Pokemon Menu (Option 2)
change_pokemon_menu = Menu('change_pokemon_menu', '''
╔═════════════════════════════════════════════════════════════════════╗
║                           CAMBIAR POKÉMON                           ║
╠═════════════════════════════════════════════════════════════════════╣
║ 1 > {0}║
║ 2 > {1}║ 
║ 3 > {2}║
║ 4 > {3}║
║ 5 > {4}║
║ 6 > {5}║
║ 0 > Salir║
╚═════════════════════════════════════════════════════════════════════╝
'''
)

# Use Item Menu (Option 3)
use_item_menu = Menu('use_item_menu', '''
╔═════════════════════════════════════════════════════════════════════╗
║                             USAR OBJETO                             ║
╠═════════════════════════════════════════════════════════════════════╣
║ 1 > {0}║
║ 2 > {1}║
║ 3 > {2}║
║ 4 > {3}║
║ 5 > {4}║
║ 6 > {5}║
║ 7 > Siguiente Pag.║
║ 0 > Salir║
╚═════════════════════════════════════════════════════════════════════╝
'''
)

# Opponent Pokemon Menu (Option 4)
opponent_pokemon_menu = Menu('opponent_pokemon_menu', '''
╔═════════════════════════════════════════════════════════════════════╗
║                         POKÉMON CONTRINCANTE                        ║
╠═════════════════════════════════════════════════════════════════════╣
║ Nivel: {0}  Salud: {2}   Velocidad: {4} 0 > Salir║
║ Ataque: {1} Defensa: {3} Nombre: {5}    1 > Habilidades║
╚═════════════════════════════════════════════════════════════════════╝
'''
)

# Opponent Pokemon Abilities Menu (Option 4.1)
opponent_pokemon_abilities_menu = Menu('opponent_pokemon_abilities_menu', '''
╔═════════════════════════════════════════════════════════════════════╗
║                         POKÉMON CONTRINCANTE                        ║
╠═════════════════════════════════════════════════════════════════════╣
║ Nivel: {0}  Salud: {2}   Velocidad: {4} 0 > Salir║
║ Ataque: {1} Defensa: {3} Nombre: {5}    1 > Habilidades║
╚═════════════════════════════════════════════════════════════════════╝
'''
)

# Actual Pokemon Menu (Option 5)
actual_pokemon_menu = Menu('actual_pokemon_menu', '''
╔═════════════════════════════════════════════════════════════════════╗
║                            POKÉMON ACTUAL                           ║
╠═════════════════════════════════════════════════════════════════════╣
║ Nivel: {0}  Salud: {2}   Velocidad: {4} 0 > Salir║
║ Ataque: {1} Defensa: {3} Nombre: {5}    1 > Habilidades║
╚═════════════════════════════════════════════════════════════════════╝
'''
)

# Actual Pokemon Abilities Menu (Option 5.1)
actual_pokemon_abilities_menu = Menu('actual_pokemon_abilities_menu', '''
╔═════════════════════════════════════════════════════════════════════╗
║                   HABILIDADES DEL POKÉMON ACTUAL                    ║
╠═════════════════════════════════════════════════════════════════════╣
║ Habilidad 1: {0} Habilidad 2: {1}║
║ Habilidad 3: {2} Habilidad 4: {3}║
║ Habilidad 5: {4} Habilidad 6: {5}║
║ Habilidad 7: {6} Habilidad 8: {7}║
║ Habilidad 9: {8} Habilidad 10: {9}║
║ 0 > Salir
╚═════════════════════════════════════════════════════════════════════╝
'''
)

# Chat Menu

chat_menu = Menu('chat_menu','''
╔════════════════════════════════════════════════╗
║                  MENÚ DE CHAT                  ║
╠════════════════════════════════════════════════╣
║ 1 > Mensajes Privados({0})║
║ 2 > Perfil                                     ║
║ 3 > Configuración                              ║
║ 0 > Salir                                      ║
╚════════════════════════════════════════════════╝
'''
)

# Private messages (Option 1)
private_messages_menu = Menu('private_messages_menu','''
╔════════════════════════════════════════════════╗
║               MÉNSAJES PRIVADOS                ║
╠════════════════════════════════════════════════╣
║ 1 > {0} 5 > {4}║
║ 2 > {1} 6 > {5}║
║ 3 > {2} 7 > {6}║
║ 4 > {3} 8 > {7}║
║ 9 > Siguiente Pag. 10 > Salir                  ║
╚════════════════════════════════════════════════╝
'''
)
# Porfile Menu (Option 2)
porfile_menu = Menu('porfile_menu', '''
╔════════════════════════════════════════════════╗
║                     PERFIL                     ║
╠════════════════════════════════════════════════╣
║ Nombre: {0}║
║ Edad: {1}║
║ Genero: {2}║
║ Pokémones: {3}║
║ ID: {4}║
║ 0 > Salir                                      ║
╚════════════════════════════════════════════════╝
'''
)

# Config Menu (Option 3)
config_menu = Menu('config_menu', '''
╔════════════════════════════════════════════════╗
║                  Configuración                 ║
╠════════════════════════════════════════════════╣
║ 1 > Cambiar Nombre                             ║
║ 2 > Cambiar Edad                               ║
║ 3 > Cambiar Genero                             ║
║ 4 > Bloquear a                                 ║
║ ID: {4}║
╚════════════════════════════════════════════════╝
'''
)

# Map menu

map_menu = Menu('map_menu', '''
############################################################
#                                                          #
#  🏠                                                      #
#                                                          #
#                                                          #
#                                                          #
#                                                          #
#                                                          #
#                                                          #
#                                                          #
#                                                          #
############################################################
'''
)

# Store

store_menu = Menu('store_menu', '''
╔════════════════════════════════════════════════╗
║                     Tienda                     ║
╠════════════════════════════════════════════════╣
║ 1 > {0}║
║ 2 > {1}║
║ 3 > {2}║
║ 4 > {3}║
║ 5 > Siguiente Pag                              ║
║ 0 > Slir                                       ║
╚════════════════════════════════════════════════╝
'''
)

menu_map = {'main_menu': main_menu,
            'battle_menu': battle_menu,
            'opponent_pokemon_menu': opponent_pokemon_menu,
            'actual_pokemon_menu': actual_pokemon_menu,
            'chat_menu': chat_menu
            }

# Menu Options
main_menu_options = {'1': battle_menu,
                     '2': chat_menu,
                     '3': map_menu,
                     '4': store_menu}

#Battle Menu Options
battle_menu_options = {
                       '1': battle_menu_attack,
                       '2': change_pokemon_menu,
                       '3': use_item_menu,
                       '4': opponent_pokemon_menu,
                       '5': actual_pokemon_menu,
                       '6': 0}
opponent_pokemon_menu_options = {'1': opponent_pokemon_abilities_menu}
actual_pokemon_menu_options = {'1': actual_pokemon_abilities_menu}

#Chat Menu Options
chat_menu_options = {'1': private_messages_menu,
                     '2': porfile_menu,
                     '3': config_menu}

menu_options = {'main_menu': main_menu_options,
                'battle_menu': battle_menu_options,
                'opponent_pokemon_menu': opponent_pokemon_menu_options,
                'actual_pokemon_menu': actual_pokemon_menu_options,
                'chat_menu': chat_menu_options
                }

for menu in menu_map.values():
    menu.set_options(menu_options[menu.name])


# Menu data
data = {}
player_data = {}

all_games_data = []
game_select_menu_data = []

def load_all_data():
    list_dir = os.listdir('./saves')

    with open('./data.json', 'r') as json_file:
        data = json.load(json_file)
    
    actual_game = data['actual_game']

    for i in range(len(list_dir)):
        with open(f'./saves/save{i+1}.json', 'r') as json_file:
            player_data = json.load(json_file)
        
        all_games_data.append(player_data)

    return all_games_data


def load_menu_options(menu):
    menu.set_options(menu_options[menu.name])

def get_menu_data(player, menu):
    menu_requeriments = {}
    with open('./menu_requeriments.json', 'r') as json_file:
        menu_requeriments = json.load(json_file)
        
    key = menu.name
    if key not in menu_requeriments: return
    requeriments = menu_requeriments[key]
    
    attributes = []

    if not player:
        attr_game = []

        all_games_data = load_all_data()
        for game in all_games_data:
            for attr in requeriments:
                attr_game.append(str(game[attr]))

            attr_game = ' '.join(attr_game)
            attributes.append(attr_game)

        return flatten_list(attributes)

    attribute = player
    
    for attr in requeriments:
        attr = attr.split('.')
        for i in range(len(attr)):
            if isinstance(attribute, list):
                attribute = [x[attr[i]] for x in attribute]
                continue
            
            attribute = getattr(attribute, attr[i])

        if isinstance(attribute, dict):
            attribute = list(attribute)
        
        if attribute:
            attributes.append(attribute)
        
        attribute = player

    return flatten_list(attributes)

def flatten_list(lst):
    resultado = []
    for elemento in lst:
        if isinstance(elemento, list):
            resultado.extend(flatten_list(elemento))
        else:
            resultado.append(elemento)
    return resultado
