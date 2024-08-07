import uuid
from dataclasses import asdict, dataclass


@dataclass
class UserModel:
    uuid: str
    username: str
    email: str
    phone: str
    hashed_password: str

    @classmethod
    def from_dict(cls, _dict):
        return cls(**_dict)

    def to_dict(self):
        return asdict(self)

    def __eq__(self, other):
        if not isinstance(other, UserModel):
            return False
        return self.username == other.username

    def __hash__(self):
        return hash(self.username)


def user_model_factory(
    username: str,
    email: str,
    hashed_password: str,
    phone: str,
) -> UserModel:
    return UserModel(
        uuid=str(uuid.uuid4()),
        username=username,
        email=email,
        phone=phone,
        hashed_password=hashed_password,
    )
