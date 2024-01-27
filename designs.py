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

    def run_menu(self):
        option = 0
        
        if self.menu_data:
            self.print_data()
            self.menu_ajust()
        
        print(self.design)
        option = input('>>> ')
        os.system('clear')
        
        if not self.static_menu:
            self.menu_options[option].run_menu()
        else:
            return option

    
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



chat_menu = '''
╔════════════════════════════════════════════════╗
║                  MENÚ DE CHAT                  ║
╠════════════════════════════════════════════════╣
║ 1 > Mensajes Privados({1})║
║ 2 > Perfil                                     ║
║ 3 > Configuración                              ║
║ 4 > Salir del Chat                             ║
╚════════════════════════════════════════════════╝
'''

# Private messages (Option 1)
private_messages_menu = '''
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
# Porfile Menu (Option 2)
porfile_menu = '''
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

# Config Menu (Option 3)
config_menu = '''
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
║  3 > {2}║
║  2 > {1}║
║  4 > {3}║
║  5 > Siguiente Pag.║
╚═════════════════════════════════════════════════════════════════════╝

''', static_menu=True
)

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
║ 8 > Salir        ║
╚══════════════════╝
'''
)

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

battle_menu_attack = Menu('battle_menu_attack', '''
╔═════════════════════════════════════════════════════════════════════╗
║                           MENÚ DE ATAQUE                            ║
╠═════════════════════════════════════════════════════════════════════╣
║ 1 > {0} 3 > {2}║
║ 2 > {1} 4 > {3}║
║ 0 > Salir                                                           ║
╚═════════════════════════════════════════════════════════════════════╝
'''
)

change_pokemon_menu = Menu('change_pokemon_menu', '''
╔═════════════════════════════════════════════════════════════════════╗
║                           CAMBIAR POKÉMON                           ║
╠═════════════════════════════════════════════════════════════════════╣
║ 1 > {0} 3 > {2} 5 > {4}║
║ 2 > {1} 4 > {3} 6 > {5}║
║ 0 > Salir║
╚═════════════════════════════════════════════════════════════════════╝
'''
)

use_item_menu = Menu('use_item_menu', '''
╔═════════════════════════════════════════════════════════════════════╗
║                             USAR OBJETO                             ║
╠═════════════════════════════════════════════════════════════════════╣
║ 1 > {0} 3 > {2} 5 > Siguiente pagina║
║ 2 > {1} 4 > {3}║
║ 0 > Salir                                                           ║
╚═════════════════════════════════════════════════════════════════════╝
'''
)

opponent_pokemon_menu = Menu('opponent_pokemon_menu', '''
╔═════════════════════════════════════════════════════════════════════╗
║                         POKÉMON CONTRINCANTE                        ║
╠═════════════════════════════════════════════════════════════════════╣
║ Nivel: {0}  Salud: {2}   Velocidad: {4} 0 > Salir║
║ Ataque: {1} Defensa: {3} Nombre: {5}    1 > Habilidades: {5}║
╚═════════════════════════════════════════════════════════════════════╝
'''
)

opponent_pokemon_abilities_menu = Menu('opponent_pokemon_abilities_menu', '''
╔═════════════════════════════════════════════════════════════════════╗
║                         POKÉMON CONTRINCANTE                        ║
╠═════════════════════════════════════════════════════════════════════╣
║ Nivel: {0}  Salud: {2}   Velocidad: {4} 0 > Salir║
║ Ataque: {1} Defensa: {3} Nombre: {5}    1 > Habilidades: {5}║
╚═════════════════════════════════════════════════════════════════════╝
'''
)

actual_pokemon_menu = Menu('actual_pokemon_menu', '''
╔═════════════════════════════════════════════════════════════════════╗
║                            POKÉMON ACTUAL                           ║
╠═════════════════════════════════════════════════════════════════════╣
║ Nivel: {0}  Salud: {2}   Velocidad: {4} 0 > Salir║
║ Ataque: {1} Defensa: {3} Nombre: {5}    1 > Habilidades: {5}║
╚═════════════════════════════════════════════════════════════════════╝
'''
)

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

# Chat menu

# Options
main_menu_options = {'1': battle_menu,
                     '2': chat_menu}
battle_menu_options = {'0': main_menu,
                       '1': battle_menu_attack,
                       '2': change_pokemon_menu,
                       '3': use_item_menu,
                       '4': opponent_pokemon_menu,
                       '5': actual_pokemon_menu,
                       '6': 0}
battle_menu_attack_options = {'0': battle_menu}
change_pokemon_menu_option = {'0': battle_menu}
use_item_menu_options = {'0': battle_menu}
opponent_pokemon_menu_options = {'0': battle_menu,
                                 '1': opponent_pokemon_abilities_menu}
opponent_pokemon_abilities_menu_options = {'0': opponent_pokemon_menu}
actual_pokemon_menu_options = {'0': battle_menu,
                               '1': actual_pokemon_abilities_menu}
actual_pokemon_abilities_menu_option = {'0': actual_pokemon_menu}

# Menu data
n_games = 0
actual_game = 0
with open('./data.json', 'r') as json_file:
    data = json.load(json_file)
    n_games = data['n_games']
    actual_game = data['actual_game']

game_select_menu_data = []
for a in os.listdir('./saves'):
    with open(f'./saves/{a}', 'r') as json_file:
        player_data = json.load(json_file)
        name = player_data['name']
        id = str(player_data['id'])

    game_select_menu_data.append(f'Nombre: {name} | ID: {id}')

game_select_menu.set_data(game_select_menu_data)

# Definir una lista de tuplas que contenga cada menú y sus opciones correspondientes
menus_and_options = [
    (main_menu, main_menu_options),
    (battle_menu, battle_menu_options),
    (battle_menu_attack, battle_menu_attack_options),
    (change_pokemon_menu, change_pokemon_menu_option),
    (use_item_menu, use_item_menu_options),
    (opponent_pokemon_menu, opponent_pokemon_menu_options),
    (opponent_pokemon_abilities_menu, opponent_pokemon_abilities_menu_options),
    (actual_pokemon_menu, actual_pokemon_menu_options),
    (actual_pokemon_abilities_menu, actual_pokemon_abilities_menu_option)
]

for menu, options in menus_and_options:
    menu.set_options(options)
