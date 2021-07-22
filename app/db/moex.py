from app.db.moex_setup import async_session, Stock
from sqlalchemy import select
import datetime
import logging

async def get_all_stocks_by_secid(secid: str):
    logging.info("Requested stock for", secid)
    async with async_session() as session:
        query = select(Stock).where(Stock.secid == secid)
        result = await session.execute(query)
        data = []
        for item_row in result.all():
            item = item_row[0]
            item_processed = {
                "id": item.id,
                "date": datetime.datetime.isoformat(item.date),
                "close": item.close,
                "open": item.open,
                "low": item.low,
                "high": item.high,
                "numtrades": item.numtrades,
                "boardid": item.boardid,
            }
            data.append(item_processed)
        response = data
    return response
