import typing
from src.adapter.spi.db.db import DbConnection
from src.adapter.spi.db.mappers import DogFactDbMapper
from src.application.repositories.dog_facts_repository_abstract import DogFactsRepositoryAbstract
from src.domain.api_exception import ApiException
from src.domain.dog_fact import DogFactEntity


class DogFactRepository(DogFactsRepositoryAbstract):
    def __init__(self, db_connection: DbConnection) -> None:
        self.mapper = DogFactDbMapper()
        self.db_connection = db_connection

    def get_dog_fact_by_id(self, dog_fact_id: int) -> DogFactEntity:
        self.db_connection.cur.execute("select * from dog_facts where id = ?", [dog_fact_id])
        res = self.db_connection.cur.fetchone()

        if not res:
            raise ApiException("couldn't retrieve Dog fact from id")

        return self.mapper.to_entity(res)

    def get_all_dog_facts(self) -> typing.List[DogFactEntity]:
        self.db_connection.cur.execute("select * from dog_facts")
        res = self.db_connection.cur.fetchall()

        if not res:
            raise ApiException("couldn't retrieve Dog facts")

        facts: typing.List[DogFactEntity] = []
        for data in res:
            facts.append(self.mapper.to_entity(data))

        return facts
