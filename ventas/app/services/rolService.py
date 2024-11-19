from app.models.rolModel import RolModel
from app.schemas.rolSchema import RolSchema


class RolService:

    def __init__(self, db) -> None:
        self.db = db

    
    def getall(self) -> list[RolSchema]:
        rols = self.db.query(RolModel).all()

        return rols
    

    def getbyId(self, id : int) -> RolSchema:

        rol = self.db.query(RolModel).filter(RolModel.id == id)

        return rol
    

    def addRol(self, data : RolSchema) -> RolSchema:

        rol = RolModel(**data.__dict__)

        self.db.add(rol)
        self.db.commit()
        self.db.refresh(rol)

        return rol

    
