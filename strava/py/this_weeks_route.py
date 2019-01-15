""" this_weeks_route.py
Gets the most running route provided the route ID.

Author: Mark Thomas
Date: 2018-02-20
"""

# ===================================================== #
# THIS IS THE ONLY THING THAT NEEDS TO CHANGE EACH WEEK #

ROUTE_ID = 16798191

DESCRIPTION = "This week we're going to try out a new route! <br />We will start off pretty easy to warm up as we make our way from Sullivan's Pond to Portland and then back up Ochterloney. Once we hit Victoria Rd we'll start to engage those butt muscles by climbing Victoria, then Thistle, and finally Forest Road. <br />Once we've hit the summit, we'll make our way back to the pond via Lyngby and Crichton. <br />As always, we meet at the Sullivans Pond Gazebo at 6:30pm."

RUN_DATE = "January 17, 2019"

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
