from sqlalchemy.orm import Session
from sqlalchemy import func, desc
from datetime import datetime, timedelta
from app import models

def get_top_products_last_month(db: Session):
    last_month = datetime.now() - timedelta(days=30)
    products = (
        db.query(models.Sale.product_name, func.sum(models.Sale.quantity).label('total_quantity'))
        .filter(models.Sale.sale_date >= last_month)
        .group_by(models.Sale.product_name)
        .order_by(desc('total_quantity'))
        .limit(5)
        .all()
    )
    return [{"product_name": p[0], "total_quantity": p[1]} for p in products]

def get_all_sales(db: Session):
    return db.query(models.Sale).all()
