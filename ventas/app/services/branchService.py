from app.models.branchModel import BranchModel
from app.schemas.branchSchema import BranchSchema


class BranchService:

    def __init__(self, db) -> None:
        self.db = db


    def addbr(self, data : BranchSchema) -> BranchSchema:

        nb = BranchModel(**data.__dict__)

        self.db.add(nb)
        self.db.commit()
        self.db.refresh(nb)
        self.db.close()

        return nb


    def geta(self) -> list[BranchSchema]:

        branchs = self.db.query(BranchModel).all()

        return branchs
    

    def getbyid(self, id : int) -> BranchSchema:

        branch = self.db.query(BranchModel).filter(BranchModel.id == id).first()

        return branch

