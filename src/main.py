from fastapi import FastAPI
from src.core.config import app_configs
from src.auth.routes import user_router
from src.auth.routes import router as auth_router
from src.core.middleware import TimeElapsedMiddleware

from src.tasks.handlers import router as tasks_router


def create_app():
    app = FastAPI(**app_configs)
    # routes
    app.include_router(auth_router)
    app.include_router(user_router)
    app.include_router(tasks_router)
    # middlewares
    app.add_middleware(middleware_class=TimeElapsedMiddleware)

    return app
