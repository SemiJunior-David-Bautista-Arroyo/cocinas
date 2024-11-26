from typing import Optional
from pydantic import BaseModel


class UserSchema(BaseModel):
    id : Optional[int] = None 
    name : str
    lastname : str
    email : str
    cellphone : str
    password_user : str
    address  : Optional[dict] = None


class AddressSchema(BaseModel):

    calle : str
    numero : str
    colonia : str



