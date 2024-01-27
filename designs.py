import init
import json, os

class Menu:
    def __init__(self, name, design, static_menu=False):
        self.name = name
        self.design = design

        self.menu_options = {}
        self.menu_data = []

        self.size_data = design.count('{')
        self.static_menu = static_menu

    def set_options(self, options):
        self.menu_options = options

    def set_data(self, data):
        self.menu_data = data

    def run_menu(self, player=0):
        option = 0
        
        self.print_data()
        self.menu_ajust()
       
        print(self.design)
        option = input('>>> ')
        os.system('clear')
        
        if option == '0' and len(player.menu_history)-1:
            player.menu_history.pop()

        if not self.static_menu and option != '0':
            set_menu_vals(self)
            player.menu_history.append(self.menu_options[option])
        elif option != '0':
            return option
        
        player.actual_menu = player.menu_history[-1]
        player.actual_menu.run_menu(player)
    
    def print_data(self):
        menu_data = self.menu_data
        size_data = self.size_data
    
        menu_data += ['?'] * (size_data - len(menu_data))
        self.design = self.design.format(*self.menu_data)
    
    def menu_ajust(self):
        menu = self.design

        side_count = 0
        size_menu = 0
    
        target_side = 2
        target_distance = 0
        
        i = 0
        while i < len(menu):
            if menu[i] == '║':
                if not size_menu: size_menu = i-1
                side_count += 1

            if side_count == target_side*2:
                target_distance = size_menu - (i-1 - size_menu*(target_side+1)+2)
                menu = menu[:i] + ' '*target_distance + menu[i:]

                side_count -= 1
                target_side += 1
                    
            i += 1
    
        self.design = menu

# Map

map_menu = '''
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
║ Ataque: {1} Defensa: {3} Nombre: {5}    1 > Habilidades: {5}║
╚═════════════════════════════════════════════════════════════════════╝
'''
)

# Opponent Pokemon Abilities Menu (Option 4.1)
opponent_pokemon_abilities_menu = Menu('opponent_pokemon_abilities_menu', '''
╔═════════════════════════════════════════════════════════════════════╗
║                         POKÉMON CONTRINCANTE                        ║
╠═════════════════════════════════════════════════════════════════════╣
║ Nivel: {0}  Salud: {2}   Velocidad: {4} 0 > Salir║
║ Ataque: {1} Defensa: {3} Nombre: {5}    1 > Habilidades: {5}║
╚═════════════════════════════════════════════════════════════════════╝
'''
)

# Actual Pokemon Menu (Option 5)
actual_pokemon_menu = Menu('actual_pokemon_menu', '''
╔═════════════════════════════════════════════════════════════════════╗
║                            POKÉMON ACTUAL                           ║
╠═════════════════════════════════════════════════════════════════════╣
║ Nivel: {0}  Salud: {2}   Velocidad: {4} 0 > Salir║
║ Ataque: {1} Defensa: {3} Nombre: {5}    1 > Habilidades: {5}║
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


# Options
main_menu_options = {'1': battle_menu,
                     '2': chat_menu}

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

# Menu data
n_games = 0
actual_game = 0
with open('./data.json', 'r') as json_file:
    data = json.load(json_file)
    n_games = data['n_games']
    actual_game = data['actual_game']

all_games_data = []
game_select_menu_data = []

for i in range(len(os.listdir('./saves'))):
    with open(f'./saves/save{i+1}.json', 'r') as json_file:
        player_data = json.load(json_file)
        name = player_data['name']
        age = player_data['age']
        gender = player_data['gender']
        pokemons = player_data['pokemon_caught']
        id = player_data['id']
    
    all_games_data.append([name, age, gender, pokemons, id])
    game_select_menu_data.append(f'Nombre: {name} | ID: {id}')

porfile_menu_data = all_games_data[actual_game-1]

game_select_menu.set_data(game_select_menu_data)
porfile_menu.set_data(porfile_menu_data)

menu_options = {'main_menu': main_menu_options,
                'battle_menu': battle_menu_options,
                'opponent_pokemon_menu': opponent_pokemon_menu_options,
                'actual_pokemon_menu': actual_pokemon_menu_options,
                'chat_menu': chat_menu_options}

def set_menu_vals(menu):
    menu.set_options(menu_options[menu.name])
