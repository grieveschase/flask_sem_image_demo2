"""empty message

Revision ID: 2d853929513c
Revises: 
Create Date: 2020-05-06 11:40:32.617005

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '2d853929513c'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('measdisplay_obs',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('tool', sa.String(length=64), nullable=True),
    sa.Column('slot', sa.Integer(), nullable=True),
    sa.Column('fov', sa.Float(), nullable=True),
    sa.Column('iprobe', sa.String(length=64), nullable=True),
    sa.Column('lot', sa.String(length=64), nullable=True),
    sa.Column('vacc', sa.Integer(), nullable=True),
    sa.Column('vhar', sa.Integer(), nullable=True),
    sa.Column('recipe', sa.String(length=64), nullable=True),
    sa.Column('site_type', sa.String(length=64), nullable=True),
    sa.Column('site_order', sa.Integer(), nullable=True),
    sa.Column('fieldx', sa.Integer(), nullable=True),
    sa.Column('fieldy', sa.Integer(), nullable=True),
    sa.Column('locx', sa.Float(), nullable=True),
    sa.Column('locy', sa.Float(), nullable=True),
    sa.Column('date', sa.DateTime(), nullable=True),
    sa.Column('port', sa.Integer(), nullable=True),
    sa.Column('cycle', sa.Integer(), nullable=True),
    sa.Column('target', sa.String(length=64), nullable=True),
    sa.Column('measdate', sa.DateTime(), nullable=True),
    sa.Column('image', sa.LargeBinary(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_measdisplay_obs_lot'), 'measdisplay_obs', ['lot'], unique=False)
    op.create_index(op.f('ix_measdisplay_obs_recipe'), 'measdisplay_obs', ['recipe'], unique=False)
    op.create_index(op.f('ix_measdisplay_obs_tool'), 'measdisplay_obs', ['tool'], unique=False)
    op.create_table('patternfov',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('tool', sa.String(length=64), nullable=True),
    sa.Column('slot', sa.Integer(), nullable=True),
    sa.Column('fov', sa.Float(), nullable=True),
    sa.Column('iprobe', sa.String(length=64), nullable=True),
    sa.Column('lot', sa.String(length=64), nullable=True),
    sa.Column('vacc', sa.Integer(), nullable=True),
    sa.Column('vhar', sa.Integer(), nullable=True),
    sa.Column('recipe', sa.String(length=64), nullable=True),
    sa.Column('site_type', sa.String(length=64), nullable=True),
    sa.Column('site_order', sa.Integer(), nullable=True),
    sa.Column('fieldx', sa.Integer(), nullable=True),
    sa.Column('fieldy', sa.Integer(), nullable=True),
    sa.Column('locx', sa.Float(), nullable=True),
    sa.Column('locy', sa.Float(), nullable=True),
    sa.Column('date', sa.DateTime(), nullable=True),
    sa.Column('port', sa.Integer(), nullable=True),
    sa.Column('cycle', sa.Integer(), nullable=True),
    sa.Column('target', sa.String(length=64), nullable=True),
    sa.Column('measdate', sa.DateTime(), nullable=True),
    sa.Column('image', sa.LargeBinary(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_patternfov_lot'), 'patternfov', ['lot'], unique=False)
    op.create_index(op.f('ix_patternfov_recipe'), 'patternfov', ['recipe'], unique=False)
    op.create_index(op.f('ix_patternfov_tool'), 'patternfov', ['tool'], unique=False)
    op.create_table('roles',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=64), nullable=True),
    sa.Column('default', sa.Boolean(), nullable=True),
    sa.Column('permissions', sa.Integer(), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('name')
    )
    op.create_index(op.f('ix_roles_default'), 'roles', ['default'], unique=False)
    op.create_table('users',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=64), nullable=True),
    sa.Column('role_id', sa.Integer(), nullable=True),
    sa.Column('password_hash', sa.String(length=128), nullable=True),
    sa.ForeignKeyConstraint(['role_id'], ['roles.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('users')
    op.drop_index(op.f('ix_roles_default'), table_name='roles')
    op.drop_table('roles')
    op.drop_index(op.f('ix_patternfov_tool'), table_name='patternfov')
    op.drop_index(op.f('ix_patternfov_recipe'), table_name='patternfov')
    op.drop_index(op.f('ix_patternfov_lot'), table_name='patternfov')
    op.drop_table('patternfov')
    op.drop_index(op.f('ix_measdisplay_obs_tool'), table_name='measdisplay_obs')
    op.drop_index(op.f('ix_measdisplay_obs_recipe'), table_name='measdisplay_obs')
    op.drop_index(op.f('ix_measdisplay_obs_lot'), table_name='measdisplay_obs')
    op.drop_table('measdisplay_obs')
    # ### end Alembic commands ###
