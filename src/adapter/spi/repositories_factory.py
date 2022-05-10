from src.adapter.spi.db.db_connection import DbConnection
from src.adapter.spi.db.dog_fact_repository import DogFactRepository
from src.adapter.spi.http.cat_fact_repository import CatFactsRepository
from src.adapter.spi.http.http_connection import HttpConnection
from src.domain.configuration_entity import ConfigurationEntity


class RepositoriesFactory:

    def __init__(self, config: ConfigurationEntity, db_connection: DbConnection, http_connection: HttpConnection) -> None:
        self.__repositories: dict = {
            "cat_fact_repository": CatFactsRepository(http_connection, config.cats_source),
            "dog_fact_repository": DogFactRepository(db_connection)
        }

    def get_repository(self, repository_name: str):
        if repository_name in self.__repositories:
            return self.__repositories[repository_name]
        else:
            raise Exception("Repository does not exist")
