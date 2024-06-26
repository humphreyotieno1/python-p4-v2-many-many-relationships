"""add employee_meetings association table

Revision ID: 8155126c4ab6
Revises: 0b0404c9fa08
Create Date: 2024-04-07 01:45:45.443540

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '8155126c4ab6'
down_revision = '0b0404c9fa08'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('employee_meetings',
    sa.Column('employee_id', sa.Integer(), nullable=False),
    sa.Column('meeting_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['employee_id'], ['employees.id'], name=op.f('fk_employee_meetings_employee_id_employees')),
    sa.ForeignKeyConstraint(['meeting_id'], ['meetings.id'], name=op.f('fk_employee_meetings_meeting_id_meetings')),
    sa.PrimaryKeyConstraint('employee_id', 'meeting_id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('employee_meetings')
    # ### end Alembic commands ###
