"""SQLAlchemy Tutorial"""
from sqlalchemy import create_engine, text

engine = create_engine("sqlite+pysqlite:///sql-alchemy.db", echo=True)

with engine.connect() as conn:
    result = conn.execute(text("SELECT x, y FROM some_table"))
    # for row in result:

    for dict_row in result.mappings():
        x = dict_row["x"]
        y = dict_row["y"]
        print(x, y)
