"""empty message

Revision ID: 6e0fed3ef0ee
Revises: 
Create Date: 2020-04-03 16:07:29.647639

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '6e0fed3ef0ee'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('User',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('fullname', sa.String(length=200), nullable=True),
    sa.Column('ic', sa.String(length=14), nullable=True),
    sa.Column('email', sa.String(length=200), nullable=True),
    sa.Column('password', sa.String(length=15), nullable=True),
    sa.Column('phone', sa.String(length=15), nullable=True),
    sa.Column('dob', sa.String(length=10), nullable=True),
    sa.Column('age', sa.Integer(), nullable=True),
    sa.Column('sex', sa.Integer(), nullable=True),
    sa.Column('access_level', sa.Integer(), nullable=True),
    sa.Column('date_created', sa.DateTime(), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('email')
    )
    op.create_table('health',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.Column('cp', sa.Integer(), nullable=True),
    sa.Column('trestbps', sa.Integer(), nullable=True),
    sa.Column('chol', sa.Integer(), nullable=True),
    sa.Column('fbs', sa.Integer(), nullable=True),
    sa.Column('restecg', sa.Integer(), nullable=True),
    sa.Column('thalach', sa.Integer(), nullable=True),
    sa.Column('exang', sa.Integer(), nullable=True),
    sa.Column('oldpeak', sa.Float(), nullable=True),
    sa.Column('slope', sa.Integer(), nullable=True),
    sa.Column('ca', sa.Float(), nullable=True),
    sa.Column('thal', sa.Float(), nullable=True),
    sa.Column('target', sa.Integer(), nullable=True),
    sa.Column('date_created', sa.DateTime(), nullable=True),
    sa.ForeignKeyConstraint(['user_id'], ['User.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('previous_record',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.Column('cp', sa.Integer(), nullable=True),
    sa.Column('trestbps', sa.Integer(), nullable=True),
    sa.Column('chol', sa.Integer(), nullable=True),
    sa.Column('fbs', sa.Integer(), nullable=True),
    sa.Column('restecg', sa.Integer(), nullable=True),
    sa.Column('thalach', sa.Integer(), nullable=True),
    sa.Column('exang', sa.Integer(), nullable=True),
    sa.Column('oldpeak', sa.Float(), nullable=True),
    sa.Column('slope', sa.Integer(), nullable=True),
    sa.Column('ca', sa.Float(), nullable=True),
    sa.Column('thal', sa.Float(), nullable=True),
    sa.Column('target', sa.Integer(), nullable=True),
    sa.Column('date_created', sa.DateTime(), nullable=True),
    sa.ForeignKeyConstraint(['user_id'], ['User.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('previous_record')
    op.drop_table('health')
    op.drop_table('User')
    # ### end Alembic commands ###