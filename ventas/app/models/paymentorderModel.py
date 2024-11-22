from app.conection.connection import base
from sqlalchemy import Column, Integer, String, ForeignKey, DECIMAL


class PaymentOrderModel(base):

    __tablename__ = 'payment_order'

    id = Column(Integer, primary_key = True)
    isbn = Column(String)
    purchase_order_id = Column(Integer, ForeignKey('purchase_order.id'))
    total = Column(DECIMAL)


