from abc import ABC, abstractmethod
import typing

from src.domain.dog_fact import DogFactEntity


class DogFactsRepositoryAbstract(ABC):
    @abstractmethod
    def get_dog_fact_by_id(self, dog_fact_id: int) -> DogFactEntity:
        """Get Fact By Id"""

    @abstractmethod
    def get_all_dog_facts(self) -> typing.List[DogFactEntity]:
        """Get a list of facts"""
