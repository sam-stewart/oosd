import urllib2
import sys
import json
import threading
import pprint # pretty print

class Forecast(threading.Thread):

    ROOT = 'http://metservice.com/publicData/'
    FORECAST_PARAM = 'localForecast'

    def __init__(self, city):
        threading.Thread.__init__(self)
        self.city = city

    def run(self):
        self.url = self.ROOT + self.FORECAST_PARAM + self.city
        print self.url
        try:
            self.response = urllib2.urlopen(self.url)
        except urllib2.HTTPError:
            self.responsejson = {}
        self.responsejson = json.loads(self.response.read())

if __name__ == '__main__':
    city = 'dunedin'
    thread = Forecast(city)
    thread.start()
    thread.join()
    pprint.pprint(thread.responsejson)


