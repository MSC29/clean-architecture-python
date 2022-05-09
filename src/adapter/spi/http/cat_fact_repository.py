import typing
from src.adapter.spi.http.http_connection import HttpConnection
from src.adapter.spi.http.mappers import CatFactHttpMapper
from src.application.repositories.cat_facts_repository_abstract import CatFactsRepositoryAbstract
from src.domain.api_exception import ApiException
from src.domain.cat_fact import CatFactEntity


class CatFactsRepository(CatFactsRepositoryAbstract):
    def __init__(self, http_connection: HttpConnection, source: str) -> None:
        self.mapper = CatFactHttpMapper()
        self.source = source
        self.http_connection = http_connection

    def get_random_cat_fact(self) -> CatFactEntity:
        res = self.http_connection.get("{}/fact".format(self.source))
        if not res.ok:
            raise ApiException("couldn't retrieve random cat fact")

        res_json = res.json()
        if not res_json:
            raise ApiException("couldn't process json response")

        return self.mapper.to_entity(res_json)

    def get_all_cat_facts(self) -> typing.List[CatFactEntity]:
        res = self.http_connection.get("{}/facts".format(self.source))
        if not res.ok:
            raise ApiException("couldn't retrieve cat facts")

        res_json = res.json()
        if not res_json:
            raise ApiException("couldn't process json response")

        facts: typing.List[CatFactEntity] = []
        for data in res_json["data"]:
            facts.append(self.mapper.to_entity(data))

        return facts
