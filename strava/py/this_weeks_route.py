""" this_weeks_route.py
Gets the most running route provided the route ID.

Author: Mark Thomas
Date: 2018-02-20
"""

# ===================================================== #
# THIS IS THE ONLY THING THAT NEEDS TO CHANGE EACH WEEK #

ROUTE_ID = 14936198 

DESCRIPTION = "This week we will make a big loop around the darkside. <br />First we will head up Maple Street and then all the way down Slayter until Albro Lake Road and then head north towards Lancaster. Once we get to Lancaster Drive, we'll follow it and cross the street and run by Mic Mac Mall via Micmac Blvd. Finally we'll take Crichton Ave and make our way back to the Gazebo. <br />As always, we meet at the Sullivans Pond Gazebo at 6:30pm."

RUN_DATE = "May 23, 2019"

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
