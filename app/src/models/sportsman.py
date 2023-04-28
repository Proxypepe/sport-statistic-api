from sqlalchemy import Column, Integer, String, Date, ForeignKey

from .base import Base


class Sportsman(Base):
    __tablename__ = 'sportsman'

    id = Column('id', Integer, primary_key=True, autoincrement=True)
    name = Column('name', String, nullable=False)
    surname = Column('surname', String, nullable=False)
    birthday = Column('birthday', Date, nullable=False)
    age = Column('age', Integer, nullable=False)

    team_id = Column('team_id', Integer, ForeignKey('team.id'), nullable=False)
