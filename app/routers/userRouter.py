from fastapi import APIRouter
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder

from app.schemas.user import UserSchema
from app.services.userService import userService
from app.conection.conection import sessionBD


user_router = APIRouter()
db = sessionBD()
service = userService(db)


@user_router.get('/user/get/{id}', tags=['User'], status_code=200, response_model=UserSchema)
def getuser(id : int) -> UserSchema:
    try:
        user = service.getclientbyId(id)
        if user is not None:
            return JSONResponse(status_code=200, content=jsonable_encoder(user))
        
        return JSONResponse(status_code=404, content={'error': 'Any user found'})
    
    except Exception as e:
        return JSONResponse(status_code=500, content={'error' : f'Error: {e}'})
    

@user_router.post('/user/add', tags=['User'], status_code=201, response_model=UserSchema)
def addUser(data : UserSchema):
    try:
        user = service.registerClient(data)
        return JSONResponse(status_code=201, content=jsonable_encoder(user))

    except Exception as e:
        return JSONResponse(status_code=500, content={'error' : f'Error: {e}'})


@user_router.get('/user/verify', tags=['User'], status_code=200)
def verify(username : str, password : str):
    try:
        user = service.verifyClient(username, password)
        return JSONResponse(status_code=200, content=jsonable_encoder(user))

    except Exception as e:
        return JSONResponse(status_code=500, content={'error' : f'Error: {e}'})
