""" this_weeks_route.py
Gets the most running route provided the route ID.

Author: Mark Thomas
Date: 2018-02-20
"""

# ===================================================== #
# THIS IS THE ONLY THING THAT NEEDS TO CHANGE EACH WEEK #

ROUTE_ID = 14936198 

DESCRIPTION = "This week we will run the Albro Lake route in reverse. <br />We will head up Crichton Ave all the way to the mall and then make the winding climb up Micmac Blvd. Once we rearch Woodland Ave, we'll cross the street and continue to Albro Lake Rd via Lancaster and Sea King Drive. Finally, we'll coast down Slayter and Maple back to the Gazebo. <br />As always, we meet at the Sullivans Pond Gazebo at 6:30pm."

RUN_DATE = "April 25, 2019"

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
