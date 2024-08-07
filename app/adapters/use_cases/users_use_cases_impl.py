from typing import Union
from app.application.schemas import (
    UserCreateInputDto,
    UserOutputDto,
    UserLoginInputDto,
)
from app.application.use_cases.users import UserServiceInterface
from app.configurator.common.hashing import Hasher
from app.domain.ports.unit_of_works.users import UserUnitOfWorkInterface
from app.domain.ports.common.responses import (
    ResponseSuccess,
    ResponseFailure,
    ResponseTypes,
)
from app.domain.models import user_model_factory


class UserServiceImpl(UserServiceInterface):
    def __init__(self, uow: UserUnitOfWorkInterface):
        self.uow = uow

    def _create(
        self, user: UserCreateInputDto
    ) -> Union[ResponseSuccess, ResponseFailure]:
        try:
            with self.uow:
                existing_user = self.uow.users.get(user.username)
                if existing_user is None:
                    hashed_password = Hasher.get_password_hash(user.password)
                    new_user = user_model_factory(
                        username=user.username,
                        hashed_password=hashed_password,
                        email=user.email,
                        phone=user.phone,
                    )
                    self.uow.users.add(new_user)
                self.uow.commit()
                user_ = self.uow.users.get(user.username)
                user_output_dto = UserOutputDto(
                    id=user_.id,
                    username=user_.username,
                    email=user_.email,
                    phone=user_.phone,
                )
                return ResponseSuccess(user_output_dto)
        except Exception as exc:
            return ResponseFailure(ResponseTypes.SYSTEM_ERROR, exc)

    def _authenticate_user(
        self, user: UserLoginInputDto
    ) -> Union[UserOutputDto, bool]:
        with self.uow:
            user_ = self.uow.users.get_by_email(user.email)
            if not user_ or not Hasher.verify_password(
                user.password, user_.hashed_password
            ):
                return False
            return UserOutputDto(
                id=user_.id,
                username=user_.username,
                email=user_.email,
                phone=user_.phone,
            )
