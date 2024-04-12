"""3.10: Add columns authentication, user_agent/version to Audit

Revision ID: 250931d82e51
Revises: 5741e5dac477
Create Date: 2024-03-27 16:08:47.242337

"""

# revision identifiers, used by Alembic.
revision = '250931d82e51'
down_revision = '5741e5dac477'

from alembic import op
import sqlalchemy as sa


def upgrade():
    try:
        op.add_column('pidea_audit', sa.Column('authentication', sa.Unicode(length=12), nullable=True))
        op.add_column('pidea_audit', sa.Column('user_agent', sa.Unicode(length=20), nullable=True))
        op.add_column('pidea_audit', sa.Column('user_agent_version',
                                               sa.Unicode(length=20), nullable=True))
    except Exception as exx:
        print("Can not add columns 'authentication', 'user_agent', 'user_agent_version' to "
              "table 'pidea_audit'. Probably already exist.")
        print(exx)


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('pidea_audit', 'user_agent_version')
    op.drop_column('pidea_audit', 'user_agent')
    op.drop_column('pidea_audit', 'authentication')
    # ### end Alembic commands ###
