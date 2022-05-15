from src.application.repositories.dog_facts_repository_abstract import DogFactsRepositoryAbstract
from src.application.usecases.interfaces import UseCaseOneEntity
from src.application.utils.error_handling_utils import ErrorHandlingUtils
from src.domain.dog_fact import DogFactEntity


class GetOneDogFactByIdUseCase(UseCaseOneEntity):
    def __init__(self, dog_fact_id: int, repository: DogFactsRepositoryAbstract) -> None:
        self.repository = repository
        self.dog_fact_id = dog_fact_id

    def execute(self) -> DogFactEntity:
        try:
            return self.repository.get_dog_fact_by_id(self.dog_fact_id)
        except Exception as exception:
            raise ErrorHandlingUtils.application_error("Cannot get single dog fact", exception)
