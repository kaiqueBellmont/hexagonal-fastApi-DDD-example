from dependency_injector import containers, providers
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from app.adapters.unit_of_works.users_uow_impl import UserSqlAlchemyUnitOfWork
from app.adapters.use_cases.users_use_cases_impl import UserServiceImpl
from app.configurator.config import settings


def create_engine_and_session_factory():
    engine = create_engine(settings.DATABASE_URL)
    session_factory = sessionmaker(bind=engine)
    return session_factory


class Container(containers.DeclarativeContainer):
    wiring_config = containers.WiringConfiguration(
        packages=["app.adapters.entrypoints.rest.v1"]
    )

    session_factory = providers.Callable(create_engine_and_session_factory)
    user_uow = providers.Singleton(
        UserSqlAlchemyUnitOfWork, session_factory=session_factory
    )

    user_service = providers.Factory(
        UserServiceImpl,
        uow=user_uow,
    )
