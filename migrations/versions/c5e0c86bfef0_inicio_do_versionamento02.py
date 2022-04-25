"""Inicio do versionamento02

Revision ID: c5e0c86bfef0
Revises: 
Create Date: 2022-04-22 17:52:53.845390

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'c5e0c86bfef0'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('hash_user', 'api_key')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('hash_user', sa.Column('api_key', sa.VARCHAR(length=511), autoincrement=False, nullable=False))
    # ### end Alembic commands ###