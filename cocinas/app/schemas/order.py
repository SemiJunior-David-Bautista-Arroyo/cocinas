from typing import Optional
from pydantic import BaseModel
from datetime import datetime

class OrderSchema(BaseModel):

    id : Optional[int] = None
    isbn : Optional[str] = None
    kitchen_id : int
    total : Optional[float] = None
    delivery_date : datetime
    user_id : int
    installer_id : float


