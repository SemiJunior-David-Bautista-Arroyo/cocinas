from app.models.purchaseorderModel import PurchaseOrderModel
from app.schemas.purchaseorderSchema import PurchaseOrderSchema
import random

class PurchaseOrderService:

    def __init__(self, db) -> None:
        self.db = db


    def generateOrder(self, order : PurchaseOrderSchema) -> PurchaseOrderSchema:
        
        isbn = f'isbn00{random.randint(0,2610)}'
        orderdict = order.__dict__
        orderdict['isbn'] = isbn
        no = PurchaseOrderModel(**orderdict)

        self.db.add(no)
        self.db.commit()    
        self.db.refresh(no)    
        self.db.close()

        return no


    def getorders(self) -> list[PurchaseOrderSchema]:

        purchaseorders = self.db.query(PurchaseOrderModel).all()

        return purchaseorders



