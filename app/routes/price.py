from fastapi import APIRouter

from app.external import fetch_products
from app.models import Product

router = APIRouter()


@router.get("/price/{max}", response_model=list[Product])
def products_under_price(max: float):
    """מחזיר מוצרים שמחירם קטן או שווה ל-max."""
    products = fetch_products()
    return [p for p in products if p.price <= max]
