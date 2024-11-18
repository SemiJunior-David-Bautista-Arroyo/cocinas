from typing import List
from app.models.designModel import DesignModel
from app.schemas.design import DesignSchema
from app.factories.factories import Factory, MODEL_MAPPING


class DesignService:

    def __init__(self, db):
        self.db = db


    def getdesign(self) -> List[DesignSchema] :

        designs = self.db.query(DesignModel).all()

        return designs 
    

    def getbyId(self, id : int) -> DesignSchema:

        design = self.db.query(DesignModel).filter(DesignModel.id == id).first()

        if design is None:
            raise Exception("Error any design found")
        
        return design
    

    def addDesign(self, data : DesignSchema):

        newde = Factory.create_instance(data, MODEL_MAPPING)


        self.db.add(newde)
        self.db.commit()
        self.db.refresh(newde)
        self.db.close()
        return newde

    
    def updatedesign(self, id : int, data : DesignSchema) -> DesignSchema:

        design = self.getbyId(id)

        if design is None:
            raise Exception("Any design was found")
        
        design.id = data.id
        design.design = data.design
        design.price = data.price

        self.db.commit()
        self.db.refresh(design)
        self.db.close()

        return design
    

    def deletedesign(self, id : int):

        design = self.getbyId(id)
        if design is None:
            raise Exception("Any desgin was found")
        
        self.db.delete(design)
        self.db.commit()
        self.db.close()
        return


    # Recibir cantidad por metro cuadrado
    def designPrice(self, id : int, quantity : int) -> float:

        design = self.getbyId(id)

        if design is None:
            raise Exception("Any desgin was found")

        designprice = design.price * quantity

        return designprice