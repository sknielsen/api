from flask import Flask, request, render_template
import urllib2
import json
from pprint import pprint

app = Flask(__name__)

def zip_to_url(zip):
    location = urllib2.urlopen('http://api.wunderground.com/api/856474bb0ccfb13e/geolookup/q/{0}.json'.format(zip))
    location_json_string = location.read()
    location_parsed_json = json.loads(location_json_string)
    location_url = location_parsed_json['location']['requesturl']
    location_url = location_url.lstrip('US/')
    location_url = location_url.replace('.html', '.json')
    location.close()
    return location_url

def get_yesterdays_temp(location):
    yesterday = urllib2.urlopen('http://api.wunderground.com/api/856474bb0ccfb13e/yesterday/q/{0}'.format(location))
    yesterday_json_string = yesterday.read()
    yesterday_parsed_json = json.loads(yesterday_json_string)
    yesterdays_temp = yesterday_parsed_json['history']['dailysummary'][0]['maxtempi']
    yesterday.close()
    return yesterdays_temp

def get_todays_temp(location):
    today = urllib2.urlopen('http://api.wunderground.com/api/856474bb0ccfb13e/forecast/q/{0}'.format(location))
    today_json_string = today.read()
    today_parsed_json = json.loads(today_json_string)
    todays_temp = today_parsed_json['forecast']['simpleforecast']['forecastday'][0]['high']['fahrenheit']
    today.close()
    return todays_temp

@app.route('/')
def warmer_or_colder():
    return render_template('warmer.html')

@app.route('/answer')
def answer():
    zip_code = request.args.get('location')
    location = zip_to_url(zip_code)
    if get_yesterdays_temp(location) > get_todays_temp(location):
        answer = 'colder than'
        image = '/static/snowflake.png'
        alt = 'Snowflake'
    elif get_yesterdays_temp(location) < get_todays_temp(location):
        answer = 'warmer than'
        image = '/static/sun.png'
        alt = 'sun'
    else:
        answer = 'the same as'
        image = ''
        alt = ''
    return render_template('answer.html', answer=answer, image=image, alt=alt)

if __name__ == "__main__":
      app.run(debug=True)
