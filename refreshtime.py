import asyncio
from Scrape import extractSlots
from db import db


async def timeRefresher(wait):
    database = db()
    while True:
        print('refreshing times')
        database.resetTimesTable()
        for each in extractSlots():
            database.addSlot(each)
        await asyncio.sleep(wait)


asyncio.run(timeRefresher(30))
