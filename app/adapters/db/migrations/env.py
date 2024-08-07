import os
import subprocess
import sys
from datetime import datetime
from alembic import context
from sqlalchemy import engine_from_config, pool
from logging.config import fileConfig
from dotenv import load_dotenv

# Carregar o arquivo .env
dotenv_path = os.path.join(
    os.path.abspath(os.path.join(os.path.dirname(__file__), "../../../")),
    "configurator/.env",
)
load_dotenv(dotenv_path)

# Obter a URL do banco de dados do .env
database_url = os.getenv("DATABASE_URL")
print(f"DATABASE_URL: {database_url}")

# Configurar o Alembic
config = context.config
if database_url:
    config.set_main_option("sqlalchemy.url", database_url)
else:
    raise ValueError("DATABASE_URL não encontrada no .env")

# Configurar o logging
if config.config_file_name is not None:
    fileConfig(config.config_file_name)

# Adiciona o diretório raiz do projeto ao sys.path
sys.path.insert(
    0, os.path.abspath(os.path.join(os.path.dirname(__file__), "../../../../"))
)

from app.adapters.db.orm import metadata

target_metadata = metadata

# Verificar se o target_metadata contém tabelas
print(f"Target Metadata: {target_metadata.tables.keys()}")


def dump_database():
    pg_dump_path = "/opt/homebrew/bin/pg_dump"  # Atualize para o caminho correto do pg_dump no seu sistema
    user = os.getenv("DB_USER")
    password = os.getenv("DB_PASSWORD")
    host = os.getenv("DB_HOST")
    port = os.getenv("DB_PORT")
    db_name = os.getenv("DB_NAME")

    dump_file_path = os.path.join(
        os.path.dirname(__file__),
        f"db_dump_{datetime.now().strftime('%Y%m%d_%H%M%S')}.sql",
    )

    try:
        result = subprocess.run(
            [
                pg_dump_path,
                "-U",
                user,
                "-h",
                host,
                "-p",
                port,
                "-d",
                db_name,
                "-f",
                dump_file_path,
            ],
            check=True,
            text=True,
            env={"PGPASSWORD": password},
        )
        if result.returncode == 0:
            print(f"Database dump created successfully: {dump_file_path}")
    except subprocess.CalledProcessError as e:
        print(f"Error during database dump: {e}")


def run_migrations_offline() -> None:
    """Executar migrações no modo offline."""
    url = config.get_main_option("sqlalchemy.url")
    context.configure(
        url=url,
        target_metadata=target_metadata,
        literal_binds=True,
        dialect_opts={"paramstyle": "named"},
    )

    with context.begin_transaction():
        context.run_migrations()
        dump_database()


def run_migrations_online() -> None:
    """Executar migrações no modo online."""
    connectable = engine_from_config(
        config.get_section(config.config_ini_section, {}),
        prefix="sqlalchemy.",
        poolclass=pool.NullPool,
    )

    with connectable.connect() as connection:
        context.configure(
            connection=connection,
            target_metadata=target_metadata,
        )

        with context.begin_transaction():
            context.run_migrations()
            dump_database()


if context.is_offline_mode():
    run_migrations_offline()
else:
    run_migrations_online()
