"""empty message

Revision ID: c1e8ceafa080
Revises: 74dd5f7c14c2
Create Date: 2022-08-06 18:23:42.984474

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'c1e8ceafa080'
down_revision = '74dd5f7c14c2'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('Artist', sa.Column('website', sa.String(length=120), nullable=True))
    op.drop_column('Artist', 'website_link')
    op.add_column('Venue', sa.Column('website', sa.String(length=120), nullable=True))
    op.drop_column('Venue', 'website_link')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('Venue', sa.Column('website_link', sa.VARCHAR(length=120), autoincrement=False, nullable=True))
    op.drop_column('Venue', 'website')
    op.add_column('Artist', sa.Column('website_link', sa.VARCHAR(length=120), autoincrement=False, nullable=True))
    op.drop_column('Artist', 'website')
    # ### end Alembic commands ###
