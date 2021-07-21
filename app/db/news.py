from typing import Dict
from app.db.db_setup import AllNews, async_session, Recommendation
from app.db.db_setup import async_engine as engine
import logging
import os
from sqlalchemy import select, update, desc

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
        await session.execute(query)
        await session.commit()


async def get_twenty_news(n: int):
    logging.info("Fetched last", n, "news")
    async with async_session() as session:
        query = select(AllNews).order_by(desc(AllNews.datetime)).limit((n+1)*20)
        result = await session.execute(query)
        data = []
        for item_row in result.all()[-20:]:
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


async def get_bos_by_id_and_secid(id: int, secid: str):
    logging.info("Getting bos for id:", id, "and secid:", secid)
    async with async_session() as session:
        query = select(Recommendation).where(Recommendation.quote == secid)
        result = await session.execute(query)
        recs  = result.all()
        boses = []
        for item_row in recs:
            item = item_row[0]
            boses.append(item.bos)
        response = {
            "bos": sum(boses)
        }
    return response
