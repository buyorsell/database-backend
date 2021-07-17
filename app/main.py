from typing import Optional

from fastapi import FastAPI

from app.db.commersant import get_all_kommersant_news, get_kommersant_record_by_id, get_kommersant_news_by_rubric

app = FastAPI()


@app.get("/")
async def read_root():
    return {"Hello": "From Our DB!"}


@app.get("/commersant")
async def fetch_all_commersant_news(id: int = -1, rubric: str = None):
	if id != -1:
		return await get_kommersant_record_by_id(id)
	elif rubric != None:
		return await get_kommersant_news_by_rubric(rubric)
	else:
		return await get_all_kommersant_news()
