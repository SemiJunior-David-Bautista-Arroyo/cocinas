from typing import Optional
from pydantic import BaseModel


class FurnitureSchema(BaseModel):
    
    id : Optional[int] = None
     
    name : str
    description : str
    quantity : int
    price : float