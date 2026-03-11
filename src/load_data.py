# src/load_data.py
import asyncio
import os

import pandas as pd

from src.core.database import engine  # Ensure this matches your structure


async def load_anime_csv():
    csv_path = "anime.csv"
    df = pd.read_csv(csv_path)

    async with engine.begin() as conn:
        await conn.run_sync(
            lambda sync_conn: df.to_sql(
                name="anime_list",
                con=sync_conn,
                if_exists="replace",
                index=False,
                chunksize=1000,
            )
        )
    print("✅ Successfully loaded into SQLite!")


if __name__ == "__main__":
    asyncio.run(load_anime_csv())
