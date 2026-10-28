import time

from fastapi import FastAPI, Request

from app.db import insert_log
from app.routes import price, products, rating, search

app = FastAPI(title="Store API")

app.include_router(products.router, prefix="/api")
app.include_router(search.router, prefix="/api")
app.include_router(price.router, prefix="/api")
app.include_router(rating.router, prefix="/api")


@app.middleware("http")
async def log_requests(request: Request, call_next):
    """מודד זמן תגובה ושומר שורת לוג לכל בקשה, כולל שגיאות."""
    start = time.time()
    try:
        response = await call_next(request)
        status_code = response.status_code
    except Exception:
        duration_ms = int((time.time() - start) * 1000)
        insert_log("Request failed with an exception", request.method, request.url.path, duration_ms)
        raise

    duration_ms = int((time.time() - start) * 1000)
    description = "Request completed successfully" if status_code < 400 else f"Request failed with status {status_code}"
    insert_log(description, request.method, request.url.path, duration_ms)
    return response
