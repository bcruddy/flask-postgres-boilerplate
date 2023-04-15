"""fix user table

Revision ID: eee8022d9d9d
Revises: 99b455ff19cc
Create Date: 2023-04-14 15:45:10.754626

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'eee8022d9d9d'
down_revision = '99b455ff19cc'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('user', schema=None) as batch_op:
        batch_op.alter_column('password',
               existing_type=sa.VARCHAR(),
               nullable=False)
        batch_op.drop_constraint('user_name_key', type_='unique')

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('user', schema=None) as batch_op:
        batch_op.create_unique_constraint('user_name_key', ['name'])
        batch_op.alter_column('password',
               existing_type=sa.VARCHAR(),
               nullable=True)

    # ### end Alembic commands ###