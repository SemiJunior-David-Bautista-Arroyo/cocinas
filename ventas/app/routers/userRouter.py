from fastapi import APIRouter
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder

from app.conection.connection import sessionDB
from app.schemas.userSchema import UserSchema
from app.services.userService import UserService


user_router = APIRouter()
db = sessionDB()
service = UserService(db)


@user_router.post('/users/add', tags=['Users'], status_code=201, response_model=UserSchema)
def adduser(data : UserSchema) -> UserSchema:
    try:
        usr = service.addUser(data)

        return JSONResponse(status_code=201, content=jsonable_encoder(usr))

    except Exception as e:
        return JSONResponse(status_code=500, content={'error' : f'Error: {e}'})


@user_router.get('/users/get_all', tags=['Users'], status_code=201, response_model=list[UserSchema])
def getAll() -> list[UserSchema]:
    try:
        usr = service.getall()

        return JSONResponse(status_code=201, content=jsonable_encoder(usr))

    except Exception as e:
        return JSONResponse(status_code=500, content={'error' : f'Error: {e}'})


@user_router.get('/users/{username}/{pasword}', tags=['Users'], status_code=200)
def verifyUser(username : str, pasword : str):
    try:
        usr = service.verifyuser(username, pasword)

        return JSONResponse(status_code=200, content=jsonable_encoder(usr))
    
    except Exception as e:
        return JSONResponse(status_code=500, content={'error' : f'Error: {e}'})

