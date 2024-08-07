import abc
from app.domain.ports.repositories.users import UserRepositoryInterface


class UserUnitOfWorkInterface(abc.ABC):
    users: UserRepositoryInterface

    def __enter__(self) -> "UserUnitOfWorkInterface":
        return self

    def __exit__(self, *args):
        self.rollback()

    def commit(self):
        self._commit()

    @abc.abstractmethod
    def _commit(self):
        raise NotImplementedError

    @abc.abstractmethod
    def rollback(self):
        raise NotImplementedError
