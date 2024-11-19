from fastapi import APIRouter
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder

from app.schemas.kitchen import KitchenSchema
from app.services.kitchenService import kitchenService
from app.conection.conection import sessionBD


kitchen_router = APIRouter()
db = sessionBD()
service = kitchenService(db)


@kitchen_router.post('/kitchen/add', tags=['Kitchen'], response_model=KitchenSchema,status_code=201)
def create(kitchen: KitchenSchema) -> KitchenSchema:
    try:
        nk = service.createkitchen(kitchen)

        if kitchen:
            return JSONResponse(status_code=201, content=jsonable_encoder(nk))

        return JSONResponse(status_code=400, content={'error' : "Can't create the kitchen"})

    except Exception as e:
        return JSONResponse(status_code=500, content={'error' : f"Error: {e}"})


@kitchen_router.get('/kitchen/getbyUser/{usrId}', tags=['Kitchen'], response_model=KitchenSchema, status_code=200)
def get(usrId : int) -> KitchenSchema:
    try:
        k = service.getbyUser(usrId)
        if k:
            return JSONResponse(status_code=201, content=jsonable_encoder(k))
        return JSONResponse(status_code=404, content={'error' : 'Any kitchend was found'})

    except Exception as e:
        return JSONResponse(status_code=500, content={'error' : f"Error: {e}"})
