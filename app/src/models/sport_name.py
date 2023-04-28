from sqlalchemy import Column, Integer, String

from .base import Base


class SportName(Base):
    __tablename__ = 'sport_name'

    id = Column('id', Integer, primary_key=True, autoincrement=True)
    name = Column('name', String)
