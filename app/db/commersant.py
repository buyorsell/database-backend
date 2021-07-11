from app.db.db_setup import session, Kommersant
from typing import List
import pandas as pd

async def get_all_kommersant_news() -> List[Kommersant]:
	df = pd.read_sql(session.query(Kommersant).statement, session.bind)
	return df.to_json()