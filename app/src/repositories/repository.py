from .base import BaseRepository
from .dao import DAO
from src.models.country import Country


class Repository(BaseRepository, DAO):
    async def get_countries(self) -> list[Country]:
        with self.session_factory() as session:
            countries = session.query(Country).all()
            if not countries:
                return []
            return countries

    async def insert_country(self, name: str) -> int:
        with self.session_factory() as session:
            country = Country(
                name=name
            )
            session.add(country)
            session.commit()
            session.refresh(country)
            return country.id

