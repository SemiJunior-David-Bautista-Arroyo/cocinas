from app.models.kitchenModel import KitchenModel
from app.schemas.kitchen import KitchenSchema
from app.factories.factories import Factory, MODEL_MAPPING


class kitchenService:

    def __init__(self,db):
        self.db = db

    
    def createkitchen(self, data : KitchenSchema):

        nd = Factory.create_instance(data, MODEL_MAPPING)
        
        self.db.add(nd)
        self.db.commit()
        self.db.refresh(nd)

        return nd

    
    def getbyUser(self, userId : int) -> KitchenSchema:
        kitchen = self.db.query(KitchenModel).filter(KitchenModel.user_id == userId).first()
        
        if kitchen: return kitchen

        return False
    



