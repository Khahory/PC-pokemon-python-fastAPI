from pydantic import BaseModel


class PokemonRequestModel(BaseModel):
    pokemon_name: str
    pokemon_tipo: str


class PokemonResponseModel(BaseModel):
    pokemon_id: int
    pokemon_name: str
    pokemon_tipo: str
