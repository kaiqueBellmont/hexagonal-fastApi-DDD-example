from typing import Callable
from sqlalchemy.orm import Session

from app.adapters.repositories.user_repository_impl import (
    UserSqlAlchemyRepository,
)
from app.domain.ports.unit_of_works.users import UserUnitOfWorkInterface


class UserSqlAlchemyUnitOfWork(UserUnitOfWorkInterface):
    def __init__(self, session_factory: Callable[[], Session]):
        self.session_factory = session_factory

    def __enter__(self):
        self.session = self.session_factory()
        self.users = UserSqlAlchemyRepository(self.session)
        return self

    def __exit__(self, *args):
        if self.session:
            self.session.close()

    def _commit(self):
        self.session.commit()

    def rollback(self):
        self.session.rollback()
