import os

from src.config.env import Env
from src.config.errors import RequiredEnvNotDefinedError


class ConfigService:
    env = Env()

    def get_string(self, envName: str, default: str = "") -> str:
        try:
            return os.environ[envName]
        except KeyError as k:
            return default

    @classmethod
    def instantiate(cls):
        yield get_config_service()


__config_service = ConfigService()


def get_config_service() -> ConfigService:
    return __config_service
