from dependency_injector.wiring import Provide, inject
from datetime import timedelta

from fastapi import APIRouter, Depends, HTTPException, Response, status
from fastapi.security import OAuth2PasswordRequestForm
from jose import JWTError, jwt

from app.adapters.entrypoints.rest.utils import OAuth2PasswordBearerWithCookie
from app.application.schemas import Token, UserLoginInputDto, UserOutputDto
from app.application.use_cases.users import UserServiceInterface
from app.configurator.common.security import create_access_token
from app.configurator.config import settings
from app.configurator.containers import Container

router = APIRouter()


@router.post("/token", response_model=Token)
@inject
def login_for_access_token(
    response: Response,
    form_data: OAuth2PasswordRequestForm = Depends(),
    user_service: UserServiceInterface = Depends(
        Provide[Container.user_service]
    ),
):
    user = UserLoginInputDto(
        email=form_data.username, password=form_data.password
    )
    user = user_service.authenticate_user(user)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
        )
    access_token_expires = timedelta(
        minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES
    )
    access_token = create_access_token(
        data={"sub": user.email}, expires_delta=access_token_expires
    )
    response.set_cookie(
        key="access_token", value=f"Bearer {access_token}", httponly=True
    )
    return {"access_token": access_token, "token_type": "bearer"}


oauth2_scheme = OAuth2PasswordBearerWithCookie(token_url="/token")


@inject
def get_current_user_from_token(
    token: str = Depends(oauth2_scheme),
    user_service: UserServiceInterface = Depends(
        Provide[Container.user_service]
    ),
):
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
    )
    try:
        payload = jwt.decode(
            token, settings.SECRET_KEY, algorithms=[settings.ALGORITHM]
        )
        user_name: str = payload.get("sub")
        if user_name is None:
            raise credentials_exception
    except JWTError as e:
        raise credentials_exception from e
    with user_service.uow:
        user = user_service.uow.users.get_by_email(user_name)
        if user is None:
            raise credentials_exception
        return UserOutputDto(
            id=user.id,
            username=user.username,
            email=user.email,
            phone=user.phone,
        )


@router.get("/users/me", response_model=UserOutputDto)
@inject
def read_users_me(
    current_user: UserOutputDto = Depends(get_current_user_from_token),
):
    return current_user
