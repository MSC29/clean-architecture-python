import typing
from fastapi import APIRouter
from fastapi_injector import Injected

from src.adapter.api.dog_facts.mapper import DogFactPresenterMapper
from src.adapter.api.dog_facts.presenter import DogFactPresenter
from src.adapter.spi.repositories_factory import RepositoriesFactory
from src.application.repositories.dog_fact_repository_abstract import DogFactRepositoryAbstract
from src.application.usecases.get_all_dog_facts_usecase import GetAllDogFactUseCase
from src.application.usecases.get_one_dog_fact_by_id_usecase import GetOneRandomDogFactUseCase

router = APIRouter()


@router.get("/")
async def get_all_dog_facts(factory: RepositoriesFactory = Injected(RepositoriesFactory)):
    repo: DogFactRepositoryAbstract = factory.get_repository("dog_fact_repository")
    mapper: DogFactPresenterMapper = DogFactPresenterMapper()

    usecase: GetAllDogFactUseCase = GetAllDogFactUseCase(repo)
    dog_facts = usecase.execute()

    facts: typing.List[DogFactPresenter] = []
    for data in dog_facts:
        facts.append(mapper.to_api(data))

    return facts


@router.get("/{fact_id}")
async def get_one_random_dog_fact(fact_id: int, factory: RepositoriesFactory = Injected(RepositoriesFactory)):
    repo: DogFactRepositoryAbstract = factory.get_repository("dog_fact_repository")
    mapper: DogFactPresenterMapper = DogFactPresenterMapper()

    usecase: GetOneRandomDogFactUseCase = GetOneRandomDogFactUseCase(fact_id, repo)
    dog_fact = usecase.execute()

    return mapper.to_api(dog_fact)
