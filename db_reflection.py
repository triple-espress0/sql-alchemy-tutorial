"""SQLAlchemy Tutorial"""
from sqlalchemy import create_engine, MetaData, Table

engine = create_engine("sqlite+pysqlite:///sql-alchemy.db", echo=True)

metadata_obj = MetaData()

some_table = Table("some_table", metadata_obj, autoload_with=engine)

print([c.name for c in some_table.columns])
