from fastapi import APIRouter
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder


from app.conection.connection import sessionDB
from app.schemas.branchSchema import BranchSchema
from app.services.branchService import BranchService


branch_router = APIRouter()
db = sessionDB()
service = BranchService(db)


@branch_router.get('/branches/get', tags=['Branches'], status_code=200, response_model=list[BranchSchema])
def getAll() -> list[BranchSchema]:
    try:
        branches = service.geta()

        return JSONResponse(status_code=200, content=jsonable_encoder(branches))
    
    except Exception as e:
        return JSONResponse(status_code=500, content={'error' : f'Error : {e}'})


@branch_router.get('/branches/get/{id}', tags=['Branches'], status_code=200, response_model=BranchSchema)
def getID(id : int) -> BranchSchema:
    try:
        branch = service.getbyid(id)

        return JSONResponse(status_code=200, content=jsonable_encoder(branch))
    
    except Exception as e:
        return JSONResponse(status_code=500, content={'error' : f'Error: {e}'})
    

@branch_router.post('/branches/add', tags=['Branches'], status_code=201, response_model=BranchSchema)
def add(branch : BranchSchema) -> BranchSchema:
    try:
        branch = service.addbr(branch)

        return JSONResponse(status_code=201, content=jsonable_encoder(branch))
    
    except Exception as e:
        raise Exception(f'Error : {e}')