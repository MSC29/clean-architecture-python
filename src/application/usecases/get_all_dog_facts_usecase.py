import typing
from src.application.repositories.dog_fact_repository_abstract import DogFactRepositoryAbstract
from src.application.usecases.interfaces import UseCaseMultipleEntities
from src.domain.dog_fact import DogFactEntity


class GetAllDogFactUseCase(UseCaseMultipleEntities):
    def __init__(self, repo: DogFactRepositoryAbstract) -> None:
        self.repo = repo

    def execute(self) -> typing.Iterable[DogFactEntity]:
        return self.repo.get_all_dog_facts()
