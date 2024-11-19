from fastapi import APIRouter
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder

from typing import List

from app.schemas.material import MaterialSchema
from app.services.materialService import MaterialService
from app.conection.conection import sessionBD


material_router = APIRouter()
db = sessionBD()
service = MaterialService(db)


@material_router.get('/material/get_all', tags=['Materials'], status_code = 200, response_model = List[MaterialSchema])
def getAll() -> List[MaterialSchema]:
    try:
        materials = service.get_materials()

        return JSONResponse(status_code=200, content=jsonable_encoder(materials))
    
    except Exception as e:
        return JSONResponse(status_code=500, content={'error' : f'Error : {e}'})
    
    
@material_router.get('/material/get/{id}', tags=['Materials'], status_code=200, response_model=MaterialSchema)
def getbyId(id : int) -> MaterialSchema:
    try:
        material = service.getbyId(id)

        return JSONResponse(status_code=200, content=jsonable_encoder(material))

    except Exception as e:
        return JSONResponse(status_code=500, content={'error' : f'Error : {e}'})


@material_router.post('/material/add', tags=['Materials'], status_code=201, response_model=MaterialSchema)
def addMaterial(data : MaterialSchema):
    try:
        nmaterial = service.addMaterial(data)

        return JSONResponse(status_code=201, content=jsonable_encoder(nmaterial))
    
    except Exception as e:
        return JSONResponse(status_code=500, content={'error' : f'Error : {e}'})


@material_router.put('/material/edit/{id}', tags=['Materials'], status_code=201, response_model=MaterialSchema)
def edit_Material(id : int, data : MaterialSchema):
    try:
        m = service.editMaterial(id, data)
        return m

    except Exception as e:
        return JSONResponse(status_code=500, content={'error' : f'Error : {e}'})       


@material_router.get('/material/price/{id}/{quantity}', tags=['Materials'],status_code=200, response_model=float)
def material_Price(id : int, quantity : int):
    try:
        price = service.materialPrice(id, quantity)

        return JSONResponse(status_code=201, content=jsonable_encoder(price))

    except Exception as e:
        return JSONResponse(status_code=500, content={'error' : f'Error : {e}'})
    

@material_router.delete('/material/delete/{id}', tags=['Materials'], status_code=200)
def deleteMaterial(id : int):
    try:
        service.deleteMaterial(id)
        
        return JSONResponse(status_code=200, content={'message' : f'Material id:{id} eliminated succesfully'})

    except Exception as e:
        return JSONResponse(status_code=500, content={'error' : f'Error : {e}'})
