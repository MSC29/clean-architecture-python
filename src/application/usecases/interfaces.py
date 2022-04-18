from abc import ABC, abstractmethod
from typing import Generic, Iterable, TypeVar

from src.domain.base_entity import BaseEntity

Entity = TypeVar("Entity")


class GenericUseCase(ABC, Generic[Entity]):
    @abstractmethod
    def execute(self) -> Entity:
        """Execute a use case & return an generic type"""


class UseCaseOneEntity(GenericUseCase):
    @abstractmethod
    def execute(self) -> BaseEntity:
        """Execute a use case & return an entity object"""


class UseCaseMultipleEntities(GenericUseCase):
    @abstractmethod
    def execute(self) -> Iterable[BaseEntity]:
        """Execute a use case & return multiple entity objects"""
