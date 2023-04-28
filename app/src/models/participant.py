from sqlalchemy import Column, Integer, String, ForeignKey

from .base import Base


class Participant(Base):
    __tablename__ = 'participant'

    id = Column('id', Integer, primary_key=True, autoincrement=True)
    league_id = Column('league_id', Integer, ForeignKey('league.id'), nullable=False)
    team_id = Column('team_id', Integer, ForeignKey('team.id'), nullable=False)
    score = Column('score', Integer, default=0, nullable=False)
