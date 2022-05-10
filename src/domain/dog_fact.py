from src.domain.base_entity import BaseEntity


class DogFactEntity(BaseEntity):
    def __init__(self, fact_id: int, fact: str) -> None:
        super().__init__()
        self.fact_id = fact_id
        self.fact_txt = fact
