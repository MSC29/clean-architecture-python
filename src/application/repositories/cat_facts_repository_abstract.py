from abc import ABC, abstractmethod
import typing

from src.domain.cat_fact import CatFactEntity


class CatFactsRepositoryAbstract(ABC):
    @abstractmethod
    def get_random_cat_fact(self) -> CatFactEntity:
        """Get random Fact"""

    @abstractmethod
    def get_all_cat_facts(self) -> typing.List[CatFactEntity]:
        """Get a list of facts"""
