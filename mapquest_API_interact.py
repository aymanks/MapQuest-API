#Ayman Syed, 87719684

#this module handles building the MapQuest URL, making HTTP requests, and
#parsing the JSON

import json
import urllib.parse
import urllib.request
import mapquest_ui

MAPQUEST_API_KEY = 'F2sDSxIEnTxVPwA7GpIvSzjGKQhJqdlR'
#http://open.mapquestapi.com/directions/v2/route?key=APIKEY&from=Irvine%2CCA&to=Los+Angeles%2CCA

BASE_MAPQUEST_URL = 'http://open.mapquestapi.com/directions/v2/route?key=' + MAPQUEST_API_KEY + '&'

def build_url(route_query: list):
    '''Creates URL from MapQuest'''
    locations = []
    first_location = 1
    
    for location in route_query:
        if first_location == 1:
            locations.append(('from', route_query[0]))
            first_location = first_location + 1
        else:
            locations.append(('to', location))

    return BASE_MAPQUEST_URL + urllib.parse.urlencode(locations)


def get_result(url: str) -> dict:
    '''takes the MapQuest URL and returns a Python dictionary that represents
    the parsed JSON response'''
    response = None

    try:
        response = urllib.request.urlopen(url)
        json_text = response.read().decode(encoding = 'utf-8')
        return json.loads(json_text)

    finally:
        if response != None:
            response.close() 
