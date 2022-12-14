"""empty message

Revision ID: f62e318a5e32
Revises: 11ef6982c479
Create Date: 2022-08-05 00:27:04.037440

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'f62e318a5e32'
down_revision = '11ef6982c479'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('Show', sa.Column('artist_id', sa.Integer(), nullable=False))
    op.add_column('Show', sa.Column('start_time', sa.DateTime(timezone=True), nullable=True))
    op.create_foreign_key(None, 'Show', 'Artist', ['artist_id'], ['id'])
    op.add_column('Venue', sa.Column('artist_id', sa.Integer(), nullable=False))
    op.create_foreign_key(None, 'Venue', 'Artist', ['artist_id'], ['id'])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'Venue', type_='foreignkey')
    op.drop_column('Venue', 'artist_id')
    op.drop_constraint(None, 'Show', type_='foreignkey')
    op.drop_column('Show', 'start_time')
    op.drop_column('Show', 'artist_id')
    # ### end Alembic commands ###
