from fastapi import FastAPI

# mis imports
from models import PokemonModel
from shemas import PokemonRequestModel

# vamos a ponerle un nombre a la aplicación
app = FastAPI(
    title="PC_Pokemon",
    description="API para la aplicación de PC Pokemon",
    version="0.0.1",
)


@app.get("/")
async def read_pokemon():
    res = await PokemonModel.get_pokemon()
    return res


@app.get("/pokemon/{pokemon_name}/{pokemon_tipo}")
async def create_pokemon(pokemon_name: str, pokemon_tipo: str):
    # primera letra en mayúscula
    pokemon_name = pokemon_name.capitalize()
    pokemon_tipo = pokemon_tipo.capitalize()

    # guardamos el pokemon
    await PokemonModel.save_pokemon(pokemon_name, pokemon_tipo)

    return {
        "pokemon_name": pokemon_name,
        "pokemon_tipo": pokemon_tipo,
    }


# eventos de inicio y fin
@app.on_event("startup")
async def startup_event():
    print("Iniciando la aplicación")


@app.on_event("shutdown")
async def shutdown_event():
    print("Cerrando la aplicación")