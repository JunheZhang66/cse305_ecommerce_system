"""add new columns for users

Revision ID: db6a1c236507
Revises: 1bd1b100bd54
Create Date: 2019-04-30 09:00:00.577495

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'db6a1c236507'
down_revision = '1bd1b100bd54'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('user', sa.Column('about_me', sa.String(length=120), nullable=True))
    op.add_column('user', sa.Column('create_time', sa.DateTime(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('user', 'create_time')
    op.drop_column('user', 'about_me')
    # ### end Alembic commands ###
