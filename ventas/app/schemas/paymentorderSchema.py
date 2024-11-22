from typing import Optional
from pydantic import BaseModel


class PaymentOrderSchema(BaseModel):

    id : Optional[int] = None
    isbn : Optional[str] = None
    purchase_order_id : int
    total : Optional[float] = None

