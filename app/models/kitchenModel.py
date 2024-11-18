from sqlalchemy import Column, ForeignKey, Integer, JSON
from app.conection.conection import base


class KitchenModel(base):

    __tablename__ = "kitchen"

    id = Column(Integer, primary_key = True )

    sizes = Column(JSON)
    design_id = Column(Integer, ForeignKey('design.id'))
    material_id = Column(Integer, ForeignKey('material.id'))
    user_id = Column(Integer, ForeignKey('user.id'))
    


