from abc import ABC, abstractmethod

from src.domain.configuration_entity import ConfigurationEntity


class DbInterface(ABC):
    @abstractmethod
    def connection(self, config: ConfigurationEntity) -> None:
        """Execute a database connecton"""

    @abstractmethod
    def migration(self) -> None:
        """Execute a database migration"""
