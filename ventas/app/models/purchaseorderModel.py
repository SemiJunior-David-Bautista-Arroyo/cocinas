from sqlalchemy import Column,String, Integer,ForeignKey, DateTime 
from app.conection.connection import base


class PurchaseOrderModel(base):

    __tablename__ = 'purchase_order'

    id = Column(Integer, primary_key = True)
    isbn = Column(String)
    furniture_id = Column(Integer, ForeignKey('furniture.id'))
    quantity = Column(Integer)
    user_id = Column(Integer, ForeignKey('user.id'))
    delivery_date = Column(DateTime)

