from typing import Optional
from pydantic import BaseModel
from datetime import datetime

class PurchaseOrderSchema(BaseModel):

    id : Optional[int] = None
    isbn : Optional[str] = None
    furniture_id : int
    quantity : int
    user_id : int
    delivery_date : datetime
    


