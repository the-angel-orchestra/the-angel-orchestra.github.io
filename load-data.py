#!/usr/bin/python
import json
import urllib.request
from scripts.models.concert import Concert
from scripts.models.concert_manager import ConcertManager
from scripts.views.concert_view import ConcertView

url = 'https://sheets.googleapis.com/v4/spreadsheets/1DvKwUS4tHe2646Fu8e1ut5JCUD-nd3AKn3TfUTI7EuI/values/Sheet1?alt=json'
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

future_concerts = concert_manager.get_future_concerts()
with open('./_includes/future-concerts.html', 'w') as f: 
    page_elements = [ConcertView(concert).html for concert in future_concerts]
    f.write('\n'.join(page_elements))

past_concerts = concert_manager.get_past_concerts()
with open('./_includes/past-concerts.html', 'w') as f: 
    page_elements = [ConcertView(concert).html for concert in past_concerts]
    f.write('\n'.join(page_elements))


url = 'https://sheets.googleapis.com/v4/spreadsheets/1whVYOsZxYCN6PssYtBWrc60hyUfq_3DzIJQPQJmhGOg/values/Sheet1?alt=json'
response = urllib.request.urlopen(url)
data = json.loads(response.read())

rehearsals_text = data['values'][1][2]
with open('./_includes/rehearsals.html', 'w') as f: 
    f.write("<p>" + rehearsals_text + "</p>")

page_elements = []
for row in data['values'][1:]:
    url = row[1]
    name = row[0]
    html = "<li><a href='{}'>{}</a></li>\n".format(url, name)
    page_elements.append(html)

with open('./_includes/imslp.html', 'w') as f: 
    f.write('\n'.join(page_elements))
