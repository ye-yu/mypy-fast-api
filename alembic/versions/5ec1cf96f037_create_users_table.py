"""create users table

Revision ID: 5ec1cf96f037
Revises: 
Create Date: 2023-11-16 20:38:58.383512

"""
from typing import Sequence, Union
from alembic import op
from src.common.get_table_name_from_class_name import get_table_name_from_class_name
from src.user.models.user_model import UserModel


# revision identifiers, used by Alembic.
revision: str = '5ec1cf96f037'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    table_name = get_table_name_from_class_name(UserModel.__name__)
    op.create_table(
        table_name,
        *UserModel.sa_attributes(),
    )


def downgrade() -> None:
    table_name = get_table_name_from_class_name(UserModel.__name__)
    op.drop_table(table_name)
