from conection.connection import base
from sqlalchemy import Column, Integer, String


class RolModel(base):

    __tablename__ = 'rol'

    id = Column(Integer, primary_key = True)
    rol = Column(String)
