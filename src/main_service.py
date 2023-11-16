from fastapi import Depends
from pydantic import BaseModel

from src.config.config_service import ConfigService


class GetResponse(BaseModel):
    Hello: str

    @classmethod
    def res(cls) -> 'GetResponse':
        r = cls(Hello="World")
        return r


class MainService:
    app_name: str = ""

    def GetResponse(self) -> GetResponse:
        return GetResponse(Hello=self.app_name)

    @staticmethod
    def instantiate(config_service: ConfigService = Depends(ConfigService.instantiate)):
        i = MainService()
        i.app_name = config_service.env.APP_NAME
        return i
