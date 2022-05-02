import typing
from fastapi import APIRouter
from fastapi_injector import Injected

from src.adapter.api.cat_facts.mapper import CatFactPresenterMapper
from src.adapter.api.cat_facts.presenter import CatFactPresenter
from src.adapter.spi.repositories_factory import RepositoriesFactory

from src.application.repositories.cat_facts_repository_abstract import CatFactsRepositoryAbstract
from src.application.usecases.get_all_cat_facts_usecase import GetAllCatFactUseCase
from src.application.usecases.get_one_random_cat_fact_usecase import GetOneRandomCatFactUseCase

router = APIRouter()


@router.get("/")
async def get_all_cat_facts(factory: RepositoriesFactory = Injected(RepositoriesFactory)):
    cat_fact_repository: CatFactsRepositoryAbstract = factory.get_repository("cat_fact_repository")
    cat_fact_presenter_mapper: CatFactPresenterMapper = CatFactPresenterMapper()

    get_all_cat_facts_usecase: GetAllCatFactUseCase = GetAllCatFactUseCase(cat_fact_repository)
    cat_facts = get_all_cat_facts_usecase.execute()

    facts: typing.List[CatFactPresenter] = []
    for data in cat_facts:
        facts.append(cat_fact_presenter_mapper.to_api(data))

    return facts


@router.get("/random")
async def get_one_random_cat_fact(factory: RepositoriesFactory = Injected(RepositoriesFactory)):
    cat_fact_repository: CatFactsRepositoryAbstract = factory.get_repository("cat_fact_repository")
    cat_fact_presenter_mapper: CatFactPresenterMapper = CatFactPresenterMapper()

    get_one_random_cat_fact_usecase: GetOneRandomCatFactUseCase = GetOneRandomCatFactUseCase(cat_fact_repository)
    cat_fact = get_one_random_cat_fact_usecase.execute()

    return cat_fact_presenter_mapper.to_api(cat_fact)
