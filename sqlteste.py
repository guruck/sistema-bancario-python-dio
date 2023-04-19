from typing import List, Optional

from sqlalchemy import ForeignKey, Column
from sqlalchemy import String, Integer
from sqlalchemy import create_engine, MetaData, Table
from sqlalchemy import inspect, select, func
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

engine = create_engine('sqlite:///teste.db')
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

    # session.add(tiago)
    # session.commit()

stmt = select(User).where(User.name.in_(['tiago','jordino','maria'])).order_by(User.name.desc())
for user in session.scalars(stmt):
    print(user)

stmt_address = select(Address).where(Address.user_id.in_([1]))
for address in session.scalars(stmt_address):
    print(address)

stmt_join=select(User.name, Address.email_address).join_from(User,Address)
print(stmt_join)
results=engine.connect().execute(stmt_join).fetchall()
for result in results: #session.scalars(stmt_join):
    print(result)

stmt_count = select(func.count('*')).select_from(User)
for result in session.scalars(stmt_count):
    print(result)

metadata_obj=MetaData()
user = Table(
    'user',
    metadata_obj,
    Column('user_id', Integer, primary_key=True),
    Column('user_name', String, nullable=False),
    Column('user_mail', String),
    Column('user_nick', String, nullable=False)
)

for table in metadata_obj.sorted_tables:
    print(table,metadata_obj.info, metadata_obj.tables)

engine2 = create_engine('sqlite:///memory.db')
metadata_obj.create_all(engine2)