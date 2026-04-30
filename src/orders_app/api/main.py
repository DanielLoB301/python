from fastapi import FastAPI
from .routers import orders
from fastapi import Depends
from fastapi.security import OAuth2PasswordRequestForm
from .auth import create_access_token


app = FastAPI(title="Orders API")
app.include_router(orders.router)

@app.get("/")
def root():
    return {"message": "API funcionando 🚀"}

app.include_router(orders.router)

@app.post("/token")
def login(form_data: OAuth2PasswordRequestForm = Depends()):
    token = create_access_token({"sub": form_data.username})
    return {"access_token": token, "token_type": "bearer"}