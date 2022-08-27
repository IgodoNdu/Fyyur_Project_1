"""empty message

Revision ID: 9d5a9bab1a54
Revises: 
Create Date: 2022-08-19 03:24:55.667746

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '9d5a9bab1a54'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('artist', sa.Column('name', sa.String(), nullable=True))
    op.add_column('artist', sa.Column('city', sa.String(length=120), nullable=True))
    op.add_column('artist', sa.Column('state', sa.String(length=120), nullable=True))
    op.add_column('artist', sa.Column('phone', sa.String(length=120), nullable=True))
    op.add_column('artist', sa.Column('genres', sa.String(length=120), nullable=True))
    op.add_column('artist', sa.Column('image_link', sa.String(length=500), nullable=True))
    op.add_column('artist', sa.Column('facebook_link', sa.String(length=120), nullable=True))
    op.add_column('artist', sa.Column('website_link', sa.String(length=150), nullable=True))
    op.add_column('artist', sa.Column('looking_for_venue', sa.Boolean(), nullable=True))
    op.add_column('artist', sa.Column('seeking_description', sa.String(length=150), nullable=True))
    op.alter_column('artist', 'id',
               existing_type=sa.INTEGER(),
               nullable=False,
               autoincrement=True)
    op.add_column('venue', sa.Column('name', sa.String(), nullable=True))
    op.add_column('venue', sa.Column('city', sa.String(length=120), nullable=True))
    op.add_column('venue', sa.Column('state', sa.String(length=120), nullable=True))
    op.add_column('venue', sa.Column('address', sa.String(length=120), nullable=True))
    op.add_column('venue', sa.Column('phone', sa.String(length=120), nullable=True))
    op.add_column('venue', sa.Column('image_link', sa.String(length=500), nullable=True))
    op.add_column('venue', sa.Column('facebook_link', sa.String(length=120), nullable=True))
    op.alter_column('venue', 'id',
               existing_type=sa.INTEGER(),
               nullable=False,
               autoincrement=True)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('venue', 'id',
               existing_type=sa.INTEGER(),
               nullable=True,
               autoincrement=True)
    op.drop_column('venue', 'facebook_link')
    op.drop_column('venue', 'image_link')
    op.drop_column('venue', 'phone')
    op.drop_column('venue', 'address')
    op.drop_column('venue', 'state')
    op.drop_column('venue', 'city')
    op.drop_column('venue', 'name')
    op.alter_column('artist', 'id',
               existing_type=sa.INTEGER(),
               nullable=True,
               autoincrement=True)
    op.drop_column('artist', 'seeking_description')
    op.drop_column('artist', 'looking_for_venue')
    op.drop_column('artist', 'website_link')
    op.drop_column('artist', 'facebook_link')
    op.drop_column('artist', 'image_link')
    op.drop_column('artist', 'genres')
    op.drop_column('artist', 'phone')
    op.drop_column('artist', 'state')
    op.drop_column('artist', 'city')
    op.drop_column('artist', 'name')
    # ### end Alembic commands ###
