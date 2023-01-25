from database import engine
from sqlalchemy import Table, Column, Integer, String, MetaData, text, Boolean, DefaultClause

# relacionamos nuestro metadata con la conexion
metadata_obj = MetaData(engine)

# creamos la tabla pokemon
pokemon_table = Table(
    "pokemon",
    metadata_obj,
    Column("id", Integer, primary_key=True, autoincrement=True),
    Column("nombre", String(50), nullable=False),
    Column("tipo", String(50), nullable=False)
)


# Fetch all pokemon
async def get_pokemon():
    try:
        select = pokemon_table.select()
        with engine.connect() as conn:
            result = conn.execute(select)
            return result.mappings().all()
    except Exception as e:
        print(e)
        return False


# Save a pokemon
async def save_pokemon(nombre, tipo):
    try:
        insert = pokemon_table.insert().values(nombre=nombre, tipo=tipo)
        with engine.connect() as conn:
            conn.execute(insert)
            conn.commit()
            return True
    except Exception as e:
        print(e)
        return False
