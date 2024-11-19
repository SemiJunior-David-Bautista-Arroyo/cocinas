from app.conection.connection import base
from sqlalchemy import Column, Integer, DECIMAL, String


class FurnitureModel(base):

    __tablename__ = "furniture"

    id = Column(Integer, primary_key = True)

    name = Column(String)
    description = Column(String)
    quantity = Column(Integer)
    price = Column(DECIMAL)


