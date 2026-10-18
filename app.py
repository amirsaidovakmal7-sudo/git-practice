from fastapi import FastAPI
from routers.auth import router as auth_router
from routers.user import user_router

app = FastAPI()
app.include_router(auth_router)
app.include_router(user_router)

app.get("/")
async def root():
    return {"message": "Welcome to my site!"}
