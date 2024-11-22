import random
from datetime import datetime

from app.models.paymentorderModel import PaymentOrderModel
from app.models.purchaseorderModel import PurchaseOrderModel
from app.models.furnitureModel import FurnitureModel
from app.models.branchModel import BranchModel
from app.schemas.paymentorderSchema import  PaymentOrderSchema

class PaymentOrderService:

    def __init__(self, db) -> None:
        self.db = db


    def generatePayment(self, data : PaymentOrderSchema, branch : int) -> PaymentOrderSchema:

        isbn = f'isbn000{random.randint(0,2610)}'

        result = (
            self.db.query(
                PurchaseOrderModel.quantity.label('purchase_order_quantity'),
                FurnitureModel.price.label('furniture_price'),
                FurnitureModel.name.label('furniture_name'),
            )
            .join(PurchaseOrderModel, PaymentOrderModel.purchase_order_id == PurchaseOrderModel.id)
            .join(FurnitureModel, FurnitureModel.id == PurchaseOrderModel.furniture_id)
            .first()
        )

        branch = self.db.query(BranchModel).filter(BranchModel.id == branch).first()

        order_quantity = result.purchase_order_quantity
        furniture_price = result.furniture_price

        total = order_quantity * furniture_price

        datadict = data.__dict__

        datadict['isbn'] = isbn

        datadict['total'] = total

        npo = PaymentOrderModel(**datadict)

        self.db.add(npo)
        self.db.commit()
        self.db.refresh(npo)

        obj = {
            'isbn' : npo.isbn,
            'furniture' : result.furniture_name,
            'total' : npo.total,
            'branch' : branch.branchname,
            'order_date' : datetime.now()
        } 

        self.db.close()

        return obj

        


