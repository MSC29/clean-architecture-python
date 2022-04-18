from src.adapter.spi.db.db import DbConnection
from src.adapter.spi.db.dog_fact_repository import DogFactRepository
from src.adapter.spi.http.cat_fact_repository import CatFactRepository
from src.domain.configuration_entity import ConfigurationEntity


class RepositoriesFactory:

    def __init__(self, config: ConfigurationEntity, db_connection: DbConnection) -> None:
        self.__repositories: dict = {
            "cat_fact_repository": CatFactRepository(config.cats_source),
            "dog_fact_repository": DogFactRepository(db_connection)
        }

    def get_repository(self, repository_name: str):
        if repository_name in self.__repositories:
            return self.__repositories[repository_name]
        else:
            raise Exception("Repository does not exist")
