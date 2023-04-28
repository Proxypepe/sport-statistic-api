import enum

from sqlalchemy import Column, Integer, String, ForeignKey, Enum, Date
from sqlalchemy.orm import relationship

from .base import Base


class Results(enum.Enum):
    HOME = 'Home team won'
    GUEST = 'Guest team won'
    DRAW = 'Draw'


class Match(Base):
    __tablename__ = 'match'

    id = Column('id', Integer, primary_key=True, autoincrement=True)
    stadium_id = Column('stadium_id', Integer, ForeignKey('stadium.id'), nullable=False)
    league_id = Column('league_id', Integer, ForeignKey('league.id'), nullable=False)
    home_team_id = Column('home_team_id', ForeignKey('team.id'), nullable=False)
    guest_team_id = Column('guest_team_id', ForeignKey('team.id'), nullable=False)
    start = Column('start', Date, nullable=True)
    end = Column('end', Date, nullable=True)
    duration = Column('duration', Integer, nullable=False, default=0)
    result = Column('result', Enum(Results), default=Results.DRAW)
    home_score = Column('home_score', Integer, nullable=False, default=0)
    guest_score = Column('guest_score', Integer, nullable=False, default=0)

    referees = relationship('Referee', secondary='match_has_referee')
