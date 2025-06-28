import asyncio
from enum import Enum
from sqlalchemy import Text, Integer
from sqlalchemy.ext.asyncio import create_async_engine
from sqlmodel import Field, SQLModel

SQLALCHEMY_DATABASE_URL = 'postgresql+asyncpg://postgres:1@localhost:5432/postgres'
engine = create_async_engine(SQLALCHEMY_DATABASE_URL, echo=True)


class Status(str, Enum):
    VAL1 = 'val1'
    VAL2 = 'val2'


class Category(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    name: str = Field(sa_type=Text)


class Product(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    name: str = Field(sa_type=Text,index=True)
    category_id: int = Field(sa_type=Integer,foreign_key='category.id')


async def create_db_and_tables():
    async with engine.begin() as conn:
        await conn.run_sync(SQLModel.metadata.create_all)

metadata = SQLModel.metadata


if __name__ == "__main__":
    asyncio.run(create_db_and_tables())



