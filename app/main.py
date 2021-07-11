from typing import Optional

from fastapi import FastAPI

from app.db.commersant import get_all_kommersant_news

app = FastAPI()


@app.get("/")
async def read_root():
    return {"Hello": "From Our DB!"}


@app.get("/commersant")
async def fetch_all_commersant_news():
	return await get_all_kommersant_news()
