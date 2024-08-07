from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# Revisão identificadora e dependências
revision = "14e6f5e786af"
down_revision = "07246a2dad78"
branch_labels = None
depends_on = None


def upgrade():
    # Renomear a coluna 'id' para 'uuid'
    op.alter_column(
        "users",
        "id",
        new_column_name="uuid",
        existing_type=sa.Integer(),
        existing_nullable=False,
    )
    # Atualize o tipo da coluna para UUID
    op.alter_column(
        "users", "uuid", type_=postgresql.UUID(), existing_type=sa.Integer()
    )


def downgrade():
    # Reverter a migração
    op.alter_column(
        "users",
        "uuid",
        new_column_name="id",
        existing_type=postgresql.UUID(),
        existing_nullable=False,
    )
    op.alter_column(
        "users", "id", type_=sa.Integer(), existing_type=postgresql.UUID()
    )
