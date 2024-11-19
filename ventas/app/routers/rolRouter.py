from fastapi import APIRouter
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse

from app.schemas.rolSchema import RolSchema
from app.services.rolService import RolService
from app.conection.connection import sessionDB


rol_router = APIRouter()
db = sessionDB()
service = RolService(db)


@rol_router.get('/rols', tags=['Roles'], status_code=200, response_model=list[RolSchema])
def get():
    try:
        rols = service.getall()

        return JSONResponse(status_code=200, content=jsonable_encoder(rols))
    
    except Exception as e:
        return JSONResponse(status_code=500, content={'error' : f'Error: {e}'})
    

@rol_router.get('/rol/{id}', tags=['Roles'], status_code=200, response_model=RolSchema)
def getId(id : int):
    try:
        rol = service.getbyId(id)
        
        return JSONResponse(status_code=200, content=jsonable_encoder(rol))
    
    except Exception as e:
        return JSONResponse(status_code=500, content={'error' : f'Error: {e}'})
    

@rol_router.post('/rols/add', tags=['Roles'], status_code=201, response_model=RolSchema)
def add(data : RolSchema):
    try:
        nr = service.addRol(data)

        return JSONResponse(status_code=200, content=jsonable_encoder(nr))
    
    except Exception as e:
        return JSONResponse(status_code=500, content={'error' : f'Error: {e}'})






