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

<<<<<<< HEAD
ROUTE_ID = 14936120

DESCRIPTION = "" # noqa E501

RUN_DATE = "November 5, 2020"
=======
ROUTE_ID = 2756324267052235118

DESCRIPTION = "" # noqa E501

RUN_DATE = "October 29, 2020"
>>>>>>> 9b477ab430c9736f8494f2907d8904b26c757244

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
