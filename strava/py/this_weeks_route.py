""" this_weeks_route.py
Gets the most running route provided the route ID.

Author: Mark Thomas
Date: 2018-02-20
"""

# ===================================================== #
# THIS IS THE ONLY THING THAT NEEDS TO CHANGE EACH WEEK #

ROUTE_ID = 14936214 

DESCRIPTION = "This week we will run an old favourite: The Dartmouth Road-runner <em>beep-beep</em>! <br />We will start by making our way up Maple and then head down Slayter until we get to Woodland Ave. We will turn around at Victoria and then make our way back to the gazebo via Thistle and Alderney, with a little detour at Pleasant St to get us onto Hawthorne. <br />It's a complicated one, I know, but the lack-luster Strava Art will be worth it! <br />As always, we meet at the Sullivans Pond Gazebo at 6:30pm."

RUN_DATE = "May 16, 2019"

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
