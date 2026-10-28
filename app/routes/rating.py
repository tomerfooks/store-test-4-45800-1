from fastapi import APIRouter

from app.external import fetch_products
from app.models import Product

router = APIRouter()


@router.get("/rating/{min}", response_model=list[Product])
def products_above_rating(min: float):
    """מחזיר מוצרים שדירוגם (rating.rate) גדול או שווה ל-min."""
    products = fetch_products()
    return [p for p in products if p.rating.rate >= min]
