from database import engine

from sqlalchemy import Table, Column, Integer, String, MetaData, text, Boolean, DefaultClause
from fastapi import HTTPException

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
async def get_pokemon(pokemon_id=None):
    try:
        select = pokemon_table.select()

        if pokemon_id:
            select = select.where(pokemon_table.c.id == pokemon_id)

        with engine.connect() as conn:
            result = conn.execute(select)
            result = result.mappings().all()

            if len(result) < 1:
                return HTTPException(status_code=404, detail="No se encontró el pokemon")
            return result

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
