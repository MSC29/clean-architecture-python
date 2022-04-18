from abc import ABC

from src.domain.base_entity import BaseEntity


class UseCase(ABC):
    def execute(self) -> BaseEntity:
        """Execute a use case & return an entity object"""
