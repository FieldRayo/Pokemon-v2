
import unittest
from init import *

class TestSerialization(unittest.TestCase):

    def setUp(self):
        # Crear instancias de objetos para las pruebas
        self.player = Player("Ash", "Male", 16)
        self.pokemon = Pokemon("Pikachu", Type("Electric"))

    def test_to_dict_and_to_object(self):
        # Convertir objeto a diccionario y luego de vuelta a objeto
        player_dict = to_dict(self.player)
        player_obj = to_object(player_dict)

        # Comprobar que los atributos del jugador son los mismos después de la conversión
        self.assertEqual(self.player.name, player_obj.name)
        self.assertEqual(self.player.gender, player_obj.gender)
        self.assertEqual(self.player.age, player_obj.age)
        self.assertEqual(self.player.id, player_obj.id)
        self.assertEqual(self.player.money, player_obj.money)
        self.assertEqual(self.player.n_game, player_obj.n_game)
        self.assertEqual(type(self.player.init_pokemon), type(player_obj.init_pokemon))

        # Convertir objeto Pokemon a diccionario y luego de vuelta a objeto Pokemon
        pokemon_dict = to_dict(self.pokemon)
        pokemon_obj = to_object(pokemon_dict)

        # Comprobar que los atributos del Pokémon son los mismos después de la conversión
        self.assertEqual(self.pokemon.name, pokemon_obj.name)
        self.assertEqual(self.pokemon.gender, pokemon_obj.gender)
        self.assertEqual(type(self.pokemon.type_), type(pokemon_obj.type_))
        self.assertEqual(self.pokemon.xp, pokemon_obj.xp)
        self.assertEqual(self.pokemon.level, pokemon_obj.level)
        self.assertEqual(self.pokemon.iv_health, pokemon_obj.iv_health)
        self.assertEqual(self.pokemon.iv_damage, pokemon_obj.iv_damage)
        self.assertEqual(self.pokemon.iv_defense, pokemon_obj.iv_defense)
        self.assertEqual(self.pokemon.iv_speed, pokemon_obj.iv_speed)
        self.assertEqual(self.pokemon.iv_precision, pokemon_obj.iv_precision)

if __name__ == '__main__':
    unittest.main()

