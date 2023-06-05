"""fix col in data table

Revision ID: 090a6cedddb7
Revises: ae00b1960587
Create Date: 2022-03-14 16:15:28.726733

"""
import sqlalchemy as sa
from alembic import op

# revision identifiers, used by Alembic.
revision = "090a6cedddb7"
down_revision = "ae00b1960587"
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column("data", sa.Column("pressure", sa.Integer(), nullable=True))
    op.drop_column("data", "humidity")
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column("data", sa.Column("humidity", sa.INTEGER(), nullable=True))
    op.drop_column("data", "pressure")
    # ### end Alembic commands ###