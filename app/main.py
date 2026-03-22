from fastapi import FastAPI
from app.routes import sms

app = FastAPI(title="AutoSpend API")

app.include_router(sms.router)