# -*- coding: utf-8 -*-
import datetime

class ConcertView():
    def __init__(self, concert):
        self.concert = concert
        self.html = self.get_html()

    def get_html(self):
        if self.concert.date_obj > datetime.datetime.now():
            return self.future_html()
        else:
            return self.past_html()

    def handle_solist(self):
        html = ""
        if self.concert.soloist_name != "":
            if self.concert.soloist_attribution != "":
                html += "<p>" + self.concert.soloist_attribution + ": "
            else:
                html += "<p>Soloist: "
            if self.concert.soloist_website != "":
                html += "<a href='" + self.concert.soloist_website + "'>" + self.concert.soloist_name + "</a></p>\n"
            else:
                html += self.concert.soloist_name + "</p>\n"
        return html

    def handle_programme(self):
        html = ""
        if len(self.concert.programme) > 0:
            html += "<ul>\n"
            for item in self.concert.programme:
                html += "<li>" + item + "</li>\n"
            html += "</ul>\n"
        return html

    def future_html(self):
        print('building html...')
        html = "<h3>" + self.concert.title + ": "
        html += self.concert.date_str + "</h3>\n"
        if not self.concert.is_empty_string(self.concert.description):
            html += self.concert.description + "\n"
        html += self.handle_solist()
        html += self.handle_programme()
        print(self.concert.start_time)
        if self.concert.start_time != 'n/a':
            print('is not na')
            html += "<p>Concert starts at " + self.concert.start_time
            html += u". " + self.concert.ticket_info + "</p>\n"
            html += "<p>" + self.concert.venue + "</p>\n"
        print(html)
        return html

    def past_html(self):
        html = "<h3>" + self.concert.date_str + "</h3>\n"
        html += self.handle_solist()
        html += self.handle_programme()
        return html
