from sqlalchemy.orm import Mapped
from sqlalchemy import Column
from sqlalchemy.orm import declarative_base, declared_attr


class Base(declarative_base()):
    __abstract__ = True

    @declared_attr.directive
    def __tablename__(cls) -> str:
        return f"{cls.__name__.lower()}"

    id: Mapped[int] = Column(primary_key=True)
