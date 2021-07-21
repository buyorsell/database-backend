from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List
from sqlalchemy.orm.exc import NoResultFound

from app.db.news import get_all_news, get_record_by_id, get_news_by_rubric, mutate_news_coords, get_twenty_news
from app.db.tickers import get_tickers

app = FastAPI()


class NewsCoords(BaseModel):
	id: int
	x: float 
	y: float 

class NewsModel(BaseModel):
	id: int
	datetime: str
	rubric: List[str]
	link: str
	title: str
	text: str
	locs: List[str]
	pers: List[str]
	orgs: List[str]
	x: float 
	y: float 
	highlights: str
	tokens: List[str]


@app.get("/")
async def read_root():
    return {"Hello": "From Our DB!"}


@app.get("/news", response_model=List[NewsModel])
async def fetch_all_news(id: int = None, rubric: str = None, page: int = None):
	if page != None:
		return await get_twenty_news(page)
	elif id != None:
		return await get_record_by_id(id)
	elif rubric != None:
		return await get_news_by_rubric(rubric)
	else:
		return await get_all_news()


@app.post("/news", responses={200: {"message": "OK"}, 404: {"status": "Not Found", "message": "Not Found"}})
async def change_news_x_y_by_id(item: NewsCoords):
	try:
		return await mutate_news_coords(item.id, item.x, item.y)
	except NoResultFound:
		raise HTTPException(status_code=404, detail="Item not found")


@app.get("/tickers")
async def serve_tickers():
	return await get_tickers()