# app/application.py
from fastapi import FastAPI

from app.adapters.db.orm import start_mappers
from app.configurator.db import init_db
from app.configurator.containers import Container
from app.adapters.entrypoints.rest.v1 import users_routes, login_routes


def create_app() -> FastAPI:
    init_db()
    start_mappers()
    _app = FastAPI()
    container = Container()
    _app.container = container
    _app.include_router(users_routes.router, prefix="/api/v1")
    _app.include_router(login_routes.router, prefix="/api/v1")
    return _app


app = create_app()
