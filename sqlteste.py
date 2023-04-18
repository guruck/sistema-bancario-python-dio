from typing import List
from typing import Optional
from sqlalchemy import ForeignKey
from sqlalchemy import String
from sqlalchemy import create_engine
from sqlalchemy import inspect
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy.orm import relationship
from sqlalchemy.orm import Session

class Base(DeclarativeBase):
    pass

class User(Base):
    __tablename__ = "user_account"
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(30))
    fullname: Mapped[Optional[str]]
    addresses: Mapped[List["Address"]] = relationship(
        back_populates="user", cascade="all, delete-orphan"
    )
    def __repr__(self) -> str:
        return f"User(id={self.id!r}, name={self.name!r}, fullname={self.fullname!r})"

class Address(Base):
    __tablename__ = "address"
    id: Mapped[int] = mapped_column(primary_key=True)
    email_address: Mapped[str]
    user_id: Mapped[int] = mapped_column(ForeignKey("user_account.id"))
    user: Mapped["User"] = relationship(back_populates="addresses")
    def __repr__(self) -> str:
        return f"Address(id={self.id!r}, email_address={self.email_address!r})"

print(User.__tablename__)
print(Address.__tablename__)

engine = create_engine('sqlite://')
Base.metadata.create_all(engine)

inspector_engine = inspect(engine)
print(inspector_engine.has_table('user_account'))
print(inspector_engine.get_table_names())
print(inspector_engine.get_schema_names())

with Session(engine) as session:
    tiago=User(
        name='tiago',
        fullname='Tiago Rodrigues',
        addresses=[Address(email_address='teste@gmail.com'),Address(email_address='teste.ti@gmail.com')]
    )

    session.add(tiago)

    session.commit()