from abc import ABC, abstractmethod
from typing import Generic, TypeVar

Entity = TypeVar("Entity")
HttpObj = TypeVar("HttpObj")


class HttpMapper(ABC, Generic[Entity, HttpObj]):

    @abstractmethod
    def to_http(self, entity: Entity) -> HttpObj:
        """Map an Entity to an HttpObj"""

    @abstractmethod
    def to_entity(self, http_obj: HttpObj) -> Entity:
        """Map an HttpObj to an Entity"""
