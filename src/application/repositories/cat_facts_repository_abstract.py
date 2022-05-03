from abc import ABC, abstractmethod
import typing

from src.domain.cat_fact import CatFactEntity


class CatFactsRepositoryAbstract(ABC):
    @abstractmethod
    def get_cat_fact(self) -> CatFactEntity:
        """Get Random Fact"""

    @abstractmethod
    def get_cat_facts(self) -> typing.List[CatFactEntity]:
        """Get a list of facts"""
