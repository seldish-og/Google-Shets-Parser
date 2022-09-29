from sqlalchemy import Column
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.types import Integer, Text, String, DateTime


Base = declarative_base()


class User(Base):
    __tablename__ = "user"

    id = Column(Integer, primary_key=True, autoincrement="auto")
    order_number = Column(Integer, nullable=False)
    price_usd = Column(Integer, nullable=False)
    price_rub = Column(Integer, nullable=False)
    order_date = Column(String(255), nullable=False)
