# this_weeks_route.py
#
# Gets the most running route provided the route ID.
#
# @author: Mark Thomas
# @date: 2018-02-20

import sys
import json
import requests

# ===================================================== #
# THIS IS THE ONLY THING THAT NEEDS TO CHANGE EACH WEEK #

ROUTE_ID = 15809780

DESCRIPTION = "This week we'll take to the streets of Westphal as we make out way down Prince Albert and over the highway.<br />Now that it is getting dark out early, don't forget to wear some brightly coloured clothes or light up gear.<br />As always, we meet at the Sullivans Pond Gazebo at 6:30pm."

RUN_DATE = "January 16, 2020"

# ===================================================== #

# Import the auth_token from the system agruments
auth_token = sys.argv[0]
print(auth_token)
print(type(auth_token))

# Get the route info from the Strava API
header = {'Authorization': 'Bearer ' + auth_token}
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
