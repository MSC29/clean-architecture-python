import typing
from src.adapter.spi.db.db_connection import DbConnection
from src.adapter.spi.db.db_models import DogFact
from src.adapter.spi.db.mappers import DogFactDbMapper
from src.application.repositories.dog_facts_repository_abstract import DogFactsRepositoryAbstract
from src.domain.api_exception import ApiException
from src.domain.dog_fact import DogFactEntity


class DogFactRepository(DogFactsRepositoryAbstract):
    def __init__(self, db_connection: DbConnection) -> None:
        self.mapper = DogFactDbMapper()
        self.db_connection = db_connection

    def get_dog_fact_by_id(self, dog_fact_id: int) -> DogFactEntity:
        res = DogFact.select().where(DogFact.id == dog_fact_id).get()

        if not res:
            raise ApiException("couldn't retrieve Dog fact from id")

        return self.mapper.to_entity(res)

    def get_all_dog_facts(self) -> typing.List[DogFactEntity]:
        res = DogFact.select()

        if not res:
            raise ApiException("couldn't retrieve Dog facts")

        facts: typing.List[DogFactEntity] = []
        for data in res:
            facts.append(self.mapper.to_entity(data))

        return facts
