from fastapi import APIRouter
from fastapi_injector import Injected

from src.adapter.api.cat_fact.mapper import CatFactPresenterMapper
from src.adapter.spi.repositories_factory import RepositoriesFactory

from src.application.repositories.cat_fact_repository_abstract import CatFactRepositoryAbstract
from src.application.usecases.get_one_cat_fact_usecase import GetOneCatFactUseCase

router = APIRouter()


@router.get("/")
async def get_one_cat_fact(factory: RepositoriesFactory = Injected(RepositoriesFactory)):
    repo: CatFactRepositoryAbstract = factory.get_repository("cat_fact_repository")
    usecase: GetOneCatFactUseCase = GetOneCatFactUseCase(repo)
    mapper: CatFactPresenterMapper = CatFactPresenterMapper()

    cat_fact = usecase.execute()

    return mapper.to_api(cat_fact)
