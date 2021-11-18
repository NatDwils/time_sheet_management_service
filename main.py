from fastapi import FastAPI
from src.services.services import user


app = FastAPI()
app.include_router(user)

