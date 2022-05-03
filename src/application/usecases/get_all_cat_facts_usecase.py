import typing
from src.application.repositories.cat_facts_repository_abstract import CatFactsRepositoryAbstract
from src.application.usecases.interfaces import UseCaseMultipleEntities
from src.application.utils.error_handling_utils import ErrorHandlingUtils
from src.domain.cat_fact import CatFactEntity


class GetAllCatFactsUseCase(UseCaseMultipleEntities):
    def __init__(self, repo: CatFactsRepositoryAbstract) -> None:
        self.repo = repo

    def execute(self) -> typing.Iterable[CatFactEntity]:
        try:
            return self.repo.get_cat_facts()
        except Exception as exception:
            raise ErrorHandlingUtils.application_error("Cannot get all cat facts", exception)
