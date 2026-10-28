# Store API

REST API ב-FastAPI שמחזיר מידע על מוצרים מתוך [fakestoreapi.com](https://fakestoreapi.com),
עם תיעוד כל בקשה בטבלת `logs` ב-MySQL.

## הרצה

```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt

cp .env.example .env   # ולמלא סיסמת DB אמיתית
docker compose up -d   # מרים MySQL + יוצר logs_db ו-logs

uvicorn app.main:app --reload --port 4000
```

## Routes

| Method | Route | תיאור |
|---|---|---|
| GET | `/api/products` | כל 20 המוצרים |
| GET | `/api/search/{text}` | מוצרים שה-title שלהם מכיל text (לא רגיש לאותיות) |
| GET | `/api/price/{max}` | מוצרים עם price <= max |
| GET | `/api/rating/{min}` | מוצרים עם rating.rate >= min |

## תיעוד API
Swagger: http://localhost:4000/docs

## Postman
`postman_collection.json` - ייבוא ישיר ל-Postman, או:
```bash
postman collection run postman_collection.json
```
