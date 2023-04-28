from fastapi import APIRouter, Depends, status, Response
from dependency_injector.wiring import inject, Provide

from src.di.containers import Container

from src.repositories.dao import DAO
from src.repositories.repository import Repository
import src.schemas.schemas as schemas

country_router = APIRouter()


@country_router.get('/countries', status_code=status.HTTP_200_OK, response_model=list[schemas.CountryFull])
@inject
async def get_countries(
        service: DAO = Depends(Provide[Container.service])
) -> list[schemas.CountryFull]:
    countries = await service.get_countries()
    return [schemas.CountryFull.from_orm(country) for country in countries]


@country_router.post('/', status_code=status.HTTP_201_CREATED, response_model=int)
@inject
async def add_country(
        country: schemas.Country,
        service: DAO = Depends(Provide[Container.service])
) -> int:
    return await service.insert_country(country.name)
