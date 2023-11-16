from typing import Iterable


class RequiredEnvNotDefinedError(Exception):
    envs: Iterable[str]

    def __init__(self, envs: Iterable[str], use_env: str, *args: object) -> None:
        formatted_env = map(lambda x: f"  - {x}", envs)
        envs_joined = "\n".join(formatted_env)
        self.envs = envs
        super().__init__(
            f"Required environment variables are not defined using environment {use_env}: \n{envs_joined}", *args)
