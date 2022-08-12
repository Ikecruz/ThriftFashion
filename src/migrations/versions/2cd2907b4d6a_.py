"""empty message

Revision ID: 2cd2907b4d6a
Revises: c03bed30d54e
Create Date: 2022-08-12 08:13:54.019914

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = '2cd2907b4d6a'
down_revision = 'c03bed30d54e'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('products', sa.Column('description', sa.String(length=60), nullable=False))
    op.drop_column('products', 'Description')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('products', sa.Column('Description', mysql.VARCHAR(length=60), nullable=False))
    op.drop_column('products', 'description')
    # ### end Alembic commands ###