from fastapi import FastAPI
from fastapi import HTTPException


# mis imports
from models import PokemonModel
from shemas import PokemonRequestModel, PokemonResponseModel

# vamos a ponerle un nombre a la aplicación
app = FastAPI(
    title="PC_Pokemon",
    description="API para la aplicación de PC Pokemon",
    version="0.0.1",
)


@app.get("/pokemon/{pokemon_id}")
async def read_pokemon(pokemon_id: int):
    res = await PokemonModel.get_pokemon(pokemon_id)

    if len(res) < 1:
        return HTTPException(status_code=404, detail="No se encontró el pokemon")

    return PokemonResponseModel(
        pokemon_id=res[0]["id"],
        pokemon_name=res[0]["nombre"],
        pokemon_tipo=res[0]["tipo"],
    )


@app.get("/pokemones/")
async def read_pokemon():
    res = await PokemonModel.get_pokemon()
    return res


@app.post("/pokemon/")
async def create_pokemon(pokemon: PokemonRequestModel):
    # primera letra en mayúscula
    pokemon_name = pokemon.pokemon_name.capitalize()
    pokemon_tipo = pokemon.pokemon_tipo.capitalize()

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
