# main.py
from fastapi import FastAPI
from sqlalchemy import text

from src.core.database import engine

app = FastAPI()


@app.get("/startup")
async def check_db():
    try:
        async with engine.connect() as conn:
            result = await conn.execute(text("SELECT COUNT(*) FROM anime_list"))
            count = result.scalar()
            # Return a dictionary so FastAPI converts it to JSON
            return {"status": "success", "count": count}
    except Exception as e:
        # Return the error details so you can see them in curl
        return {"status": "error", "message": str(e)}
