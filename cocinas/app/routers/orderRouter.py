from fastapi import APIRouter
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder

from app.conection.conection import sessionBD
from app.services.orderServices import OrderServices
from app.schemas.order import OrderSchema


order_router = APIRouter()
db = sessionBD()
service = OrderServices(db)


@order_router.post('/order', tags=['Orders'], status_code=201 )
def create(data : OrderSchema):
    try:
        orderdata = service.createOrder(data)

        return JSONResponse(status_code=201, content=jsonable_encoder(orderdata))
    
    except Exception as e:
        return JSONResponse(status_code=500, content={'error' : f'Error: {e}'})


@order_router.get('/order/{id}', tags=['Orders'], status_code=200)
def get(id : int) :
    try:
        order = service.getbyID(id)

        return JSONResponse(status_code=200, content=jsonable_encoder(order)) 
    
    except Exception as e:
        return JSONResponse(status_code=500, content={'error' : f'Error: {e}'})


@order_router.get('/order/user/{id}', tags=['Orders'], status_code=200)
def get(id : int) :
    try:
        order = service.getbyUser(id)

        return JSONResponse(status_code=200, content=jsonable_encoder(order)) 
    
    except Exception as e:
        return JSONResponse(status_code=500, content={'error' : f'Error: {e}'})
        




