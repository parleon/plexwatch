
from Scrape import extractSlots
from db import db


async def timeRefresher():
    database = db()
    print('refreshing times')
    database.resetTimesTable()
    for each in extractSlots():
        database.addSlot(each)




