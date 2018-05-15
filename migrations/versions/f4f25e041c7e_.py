"""empty message

Revision ID: f4f25e041c7e
Revises: 
Create Date: 2018-05-11 15:01:00.556875

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = 'f4f25e041c7e'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('area',
    sa.Column('area', sa.String(length=256), nullable=False),
    sa.Column('data', postgresql.JSON(astext_type=sa.Text()), nullable=True),
    sa.PrimaryKeyConstraint('area')
    )
    op.create_table('attribution',
    sa.Column('attribution', sa.String(length=64), nullable=False),
    sa.Column('name', sa.String(length=256), nullable=True),
    sa.PrimaryKeyConstraint('attribution')
    )
    op.create_table('category',
    sa.Column('category', sa.String(length=64), nullable=False),
    sa.Column('text', sa.Text(), nullable=True),
    sa.PrimaryKeyConstraint('category')
    )
    op.create_table('licence',
    sa.Column('licence', sa.String(length=256), nullable=False),
    sa.Column('name', sa.String(length=256), nullable=True),
    sa.Column('text', sa.Text(), nullable=True),
    sa.PrimaryKeyConstraint('licence')
    )
    op.create_table('organisation',
    sa.Column('organisation', sa.String(length=64), nullable=False),
    sa.Column('name', sa.String(length=256), nullable=True),
    sa.Column('website', sa.String(length=256), nullable=True),
    sa.Column('text', sa.Text(), nullable=True),
    sa.Column('area_id', sa.String(length=256), nullable=True),
    sa.Column('category_id', sa.String(length=64), nullable=True),
    sa.ForeignKeyConstraint(['area_id'], ['area.area'], name='organisation_area_fkey'),
    sa.ForeignKeyConstraint(['category_id'], ['category.category'], name='organisation_category_fkey'),
    sa.PrimaryKeyConstraint('organisation')
    )
    op.create_table('publication',
    sa.Column('publication', sa.String(length=64), nullable=False),
    sa.Column('name', sa.String(length=256), nullable=True),
    sa.Column('organisation_id', sa.String(length=64), nullable=True),
    sa.Column('licence_id', sa.String(length=256), nullable=True),
    sa.Column('attribution_id', sa.String(length=64), nullable=True),
    sa.Column('category_id', sa.String(length=64), nullable=True),
    sa.Column('url', sa.Text(), nullable=True),
    sa.Column('data_url', sa.Text(), nullable=True),
    sa.ForeignKeyConstraint(['attribution_id'], ['attribution.attribution'], name='publication_attribution_fkey'),
    sa.ForeignKeyConstraint(['category_id'], ['category.category'], name='publication_category_fkey'),
    sa.ForeignKeyConstraint(['licence_id'], ['licence.licence'], name='publication_licence_fkey'),
    sa.ForeignKeyConstraint(['organisation_id'], ['organisation.organisation'], name='publication_organisation_fkey'),
    sa.PrimaryKeyConstraint('publication')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('publication')
    op.drop_table('organisation')
    op.drop_table('licence')
    op.drop_table('category')
    op.drop_table('attribution')
    op.drop_table('area')
    # ### end Alembic commands ###