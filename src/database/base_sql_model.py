from typing import Any
from sqlalchemy.ext.declarative import declarative_base, declared_attr

from src.common.get_table_name_from_class_name import get_table_name_from_class_name


class DeclaredTableName(object):
    @declared_attr
    def __tablename__(cls: Any) -> Any:
        return get_table_name_from_class_name(cls.__name__)


BaseSQLModel = declarative_base(cls=DeclaredTableName)
