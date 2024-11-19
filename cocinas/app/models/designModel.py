from sqlalchemy import Column, String, Integer, DECIMAL
from app.conection.conection import base


class DesignModel(base):

    __tablename__ = 'design'

    id = Column(Integer, primary_key = True)

    design = Column(String)
    price = Column(DECIMAL)

