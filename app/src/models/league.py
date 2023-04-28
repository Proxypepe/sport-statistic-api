from sqlalchemy import Column, Integer, String, Date, ForeignKey

from .base import Base


class League(Base):
    __tablename__ = 'league'

    id = Column('id', Integer, primary_key=True, autoincrement=True)
    name = Column('name', String, nullable=False)
    season = Column('season', Integer, nullable=False)
    start = Column('start', Date, nullable=True)
    end = Column('end', Date, nullable=True)
    country_id = Column('country_id', Integer, ForeignKey('country.id'), nullable=False)
    sport_name_id = Column('sport_name_id', Integer, ForeignKey('country.id'), nullable=False)
