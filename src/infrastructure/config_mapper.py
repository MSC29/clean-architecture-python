from dotenv import dotenv_values

from src.domain.configuration_entity import ConfigurationEntity


class ConfigurationMapper:
    def __init__(self) -> None:
        config_raw = dotenv_values(".env")

        dog_source = config_raw.get("DOGS_SOURCE")
        cat_source = config_raw.get("CATS_SOURCE")

        if dog_source is None or cat_source is None:
            raise Exception()

        self.config = ConfigurationEntity(dog_source, cat_source)

    def get_config(self) -> ConfigurationEntity:
        return self.config