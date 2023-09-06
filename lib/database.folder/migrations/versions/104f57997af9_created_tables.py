"""created tables

Revision ID: 104f57997af9
Revises: 76c6fd47701a
Create Date: 2023-09-06 09:44:40.689614

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '104f57997af9'
down_revision: Union[str, None] = '76c6fd47701a'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('customers',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('first_name', sa.String(), nullable=True),
    sa.Column('last_name', sa.String(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('transactions',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('date', sa.Date(), nullable=True),
    sa.Column('transaction_type', sa.String(), nullable=True),
    sa.Column('amount', sa.Float(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('accounts',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('account_type', sa.String(), nullable=True),
    sa.Column('transaction_id', sa.Integer(), nullable=True),
    sa.Column('customer_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['customer_id'], ['customers.id'], name=op.f('fk_accounts_customer_id_customers')),
    sa.ForeignKeyConstraint(['transaction_id'], ['transactions.id'], name=op.f('fk_accounts_transaction_id_transactions')),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('accounts')
    op.drop_table('transactions')
    op.drop_table('customers')
    # ### end Alembic commands ###
