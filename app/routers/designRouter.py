from fastapi import APIRouter
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder

from typing import List

from app.schemas.design import DesignSchema
from app.services.designService import DesignService
from app.conection.conection import sessionBD


design_router = APIRouter()
db = sessionBD()
service = DesignService(db)


@design_router.get('/design/get_all', tags=['Design'], response_model=List[DesignSchema], status_code=200)
def getall() -> List[DesignSchema]:
    try:
        designs = service.getdesign()
        if designs is None:
            return JSONResponse(status_code=404, content={'error' : 'Any design was found'})

        return JSONResponse(status_code=200, content=jsonable_encoder(designs))
    
    except Exception as e:

        return JSONResponse(status_code=500, content={'error' : f'Error: {e}' })


@design_router.get('/design/get/{id}', tags=['Design'], response_model=DesignSchema, status_code=200)
def getbyId(id : int):
    try:
        design = service.getbyId(id)
        if design is None:
            return JSONResponse(status_code=404, content={'error' : 'Any design id: {id} was found'})
        
        return JSONResponse(status_code=200, content=jsonable_encoder(design))
    
    except Exception as e:
        return JSONResponse(status_code=500, content={'error' : f'Error : {e}'})


@design_router.post('/design/add', tags=['Design'], response_model=dict, status_code=201 )
def addDesign(data: DesignSchema) -> dict:
    try:
        design = service.addDesign(data)
        return JSONResponse(status_code=201, content=jsonable_encoder(design))
    
    except Exception as e:
        
        return JSONResponse(status_code=500, content={'error' : f'Error: {e}'})


@design_router.put('/design/edit/{id}', tags=['Design'], response_model=dict, status_code=201)
def updateDesign(data : DesignSchema) -> dict:
    try:
        service.updatedesign(data)
        return JSONResponse(status_code=201, content={'message' : 'Design was updated succesfully'})
    
    except Exception as e:
        return JSONResponse(status_code=500, content={'error' : f'Error: {e}'})
    

@design_router.delete('/design/delete/{id}', tags=['Design'],response_model=dict ,status_code=201)
def deleteDesign(id : int) -> dict:
    try:
        service.deletedesign(id)
        return JSONResponse(status_code=201, content={'message' : 'Design was deleted succesfully'})

    except Exception as e:
        return JSONResponse(status_code=500, content={'error' : f'Error: {e}'})
    

@design_router.get('/design/price/{id}/{quantity}', tags=['Design'], response_model=float, status_code=200)
def getprice(id : int, quantity : int):
    try:
        designPrice = service.designPrice(id, quantity)
        return JSONResponse(status_code=200, content=jsonable_encoder(designPrice))
    
    except Exception as e:
        return JSONResponse(status_code=500, content={'error' : f'Error: {e}'})

        

