# this_weeks_route.py
# Gets the most running route provided the route ID.
#
# @author: Mark Thomas
# @date: 2018-02-20

import json
import requests
import argparse

# ===================================================== #
# THIS IS THE ONLY THING THAT NEEDS TO CHANGE EACH WEEK #

ROUTE_ID = 17126168

DESCRIPTION = "Due to the ongoing pandemic, we are no longer running as a crew!<br />We at Dartmouth Runners encourage you to wash your hands, stay safe, and stay home as much as possible.<br />See you on the other side of all this! ⚡❤ " # noqa E501

RUN_DATE = ""

# ===================================================== #

parser = argparse.ArgumentParser()
parser.add_argument('--auth-token', type=str)


def main():
    # Parge the auth token
    args = parser.parse_args()

    # Get the route info from the Strava API
    header = {'Authorization': 'Bearer ' + args.auth_token}
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


if __name__ == '__main__':
    main()
