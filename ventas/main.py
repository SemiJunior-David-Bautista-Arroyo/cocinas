from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from fastapi.encoders import jsonable_encoder
from fastapi.middleware.cors import CORSMiddleware


from app.middlewares.errorHandle import ErrorHandle
from app.routers.rolRouter import rol_router
from app.routers.userRouter import user_router
from app.routers.furnitureRouter import furniture_router
from app.routers.purchaseorderRouter import purchase_router


app = FastAPI()
app.title = "Centralized Tico System"
app.description = "Centralized Tico System"


origins = [
    "http://localhost/",
    "http://localhost:5000",
    "http://localhost:8000",
]


app.add_middleware(ErrorHandle)
app.add_middleware(
    CORSMiddleware,
    allow_origins = origins,
    allow_credentials = True,
    allow_methods = ['*'],
    allow_headers = ['*'],
)


app.include_router(rol_router)
app.include_router(user_router)
app.include_router(furniture_router)
app.include_router(purchase_router)


@app.get('/', tags=['home'])
def home():
    return HTMLResponse(
        """
        <div align="center">
            <h1>Mueblerías tico API of the system</h1><br>
        </div>
        """)
