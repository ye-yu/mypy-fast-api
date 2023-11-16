from configparser import ConfigParser
import logging
from typing import Any, MutableMapping
from pydantic import BaseModel, ConfigDict, Field, ValidationError

from src.config.errors import RequiredEnvNotDefinedError


def error_type_to_readable(error_type: str):
    if error_type == 'missing':
        return 'missing'
    if error_type.endswith('_parsing'):
        expected_type = error_type[:-8]
        return f"cannot parse to {expected_type}"


class Env(BaseModel):
    app_name: str = Field(default="")
    app_secret: str
    db_url: str
    count: int

    model_config = ConfigDict(hide_input_in_errors=True)

    def __init__(self):
        env: MutableMapping[str, Any] = {}
        use_env = ''
        try:
            parser = ConfigParser()
            parser.read('./env.ini')
            default_section = parser['DEFAULT']
            use_env = default_section.get('use_env', 'development')
            logging.info(f"Using environment, {use_env}")

            section = parser[use_env]

            for name, field in Env.model_fields.items():
                if not name in section.keys():
                    continue
                try:
                    annotation = field.annotation
                    if annotation is None or annotation == str:
                        # assume string for None
                        env[name] = section.get(name)
                    elif annotation == int:
                        env[name] = section.getint(name)
                    elif annotation == float:
                        env[name] = section.getfloat(name)
                    elif annotation == bool:
                        env[name] = section.getboolean(name)
                    else:
                        pass
                except ValueError:
                    # just assign string and let pydantic validation throw type error
                    env[name] = section.get(name)

        except Exception as e:
            logging.error(f"Unable to read ./env.ini, {e}")
        try:
            BaseModel.__init__(self, **env)
        except ValidationError as ve:
            envs = set(f"{i['loc'][0]} ({error_type_to_readable(i['type'])})"
                       for i in ve.errors())
            raise RequiredEnvNotDefinedError(envs, use_env)
