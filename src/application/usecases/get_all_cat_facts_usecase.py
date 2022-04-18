import typing
from src.application.repositories.cat_fact_repository_abstract import CatFactRepositoryAbstract
from src.application.usecases.interfaces import UseCaseMultipleEntities
from src.domain.cat_fact import CatFactEntity


class GetAllCatFactUseCase(UseCaseMultipleEntities):
    def __init__(self, repo: CatFactRepositoryAbstract) -> None:
        self.repo = repo

    def execute(self) -> typing.Iterable[CatFactEntity]:
        return self.repo.get_cat_facts()
