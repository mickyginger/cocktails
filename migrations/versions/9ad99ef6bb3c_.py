"""empty message

Revision ID: 9ad99ef6bb3c
Revises: d04048912bda
Create Date: 2018-09-23 18:23:17.387323

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = '9ad99ef6bb3c'
down_revision = 'd04048912bda'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('cocktails', sa.Column('ingredients', postgresql.JSON(astext_type=sa.Text()), nullable=False))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('cocktails', 'ingredients')
    # ### end Alembic commands ###
