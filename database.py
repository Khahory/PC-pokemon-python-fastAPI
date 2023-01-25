from sqlalchemy import create_engine, text

db = "PC.db"
engine = create_engine("sqlite+pysqlite:///"+db, echo=True, future=True)

with engine.connect() as conn:
    print("DATABASE: " + db)