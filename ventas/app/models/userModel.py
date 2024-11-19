from app.conection.connection import base
from sqlalchemy import Column, Integer, String, ForeignKey, JSON


class UserModel(base):

    __tablename__ = 'user'

    id = Column(Integer, primary_key = True)
    name = Column(String)
    lastname = Column(String)
    username = Column(String)
    cellphone = Column(String)
    address = Column(JSON)
    password_user = Column(String)
    rol_id = Column(Integer, ForeignKey('rol.id'))
    
