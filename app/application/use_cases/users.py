from abc import ABC, abstractmethod
from typing import Union

from app.application.schemas import (
    UserCreateInputDto,
    UserLoginInputDto,
    UserOutputDto,
)
from app.domain.ports.common.responses import ResponseSuccess, ResponseFailure
from app.domain.ports.unit_of_works.users import UserUnitOfWorkInterface


class UserServiceInterface(ABC):
    @abstractmethod
    def __init__(self, uow: UserUnitOfWorkInterface):
        self.uow = uow

    def create(
        self, user: UserCreateInputDto
    ) -> Union[ResponseSuccess, ResponseFailure]:
        return self._create(user)

    def authenticate_user(
        self, user: UserLoginInputDto
    ) -> Union[UserOutputDto, bool]:
        return self._authenticate_user(user)

    @abstractmethod
    def _create(
        self, user: UserCreateInputDto
    ) -> Union[ResponseSuccess, ResponseFailure]:
        raise NotImplementedError

    @abstractmethod
    def _authenticate_user(
        self, user: UserLoginInputDto
    ) -> Union[UserOutputDto, bool]:
        raise NotImplementedError
