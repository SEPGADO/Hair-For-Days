"""restored password column

Revision ID: 1d69659cc512
Revises: 59627da2b688
Create Date: 2021-11-29 07:56:28.800075

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '1d69659cc512'
down_revision = '59627da2b688'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('register', sa.Column('password', sa.String(length=200), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('register', 'password')
    # ### end Alembic commands ###
