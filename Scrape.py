import config
import requests
from bs4 import BeautifulSoup


def extractSlots(pool=False):
    url = config.GYM_URL
    if pool:
        url = config.POOL_URL

    page = requests.get(url)
    soup = BeautifulSoup(page.content, 'html.parser')

    slot_list = []
    for slot_soup in soup.find_all('div', {"class": "col-sm-6 col-md-4 program-schedule-card"}):
        slot_list.append(Slot(slot_soup))
    return slot_list


class Slot:
    def __init__(self, slot_soup):
        self.dirty = slot_soup.text

        cleaned = ''
        for char in self.dirty:
            if char == '\r':
                cleaned += ' '
            elif char != '\n' and char != '\t':
                cleaned += char

        self.available = 'no spots' not in self.dirty.lower()

        dash_splits = cleaned.split('-')
        for i in range(1, 13):
            sub = str(i) + ':'
            if sub in dash_splits[0]:
                if 'AM' in dash_splits[0]:
                    self.start_hour = i
                else:
                    self.start_hour = i + 12

        space_splits = cleaned.split(' ')
        switch = {
            "January": 1,
            "February": 2,
            "March": 3,
            "April": 4,
            "May": 5,
            "June": 6,
            "July": 7,
            "August": 8,
            "September": 9,
            "October": 10,
            "November": 11,
            "December": 12
        }
        self.month = switch.get(space_splits[2])
        self.day = int(space_splits[3][0:-1])
        self.year = space_splits[4]

        self.time = space_splits[6] + space_splits[7] + space_splits[8] + space_splits[9] + space_splits[10]

        if self.available:
            self.num_slots = space_splits[11]
        else:
            self.num_slots = 0

        self.id = int(f'{self.month}{self.day}{self.start_hour}')

    def toString(self):
        return f"{self.month}/{self.day}/{self.year} {self.time} {self.available} {self.num_slots} {self.id}"
