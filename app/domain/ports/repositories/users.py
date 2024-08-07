from abc import ABC, abstractmethod
from app.domain.models.user_model import UserModel


class UserRepositoryInterface(ABC):

    def add(self, user: UserModel):
        self._add(user)

    def get(self, username: str) -> UserModel:
        user = self._get(username)
        return user

    def get_by_email(self, email: str) -> UserModel:
        user = self._get_by_email(email)
        return user

    def get_by_id(self, id: int) -> UserModel:
        user = self._get_by_id(id)
        return user

    def get_by_name(self, username: str) -> UserModel:
        user = self._get_by_name(username)
        return user

    @abstractmethod
    def _add(self, user: UserModel):
        raise NotImplementedError

    @abstractmethod
    def _get(self, user_name: str) -> UserModel:
        raise NotImplementedError

    @abstractmethod
    def _get_by_email(self, email: str) -> UserModel:
        raise NotImplementedError

    @abstractmethod
    def _get_by_id(self, id: int) -> UserModel:
        raise NotImplementedError

    @abstractmethod
    def _get_by_name(self, username: str) -> UserModel:
        raise NotImplementedError
