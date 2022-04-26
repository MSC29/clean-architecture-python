
from fastapi import FastAPI
from injector import Injector, SingletonScope
from fastapi_injector import attach_injector

from src.adapter.api.cat_facts import controllers as cat_facts_controller
from src.adapter.api.dog_facts import controllers as dog_facts_controller
from src.adapter.spi.db.db import DbConnection
from src.adapter.spi.http.http import HttpConnection
from src.adapter.spi.repositories_factory import RepositoriesFactory
from src.domain.configuration_entity import ConfigurationEntity
from src.infrastructure.config_mapper import ConfigurationMapper

config: ConfigurationEntity = ConfigurationMapper().get_config()
db_connection: DbConnection = DbConnection(config)
http_connection: HttpConnection = HttpConnection()
repositories_factory = RepositoriesFactory(config, db_connection, http_connection)


def create_app(injector: Injector) -> FastAPI:
    app: FastAPI = FastAPI()

    app.include_router(dog_facts_controller.router, prefix="/dogs", tags=["dogs"])
    app.include_router(cat_facts_controller.router, prefix="/cats", tags=["cats"])

    injector.binder.bind(RepositoriesFactory, to=repositories_factory, scope=SingletonScope)

    attach_injector(app, injector)
    return app
