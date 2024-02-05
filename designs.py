from init import Menu
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
{0} {1}
'''
)

# Battle Menu Attack (Option 1)

battle_menu_attack = Menu('battle_menu_attack', '''
╔═════════════════════════════════════════════════════════════════════╗
║                           MENÚ DE ATAQUE                            ║
╠═════════════════════════════════════════════════════════════════════╣
║ 1 > {0}║
║ 2 > {1}║
║ 3 > {3}║
║ 4 > {3}║
║ 5 > {4}║
║ 0 > Salir                                                           ║
╚═════════════════════════════════════════════════════════════════════╝
''', static_menu=True
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
''', static_menu=True
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
''', static_menu=True
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
profile_menu = Menu('porfile_menu', '''
╔════════════════════════════════════════════════╗
║                     PERFIL                     ║
╠════════════════════════════════════════════════╣
║ Nombre: {0}║
║ Edad: {1}║
║ Genero: {2}║
║ Pokémon Principal: {3}║
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

menu_opions = {}

from functools import partial

def load_menu(player):
    global menu_opions

    # Main Menu Options
    main_menu_options = {
        0: partial(battle_menu.open, player),
        1: partial(chat_menu.open, player),
        2: partial(map_menu.open, player),
        3: partial(store_menu.open, player)
    }

    # Battle Menu Options
    battle_menu_options = {
        0: partial(battle_menu_attack.open, player),
        1: partial(change_pokemon_menu.open, player),
        2: partial(use_item_menu.open, player),
        3: partial(opponent_pokemon_menu.open, player),
        4: partial(actual_pokemon_menu.open, player),
        5: 0
    }

    # Opponent Pokemon Menu Options
    opponent_pokemon_menu_options = {
        0: partial(opponent_pokemon_abilities_menu.open, player)
    }

    # Actual Pokemon Menu Options
    actual_pokemon_menu_options = {
        0: partial(actual_pokemon_abilities_menu.open, player)
    }

    # Chat Menu Options
    chat_menu_options = {
        0: partial(private_messages_menu.open, player),
        1: partial(profile_menu.open, player),
        2: partial(config_menu.open, player)
    }

    menu_options = {'main_menu': main_menu_options,
                    'battle_menu': battle_menu_options,
                    'opponent_pokemon_menu': opponent_pokemon_menu_options,
                    'actual_pokemon_menu': actual_pokemon_menu_options,
                    'chat_menu': chat_menu_options
                    }

    for menu in menu_map.values():
        menu.set_options(menu_options[menu.name])

