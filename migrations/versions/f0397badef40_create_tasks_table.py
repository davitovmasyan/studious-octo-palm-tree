"""create tasks table

Revision ID: f0397badef40
Revises: 
Create Date: 2023-11-09 15:38:41.180711

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.sql import func


# revision identifiers, used by Alembic.
revision = 'f0397badef40'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        'tasks',
        sa.Column('id', sa.Integer(), primary_key=True),
        sa.Column('name', sa.String(100), unique=True, nullable=False),
        sa.Column('starts_at', sa.DateTime(), nullable=True),
        sa.Column('expires', sa.DateTime(), nullable=True),
        sa.Column('created', sa.DateTime(), default=func.now())
    )


def downgrade():
    op.drop_table('tasks')
