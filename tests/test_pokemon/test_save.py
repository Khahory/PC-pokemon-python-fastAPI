from models import PokemonModel


def test_save_pokemon():
    # creamos un pokemon
    pokemon_name = "Pikachu"
    pokemon_tipo = "Electrico"

    # guardamos el pokemon
    res = PokemonModel.save_pokemon(pokemon_name, pokemon_tipo)
    assert res is True

