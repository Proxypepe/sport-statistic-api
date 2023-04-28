from src.repositories.repository import Repository
from src.schemas.schemas import CountryFull
from src.models.country import Country


class Service:
    def __init__(self, repository: Repository):
        self._repository = repository

    async def get_countries(self) -> list[CountryFull]:
        return await self._repository.get_countries()

    async def insert_country(self, name: str) -> int:
        return await self._repository.insert_country(name)
