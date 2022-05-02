import typing
from src.application.repositories.cat_facts_repository_abstract import CatFactsRepositoryAbstract
from src.application.usecases.interfaces import UseCaseMultipleEntities
from src.domain.cat_fact import CatFactEntity


class GetAllCatFactUseCase(UseCaseMultipleEntities):
    def __init__(self, repo: CatFactsRepositoryAbstract) -> None:
        self.repo = repo

    # TODO Error Handling
    def execute(self) -> typing.Iterable[CatFactEntity]:
        return self.repo.get_cat_facts()
