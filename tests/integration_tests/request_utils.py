from injector import Injector
from fastapi.testclient import TestClient

from src.infrastructure.app import create_app

app = create_app(Injector())


class RequestsUtils:

    @staticmethod
    def client() -> TestClient:
        return TestClient(app)
