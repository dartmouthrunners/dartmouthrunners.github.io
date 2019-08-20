""" this_weeks_route.py
Gets the most running route provided the route ID.

Author: Mark Thomas
Date: 2018-02-20
"""

# ===================================================== #
# THIS IS THE ONLY THING THAT NEEDS TO CHANGE EACH WEEK #

ROUTE_ID = 21186733 

DESCRIPTION = "This week we will try out a new route that takes us to some of the best algae-free swimming spots in Dartmouth. <br />First we will make our way past Lake Banook and start climbing to Penhorn Lake via Harris Road. Once we get to Penhorn, we will cut over to Oat Hill Lake and run through the trail until we reach Lorne Avenue. <br />Finally, we'll make our way back to the gazebo via Sinclair and Hawthorne. <br />As always, we meet at the Sullivans Pond Gazebo at 6:30pm."

RUN_DATE = "August 22, 2019"

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
