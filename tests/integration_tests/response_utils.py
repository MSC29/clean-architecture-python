import json
from types import SimpleNamespace as Namespace
from typing import Any
from injector import Injector
import requests

from src.infrastructure.app import create_app

app = create_app(Injector())


class ResponseUtils:

    @staticmethod
    def ok_and_parse(response: requests.Response) -> Any:
        assert response.status_code == 200
        return json.loads(response.text, object_hook=lambda d: Namespace(**d))
