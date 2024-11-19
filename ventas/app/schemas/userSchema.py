from typing import Optional
from pydantic import BaseModel

class UserSchema(BaseModel):

    id : Optional[int] = None

    name : str
    lastname : str
    username : str
    cellphone : str
    address : dict
    password_user : str
    rol_id : int