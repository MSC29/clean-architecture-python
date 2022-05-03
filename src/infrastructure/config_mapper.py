from typing import Dict, Optional
from dotenv import dotenv_values

from src.domain.configuration_entity import ConfigurationEntity


class ConfigurationMapper:
    def __init__(self, env: str) -> None:

        env = env.lower()

        __config_raw: Dict[str, Optional[str]] = dotenv_values(".env.{}".format(env))

        dog_source = __config_raw.get("DOGS_SOURCE")
        cat_source = __config_raw.get("CATS_SOURCE")

        if dog_source is None or cat_source is None:
            raise Exception()

        self.config = ConfigurationEntity(dog_source, cat_source, env)

    def get_config(self) -> ConfigurationEntity:
        return self.config
