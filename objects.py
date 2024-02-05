from init import *

# Skills
placaje = Skill('Placaje', 1, None)
skills_data = {'Placaje': placaje}

# Types - fire
fire = Type('fire')
fire.set_stats([1.5, 2, 0.8, 1.2, 0.6])
fire.set_counter(['water', 'stone', 'electric', 'ice'])

# Types - plant
plant = Type('plant')
plant.set_stats([2, 1, 1.2, 0.8, 1.5])
plant.set_counter(['fire', 'electric', 'ice', 'flying'])

# Types - water
water = Type('water')
water.set_stats([1.2, 0.8, 1, 1.6, 1.8])
water.set_counter(['plant', 'electric', 'stone', 'fighter'])

# Types - electric
electric = Type('electric')
electric.set_stats([1, 1.5, 0.8, 2, 1.2])

# Pokemon - Charmander
charmander = Pokemon('Charmander', fire)
charmander.set_type(fire)
charmander.set_counter(fire)
charmander.set_skill(placaje)

charmander.set_init_stats(random.sample(range(0, 100), 5))
charmander.set_standard_stats()

charmander.xp_need = 1
charmander.isinit_pokemon = True

# Pokemon - Bulbasaur
bulbasaur = Pokemon('Bulbasaur', plant)
bulbasaur.set_type(plant)
bulbasaur.set_counter(plant)
bulbasaur.set_skill(placaje)

bulbasaur.set_init_stats(random.sample(range(0, 100), 5))
bulbasaur.set_standard_stats()

bulbasaur.xp_need = 1
bulbasaur.isinit_pokemon = True

# Pokemon - Squirtle
squirtle = Pokemon('Squirtle', water)
squirtle.set_type(water)
squirtle.set_counter(water)
squirtle.set_skill(placaje)

squirtle.set_init_stats(random.sample(range(0, 100), 5))
squirtle.set_standard_stats()

squirtle.xp_need = 1
squirtle.isinit_pokemon = True

# Pokemon - Yalo
yalo = Pokemon('Yalo', electric)
yalo.set_type(electric)
yalo.set_counter(electric)
yalo.set_skill(placaje)

yalo.set_init_stats(random.sample(range(0, 100), 5))
yalo.set_standard_stats()

yalo.xp_need = 1
yalo.isinit_pokemon = True

# Pokemon - Data
init_pokemon_data = {'Charmander': charmander,
                     'Bulbasaur': bulbasaur,
                     'Squirtle': squirtle}

pokemon_data = {'Charmander': charmander,
                'Bulbasaur': bulbasaur,
                'Squirtle': squirtle,
                'Yalo': yalo}

# Objects

# Objects - Potion

def potion(level=0, pokemon=None):
    healing_percentage = level*0.20
    pokemon_health = pokemon.health
    healing_increase = pokemon_health + pokemon_health * healing_percentage
        
    if pokemon_health+healing_increase < pokemon.max_health:
        pokemon.health += healing_increase
    else:
        pokemon.health = pokemon.max_health

potion_1 = Object('potion_1', 10, 'Healing potion +20%', potion)
potion_2 = Object('potion_2', 25, 'Healing potion +40%', potion)
potion_3 = Object('potion_3', 45, 'Healing potion +60%', potion)
potion_4 = Object('potion_4', 70, 'Healing potion +80%', potion)
potion_5 = Object('potion_5', 95, 'Healing potion +100%', potion)

for n, o in enumerate((potion_1, potion_2, potion_3, potion_4, potion_5)):
    o.level = n+1

