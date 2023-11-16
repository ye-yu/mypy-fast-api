import os

from pydantic import ValidationError

from .env import Env
from .errors import RequiredEnvNotDefinedError


class ConfigService:
    env = Env()

    def get_string(self, envName: str, default: str = "") -> str:
        try:
            return os.environ[envName]
        except KeyError as k:
            return default

    @classmethod
    def instantiate(cls):
        try:
            yield cls()
        except ValidationError as ve:
            envs = set(str(i['loc'][0]) for i in ve.errors())
            raise RequiredEnvNotDefinedError(envs, ve)
