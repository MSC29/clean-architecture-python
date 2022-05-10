from typing import Any
from src.adapter.api.cat_facts.cat_facts_presenters import CatFactPresenter
from src.application.mappers.api_mapper import ApiMapper
from src.domain.cat_fact import CatFactEntity


class CatFactPresenterMapper(ApiMapper):

    def to_api(self, entity: CatFactEntity) -> CatFactPresenter:
        return CatFactPresenter(entity.fact_txt, entity.fact_length)

    def to_entity(self, payload: Any) -> CatFactEntity:
        raise Exception("not implemented")
