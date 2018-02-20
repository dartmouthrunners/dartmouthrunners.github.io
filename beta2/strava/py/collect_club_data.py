""" collect_club_data.py
Gathers the club stats for each member of DRA and save the results to be
visulized using d3.

Author: Mark Thomas
Date: 2018-02-16
"""

## Imports
import json
import time
from datetime import datetime, timedelta
import requests
import pandas as pd
from pymongo import MongoClient

## Create the mongo client and select the database
client = MongoClient('mongodb://localhost:27017/')
db = client.dartmouth_runners

## Read the Strava API token from file
with open('strava/auth_token', 'r') as f:
    API_TOKEN = f.readline().rstrip()

## Delete the old activities
db.activities.delete_many({})

## Request the most recent 300 activities (3 pages, 100 per page)
# Define the header
header = {'Authorization': 'Bearer ' + API_TOKEN}

for i in range(1, 4):
    request_uri = 'https://www.strava.com/api/v3/clubs/253520/activities?page=' + str(i) + '&per_page=100'
    response = requests.get(request_uri, headers=header)
    activities = json.loads(response.content)
    db.activities.insert_many(activities)
