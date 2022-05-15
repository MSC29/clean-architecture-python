import typing
from src.application.repositories.dog_facts_repository_abstract import DogFactsRepositoryAbstract
from src.application.usecases.interfaces import UseCaseMultipleEntities
from src.application.utils.error_handling_utils import ErrorHandlingUtils
from src.domain.dog_fact import DogFactEntity


class GetAllDogFactsUseCase(UseCaseMultipleEntities):
    def __init__(self, repository: DogFactsRepositoryAbstract) -> None:
        self.repository = repository

    def execute(self) -> typing.Iterable[DogFactEntity]:
        try:
            return self.repository.get_all_dog_facts()
        except Exception as exception:
            raise ErrorHandlingUtils.application_error("Cannot get all dog facts", exception)
