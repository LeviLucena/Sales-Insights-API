from pydantic import BaseModel
from datetime import date

class SaleBase(BaseModel):
    product_name: str
    quantity: int
    sale_date: date

class Sale(SaleBase):
    id: int

    class Config:
        orm_mode = True
