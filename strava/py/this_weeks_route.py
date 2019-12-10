""" this_weeks_route.py
Gets the most running route provided the route ID.

Author: Mark Thomas
Date: 2018-02-20
"""

# ===================================================== #
# THIS IS THE ONLY THING THAT NEEDS TO CHANGE EACH WEEK #

ROUTE_ID = 16798191

DESCRIPTION = "Let's get those glutes working by climbing a few hills!<br />Now that it is getting dark out early, don't forget to wear some brightly coloured clothes or light up gear.<br />As always, we meet at the Sullivans Pond Gazebo at 6:30pm."

RUN_DATE = "December 12, 2019"

# ===================================================== #

import json
import pickle
import requests

# Get a new auth_token each time
with open('strava/auth_request', 'rb') as f:
    auth_request = pickle.load(f)

files = {
    'client_id': (None, auth_request['client_id']),
    'client_secret': (None, auth_request['client_secret']),
    'code': (None, auth_request['code']),
    'grant_type': (None, 'authorization_code'),
}

response = requests.post('https://www.strava.com/oauth/token', files=files)
api_token = json.loads(response.content)['access_token']

# Get the route info from the Strava API
header = {'Authorization': 'Bearer ' + api_token}
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
