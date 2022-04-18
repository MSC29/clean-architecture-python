import sqlite3
from src.domain.api_exception import ApiException
from src.domain.configuration_entity import ConfigurationEntity


class DbConnection:
    def __init__(self, config: ConfigurationEntity) -> None:
        try:
            self.con = sqlite3.connect(config.dogs_source)
            self.cur = self.con.cursor()

            self.__migration()
        except Exception as error:
            raise ApiException(str(error))

    def __migration(self):
        try:
            self.cur.execute('''CREATE TABLE IF NOT EXISTS dog_facts (id INTEGER PRIMARY KEY AUTOINCREMENT, fact TEXT)''')
            self.cur.execute("INSERT INTO dog_facts (fact) VALUES ('a fact'), ('another fact'), ('yet another fact')")
        except Exception as error:
            raise ApiException(error)
