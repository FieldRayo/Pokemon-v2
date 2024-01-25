# Init main menu
main_menu = f'''
╔══════════════════╗
║     POKÉMON      ║
╠══════════════════╣
║ 1 > Batalla      ║
║ 2 > Pokedex      ║
║ 3 > Bolsa        ║
║ 4 > Salir        ║
╚══════════════════╝
'''

# Battle main menu
battle_menu = f'''
╔═════════════════════════════════════════════════════════════════════╗
║                              BATALLA                                ║
╠═════════════════════════════════════════════════════════════════════╣
║  1 > Atacar           3 > Usar Objeto           5 > Pokémon Actual  ║
║  2 > Cambiar Pokémon  4 > Pokémon Contrincante  6 > Huir            ║                             ║
╚═════════════════════════════════════════════════════════════════════╝
'''

# Battle atack menu (Option 1)
battle_menu_attack = '''
╔═════════════════════════════════════════════════════════════════════╗
║                           MENÚ DE ATAQUE                            ║
╠═════════════════════════════════════════════════════════════════════╣
║ 1 > {0} 3 > {2} 5 > Salir║
║ 2 > {1} 4 > {3} 6 > Volver al Menú║
╚═════════════════════════════════════════════════════════════════════╝
'''

# Battle menu for changing Pokémon (Option 2)
change_pokemon_menu = f'''
╔═════════════════════════════════════════════════════════════════════╗
║                           CAMBIAR POKÉMON                           ║
╠═════════════════════════════════════════════════════════════════════╣
║ 1 > {0} 3 > {2} 5 > {4}║
║ 2 > {1} 4 > {3} 6 > Volver al Menú║
╚═════════════════════════════════════════════════════════════════════╝
'''

# Battle menu for using an item (Option 3)
use_item_menu = f'''
╔═════════════════════════════════════════════════════════════════════╗
║                             USAR OBJETO                             ║
╠═════════════════════════════════════════════════════════════════════╣
║ 1 > {0} 2 > {2} 3 > Siguiente pagina║
║ 4 > {1} 5 > {3} 6 > Volver al Menú║
╚═════════════════════════════════════════════════════════════════════╝
'''

# Battle menu for opponent's Pokémon (Option 4)
opponent_pokemon_menu = f'''
╔═════════════════════════════════════════════════════════════════════╗
║                         POKÉMON CONTRINCANTE                        ║
╠═════════════════════════════════════════════════════════════════════╣
║ Nivel: {0}  Salud: {2}   Velocidad: {4} 1 > Volver al menu║
║ Ataque: {1} Defensa: {3} Nombre: {5}    2 > Habilidades: {5}║
╚═════════════════════════════════════════════════════════════════════╝
'''

# Battle menu for opponent's Pokémon abilities (Option 4.1)
opponent_pokemon_abilities_menu = f'''
╔═════════════════════════════════════════════════════════════════════╗
║                HABILIDADES DEL POKÉMON CONTRINCANTE                 ║
╠═════════════════════════════════════════════════════════════════════╣
║ Habilidad 1: {0} Habilidad 2: {1}║
║ Habilidad 3: {2} Habilidad 4: {3}║
║ Habilidad 5: {4} Habilidad 6: {5}║
║ Habilidad 7: {6} Habilidad 8: {7}║
║ Habilidad 9: {8} Habilidad 10: {9}║
║ 1 > Volver al Menú
╚═════════════════════════════════════════════════════════════════════╝
'''

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

print(menu_ajust(opponent_pokemon_abilities_menu))

