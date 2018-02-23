""" this_weeks_route.py
Gets the most running route provided the route ID.

Author: Mark Thomas
Date: 2018-02-20
"""

# ===================================================== #
# THIS IS THE ONLY THING THAT NEEDS TO CHANGE EACH WEEK #
ROUTE_ID = 11136796

DESCRIPTION = "What are Thursdays for….? For the 'voys (voyages of friendship, I mean come on this works on so many levels). Get your shoes tied up, grab your reflective devices and let's head out for a February run.<br />We run the Dartmouth Roadrunner. Starts with a trip up Maple, head out Slayter and back Victoria. Head down Thistle to Alderney, back up Portland, and around the Pleasant-Portland-Hawthorne loop back to the Gazebo.<br />Remember to check out the route map, posted above or on Strava. We meet at the Sullivan's Pond Gazebo at 6:25 and leave at 6:30pm sharp. Bring friends!!!"

RUN_DATE = "February 22, 2018"
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
