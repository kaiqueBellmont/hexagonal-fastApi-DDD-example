import json
from fastapi import APIRouter, Depends, Response
from fastapi.encoders import jsonable_encoder
from dependency_injector.wiring import Provide, inject

from app.adapters import STATUS_CODES
from app.configurator.containers import Container
from app.application.schemas.user_schemas import User, UserCreateInputDto
from app.application.use_cases.users import UserServiceInterface

router = APIRouter()


@router.post("/users", response_model=User)
@inject
def create_user(
        user: UserCreateInputDto,
        user_service: UserServiceInterface = Depends(
            Provide[Container.user_service]
        ),
):
    response = user_service.create(user=user)
    data = jsonable_encoder(response.value)
    return Response(
        content=json.dumps(data),
        media_type="application/json",
        status_code=STATUS_CODES[response.type],
    )


@router.get("/ok")
def health_check():
    return Response("OK - Ta rodando liso :)", status_code=200)
