from typing import Optional
from pydantic import BaseModel


class BranchSchema(BaseModel):

    id : Optional[int] = None
    branchname : str
    address : dict

