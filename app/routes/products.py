from fastapi import APIRouter

from app.external import fetch_products
from app.models import Product

router = APIRouter()


@router.get("/products", response_model=list[Product])
def get_products():
    """מחזיר את כל המוצרים כמו שהתקבלו מה-API החיצוני."""
    return fetch_products()
