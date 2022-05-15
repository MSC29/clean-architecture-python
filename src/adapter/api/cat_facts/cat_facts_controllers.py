import typing
from fastapi import APIRouter
from fastapi_injector import Injected

from src.adapter.api.cat_facts.cat_facts_mappers import CatFactPresenterMapper
from src.adapter.api.cat_facts.cat_facts_presenters import CatFactPresenter
from src.adapter.api.shared.api_error_handling import ApiErrorHandling
from src.adapter.spi.repositories_factory import RepositoriesFactory

from src.application.repositories.cat_facts_repository_abstract import CatFactsRepositoryAbstract
from src.application.usecases.get_all_cat_facts_usecase import GetAllCatFactsUseCase
from src.application.usecases.get_one_random_cat_fact_usecase import GetOneRandomCatFactUseCase

router = APIRouter()


@router.get("/")
async def get_all_cat_facts(factory: RepositoriesFactory = Injected(RepositoriesFactory)):
    try:
        cat_fact_repository: CatFactsRepositoryAbstract = factory.get_repository(
            "cat_fact_repository")
        cat_fact_presenter_mapper: CatFactPresenterMapper = CatFactPresenterMapper()

        get_all_cat_facts_usecase: GetAllCatFactsUseCase = GetAllCatFactsUseCase(
            cat_fact_repository)
        cat_facts = get_all_cat_facts_usecase.execute()

        facts: typing.List[CatFactPresenter] = []
        for data in cat_facts:
            facts.append(cat_fact_presenter_mapper.to_api(data))

        return facts
    except Exception as exception:
        raise ApiErrorHandling.http_error("Unexpected error getting all cat facts", exception)


@router.get("/random")
async def get_one_random_cat_fact(factory: RepositoriesFactory = Injected(RepositoriesFactory)):
    try:
        cat_fact_repository: CatFactsRepositoryAbstract = factory.get_repository(
            "cat_fact_repository")
        cat_fact_presenter_mapper: CatFactPresenterMapper = CatFactPresenterMapper()

        get_one_random_cat_fact_usecase: GetOneRandomCatFactUseCase = GetOneRandomCatFactUseCase(
            cat_fact_repository)
        cat_fact = get_one_random_cat_fact_usecase.execute()

        return cat_fact_presenter_mapper.to_api(cat_fact)
    except Exception as exception:
        raise ApiErrorHandling.http_error("Unexpected error getting a random cat fact", exception)
