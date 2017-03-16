import urllib2
import json
from pprint import pprint

yesterday = urllib2.urlopen('http://api.wunderground.com/api/856474bb0ccfb13e/yesterday/q/CA/San_Francisco.json')
today = urllib2.urlopen('http://api.wunderground.com/api/856474bb0ccfb13e/forecast/q/CA/San_Francisco.json')
yesterday_json_string = yesterday.read()
today_json_string = today.read()
yesterday_parsed_json = json.loads(yesterday_json_string)
pprint(yesterday_parsed_json)
y_temp = yesterday_parsed_json['history']['dailysummary'][0]['maxtempi']
print y_temp
today_parsed_json = json.loads(today_json_string)
today.close()
yesterday.close()
