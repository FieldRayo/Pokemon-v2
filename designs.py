import init
import json, os

# Select game
game_select_menu = '''
╔═════════════════════════════════════════════════════════════════════╗
║                             Partidas                                ║
╠═════════════════════════════════════════════════════════════════════╣
║  1 > {0} 3 > {2} 5 > Siguiente Pag.║
║  2 > {1} 4 > {3}║
╚═════════════════════════════════════════════════════════════════════╝

'''


# Init main menu
main_menu = f'''
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

# Battle main menu
battle_menu = f'''
╔═════════════════════════════════════════════════════════════════════╗
║                              BATALLA                                ║
╠═════════════════════════════════════════════════════════════════════╣
║  1 > Atacar           3 > Usar Objeto           5 > Pokémon Actual  ║
║  2 > Cambiar Pokémon  4 > Pokémon Contrincante  6 > Huir            ║
║  0 > Salir                                                          ║
╚═════════════════════════════════════════════════════════════════════╝
'''

# Battle atack menu (Option 1)
battle_menu_attack = '''
╔═════════════════════════════════════════════════════════════════════╗
║                           MENÚ DE ATAQUE                            ║
╠═════════════════════════════════════════════════════════════════════╣
║ 1 > {0} 3 > {2}║
║ 2 > {1} 4 > {3}║
║ 0 > Salir                                                           ║
╚═════════════════════════════════════════════════════════════════════╝
'''

# Battle menu for changing Pokémon (Option 2)
change_pokemon_menu = '''
╔═════════════════════════════════════════════════════════════════════╗
║                           CAMBIAR POKÉMON                           ║
╠═════════════════════════════════════════════════════════════════════╣
║ 1 > {0} 3 > {2} 5 > {4}║
║ 2 > {1} 4 > {3} 6 > {5}║
║ 0 > Salir║
╚═════════════════════════════════════════════════════════════════════╝
'''

# Battle menu for using an item (Option 3)
use_item_menu = '''
╔═════════════════════════════════════════════════════════════════════╗
║                             USAR OBJETO                             ║
╠═════════════════════════════════════════════════════════════════════╣
║ 1 > {0} 3 > {2} 5 > Siguiente pagina║
║ 2 > {1} 4 > {3}║
║ 0 > Salir                                                           ║
╚═════════════════════════════════════════════════════════════════════╝
'''

# Battle menu for opponent's Pokémon (Option 4)
opponent_pokemon_menu = '''
╔═════════════════════════════════════════════════════════════════════╗
║                         POKÉMON CONTRINCANTE                        ║
╠═════════════════════════════════════════════════════════════════════╣
║ Nivel: {0}  Salud: {2}   Velocidad: {4} 0 > Salir║
║ Ataque: {1} Defensa: {3} Nombre: {5}    1 > Habilidades: {5}║
╚═════════════════════════════════════════════════════════════════════╝
'''

# Battle menu for opponent's Pokémon abilities (Option 4.1)
opponent_pokemon_abilities_menu = '''
╔═════════════════════════════════════════════════════════════════════╗
║                HABILIDADES DEL POKÉMON CONTRINCANTE                 ║
╠═════════════════════════════════════════════════════════════════════╣
║ Habilidad 1: {0} Habilidad 2: {1}║
║ Habilidad 3: {2} Habilidad 4: {3}║
║ Habilidad 5: {4} Habilidad 6: {5}║
║ Habilidad 7: {6} Habilidad 8: {7}║
║ Habilidad 9: {8} Habilidad 10: {9}║
║ 0 > Salir
╚═════════════════════════════════════════════════════════════════════╝
'''



# Battle menu for actual Pokémon (Option 5)
actual_pokemon_menu = '''
╔═════════════════════════════════════════════════════════════════════╗
║                            POKÉMON ACTUAL                           ║
╠═════════════════════════════════════════════════════════════════════╣
║ Nivel: {0}  Salud: {2}   Velocidad: {4} 0 > Salir║
║ Ataque: {1} Defensa: {3} Nombre: {5}    1 > Habilidades: {5}║
╚═════════════════════════════════════════════════════════════════════╝
'''

# Battle menu for actual Pokémon abilities (Option 5.1)
actual_pokemon_abilities_menu = '''
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

# Chat main menu
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

def get_option_menu(menu):
    return {main_menu: main_menu_options,
                       battle_menu: battle_menu_options,
                       battle_menu_attack: battle_menu_attack_options,
                       change_pokemon_menu: change_pokemon_menu_option,
                       use_item_menu: use_item_menu_options,
                       opponent_pokemon_menu: opponent_pokemon_menu_options,
                       opponent_pokemon_abilities_menu: opponent_pokemon_abilities_menu_options,
                       actual_pokemon_menu: actual_pokemon_menu_options,
                       actual_pokemon_abilities_menu: actual_pokemon_abilities_menu_option
                       }.get(menu, 0)

def menu_ajust(menu):
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
    
    return menu


