from init import *

# Skills
placaje = Skill('Placaje', 3, None)
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
water.set_stats([1.2, 0.8, 1, 2, 1.8])
water.set_counter(['plant', 'electric', 'stone', 'fighter'])

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

# Pokemon - Data
init_pokemon_data = {'Charmander': charmander,
                     'Bulbasaur': bulbasaur,
                     'Squirtle': squirtle}
pokemon_data = {'Charmander': charmander,
                'Bulbasaur': bulbasaur,
                'Squirtle': squirtle}

