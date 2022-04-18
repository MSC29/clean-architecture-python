from src.application.repositories.cat_fact_repository_abstract import CatFactRepositoryAbstract
from src.application.usecases.interface import UseCase
from src.domain.base_entity import BaseEntity
from src.domain.cat_fact import CatFactEntity


class GetOneCatFactUseCase(UseCase):
    def __init__(self, repo: CatFactRepositoryAbstract) -> None:
        self.repo = repo

    def execute(self) -> CatFactEntity:
        return self.repo.get_cat_fact()
