from fastapi import FastAPI
from .routers import orders

app = FastAPI(title="Orders API")

app.include_router(orders.router)