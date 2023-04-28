from sqlalchemy import Column, Integer, String, ForeignKey, Enum
import enum
from .base import Base


class EventType(enum.Enum):
    START = "match started"


class Event(Base):
    __tablename__ = 'event'

    id = Column('id', Integer, primary_key=True, autoincrement=True)
    match_id = Column('match_id', Integer, ForeignKey('match.id'))
    result = Column('result', Enum(EventType), default=EventType.START)
