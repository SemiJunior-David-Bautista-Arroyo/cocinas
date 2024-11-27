import random
from datetime import datetime

from app.models.paymentorderModel import PaymentOrderModel
from app.models.purchaseorderModel import PurchaseOrderModel
from app.models.furnitureModel import FurnitureModel
from app.models.branchModel import BranchModel
from app.schemas.paymentorderSchema import  PaymentOrderSchema
from app.services.furnitureService import FurnitureService

class PaymentOrderService:

    def __init__(self, db) -> None:
        self.db = db


    def generatePayment(self, data : PaymentOrderSchema, branch : int) -> PaymentOrderSchema:

        isbn = f'isbn000{random.randint(0,2610)}'
        
        PurchaseOrder = self.db.query(PurchaseOrderModel).filter(PurchaseOrderModel.id == data.purchase_order_id).first()
        Furniture = self.db.query(FurnitureModel).filter(FurnitureModel.id == PurchaseOrder.furniture_id).first()

        branch = self.db.query(BranchModel).filter(BranchModel.id == branch).first()

        order_quantity = PurchaseOrder.quantity
        furniture_price = Furniture.price

        total = order_quantity * furniture_price

        datadict = data.__dict__

        datadict['isbn'] = isbn

        datadict['total'] = total

        npo = PaymentOrderModel(**datadict)

        FurnitureService(self.db).updateQuantity(PurchaseOrder.id, order_quantity)

        self.db.add(npo)
        self.db.commit()
        self.db.refresh(npo)

        obj = {
            'isbn' : npo.isbn,
            'furniture' : Furniture.name,
            'quantity' : order_quantity,
            'total' : npo.total,
            'branch' : branch.branchname,
            'order_date' : datetime.now()
        } 

        self.db.close()

        return obj
    


    def dailyReport(self) :

        ventas = self.db.query(PaymentOrderModel).all()

        totalventas = len(ventas)
        dailyTotal = 0

        for venta in ventas:
            dailyTotal += venta.total

        dailyInfo ={
            'Totaldailysales' : totalventas,
            'dailytotal' : dailyTotal,
            'sales' : [x for x in ventas]
        }
        
        return dailyInfo

        


