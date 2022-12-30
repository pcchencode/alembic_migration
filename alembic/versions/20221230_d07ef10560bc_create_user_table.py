"""create user table

Revision ID: d07ef10560bc
Revises: 
Create Date: 2022-12-30 11:25:56.967179

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'd07ef10560bc'
down_revision = None
branch_labels = None
depends_on = None

# 新增一張表
def upgrade():
    op.create_table(
        'user',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('customer_id', sa.Unicode(10), comment='客戶編號'),
        sa.Column('name', sa.Unicode(10), comment='客戶姓名'),
        comment='測試客戶表',
    )

# 記得要撰寫相對應的降版
def downgrade():
    op.drop_table('user')
