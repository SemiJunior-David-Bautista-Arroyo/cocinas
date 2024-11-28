from app.models.furnitureModel import FurnitureModel
from app.schemas.furnitureSchema import FurnitureSchema


class FurnitureService:

    def __init__(self, db) -> None:
        self.db = db


    def addFurniture(self, data : FurnitureSchema) -> FurnitureSchema:

        furniture = FurnitureModel(**data.__dict__)

        self.db.add(furniture)
        self.db.commit()
        self.db.refresh(furniture)
        self.db.close()
        return furniture
    

    def getall(self) -> list[FurnitureSchema]:

        furnitures = self.db.query(FurnitureModel).all()

        return furnitures


    def getId(self, id : int) -> FurnitureSchema :

        furniture = self.db.query(FurnitureModel).filter(FurnitureModel.id == id).first()

        return furniture


    def updateQuantity(self, id : int, q = int) -> FurnitureSchema:
        
        furniture = self.getId(id)

        furniture.quantity -= q

        self.db.refresh(furniture)
        self.db.commit()

        return furniture
