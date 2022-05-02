import typing
from src.application.repositories.dog_facts_repository_abstract import DogFactsRepositoryAbstract
from src.application.usecases.interfaces import UseCaseMultipleEntities
from src.domain.dog_fact import DogFactEntity


class GetAllDogFactUseCase(UseCaseMultipleEntities):
    def __init__(self, repo: DogFactsRepositoryAbstract) -> None:
        self.repo = repo

    # TODO Error Handling
    def execute(self) -> typing.Iterable[DogFactEntity]:
        return self.repo.get_all_dog_facts()
