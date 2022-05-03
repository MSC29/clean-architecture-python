from src.application.repositories.cat_facts_repository_abstract import CatFactsRepositoryAbstract
from src.application.usecases.interfaces import UseCaseOneEntity
from src.application.utils.error_handling_utils import ErrorHandlingUtils
from src.domain.cat_fact import CatFactEntity


class GetOneRandomCatFactUseCase(UseCaseOneEntity):
    def __init__(self, repo: CatFactsRepositoryAbstract) -> None:
        self.repo = repo

    def execute(self) -> CatFactEntity:
        try:
            return self.repo.get_random_cat_fact()
        except Exception as exception:
            raise ErrorHandlingUtils.application_error("Cannot get random cat fact", exception)
