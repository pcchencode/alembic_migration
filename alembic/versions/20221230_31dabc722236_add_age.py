"""add age

Revision ID: 31dabc722236
Revises: d07ef10560bc
Create Date: 2022-12-30 13:28:34.909774

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '31dabc722236'
down_revision = 'd07ef10560bc'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column('user', sa.Column('age', sa.Integer, comment='客戶年齡'))


def downgrade():
    op.drop_column('user', 'age')
