import os


class ConfigService:
    def get_string(self, envName: str, default: str = "") -> str:
        try:
            return os.environ[envName]
        except KeyError as k:
            return default

    @classmethod
    def instantiate(cls):
        yield cls()
