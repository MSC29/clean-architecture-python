from src.application.repositories.cat_fact_repository_abstract import CatFactRepositoryAbstract
from src.application.usecases.interfaces import UseCaseOneEntity
from src.domain.cat_fact import CatFactEntity


class GetOneRandomCatFactUseCase(UseCaseOneEntity):
    def __init__(self, repo: CatFactRepositoryAbstract) -> None:
        self.repo = repo

    def execute(self) -> CatFactEntity:
        return self.repo.get_cat_fact()
