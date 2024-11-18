from app.conection.conection import base
from sqlalchemy import Column, String, Integer, JSON



class UserModel(base):

    __tablename__ = "user"

    id = Column(Integer, primary_key=True)
    name = Column(String)
    lastname = Column(String)
    email = Column(String)
    cellphone = Column(String)
    password_user = Column(String)
    address = Column(JSON)

