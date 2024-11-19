from fastapi import APIRouter
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder

from app.schemas.installer import InstallerSchema
from app.services.installerService import InstallerService
from app.conection.conection import sessionBD


installer_router = APIRouter()
db = sessionBD()
service = InstallerService(db)


@installer_router.get('/installers', tags=['Installer'], response_model=list[InstallerSchema], status_code=201)
def getall():
    try:
        installers = service.getInstallers()
        
        return JSONResponse(status_code=200, content=jsonable_encoder(installers))
    
    except Exception as e:
        return JSONResponse(status_code=500, content={'message' : f'Error: {e}'})


@installer_router.get('/installers/{id}', tags=['Installer'], response_model=list[InstallerSchema], status_code=201)
def getId(id : int):
    try:
        installers = service.getbyID(id)
        return JSONResponse(status_code=200, content=jsonable_encoder(installers))
    
    except Exception as e:
        return JSONResponse(status_code=500, content={'message' : f'Error: {e}'})
    

@installer_router.post('/installers/add', tags=['Installer'], response_model=InstallerSchema, status_code=201)
def create(data : InstallerSchema):
    try:
        installer = service.createinstaller(data)

        return JSONResponse(status_code=201, content=jsonable_encoder(installer))
    
    except Exception as e:
        return JSONResponse(status_code=500, content={'message' : f'Error: {e}'})

