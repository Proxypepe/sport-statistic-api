"""init tables

Revision ID: 44e83aa0bbc8
Revises: 
Create Date: 2023-04-05 11:56:26.512164

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '44e83aa0bbc8'
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('country',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('name', sa.String(length=96), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_country_name'), 'country', ['name'], unique=False)
    op.create_table('referee',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('name', sa.String(length=96), nullable=False),
    sa.Column('surname', sa.String(length=96), nullable=False),
    sa.Column('age', sa.Integer(), nullable=False),
    sa.Column('birthdate', sa.Date(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('sport_name',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('name', sa.String(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('sportsman',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('name', sa.String(), nullable=False),
    sa.Column('surname', sa.String(), nullable=False),
    sa.Column('birthday', sa.Date(), nullable=False),
    sa.Column('age', sa.Integer(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('league',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('name', sa.String(), nullable=False),
    sa.Column('season', sa.Integer(), nullable=False),
    sa.Column('start', sa.Date(), nullable=True),
    sa.Column('end', sa.Date(), nullable=True),
    sa.Column('country_id', sa.Integer(), nullable=False),
    sa.Column('sport_name_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['country_id'], ['country.id'], ),
    sa.ForeignKeyConstraint(['sport_name_id'], ['country.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('stadium',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('opening_date', sa.Date(), nullable=False),
    sa.Column('capacity', sa.Integer(), nullable=False),
    sa.Column('country_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['country_id'], ['country.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('team',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('league_id', sa.Integer(), nullable=False),
    sa.Column('country_id', sa.Integer(), nullable=False),
    sa.Column('owner', sa.String(), nullable=True),
    sa.ForeignKeyConstraint(['country_id'], ['country.id'], ),
    sa.ForeignKeyConstraint(['league_id'], ['league.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('match',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('stadium_id', sa.Integer(), nullable=False),
    sa.Column('league_id', sa.Integer(), nullable=False),
    sa.Column('home_team_id', sa.Integer(), nullable=False),
    sa.Column('guest_team_id', sa.Integer(), nullable=False),
    sa.Column('start', sa.Date(), nullable=True),
    sa.Column('end', sa.Date(), nullable=True),
    sa.Column('duration', sa.Integer(), nullable=False),
    sa.Column('result', sa.Enum('HOME', 'GUEST', 'DRAW', name='results'), nullable=True),
    sa.Column('home_score', sa.Integer(), nullable=False),
    sa.Column('guest_score', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['guest_team_id'], ['team.id'], ),
    sa.ForeignKeyConstraint(['home_team_id'], ['team.id'], ),
    sa.ForeignKeyConstraint(['league_id'], ['league.id'], ),
    sa.ForeignKeyConstraint(['stadium_id'], ['stadium.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('participant',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('league_id', sa.Integer(), nullable=False),
    sa.Column('team_id', sa.Integer(), nullable=False),
    sa.Column('score', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['league_id'], ['league.id'], ),
    sa.ForeignKeyConstraint(['team_id'], ['team.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('event',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('match_id', sa.Integer(), nullable=True),
    sa.Column('result', sa.Enum('START', name='eventtype'), nullable=True),
    sa.ForeignKeyConstraint(['match_id'], ['match.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('event')
    op.drop_table('participant')
    op.drop_table('match')
    op.drop_table('team')
    op.drop_table('stadium')
    op.drop_table('league')
    op.drop_table('sportsman')
    op.drop_table('sport_name')
    op.drop_table('referee')
    op.drop_index(op.f('ix_country_name'), table_name='country')
    op.drop_table('country')
    # ### end Alembic commands ###