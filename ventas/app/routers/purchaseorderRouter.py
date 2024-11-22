from fastapi import APIRouter
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder

from app.conection.connection import sessionDB
from app.services.purchaseorderService import PurchaseOrderService
from app.schemas.purchaseorderSchema import PurchaseOrderSchema


purchase_router = APIRouter()
db = sessionDB()
service = PurchaseOrderService(db)


@purchase_router.post('/purchases', tags=['Purchases'], status_code=201, response_model=PurchaseOrderSchema)
def add(data : PurchaseOrderSchema) -> PurchaseOrderSchema:
    try:
        order = service.generateOrder(data)

        return JSONResponse(status_code=201, content=jsonable_encoder(order))

    except Exception as e:

        return JSONResponse(status_code=500, content={'error' : f'error: {e}'})


@purchase_router.get('/purchases/get', tags=['Purchases'], status_code=200, response_model=list[PurchaseOrderSchema])
def get() -> list[PurchaseOrderSchema]:
    try:
        purchases = service.getorders()

        return JSONResponse(status_code=200, content=jsonable_encoder(purchases))
    
    except Exception as e:
        raise Exception(f'error : {e}')


