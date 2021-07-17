from typing import Dict
from app.db.db_setup import Kommersant
import logging
import os
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy import select, or_
from sqlalchemy.orm import sessionmaker
import datetime

engine = create_async_engine(
    os.environ.get('PostgresDB'), echo=True,
)
async_session = sessionmaker(
    engine, expire_on_commit=False, class_=AsyncSession
)


async def get_all_kommersant_news():
    logging.info("Kommersant requested")
    async with async_session() as session:
        query = select(Kommersant)
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
        response = {
            "data": data,
        }
    return response


async def get_kommersant_news_by_rubric(rubric: str):
    logging.info("Kommersant requested")
    async with async_session() as session:
        query = select(Kommersant).where(Kommersant.rubric.any(rubric))
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
        response = {
            "data": data,
        }
    return response


async def get_kommersant_record_by_id(id: int):
    logging.info("Kommersant by id requested")
    async with async_session() as session:
        query = select(Kommersant).where(Kommersant.id == id)
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
        response = {
            "data": data,
        }
    return response
