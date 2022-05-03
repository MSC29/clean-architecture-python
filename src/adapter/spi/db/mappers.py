from typing import Any
from src.application.mappers.db_mapper import DbMapper, DbModel
from src.domain.dog_fact import DogFactEntity


class DogFactDbMapper(DbMapper):

    def to_db(self, entity: DogFactEntity) -> DbModel:
        raise Exception("not implemented")

    def to_entity(self, db_obj: Any) -> DogFactEntity:
        return DogFactEntity(db_obj[0], db_obj[1])
