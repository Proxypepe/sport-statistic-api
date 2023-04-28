from fastapi import FastAPI

from src.di.containers import Container
from src.models.base import Base
from src.endpoints.country import country_router


def create_app() -> FastAPI:
    container = Container()

    # db = container.db()
    # db.create_database()

    app = FastAPI()
    app.container = container
    app.include_router(country_router, prefix='/api/v1/country', tags=['Country'])

    return app
