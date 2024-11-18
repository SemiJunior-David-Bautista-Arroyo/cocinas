from sqlalchemy import Column, String, Integer
from app.conection.conection import base


class InstallerModel(base):

    __tablename__ = 'installer'

    id = Column(Integer, primary_key = True)

    name = Column(String)
    lastname = Column(String)


