from sqlalchemy import Column, Integer, JSON, String
from app.conection.connection import base


class BranchModel(base):

    id = Column(Integer, primary_key = True)

    branchname = Column(String)
    address = Column(JSON)

