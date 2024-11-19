from typing import Optional
from pydantic import BaseModel


class RolSchema(BaseModel):

    id : Optional[int] = None
    rol : str

