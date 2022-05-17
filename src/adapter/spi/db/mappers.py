from src.adapter.spi.db.db_models import DogFact
from src.application.mappers.db_mapper import DbMapper, DbModel
from src.domain.dog_fact import DogFactEntity


class DogFactDbMapper(DbMapper):

    def to_db(self, entity: DogFactEntity) -> DbModel:
        raise Exception("not implemented")

    def to_entity(self, model: DogFact) -> DogFactEntity:
        return DogFactEntity(model.id, model.fact)
