from src.application.repositories.cat_facts_repository_abstract import CatFactsRepositoryAbstract
from src.application.usecases.interfaces import UseCaseOneEntity
from src.domain.cat_fact import CatFactEntity


class GetOneRandomCatFactUseCase(UseCaseOneEntity):
    def __init__(self, repo: CatFactsRepositoryAbstract) -> None:
        self.repo = repo

    # TODO Error Handling
    def execute(self) -> CatFactEntity:
        return self.repo.get_cat_fact()
