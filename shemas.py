from pydantic import BaseModel


class PokemonRequestModel(BaseModel):
    pokemon_name: str
    pokemon_tipo: str
