from app.domain.models.user_model import UserModel
from app.domain.ports.repositories.users import UserRepositoryInterface


class UserSqlAlchemyRepository(UserRepositoryInterface):
    def __init__(self, session):
        super().__init__()
        self.session = session

    def _add(self, user):
        self.session.add(user)

    def _get(self, username: str) -> UserModel:
        return (
            self.session.query(UserModel).filter_by(username=username).first()
        )

    def _get_by_email(self, email: str) -> UserModel:
        return self.session.query(UserModel).filter_by(email=email).first()

    def _get_by_id(self, id: str) -> UserModel:
        return self.session.query(UserModel).filter_by(id=id).first()

    def _get_by_name(self, username: str) -> UserModel:
        return (
            self.session.query(UserModel).filter_by(username=username).first()
        )
