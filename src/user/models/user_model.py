from typing import overload
from sqlalchemy import TEXT, Column, Integer, String
from src.database.timestamped_model import TimestampedModel
from src.database.base_sql_model import BaseSQLModel


class UserModel(BaseSQLModel, TimestampedModel):
    user_id = Column(Integer, nullable=False,
                     primary_key=True, autoincrement=True)
    username = Column(String(50), nullable=False)
    password = Column(TEXT, nullable=False)

    @staticmethod
    def sa_attributes():
        return [
            Column('user_id', Integer, nullable=False,
                   primary_key=True, autoincrement=True),
            Column('username', String(50), nullable=False),
            Column('password', TEXT, nullable=False),
        ] + TimestampedModel.sa_attributes()
