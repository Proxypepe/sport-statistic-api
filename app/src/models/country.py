from sqlalchemy import Column, Integer, String

from .base import Base


class Country(Base):
    __tablename__ = 'country'

    id = Column('id', Integer, primary_key=True, autoincrement=True)
    name = Column('name', String(96), nullable=False, index=True, unique=True)
