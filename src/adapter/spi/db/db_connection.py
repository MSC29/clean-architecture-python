from peewee import SqliteDatabase, Database

from src.adapter.spi.db.db_models import DogFact
from src.application.spi.db_interface import DbInterface
from src.domain.api_exception import ApiException
from src.domain.configuration_entity import ConfigurationEntity


class DbConnection(DbInterface):
    def __init__(self, config: ConfigurationEntity) -> None:
        try:
            self.connection(config)

            if config.env != "test":
                self.migration()
        except Exception as error:
            raise ApiException(
                "error initializing connection to DB: {}".format(str(error))) from error

    def connection(self, config: ConfigurationEntity) -> None:
        self.database = SqliteDatabase(config.dogs_source)
        self.database.bind([DogFact])
        self.database.connect()

    def migration(self):
        try:
            self.database.create_tables([DogFact])
            DogFact.truncate_table()
            DogFact.create(id=1, fact="a first fact")
            DogFact.create(id=2, fact="a second fact")
            DogFact.create(id=3, fact="a third fact")
        except Exception as error:
            raise ApiException("error running migration to DB: {}".format(str(error))) from error

    def get_db(self) -> Database:
        return self.database
