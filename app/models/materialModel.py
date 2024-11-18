from sqlalchemy import Column, Integer, String, DECIMAL
from app.conection.conection import base


class MaterialModel(base):

    __tablename__ = 'material'


    id = Column(Integer, primary_key = True)

    material = Column(String)
    price = Column(DECIMAL)


