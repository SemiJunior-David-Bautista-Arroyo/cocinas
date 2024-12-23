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


@payment_router.get('/payments/report', tags=['Payment Order'], status_code=200, response_model=list)
def dailyReport() -> list:
    try:
        report = service.dailyReport()

        return JSONResponse(status_code=200, content=jsonable_encoder(report))
    
    except Exception as e:
        raise Exception(f'Error : {e}')