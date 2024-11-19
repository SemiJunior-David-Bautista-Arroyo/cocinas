from sqlalchemy import Column, Integer, String, ForeignKey, DECIMAL, DateTime
from app.conection.conection import base


class OrderModel(base):

    __tablename__ = "order"

    id = Column(Integer, primary_key = True)
    isbn = Column(String)
    kitchen_id = Column(Integer, ForeignKey('kitchen.id'))
    total = Column(DECIMAL)
    delivery_date = Column(DateTime)
    user_id = Column(Integer, ForeignKey('user.id'))
    installer_id = Column(Integer, ForeignKey('installer.id'))



