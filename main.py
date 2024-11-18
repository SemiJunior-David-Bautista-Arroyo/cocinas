from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from fastapi.middleware.cors import CORSMiddleware

from app.middlewares.errorhandle import ErrorHandle
from app.routers.userRouter import user_router
from app.routers.designRouter import design_router
from app.routers.kitchenRouter import kitchen_router
from app.routers.materialRouter import material_router
from app.routers.installerRouter import installer_router
from app.routers.orderRouter import order_router


app = FastAPI()
app.title = 'Mueblería Tico Sistema Instalación Cocinas'
app.description = 'First centralized system for the Mueblería Tico company'


app.add_middleware(ErrorHandle)

origins = [
    "http://localhost",
    "http://localhost:5000",
    "http://localhost:8000",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins = origins,
    allow_credentials = True,
    allow_methods = ['*'],
    allow_headers = ['*']
)


app.include_router(user_router)
app.include_router(design_router)
app.include_router(kitchen_router)
app.include_router(material_router)
app.include_router(installer_router)
app.include_router(order_router)


@app.get('/', tags=['home'])
def home():
    return HTMLResponse(
        """
        <div align="center">
            <h1>Mueblerías tico API to make an order of integral kitchen</h1><br>
        </div>
        """)
