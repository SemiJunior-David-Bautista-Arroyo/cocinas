from typing import Optional
from pydantic import BaseModel


class InstallerSchema(BaseModel):

    id : Optional[int] = None
    name : str
    lastname : str


