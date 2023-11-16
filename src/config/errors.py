from typing import Iterable


class RequiredEnvNotDefinedError(Exception):
    envs: Iterable[str]

    def __init__(self, envs: Iterable[str], *args: object) -> None:
        envs_joined = ", ".join(envs)
        self.envs = envs
        super().__init__(
            f"Required environment variables are not defined: {envs_joined}", *args)
