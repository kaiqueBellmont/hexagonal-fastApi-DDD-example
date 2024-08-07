# app/adapters/orm/models/user_db_model.py
import uuid

from sqlalchemy import Column, String, MetaData, Table
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import registry

from app.domain.models.user_model import UserModel

metadata = MetaData()
mapper_registry = registry(metadata=metadata)

users = Table(
    "users",
    mapper_registry.metadata,
    Column(
        "id",
        UUID(as_uuid=True),
        primary_key=True,
        default=uuid.uuid4,
        index=True,
    ),
    Column("username", String, unique=True, nullable=False),
    Column("email", String, nullable=False, unique=True, index=True),
    Column("phone", String, unique=True, nullable=False),
    Column("hashed_password", String, nullable=False),
)


def start_mappers():
    mapper_registry.map_imperatively(UserModel, users)
