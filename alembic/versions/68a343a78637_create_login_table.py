"""created tables login

Revision ID: 68a343a78637
Revises: 
Create Date: 2022-06-30 21:59:26.580538

"""
from alembic import op
import sqlalchemy as sa

# revision identifiers, used by Alembic.
from sqlalchemy import func

from app.utils.data_loader import load_country_data

revision = '68a343a78637'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.create_table('login',
                    sa.Column('id', sa.BigInteger, nullable=False),
                    sa.Column('email_address', sa.String(255), nullable=False),
                    sa.Column('password_hash', sa.Text, nullable=False),
                    sa.Column('status', sa.String(5), nullable=False),
                    sa.Column('created_at', sa.TIMESTAMP, nullable=False, server_default=func.now()),
                    sa.Column('created_by', sa.String(255), nullable=True),
                    sa.Column('updated_at', sa.TIMESTAMP, nullable=True),
                    sa.Column('updated_by', sa.String(255), nullable=True),
                    sa.PrimaryKeyConstraint('id'))

    op.create_table('country',
                    sa.Column('id', sa.BigInteger, nullable=False),
                    sa.Column('country_code', sa.String(100), nullable=False),
                    sa.Column('country_name', sa.String(100), nullable=False),
                    sa.Column('country_flag', sa.String, nullable=False),
                    sa.Column('created_at', sa.TIMESTAMP, nullable=False, server_default=func.now()),
                    sa.Column('created_by', sa.String(255), nullable=True),
                    sa.Column('updated_at', sa.TIMESTAMP, nullable=True),
                    sa.Column('updated_by', sa.String(255), nullable=True),
                    sa.PrimaryKeyConstraint('id'),
                    sa.UniqueConstraint('country_code'))

    op.create_table('profile',
                    sa.Column('id', sa.BigInteger, nullable=False),
                    sa.Column('login_id', sa.BigInteger, nullable=False),
                    sa.Column('first_name', sa.String(100), nullable=True),
                    sa.Column('middle_name', sa.String(100), nullable=True),
                    sa.Column('last_name', sa.String(100), nullable=True),
                    sa.Column('gender_code', sa.String(100), nullable=True),
                    sa.Column('country_code', sa.String(100), nullable=True),
                    sa.Column('created_at', sa.TIMESTAMP, nullable=False, server_default=func.now()),
                    sa.Column('created_by', sa.String(255), nullable=True),
                    sa.Column('updated_at', sa.TIMESTAMP, nullable=True),
                    sa.Column('updated_by', sa.String(255), nullable=True),
                    sa.PrimaryKeyConstraint('id'),
                    sa.ForeignKeyConstraint(columns=['login_id'], refcolumns=['login.id'], onupdate='CASCADE',
                                            ondelete='CASCADE'),
                    sa.ForeignKeyConstraint(columns=['country_code'], refcolumns=['country.country_code'],
                                            onupdate='CASCADE',
                                            ondelete='CASCADE'),
                    sa.CheckConstraint(name='gender_code_value_constraint',
                                       sqltext="((gender_code)::text = ANY ((ARRAY['M'::character varying, "\
                                               "'F'::character varying, 'T'::character varying])::text[]))"))

    load_country_data()


def downgrade():
    op.drop_table('profile')
    op.drop_table('country')
    op.drop_table('login')
