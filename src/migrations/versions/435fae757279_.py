"""empty message

Revision ID: 435fae757279
Revises: bdcdd4c6d26f
Create Date: 2022-08-11 00:51:10.016600

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '435fae757279'
down_revision = 'bdcdd4c6d26f'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('users',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('email', sa.String(length=80), nullable=False),
    sa.Column('name', sa.String(length=80), nullable=False),
    sa.Column('number', sa.String(length=80), nullable=False),
    sa.Column('username', sa.String(length=80), nullable=False),
    sa.Column('password', sa.String(length=80), nullable=False),
    sa.Column('token', sa.String(length=80), nullable=False),
    sa.Column('email_verified', sa.Boolean(), nullable=False),
    sa.Column('join_date', sa.DateTime(timezone=True), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('users')
    # ### end Alembic commands ###
