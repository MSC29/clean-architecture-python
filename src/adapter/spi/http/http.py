import requests
from requests import Response

from src.application.spi.http_interface import HttpInterface


class HttpConnection(HttpInterface):
    def __init__(self) -> None:
        pass

    def get(self, url: str, params=None, **kwargs) -> Response:
        return requests.get(url, params, **kwargs)
