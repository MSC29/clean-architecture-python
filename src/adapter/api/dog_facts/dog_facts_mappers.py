from typing import Any
from src.adapter.api.dog_facts.dog_facts_presenters import DogFactPresenter
from src.application.mappers.api_mapper import ApiMapper
from src.domain.dog_fact import DogFactEntity


class DogFactPresenterMapper(ApiMapper):

    def to_api(self, entity: DogFactEntity) -> DogFactPresenter:
        return DogFactPresenter(entity.fact_id, entity.fact_txt)

    def to_entity(self, payload: Any) -> DogFactEntity:
        raise Exception("not implemented")
