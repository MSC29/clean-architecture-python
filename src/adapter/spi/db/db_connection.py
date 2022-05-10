import sqlite3
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
            raise ApiException("error initializing connection to DB: {}".format(str(error))) from error

    def connection(self, config: ConfigurationEntity) -> None:
        self.con = sqlite3.connect(config.dogs_source, check_same_thread=False)
        self.cur = self.con.cursor()

    def migration(self):
        try:
            self.cur.execute("DROP TABLE IF EXISTS dog_facts")
            self.cur.execute("CREATE TABLE IF NOT EXISTS dog_facts (id INTEGER PRIMARY KEY AUTOINCREMENT, fact TEXT)")
            self.cur.execute("INSERT INTO dog_facts (fact) VALUES ('a fact'), ('another fact'), ('yet another fact')")
            self.con.commit()
        except Exception as error:
            raise ApiException("error running migration to DB: {}".format(str(error))) from error
