from abc import ABC, abstractmethod
from typing import TypeVar

Entity = TypeVar("Entity")
DbModel = TypeVar("DbModel")


class DbMapper(ABC):

    @abstractmethod
    def to_db(self, entity: Entity) -> DbModel:
        """Map an Entity to a db model"""

    @abstractmethod
    def to_entity(self, db_obj: DbModel) -> Entity:
        """Map a db model to an Entity"""
