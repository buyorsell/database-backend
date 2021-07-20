from typing import Dict
from app.db.db_setup import AllNews, async_session
from app.db.db_setup import async_engine as engine
import logging
import os
from sqlalchemy import select, update

import datetime



async def get_all_news():
    logging.info("Kommersant requested")
    async with async_session() as session:
        query = select(AllNews)
        result = await session.execute(query)
        data = []
        for item_row in result.all():
            item = item_row[0]
            item_processed = {
                "id": item.id,
                "datetime": datetime.datetime.isoformat(item.datetime),
                "rubric": item.rubric,
                "link": item.link,
                "title": item.title,
                "text": item.text,
                "locs": item.locs,
                "pers": item.pers,
                "orgs": item.orgs,
                "x": item.x,
                "y": item.y,
                "highlights": item.highlights,
                "tokens": item.tokens,
            }
            data.append(item_processed)
        response = data
    return response


async def get_news_by_rubric(rubric: str):
    logging.info("News by rubric requested")
    async with async_session() as session:
        query = select(AllNews).where(AllNews.rubric.any(rubric))
        result = await session.execute(query)
        data = []
        for item_row in result.all():
            item = item_row[0]
            item_processed = {
                "id": item.id,
                "datetime": datetime.datetime.isoformat(item.datetime),
                "rubric": item.rubric,
                "link": item.link,
                "title": item.title,
                "text": item.text,
                "locs": item.locs,
                "pers": item.pers,
                "orgs": item.orgs,
                "x": item.x,
                "y": item.y,
                "highlights": item.highlights,
                "tokens": item.tokens,
            }
            data.append(item_processed)
        response = data
    return response


async def get_record_by_id(id: int):
    logging.info("News by id requested")
    async with async_session() as session:
        query = select(AllNews).where(AllNews.id == id)
        result = await session.execute(query)
        data = []
        for item_row in result.all():
            item = item_row[0]
            item_processed = {
                "id": item.id,
                "datetime": datetime.datetime.isoformat(item.datetime),
                "rubric": item.rubric,
                "link": item.link,
                "title": item.title,
                "text": item.text,
                "locs": item.locs,
                "pers": item.pers,
                "orgs": item.orgs,
                "x": item.x,
                "y": item.y,
                "highlights": item.highlights,
                "tokens": item.tokens,
            }
            data.append(item_processed)
        response = data
    return response


async def mutate_news_coords(id: int, x: float, y: float):
	logging.info("News entry: mutate coords")
	async with async_session() as session:
		query = update(AllNews).where(AllNews.id == id).values(x=x, y=y)
		print(query)
		await session.execute(query)
		await session.commit()

