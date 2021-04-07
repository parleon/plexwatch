class User:
    def __init__(self, time_id, ph_string):
        self.time_id = time_id
        clean_ph = ''.join(filter(lambda i: i.isdigit(), ph_string))
        if len(clean_ph) == 10 or (len(clean_ph) == 11 and int(clean_ph[0]) == 1):
            self.phone_number = int(clean_ph)
        else:
            raise IOError('invalid phone number')
        self.user_id = f'{clean_ph}{time_id}'

    def toString(self):
        return f'{self.user_id}'

