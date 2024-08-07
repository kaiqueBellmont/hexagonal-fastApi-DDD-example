## TODO: refactor repositories IMPL to make what the DB does and refactor alembic files

## To create a migration :

```bash
cd app/adapters/db
alembic revision -m "Descrição da migração"


"""Descrição da migração

Revision ID: <id_unico>
Revises: <id_da_migração_anterior>
Create Date: YYYY-MM-DD HH:MM:SS
"""

from alembic import op
import sqlalchemy as sa

# revision identifiers, used by Alembic.
revision = '<id_unico>'
down_revision = '<id_da_migração_anterior>'
branch_labels = None
depends_on = None

def upgrade():
    # Adicione aqui as operações para aplicar a migração
    pass

def downgrade():
    # Adicione aqui as operações para reverter a migração
    pass


alembic upgrade head
```