from typing import Optional
from pydantic import BaseModel


class DesignSchema(BaseModel):
    id : Optional[int] = None
    design : str
    price : float

