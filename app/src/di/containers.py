from dependency_injector import containers, providers

from src.db.database import Database
from src.repositories.repository import Repository
from src.services.service import Service
from src.core.config import Config


class Container(containers.DeclarativeContainer):
    wiring_config = containers.WiringConfiguration(
        modules=["src.endpoints.country"]
    )
    c = providers.Configuration()
    config = Config()
    print(f"postgresql://{config.DB_USERNAME}:{config.DB_PASSWORD}@{config.DB_HOST}:{config.DB_PORT}/{config.DB_NAME}")
    db = providers.Singleton(
        Database,
        db_url=f"postgresql://{config.DB_USERNAME}:{config.DB_PASSWORD}@{config.DB_HOST}:{config.DB_PORT}/{config.DB_NAME}"
    )

    repository = providers.Factory(
        Repository,
        session_factory=db.provided.session,
    )

    service = providers.Factory(
        Service,
        repository=repository,
    )
