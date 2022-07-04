#!/usr/bin/python
import os
import json
import yaml
import urllib.request
from scripts.models.concert import Concert
from scripts.models.concert_manager import ConcertManager
from scripts.views.concert_view import ConcertView

API_KEY = os.environ['API_KEY']

url = 'https://sheets.googleapis.com/v4/spreadsheets/1DvKwUS4tHe2646Fu8e1ut5JCUD-nd3AKn3TfUTI7EuI/values/Sheet1?alt=json&key=' + API_KEY
response = urllib.request.urlopen(url)
data = json.loads(response.read())

col_names = data['values'][0]
rows = data['values'][1:]

concert_manager = ConcertManager()
for row in rows:
    named_row = {}
    for idx, col_name in enumerate(col_names):
        if idx < len(row):
            named_row[col_name] = row[idx]
        else:
            named_row[col_name] = ''
    concert = Concert(named_row)
    concert_manager.concerts.append(concert)

next_concert = concert_manager.get_next_concert()
with open('./_includes/next-concert.html', 'w') as f: 
    f.write(ConcertView(next_concert).html)

# minute, hour, day, month = next_concert.date_obj.minute, next_concert.date_obj.hour, next_concert.date_obj.day, next_concert.date_obj.month

# cron_str = f'{minute + 1} {hour + 1} {day} {month} *'

# with open('./.github/workflows/main.yml') as f:
#     current_yml_as_list = f.readlines()

# future_yml_as_list = current_yml_as_list.copy()

# for idx, line in enumerate(current_yml_as_list):
#     if 'schedule' in line:
#         future_yml_as_list[idx + 1] = f'    - cron: "{cron_str}"\n'

# with open('./.github/workflows/main.yml', 'w') as f:
#     f.write(''.join(future_yml_as_list))

future_concerts = concert_manager.get_future_concerts()
with open('./_includes/future-concerts.html', 'w') as f: 
    page_elements = [ConcertView(concert).html for concert in future_concerts]
    f.write('\n'.join(page_elements))

past_concerts = concert_manager.get_past_concerts()
with open('./_includes/past-concerts.html', 'w') as f: 
    page_elements = [ConcertView(concert).html for concert in past_concerts]
    f.write('\n'.join(page_elements))


url = 'https://sheets.googleapis.com/v4/spreadsheets/1whVYOsZxYCN6PssYtBWrc60hyUfq_3DzIJQPQJmhGOg/values/Sheet1?alt=json&key=' + API_KEY
response = urllib.request.urlopen(url)
data = json.loads(response.read())

rehearsals_text = data['values'][1][2]
with open('./_includes/rehearsals.html', 'w') as f: 
    f.write("<p>" + rehearsals_text + "</p>")

page_elements = []
for row in data['values'][1:]:
    url = row[1]
    name = row[0]
    html = '<li><a href="{}">{}</a></li>\n'.format(url, name)
    page_elements.append(html)

with open('./_includes/imslp.html', 'w') as f: 
    f.write('\n'.join(page_elements))
