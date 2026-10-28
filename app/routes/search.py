from fastapi import APIRouter

from app.external import fetch_products
from app.models import Product

router = APIRouter()


@router.get("/search/{text}", response_model=list[Product])
def search_products(text: str):
    """מחזיר מוצרים שה-title שלהם מכיל את text (case-insensitive)."""
    products = fetch_products()
    return [p for p in products if text.lower() in p.title.lower()]
