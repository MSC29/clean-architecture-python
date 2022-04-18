from typing import Any
from src.application.mappers.http_mapper import HttpMapper
from src.domain.cat_fact import CatFactEntity


class CatFactHttpMapper(HttpMapper):

    def to_http(self, entity: CatFactEntity) -> Any:
        raise Exception("not implemented")

    def to_entity(self, http_obj: Any) -> CatFactEntity:
        return CatFactEntity(http_obj["fact"], http_obj["length"])
