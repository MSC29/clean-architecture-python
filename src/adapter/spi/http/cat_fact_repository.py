import typing
import requests
from src.adapter.spi.http.mapper import CatFactHttpMapper
from src.application.repositories.cat_fact_repository_abstract import CatFactRepositoryAbstract
from src.domain.api_exception import ApiException
from src.domain.cat_fact import CatFactEntity


class CatFactRepository(CatFactRepositoryAbstract):
    def __init__(self) -> None:
        self.mapper = CatFactHttpMapper()

    def get_cat_fact(self) -> CatFactEntity:
        res = requests.get("https://catfact.ninja/fact")
        if not res.ok:
            raise ApiException("couldn't retrieve random cat fact")

        res_json = res.json()
        if not res_json:
            raise ApiException("couldn't process json response")

        return self.mapper.to_entity(res_json)

    def get_cat_facts(self) -> typing.List[CatFactEntity]:
        res = requests.get("https://catfact.ninja/facts")
        if not res.ok:
            raise ApiException("couldn't retrieve cat facts")

        res_json = res.json()
        if not res_json:
            raise ApiException("couldn't process json response")

        facts: typing.List[CatFactEntity] = []
        for data in res_json:
            facts.append(self.mapper.to_entity(data))

        return facts
