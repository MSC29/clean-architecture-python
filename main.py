from injector import Injector
import uvicorn

from src.infrastructure.app import create_app

app = create_app(Injector())

if __name__ == "__main__":
    uvicorn.run("main:app")
