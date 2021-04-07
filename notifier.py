from db import db
from datetime import datetime
import config
from twilio.rest import Client

client = Client(config.account_sid, config.auth_token)


def expired(time_id):
    database = db()
    now = datetime.now()
    hour = now.hour
    slot = database.getTimesById(time_id)
    if hour == slot['start_hour'] - 1 or (hour == 24 and now == 11):
        if now.minute > 30:
            return True
    return False


def mention(to, body):
    try:
        client.api.account.messages.create(to=to, from_=config.number, body=body)
        print("notified: " + to)
    except:
        print("failed to notify " + to)


def checkNotify():
    database = db()
    print('Checking and Notifying')
    users = database.getUsers()
    times = database.getTimes()
    time_id = []
    for time in times:
        time_id.append(time['id'])
    now_available = []
    for user in users:
        if user['time_id'] not in time_id:
            now_available.append(user['time_id'])
    notifying = []
    for id_ in now_available:
        if not expired(id_):
            gotten = database.getUsers(id_)
            for got in gotten:
                if got['phone_number'] not in notifying:
                    notifying.append(got['phone_number'])
        database.popUserByTime(id_)
    for each in notifying:
        mention(str(each), "Hello, this is PlexWatch! You can now sign up for your gym time.")
