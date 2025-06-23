from fastapi import FastAPI
import uvicorn
from users.views import router as users_router
import users.views

app = FastAPI()
app.include_router(users_router, include_in_schema=True)

print("▶️ app.routes:", [r.path for r in app.routes])

@app.get("/")
def gw():
    return {"message": "hw"}

if __name__ == '__main__':
    uvicorn.run("main:app", reload=True)
