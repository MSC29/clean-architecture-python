from abc import ABC
import typing

from src.domain.cat_fact import CatFactEntity


class CatFactRepositoryAbstract(ABC):
    def get_cat_fact(self) -> CatFactEntity:
        """Get Random Fact"""

    def get_cat_facts(self) -> typing.List[CatFactEntity]:
        """Get a list of facts"""
