from typing import Optional
from pydantic import BaseModel, Field, confloat


class KitchenSchema(BaseModel):

    id : Optional[int] = None
    sizes : dict
    design_id : int
    material_id : int
    user_id : int
    



