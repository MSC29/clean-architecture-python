import typing
from fastapi import APIRouter
from fastapi_injector import Injected

from src.adapter.api.dog_facts.mapper import DogFactPresenterMapper
from src.adapter.api.dog_facts.presenter import DogFactPresenter
from src.adapter.spi.repositories_factory import RepositoriesFactory
from src.application.repositories.dog_facts_repository_abstract import DogFactsRepositoryAbstract
from src.application.usecases.get_all_dog_facts_usecase import GetAllDogFactUseCase
from src.application.usecases.get_one_dog_fact_by_id_usecase import GetOneDogFactByIdUseCase

router = APIRouter()


@router.get("/")
async def get_all_dog_facts(factory: RepositoriesFactory = Injected(RepositoriesFactory)):
    dog_facts_repository: DogFactsRepositoryAbstract = factory.get_repository("dog_fact_repository")
    dog_fact_presenter_mapper: DogFactPresenterMapper = DogFactPresenterMapper()

    get_all_dog_facts_usecase: GetAllDogFactUseCase = GetAllDogFactUseCase(dog_facts_repository)
    dog_facts = get_all_dog_facts_usecase.execute()

    facts: typing.List[DogFactPresenter] = []
    for data in dog_facts:
        facts.append(dog_fact_presenter_mapper.to_api(data))

    return facts


@router.get("/{dog_fact_id}")
async def get_one_dog_fact_by_id(dog_fact_id: int, factory: RepositoriesFactory = Injected(RepositoriesFactory)):
    dog_facts_repository: DogFactsRepositoryAbstract = factory.get_repository("dog_fact_repository")
    dog_fact_presenter_mapper: DogFactPresenterMapper = DogFactPresenterMapper()

    get_one_dog_fact_by_id_usecase: GetOneDogFactByIdUseCase = GetOneDogFactByIdUseCase(dog_fact_id, dog_facts_repository)
    dog_fact = get_one_dog_fact_by_id_usecase.execute()

    return dog_fact_presenter_mapper.to_api(dog_fact)
