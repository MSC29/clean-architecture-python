from abc import ABC, abstractmethod
from typing import Generic, TypeVar

HttpResponse = TypeVar("HttpResponse")


class HttpInterface(ABC, Generic[HttpResponse]):
    @abstractmethod
    def get(self, url: str, params=None, **kwargs) -> HttpResponse:
        """Execute an Http get request"""
