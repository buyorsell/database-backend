from app.db.db_setup import Topic, Entity, async_session
from sqlalchemy import select
import logging

async def get_topics():
	logging.info("Requested topics")
	async with async_session() as session:
		query = select(Topic)
		result = await session.execute(query)
		data = []
		for item_row in result.all():
			item = item_row[0]
			item_processed = {
				"id": item.id,
				"name": item.name,
			}
			data.append(item_processed)
		response = data
	return response


async def get_entities():
	logging.info("Requested entities")
	async with async_session() as session:
		query = select(Entity)
		result = await session.execute(query)
		data = []
		for item_row in result.all():
			item = item_row[0]
			item_processed = {
				"id": item.id,
				"name": item.name,
			}
			data.append(item_processed)
		response = data
	return response
