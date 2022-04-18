from abc import ABC
from typing import TypeVar

Entity = TypeVar("Entity")
HttpObj = TypeVar("HttpObj")


class HttpMapper(ABC):
    def to_http(self, entity: Entity) -> HttpObj:
        """Map an Entity to an http object"""

    def to_entity(self, http_obj: HttpObj) -> Entity:
        """Map an http object to an Entity"""
