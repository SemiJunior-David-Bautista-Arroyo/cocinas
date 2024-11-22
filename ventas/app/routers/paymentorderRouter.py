from fastapi import APIRouter
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder

from app.conection.connection import sessionDB
from app.schemas.paymentorderSchema import PaymentOrderSchema
from app.services.paymentorderService import PaymentOrderService


payment_router = APIRouter()
db = sessionDB()
service = PaymentOrderService(db)


@payment_router.post('/payments/{branch}', tags=['Payment Order'], status_code=201)
def addPayment(branch : int, data : PaymentOrderSchema):
    try:
        paymentOrder = service.generatePayment(data, branch)

        return JSONResponse(status_code=201, content=jsonable_encoder(paymentOrder))

    except Exception as e:
        return JSONResponse(status_code=500, content={'error' : f'Error: {e}'})

