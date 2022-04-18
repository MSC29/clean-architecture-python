from src.adapter.spi.http.cat_fact_repository import CatFactRepository


class RepositoriesFactory:

    repositories: dict = {
        "cat_fact_repository": CatFactRepository
    }

    def __init__(self) -> None:
        pass

    def get_repository(self, repository_name: str):
        if repository_name in RepositoriesFactory.repositories:
            return RepositoriesFactory.repositories[repository_name]()
        else:
            raise Exception("Repository does not exist")
