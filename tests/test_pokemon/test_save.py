from models import PokemonModel
import pytest

# indicamos que vamos a usar el plugin pytest_asyncio
# con esto puedo llamar funciones async
pytest_plugins = ('pytest_asyncio',)


@pytest.mark.asyncio
async def test_save_pokemon():
    # creamos un pokemon
    pokemon_name = "Pikachu"
    pokemon_tipo = "Electrico"

    # guardamos el pokemon
    res = await PokemonModel.save_pokemon(pokemon_name, pokemon_tipo)
    assert res is True
