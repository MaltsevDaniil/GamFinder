from fastapi import FastAPI
import uvicorn
from users.views import router as users_router
import users.views
from users.settings import SessionLocal

app = FastAPI()
app.include_router(users_router, include_in_schema=True)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
