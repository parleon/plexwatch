import sqlite3


class db:

    def __init__(self):
        self.connection = sqlite3.connect('database.db')

        try:
            self.connection.execute('CREATE TABLE times (month INT, day INT, year INT, time TEXT,'
                                    'availability INT, slots INT, start_hour INT, time_id INT UNIQUE)')
        except:
            pass
        try:
            self.connection.execute('CREATE TABLE users (user_id INT UNIQUE, phone_number INT, time_id INT)')
        except:
            pass

        self.connection.commit()

    def resetTimesTable(self):
        self.connection.execute('DROP TABLE times')
        self.connection.execute('CREATE TABLE times (month INT, day INT, year INT, time TEXT,'
                                'availability INT, slots INT, start_hour INT, time_id INT UNIQUE)')
        self.connection.commit()


    def addSlot(self, slot):
        args = (slot.month, slot.day, slot.year, slot.time,
                slot.available, slot.num_slots, slot.start_hour, slot.id)
        sql = 'INSERT INTO times (month, day, year, time, availability, slots, start_hour, time_id)' \
              'VALUES (?,?,?,?,?,?,?,?)'

        try:
            self.connection.execute(sql, args)
            self.connection.commit()
        except sqlite3.IntegrityError:
            pass

    def getTimes(self, unavailable=True):
        if unavailable:
            sql = 'SELECT * FROM times WHERE availability=0'
        else:
            sql = 'SELECT * FROM times'
        cursor = self.connection.cursor()
        cursor.execute(sql)
        data = cursor.fetchall()
        cursor.close()
        self.connection.commit()

        returning = []
        for datum in data:
            appendict = {
                'month': datum[0],
                'day': datum[1],
                'year': datum[2],
                'time': datum[3],
                'available': datum[4],
                'slots': datum[5],
                'start_hour': datum[6],
                'id': datum[7]
            }
            returning.append(appendict)
        return returning

    def resetUsersTable(self):
        self.connection.execute('DROP TABLE users')
        self.connection.execute('CREATE TABLE users (user_id INT UNIQUE, phone_number INT, time_id INT)')
        self.connection.commit()

    def addUser(self, user):
        args = (user.user_id, user.phone_number, user.time_id)
        sql = 'INSERT INTO users (user_id, phone_number, time_id)' \
              'VALUES (?,?,?)'
        self.connection.execute(sql, args)
        self.connection.commit()

    def getUsers(self, arg=None):
        if arg is None:
            sql = 'SELECT * FROM users'
        else:
            sql = f'SELECT * FROM users WHERE time_id="{arg}"'
        cursor = self.connection.cursor()
        cursor.execute(sql)
        data = cursor.fetchall()
        cursor.close()
        self.connection.commit()

        returning = []
        for datum in data:
            appendict = {
                'user_id': datum[0],
                'phone_number': datum[1],
                'time_id': datum[2]
            }
            returning.append(appendict)
        return returning

    def popUserByTime(self, time_id):
        sql = f'DELETE FROM users WHERE time_id={time_id}'
        self.connection.execute(sql)
        self.connection.commit()
