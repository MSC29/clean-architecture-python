import typing
from fastapi import APIRouter
from fastapi_injector import Injected

from src.adapter.api.cat_fact.mapper import CatFactPresenterMapper
from src.adapter.api.cat_fact.presenter import CatFactPresenter
from src.adapter.spi.repositories_factory import RepositoriesFactory

from src.application.repositories.cat_fact_repository_abstract import CatFactRepositoryAbstract
from src.application.usecases.get_all_cat_facts_usecase import GetAllCatFactUseCase
from src.application.usecases.get_one_random_cat_fact_usecase import GetOneRandomCatFactUseCase

router = APIRouter()


@router.get("/")
async def get_all_cat_facts(factory: RepositoriesFactory = Injected(RepositoriesFactory)):
    repo: CatFactRepositoryAbstract = factory.get_repository("cat_fact_repository")
    usecase: GetAllCatFactUseCase = GetAllCatFactUseCase(repo)
    mapper: CatFactPresenterMapper = CatFactPresenterMapper()

    cat_facts = usecase.execute()

    facts: typing.List[CatFactPresenter] = []
    for data in cat_facts:
        facts.append(mapper.to_api(data))

    return facts


@router.get("/random")
async def get_one_random_cat_fact(factory: RepositoriesFactory = Injected(RepositoriesFactory)):
    repo: CatFactRepositoryAbstract = factory.get_repository("cat_fact_repository")
    usecase: GetOneRandomCatFactUseCase = GetOneRandomCatFactUseCase(repo)
    mapper: CatFactPresenterMapper = CatFactPresenterMapper()

    cat_fact = usecase.execute()

    return mapper.to_api(cat_fact)
