from abc import ABC, abstractmethod
from typing import Generic, TypeVar

Entity = TypeVar("Entity")
DbModel = TypeVar("DbModel")


class DbMapper(ABC, Generic[Entity, DbModel]):

    @abstractmethod
    def to_db(self, entity: Entity) -> DbModel:
        """Map an Entity to a DbModel"""

    @abstractmethod
    def to_entity(self, model: DbModel) -> Entity:
        """Map a DbModel to an Entity"""
