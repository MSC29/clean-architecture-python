from src.domain.base_entity import BaseEntity


class CatFactEntity(BaseEntity):
    def __init__(self, fact_txt: str, fact_length: int, ) -> None:
        super().__init__()
        self.fact_txt = fact_txt
        self.fact_length = fact_length
