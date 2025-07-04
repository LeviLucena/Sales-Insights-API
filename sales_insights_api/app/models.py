from sqlalchemy import Column, Integer, String, Date
from app.database import Base

class Sale(Base):
    __tablename__ = "sales"

    id = Column(Integer, primary_key=True, index=True)
    product_name = Column(String, index=True)
    quantity = Column(Integer)
    sale_date = Column(Date)
