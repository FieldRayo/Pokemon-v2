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
╔══════════════════════════════════════════════════════════════════╗
║                             BATALLA                              ║
╠══════════════════════════════════════════════════════════════════╣
║ 1 > Atacar          3 > Usar Objeto          5 > Pokémon Actual  ║
║ 2 > Cambiar Pokémon 4 > Pokémon Contrincante 6 > Huir            ║                             ║
╚══════════════════════════════════════════════════════════════════╝
'''

# Battle atack menu
battle_menu_attack = f'''
╔══════════════════════════════════════════════════════════════════╗
║                   MENÚ DE ATAQUE                                 ║
╠══════════════════════════════════════════════════════════════════╣
║ 1 > {0} 3 > {2} 5 > Salir║
║ 2 > {1} 4 > {3} 6 > Volver al Menú║
╚══════════════════════════════════════════════════════════════════╝
'''

def menu_ajust(menu):
    side_count = 0
    size_menu = 0

    side_a, side_b = False, False
    
    i = 0
    while not side_b:
        if menu[i] == '║':
            if not size_menu: size_menu = i-1
            side_count += 1
        
        if side_count == 4 and not side_a:
            menu = menu[:i-1] + ' '*(size_menu - (i-1 - size_menu*3)-2) + menu[i-1:]
            side_a = True

        elif side_count == 7 and not side_b:
            menu = menu[:i-1] + ' '*(size_menu - (i-1 - size_menu*4)-2) + menu[i-1:]
            side_b = True

        i += 1
    
    return menu

