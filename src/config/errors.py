from typing import Iterable


class RequiredEnvNotDefinedError(Exception):
    envs: Iterable[str]

    def __init__(self, envs: Iterable[str], use_env: str, ini_path: str, *args: object) -> None:
        formatted_env = map(lambda x: f"    - {x}", envs)
        envs_joined = "\n".join(formatted_env)
        self.envs = envs
        super().__init__(
            f"\n  Required environment variables are not defined using environment {use_env}: \n{envs_joined}\n\n  Reading .ini from {ini_path}", *args)
