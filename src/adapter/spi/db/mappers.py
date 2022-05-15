from typing import Any
from src.application.mappers.db_mapper import DbMapper, DbModel
from src.domain.dog_fact import DogFactEntity


class DogFactDbMapper(DbMapper):

    def to_db(self, entity: DogFactEntity) -> DbModel:
        raise Exception("not implemented")

    def to_entity(self, model: Any) -> DogFactEntity:
        return DogFactEntity(model[0], model[1])
