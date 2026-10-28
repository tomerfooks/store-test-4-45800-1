import os

import mysql.connector
from dotenv import load_dotenv

load_dotenv()


def _connection():
    return mysql.connector.connect(
        host=os.getenv("DB_HOST"),
        port=os.getenv("DB_PORT"),
        user=os.getenv("DB_USER"),
        password=os.getenv("DB_PASSWORD"),
        database=os.getenv("DB_NAME"),
    )


def insert_log(description: str, method: str, route: str, duration_ms: int) -> None:
    """שומר שורת לוג בטבלת logs."""
    conn = _connection()
    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO logs (description, method, route, duration_ms) VALUES (%s, %s, %s, %s)",
        (description, method, route, duration_ms),
    )
    conn.commit()
    cursor.close()
    conn.close()
