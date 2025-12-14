from fastapi import FastAPI
import psycopg2
import os

app = FastAPI()

DB_CONFIG = {
    "host": os.getenv("DB_HOST", "db"),
    "dbname": os.getenv("DB_NAME", "appdb"),
    "user": os.getenv("DB_USER", "appuser"),
    "password": os.getenv("DB_PASSWORD", "strongpassword")
}

@app.get("/items")
def get_items():
    conn = psycopg2.connect(**DB_CONFIG)
    cur = conn.cursor()
    cur.execute("SELECT name FROM items;")
    rows = cur.fetchall()
    cur.close()
    conn.close()
    return [{"name": r[0]} for r in rows]