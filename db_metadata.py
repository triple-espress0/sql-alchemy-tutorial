"""SQLAlchemy Tutorial"""
from sqlalchemy import (
    create_engine,
    Column,
    ForeignKey,
    Integer,
    MetaData,
    Table,
    String,
)

engine = create_engine("sqlite+pysqlite:///sql-alchemy.db", echo=True)

metadata_obj = MetaData()

user_table = Table(
    "user_account",
    metadata_obj,
    Column("id", Integer, primary_key=True),
    Column("name", String(30)),
    Column("fullname", String),
)

address_table = Table(
    "address",
    metadata_obj,
    Column("id", Integer, primary_key=True),
    Column("user_id", ForeignKey("user_account.id"), nullable=False),
    Column("email_address", String, nullable=False),
)

metadata_obj.create_all(engine)
