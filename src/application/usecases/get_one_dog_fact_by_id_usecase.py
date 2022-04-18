from src.application.repositories.dog_fact_repository_abstract import DogFactRepositoryAbstract
from src.application.usecases.interfaces import UseCaseOneEntity
from src.domain.dog_fact import DogFactEntity


class GetOneRandomDogFactUseCase(UseCaseOneEntity):
    def __init__(self, dog_fact_id: int, repo: DogFactRepositoryAbstract) -> None:
        self.repo = repo
        self.dog_fact_id = dog_fact_id

    def execute(self) -> DogFactEntity:
        return self.repo.get_dog_fact_by_id(self.dog_fact_id)
