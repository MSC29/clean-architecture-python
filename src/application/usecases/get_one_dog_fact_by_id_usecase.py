from src.application.repositories.dog_facts_repository_abstract import DogFactsRepositoryAbstract
from src.application.usecases.interfaces import UseCaseOneEntity
from src.domain.dog_fact import DogFactEntity


class GetOneDogFactByIdUseCase(UseCaseOneEntity):
    def __init__(self, dog_fact_id: int, repo: DogFactsRepositoryAbstract) -> None:
        self.repo = repo
        self.dog_fact_id = dog_fact_id

    # TODO Error Handling
    def execute(self) -> DogFactEntity:
        return self.repo.get_dog_fact_by_id(self.dog_fact_id)
