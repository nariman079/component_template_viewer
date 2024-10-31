"""empty message

Revision ID: f8743d0d9259
Revises: ee2bae46c5dd
Create Date: 2024-10-30 18:27:18.143424

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'f8743d0d9259'
down_revision: Union[str, None] = 'ee2bae46c5dd'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('vpn_data', 'start_bot_image_url',
               existing_type=sa.VARCHAR(length=2048),
               nullable=True)
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('vpn_data', 'start_bot_image_url',
               existing_type=sa.VARCHAR(length=2048),
               nullable=False)
    # ### end Alembic commands ###