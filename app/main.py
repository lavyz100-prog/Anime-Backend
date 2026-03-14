from fastapi import FastAPI

from app.api.v1 import app as routes

app = FastAPI()

app.include_router(routes)


@app.get("/")
async def root():
    return {"message": "Hello World"}
