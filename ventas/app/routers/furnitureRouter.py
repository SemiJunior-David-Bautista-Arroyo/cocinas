from fastapi import APIRouter
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder

from app.schemas.furnitureSchema import FurnitureSchema
from app.services.furnitureService import FurnitureService
from app.conection.connection import sessionDB


furniture_router = APIRouter()
db = sessionDB()
service = FurnitureService(db)


@furniture_router.post('/furnitures/add', tags=['Furnitures'], response_model=FurnitureSchema, status_code=201)
def add(data : FurnitureSchema) -> FurnitureSchema:
    try:
        furniture = service.addFurniture(data)

        return JSONResponse(status_code=201, content=jsonable_encoder(furniture))
    
    except Exception as e:
        return JSONResponse(status_code=500, content={'error' : f'Error: {e}'})


@furniture_router.get('/furnitures', tags=['Furnitures'], response_model=list[FurnitureSchema], status_code=200)
def getAll() -> list[FurnitureSchema]:
    try:
        furnitures = service.getall()

        return JSONResponse(status_code=200, content=jsonable_encoder(furnitures))
    
    except Exception as e:
        return JSONResponse(status_code=500, content={'error' : f'Error: {e}'})
    

@furniture_router.get('/furnitures/{id}', tags=['Furnitures'], response_model=FurnitureSchema, status_code=200)
def getbyId(id : int) -> FurnitureSchema:
    try:
        furnitures = service.getId(id)

        return JSONResponse(status_code=200, content=jsonable_encoder(furnitures))
    
    except Exception as e:
        return JSONResponse(status_code=500, content={'error' : f'Error: {e}'})


@furniture_router.patch('/furnitures/{id}/{q}', tags=['Furnitures'], status_code=201, response_model = FurnitureSchema )
def updateQ(id : int, q : int) -> FurnitureSchema:
    try:
        furniture = service.updateQuantity(id, q)

        return JSONResponse(status_code=201, content=jsonable_encoder(furniture))

    except Exception as e:
        return JSONResponse(status_code=500, content={'error' : f'Error: {e}'})