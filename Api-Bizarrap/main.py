from fastapi import FastAPI
import psycopg2
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

origins = [
    "http://localhost:3000",  # Cambia esta URL según corresponda
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["GET", "POST", "PUT", "DELETE"],
    allow_headers=["*"],
)

conn = psycopg2.connect(
    user="postgres",
    password="bartolita7",
    host="postgres-db",
    port="5432",
    database="postgres"
)


@app.get("/")
async def main():
    return "hola"

@app.get("/music")
async def root():
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM music")
    res = cursor.fetchall()
    cursor.close()
    return res
