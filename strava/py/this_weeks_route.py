""" this_weeks_route.py
Gets the most recent route provided the route ID.

Author: Mark Thomas
Date: 2018-02-20
"""

## Imports
import json
import requests

## Read the Strava API token from file
with open('beta2/strava/auth_token', 'r') as f:
    API_TOKEN = f.readline().rstrip()

## Request the most recent 300 activities (3 pages, 100 per page)
# Define the header
header = {'Authorization': 'Bearer ' + API_TOKEN}
request_uri = 'https://www.strava.com/api/v3/routes/11136796'
response = requests.get(request_uri, headers=header)

data = json.loads(response.content)
data
