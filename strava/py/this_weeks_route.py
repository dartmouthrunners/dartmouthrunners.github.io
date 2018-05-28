""" this_weeks_route.py
Gets the most running route provided the route ID.

Author: Mark Thomas
Date: 2018-02-20
"""

# ===================================================== #
# THIS IS THE ONLY THING THAT NEEDS TO CHANGE EACH WEEK #
ROUTE_ID = 13484005

DESCRIPTION = "We end May with Drill Night!<br />This Thursday we get a mixture of distance and strength.<br />A 6km run, plus a set of exercise every 1KM<br />As alway we meet at the SPG at 6:30pm!"

RUN_DATE = "May 31, 2018" 
# ===================================================== #  

 ## Imports
import json
import requests

## Read the Strava API token from file
with open('strava/auth_token', 'r') as f:
    API_TOKEN = f.readline().rstrip()

## Request the most recent 300 activities (3 pages, 100 per page)
# Define the header
header = {'Authorization': 'Bearer ' + API_TOKEN}
request_uri = 'https://www.strava.com/api/v3/routes/' + str(ROUTE_ID)
response = requests.get(request_uri, headers=header)

route_data = json.loads(response.content)
reduced_json = {
    'id': route_data['id'],
    'name': route_data['name'],
    'distance': route_data['distance'],
    'elevation_gain': route_data['elevation_gain'],
    'polyline': route_data['map']['polyline'],
    'description': DESCRIPTION,
    'date': RUN_DATE
}

with open('strava/data/route_details.json', 'w') as f:
    json.dump(reduced_json, f)
