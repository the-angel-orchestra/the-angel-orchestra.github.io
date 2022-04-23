from datetime import datetime

class Concert():
    def __init__(self, data):
        self.data = data
        self.title = data['title']
        self.description = data['description']
        self.date_str = data['date']
        self.date_obj = self.get_date_obj()
        self.soloist_name = data['soloist_name'] if 'soloist_name' in data else ""
        self.soloist_website = data['soloist_website'] if 'soloist_website' in data else ""
        self.soloist_attribution = data['soloist_attribution'] if 'soloist_attribution' in data else ""
        self.venue = data['venue'] if not self.is_empty_string(data['venue']) else "Saint Silas Church on Risinghill Street, N1 9UL"
        self.start_time = data['start_time'] if not self.is_empty_string(data['start_time']) else "5pm"
        self.programme = self.get_programme()
        self.full_price = data['full_price']
        self.concession_price = data['concession_price']
        self.ticket_info = data['ticket_info']

    def is_empty_string(self, test_str):
        return test_str.strip() == ""

    def get_programme(self):
        items = [[k, v] for k, v in self.data.items() if 'programme' in k]
        return [v for _, v in sorted(items) if not self.is_empty_string(v)]

    def get_date_obj(self):
        date_str = self.date_str
        if ' and ' in date_str:
            date_str = date_str.split(' and ')[1]
        return datetime.strptime(date_str + ' 22', '%d %B %Y %H')
