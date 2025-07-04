from sqlalchemy.orm import Session
from sqlalchemy import func, desc, text
from datetime import datetime, timedelta
from app import models

def get_top_products_last_month(db: Session):
    last_month = datetime.now() - timedelta(days=30)

    products = (
        db.query(
            models.Product.name,
            func.sum(models.Sale.quantity).label('total_quantity')
        )
        .join(models.Sale, models.Product.id == models.Sale.product_id)
        # Usa texto para comparar corretamente no SQLite
        .filter(text(f"date(sale_date) >= date('{last_month.date()}')"))
        .group_by(models.Product.name)
        .order_by(desc('total_quantity'))
        .limit(5)
        .all()
    )

    return [{"product_name": p[0], "total_quantity": p[1]} for p in products]
