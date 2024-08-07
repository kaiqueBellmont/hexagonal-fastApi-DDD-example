from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# Revisão identificadora e dependências
revision = "e9533847a2fb"  # Substitua por um novo identificador gerado
down_revision = "14e6f5e786af"  # ID da migração que você está revertendo
branch_labels = None
depends_on = None


def upgrade():
    # Código para reverter a mudança de nome da coluna, mantendo o tipo UUID
    op.alter_column(
        "users",
        "uuid",
        new_column_name="id",
        existing_type=postgresql.UUID(),
        existing_nullable=False,
    )


def downgrade():
    # Código para reverter a mudança de nome da coluna, se necessário
    op.alter_column(
        "users",
        "id",
        new_column_name="uuid",
        existing_type=postgresql.UUID(),
        existing_nullable=False,
    )
