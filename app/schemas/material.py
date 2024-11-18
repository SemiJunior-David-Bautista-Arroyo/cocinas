from typing import Optional
from pydantic import BaseModel


class MaterialSchema(BaseModel):
    id : Optional[int] = None
    material : str
    price : float


