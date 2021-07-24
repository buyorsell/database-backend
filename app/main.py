from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List
from sqlalchemy.orm.exc import NoResultFound

from app.db.news import get_all_news, get_record_by_id, get_news_by_rubric, mutate_news_coords, get_twenty_news, get_bos_by_id_and_secid
from app.db.moex import get_all_stocks_by_secid
from app.db.tickers import get_tickers
from app.db.misc import get_topics, get_entities

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


@app.get("/news")
async def fetch_all_news(id: int = None, rubric: str = None, page: int = None, secid: str = None):
	if page != None:
		return await get_twenty_news(page)
	elif id != None and secid != None:
		return await get_bos_by_id_and_secid(id, secid)
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

@app.get("/stock/{secid}")
async def serve_stock(secid: str):
	return await get_all_stocks_by_secid(secid)

@app.get("/entities")
async def serve_entities():
	return await get_entities()

@app.get("/topics")
async def serve_topics():
	return await get_topics()

