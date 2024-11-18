import random
from datetime import date, timedelta

from app.models.orderModel import OrderModel
from app.schemas.order import OrderSchema
from app.models.kitchenModel import KitchenModel
from app.models.materialModel import MaterialModel
from app.models.designModel import DesignModel
from app.models.userModel import UserModel
from app.models.installerModel import InstallerModel


class OrderServices:
    
    def __init__(self, db):
        self.db = db

    
    def getbyID(self, id : int) -> OrderSchema:
        order = self.db.query(OrderModel).filter(OrderModel.id == id).first()

        if order is None:
            raise Exception('Any order was found')
        
        return order


    def getkitchenPrice(self, id : int) -> float:

        kitchen = self.db.query(KitchenModel).filter(KitchenModel.id == id).first()
        material = self.db.query(MaterialModel.price).filter(MaterialModel.id == kitchen.material_id).first()
        design = self.db.query(DesignModel.price).filter(DesignModel.id == kitchen.design_id).first()

        w = kitchen.sizes['w']
        h = kitchen.sizes['h']

        sizem2 = w * h
        dp = sizem2 - int(sizem2)

        if dp >= 0.001 : 
            fs = int(sizem2) + 1
        
        fs = int(sizem2)

        material_price = material[0] * fs

        total = material_price + design[0]

        return total


    def createOrder(self, data : OrderSchema): 
        
        kitchenPrice = self.getkitchenPrice(data.kitchen_id)
        
        kitchen = (
        self.db.query(KitchenModel, MaterialModel.material, DesignModel.design)
        .join(MaterialModel, KitchenModel.material_id == MaterialModel.id)
        .join(DesignModel, KitchenModel.design_id == DesignModel.id)
        .filter(KitchenModel.id == data.kitchen_id)
        .first()
        )
        
        user = self.db.query(UserModel.name).filter(UserModel.id == data.user_id).first()
        installer = self.db.query(InstallerModel.name).filter(InstallerModel.id == data.installer_id).first()

        dataDict = data.__dict__

        isbn = f'isbn00{random.randint(0,2610)}'

        delivery = date.today() + timedelta(days=10)

        dataDict['isbn'] = isbn
        dataDict['total'] = kitchenPrice
        dataDict['delivery_date'] = delivery

        new_order = OrderModel(**dataDict)
        self.db.add(new_order)
        self.db.commit()
        self.db.refresh(new_order)

        orden = {
            "isbn" : new_order.isbn,
            "kitchen" : {
                "material" : kitchen.material,
                "design" : kitchen.design,
            },
            "total" : new_order.total,
            "delivery_date" : new_order.delivery_date,
            "user" : user[0],
            "installer" : installer[0],
        }

        return orden
    
    
    def getbyUser(self, userId : int):
        
        ordenes = (
        self.db.query(
            OrderModel,
            KitchenModel,
            MaterialModel.material,
            DesignModel.design,
            UserModel.name.label("user_name"),
            InstallerModel.name.label("installer_name")
        )
        .join(KitchenModel, OrderModel.kitchen_id == KitchenModel.id)
        .join(MaterialModel, KitchenModel.material_id == MaterialModel.id)
        .join(DesignModel, KitchenModel.design_id == DesignModel.id)
        .join(UserModel, OrderModel.user_id == UserModel.id)
        .join(InstallerModel, OrderModel.installer_id == InstallerModel.id)
        .filter(OrderModel.user_id == userId)
        .all()
        )

        result = []
        for order, kitchen, material, design, user_name, installer_name in ordenes:
            result.append({
                "isbn": order.isbn,
                "kitchen": {
                    "material": material,
                    "design": design,
                    "sizes": kitchen.sizes,
                },
                "total": order.total,
                "delivery_date": order.delivery_date,
                "user": user_name,
                "installer": installer_name,
            })
         
        return result


