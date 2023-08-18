"""SQLAlchemy Tutorial"""


from sqlalchemy import (
    bindparam,
    create_engine,
    Column,
    ForeignKey,
    insert,
    Integer,
    MetaData,
    Table,
    select,
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

# -------------------------
# stmt = insert(user_table).values(name="spongebob", fullname="Spongebob Squarepants")

# print(stmt)

# compiled = stmt.compile()

# print(compiled.params)

# with engine.connect() as conn:
#     result = conn.execute(stmt)
#     conn.commit()
#     print(result.inserted_primary_key)
# -------------------------

# with engine.connect() as conn:
#     result = conn.execute(
#         insert(user_table),
#         [
#             {"name": "sandy", "fullname": "Sandy Cheeks"},
#             {"name": "patrick", "fullname": "Patrick Star"},
#         ],
#     )
#     conn.commit()
# -------------------------

# scalar_subq = (
#     select(user_table.c.id)
#     .where(user_table.c.name == bindparam("username"))
#     .scalar_subquery()
# )

# with engine.connect() as conn:
#     result = conn.execute(
#         insert(address_table).values(user_id=scalar_subq),
#         [
#             {
#                 "username": "spongebob",
#                 "email_address": "spongebob@sqlalchemy.org",
#             },
#             {"username": "sandy", "email_address": "sandy@sqlalchemy.org"},
#             {"username": "sandy", "email_address": "sandy@squirrelpower.org"},
#         ],
#     )
#     conn.commit()
# -------------------------

# print(insert(user_table).values().compile(engine))
# -------------------------

insert_stmt = insert(address_table).returning(
    address_table.c.id, address_table.c.email_address
)
print(insert_stmt)
