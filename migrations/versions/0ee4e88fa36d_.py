"""empty message

Revision ID: 0ee4e88fa36d
Revises: 0519b333d426
Create Date: 2022-08-13 20:00:46.193806

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = '0ee4e88fa36d'
down_revision = '0519b333d426'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('products', sa.Column('category_id', sa.Integer(), nullable=True))
    op.add_column('products', sa.Column('gender', sa.String(length=50), nullable=False))
    op.add_column('products', sa.Column('description', sa.String(length=60), nullable=False))
    op.create_foreign_key(None, 'products', 'categories', ['category_id'], ['id'])
    op.drop_column('products', 'category')
    op.add_column('users', sa.Column('status', sa.Boolean(), nullable=False))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('users', 'status')
    op.add_column('products', sa.Column('category', mysql.VARCHAR(length=80), nullable=False))
    op.drop_constraint(None, 'products', type_='foreignkey')
    op.drop_column('products', 'description')
    op.drop_column('products', 'gender')
    op.drop_column('products', 'category_id')
    # ### end Alembic commands ###
