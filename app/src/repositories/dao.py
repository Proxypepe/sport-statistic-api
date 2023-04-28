from abc import ABC, abstractmethod
from src.schemas.schemas import CountryFull


class DAO(ABC):
    @abstractmethod
    async def get_countries(self) -> list[CountryFull]:
        raise NotImplementedError("Implement me!")

    @abstractmethod
    async def insert_country(self, name: str) -> int:
        raise NotImplementedError("Implement me!")

