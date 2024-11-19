from typing import List

from app.models.materialModel import MaterialModel
from app.schemas.material import MaterialSchema
from app.factories.factories import Factory, MODEL_MAPPING


class MaterialService:

    def __init__(self, db): 
        self.db  = db


    def get_materials(self) -> List[MaterialSchema]:

        materials = self.db.query(MaterialModel).all()
        self.db.close()

        return materials


    def getbyId(self, id : int ) -> MaterialSchema:

        material = self.db.query(MaterialModel).filter(MaterialModel.id == id).first()

        return material
    

    def addMaterial(self, data : MaterialSchema):
        try:
            newMaterial = Factory.create_instance(data, MODEL_MAPPING)
            
            self.db.add(newMaterial)
            self.db.commit()
            self.db.refresh(newMaterial)
            self.db.close()
            return newMaterial
        except Exception as e:
            raise Exception ('An unexpected error ocurred')
    
    
    def editMaterial(self, id : int, data : MaterialSchema) -> MaterialSchema:

        material = self.getbyId(id) 

        if material is None:
            raise Exception ("Material don't exists")
            
        material.material = data.material
        material.price = data.price

        self.db.commit()
        self.db.refresh(material)

        return material
    
    
    def deleteMaterial(self, id : int):

        material = self.getbyId(id)
        
        if material is None:
            raise Exception ("Material don't exists")

        self.db.delete(material)
        self.db.commit()

        return

    # recibir cantidad por metro cuadrado
    def materialPrice(self, id : int, quantity : int) -> float:

        material = self.getbyId(id)
        if material is None:
            raise Exception("MAterial was'nt found")

        materialprice =  material.price * quantity

        return materialprice

