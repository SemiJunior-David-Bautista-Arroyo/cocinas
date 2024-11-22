from sqlalchemy import Column, Integer, JSON, String
from app.conection.connection import base


class BranchModel(base):

    __tablename__ = 'branch'

    id = Column(Integer, primary_key = True)

    branchname = Column(String)
    address = Column(JSON)

