from models import PokemonModel

# creamos la tabla
PokemonModel.metadata_obj.drop_all()
PokemonModel.metadata_obj.create_all()
