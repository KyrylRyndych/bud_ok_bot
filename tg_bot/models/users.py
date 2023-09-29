from .base_model import Base
from sqlalchemy.orm import Mapped


class User(Base):
    name: Mapped[str]
    email: Mapped[str]
