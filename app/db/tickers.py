from app.db.db_setup import Ticker, async_engine, async_session
from sqlalchemy import select, update
from sqlalchemy.orm import sessionmaker
import logging

async def get_tickers():
    logging.info("Tickers requested")
    async with async_session() as session:
        query = select(Ticker)
        result = await session.execute(query)
        data = []
        for item_row in result.all():
            item = item_row[0]
            item_processed = {
                "sec_id": item.sec_id,
                "shortname": item.shortname,
                "bos": item.bos,
            }
            data.append(item_processed)
        response = data
        await session.close()
    return response
