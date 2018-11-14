""" this_weeks_route.py
Gets the most running route provided the route ID.

Author: Mark Thomas
Date: 2018-02-20
"""

# ===================================================== #
# THIS IS THE ONLY THING THAT NEEDS TO CHANGE EACH WEEK #

ROUTE_ID = 15285960

DESCRIPTION = "This week we will stick to a personal favourite of mine (Mark). First we will leave the pond and head along the Lake Banook trail towards Mic Mac Mall (up Prince Albert). We will turn around once we hit Micmac Blvd and head back the same way we came. <br />Heads up! There is a bit of a dark path on this one, so wear a headlamp if you have one, and now that the sun is setting early, make sure to wear your bright clothes! <br />As always, we meet at the Sullivans Pond Gazebo at 6:30pm."

RUN_DATE = "November 15, 2018"

# ===================================================== #

import json
import requests

with open('strava/auth_token', 'r') as f:
    API_TOKEN = f.readline().rstrip()

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
