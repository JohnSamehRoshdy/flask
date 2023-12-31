"""add category_id to students table

Revision ID: 85b42ce2ddcb
Revises: 1c60c6642ea7
Create Date: 2023-10-30 14:04:32.498554

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '85b42ce2ddcb'
down_revision = '1c60c6642ea7'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('posts', schema=None) as batch_op:
        batch_op.add_column(sa.Column('category_id', sa.Integer(), nullable=True))
        batch_op.create_foreign_key(None, 'categories', ['category_id'], ['id'])

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('posts', schema=None) as batch_op:
        batch_op.drop_constraint(None, type_='foreignkey')
        batch_op.drop_column('category_id')

    # ### end Alembic commands ###
