from sqlalchemy import Column, Integer, String, ForeignKey

from .base import Base


class Team(Base):
    __tablename__ = 'team'

    id = Column(Integer, primary_key=True, autoincrement=True)
    league_id = Column('league_id', Integer, ForeignKey('league.id'), nullable=False)
    country_id = Column('country_id', Integer, ForeignKey('country.id'), nullable=False)
    owner = Column('owner', String, nullable=True)
