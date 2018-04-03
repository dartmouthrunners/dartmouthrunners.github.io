""" this_weeks_route.py
Gets the most running route provided the route ID.

Author: Mark Thomas
Date: 2018-02-20
"""

# ===================================================== #
# THIS IS THE ONLY THING THAT NEEDS TO CHANGE EACH WEEK #
ROUTE_ID = 12514044

DESCRIPTION = "It’s time for a Dartmouth Runners Social!<br />Let’s celebrate April with a run and beer at Celtic Corner.<br />We will run ~6km around the Dartmouth Waterfront and with a quick view of the Tuft’s Cove smoke stacks<br />Bring running shoes, your ID and a smile!<br />See you Thursday at 6:30pm SHARP! Remember, we meet at the Sullivans Pond Gazebo."

RUN_DATE = "April 5, 2018"
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
