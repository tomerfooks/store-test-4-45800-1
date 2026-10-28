import requests

from app.models import Product

FAKESTORE_URL = "https://fakestoreapi.com/products"


def fetch_products() -> list[Product]:
    """שולף את כל המוצרים מה-API החיצוני."""
    response = requests.get(FAKESTORE_URL, timeout=10)
    response.raise_for_status()
    return [Product(**item) for item in response.json()]
