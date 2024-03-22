import os

from dotenv import load_dotenv

from fastapi_users import FastAPIUsers
from fastapi_users.authentication import (
    AuthenticationBackend,
    CookieTransport,
    JWTStrategy,
)

from src.core.database import UserModel
from .manager import get_user_manager


load_dotenv()
SECRET = os.getenv('SECRET')

cookie_transport = CookieTransport(cookie_max_age=60*60)


def get_jwt_strategy() -> JWTStrategy:
    return JWTStrategy(secret=SECRET, lifetime_seconds=60*60)


auth_backend = AuthenticationBackend(
    name='jwt',
    transport=cookie_transport,
    get_strategy=get_jwt_strategy,
)

fastapi_users = FastAPIUsers[UserModel, int](get_user_manager, [auth_backend])

current_active_user = fastapi_users.current_user(active=True)
is_admin = fastapi_users.current_user(superuser=True)
