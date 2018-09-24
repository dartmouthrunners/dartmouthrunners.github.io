""" this_weeks_route.py
Gets the most running route provided the route ID.

Author: Mark Thomas
Date: 2018-02-20
"""

# ===================================================== #
# THIS IS THE ONLY THING THAT NEEDS TO CHANGE EACH WEEK #

ROUTE_ID = 15050887

DESCRIPTION = "Back by request: <br />This week we will head to the smoke stacks via Wyse Rd, turn around once we hit Albro Lake Rd, and then head back via Windmill and then Ochterloney. <br />As always, we meet at the Sullivans Pond Gazebo at 6:30pm."

RUN_DATE = "September 27, 2018"

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
