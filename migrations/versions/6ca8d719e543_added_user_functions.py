"""added user functions

Revision ID: 6ca8d719e543
Revises: c62e87d6ec9d
Create Date: 2023-03-02 13:41:14.999096

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = '6ca8d719e543'
down_revision = 'c62e87d6ec9d'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('Customers',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('first_name', sa.String(length=50), nullable=False),
    sa.Column('last_name', sa.String(length=50), nullable=False),
    sa.Column('street_address', sa.String(length=50), nullable=False),
    sa.Column('city', sa.String(length=50), nullable=False),
    sa.Column('zipcode', sa.String(length=10), nullable=False),
    sa.Column('country', sa.String(length=30), nullable=False),
    sa.Column('country_code', sa.String(length=2), nullable=False),
    sa.Column('birthday', sa.Date(), nullable=False),
    sa.Column('national_id', sa.String(length=20), nullable=False),
    sa.Column('telephone_country_code', sa.Integer(), nullable=False),
    sa.Column('telephone', sa.String(length=20), nullable=False),
    sa.Column('email_address', sa.String(length=50), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('Roles',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=50), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('name')
    )
    op.create_table('Accounts',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('account_type', sa.String(length=10), nullable=False),
    sa.Column('created', sa.DateTime(), nullable=False),
    sa.Column('balance', sa.Integer(), nullable=False),
    sa.Column('customer_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['customer_id'], ['Customers.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('Users',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('email_address', sa.String(length=128), nullable=False),
    sa.Column('hashed_password', sa.String(length=128), nullable=False),
    sa.Column('role', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['role'], ['Roles.id'], ),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('email_address')
    )
    op.create_table('Transactions',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('type', sa.String(length=20), nullable=False),
    sa.Column('operation', sa.String(length=50), nullable=False),
    sa.Column('date', sa.DateTime(), nullable=False),
    sa.Column('amount', sa.Integer(), nullable=False),
    sa.Column('new_balance', sa.Integer(), nullable=False),
    sa.Column('account_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['account_id'], ['Accounts.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.drop_table('users')
    with op.batch_alter_table('roles', schema=None) as batch_op:
        batch_op.drop_index('name')

    op.drop_table('roles')
    op.drop_table('transactions')
    op.drop_table('accounts')
    op.drop_table('customers')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('customers',
    sa.Column('id', mysql.INTEGER(display_width=11), autoincrement=True, nullable=False),
    sa.Column('first_name', mysql.VARCHAR(length=50), nullable=False),
    sa.Column('last_name', mysql.VARCHAR(length=50), nullable=False),
    sa.Column('street_address', mysql.VARCHAR(length=50), nullable=False),
    sa.Column('city', mysql.VARCHAR(length=50), nullable=False),
    sa.Column('zipcode', mysql.VARCHAR(length=10), nullable=False),
    sa.Column('country', mysql.VARCHAR(length=30), nullable=False),
    sa.Column('country_code', mysql.VARCHAR(length=2), nullable=False),
    sa.Column('birthday', sa.DATE(), nullable=False),
    sa.Column('national_id', mysql.VARCHAR(length=20), nullable=False),
    sa.Column('telephone_country_code', mysql.INTEGER(display_width=11), autoincrement=False, nullable=False),
    sa.Column('telephone', mysql.VARCHAR(length=20), nullable=False),
    sa.Column('email_address', mysql.VARCHAR(length=50), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    mysql_collate='utf8mb4_general_ci',
    mysql_default_charset='utf8mb4',
    mysql_engine='InnoDB'
    )
    op.create_table('accounts',
    sa.Column('id', mysql.INTEGER(display_width=11), autoincrement=True, nullable=False),
    sa.Column('account_type', mysql.VARCHAR(length=10), nullable=False),
    sa.Column('created', mysql.DATETIME(), nullable=False),
    sa.Column('balance', mysql.INTEGER(display_width=11), autoincrement=False, nullable=False),
    sa.Column('customer_id', mysql.INTEGER(display_width=11), autoincrement=False, nullable=False),
    sa.ForeignKeyConstraint(['customer_id'], ['customers.id'], name='accounts_ibfk_1'),
    sa.PrimaryKeyConstraint('id'),
    mysql_collate='utf8mb4_general_ci',
    mysql_default_charset='utf8mb4',
    mysql_engine='InnoDB'
    )
    op.create_table('transactions',
    sa.Column('id', mysql.INTEGER(display_width=11), autoincrement=True, nullable=False),
    sa.Column('type', mysql.VARCHAR(length=20), nullable=False),
    sa.Column('operation', mysql.VARCHAR(length=50), nullable=False),
    sa.Column('date', mysql.DATETIME(), nullable=False),
    sa.Column('amount', mysql.INTEGER(display_width=11), autoincrement=False, nullable=False),
    sa.Column('new_balance', mysql.INTEGER(display_width=11), autoincrement=False, nullable=False),
    sa.Column('account_id', mysql.INTEGER(display_width=11), autoincrement=False, nullable=False),
    sa.ForeignKeyConstraint(['account_id'], ['accounts.id'], name='transactions_ibfk_1'),
    sa.PrimaryKeyConstraint('id'),
    mysql_collate='utf8mb4_general_ci',
    mysql_default_charset='utf8mb4',
    mysql_engine='InnoDB'
    )
    op.create_table('roles',
    sa.Column('id', mysql.INTEGER(display_width=11), autoincrement=True, nullable=False),
    sa.Column('name', mysql.VARCHAR(length=50), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    mysql_collate='utf8mb4_general_ci',
    mysql_default_charset='utf8mb4',
    mysql_engine='InnoDB'
    )
    with op.batch_alter_table('roles', schema=None) as batch_op:
        batch_op.create_index('name', ['name'], unique=False)

    op.create_table('users',
    sa.Column('id', mysql.INTEGER(display_width=11), autoincrement=True, nullable=False),
    sa.Column('email_address', mysql.VARCHAR(length=50), nullable=False),
    sa.Column('hashed_password', mysql.VARCHAR(length=128), nullable=False),
    sa.Column('role', mysql.INTEGER(display_width=11), autoincrement=False, nullable=False),
    sa.ForeignKeyConstraint(['role'], ['roles.id'], name='users_ibfk_1'),
    sa.PrimaryKeyConstraint('id'),
    mysql_collate='utf8mb4_general_ci',
    mysql_default_charset='utf8mb4',
    mysql_engine='InnoDB'
    )
    op.drop_table('Transactions')
    op.drop_table('Users')
    op.drop_table('Accounts')
    op.drop_table('Roles')
    op.drop_table('Customers')
    # ### end Alembic commands ###
