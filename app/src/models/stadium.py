from sqlalchemy import Column, Integer, String, Date, ForeignKey

from .base import Base


class Stadium(Base):
    __tablename__ = 'stadium'

    id = Column(Integer, primary_key=True, autoincrement=True)
    opening_date = Column(Date, nullable=False)
    capacity = Column(Integer, nullable=False)
    country_id = Column(Integer, ForeignKey('country.id'), nullable=False)
