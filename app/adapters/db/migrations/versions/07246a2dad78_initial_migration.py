"""create users table

Revision ID: <sua_revision_id>
Revises:
Create Date: 2024-08-06 00:00:00

"""

from alembic import op
import sqlalchemy as sa
import sqlalchemy.dialects.postgresql as postgresql

# Revisão e dependências
revision = "07246a2dad78"
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # Criar a tabela 'users'
    op.create_table(
        "users",
        sa.Column(
            "id",
            postgresql.UUID(as_uuid=True),
            primary_key=True,
            default=sa.text("uuid_generate_v4()"),
            index=True,
        ),
        sa.Column("username", sa.String(), unique=True, index=True),
        sa.Column("email", sa.String(), unique=True, index=True),
        sa.Column("phone", sa.String(), unique=True, index=True),
        sa.Column("hashed_password", sa.String()),
    )


def downgrade():
    # Dropar a tabela 'users'
    op.drop_table("users")
