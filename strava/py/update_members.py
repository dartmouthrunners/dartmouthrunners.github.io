#!/usr/local/bin/python3

""" update_members.py
Gets the full list of DRA members and inserts them into the
MongoDB database. If they already exist, they are simply overwritten.
In this way, updates to user profiles are carried forward.

Author: Mark Thomas
Date: 2018-02-16
"""

## Imports
import json
import requests
from pymongo import MongoClient

## Read the API token from file
with open('strava/auth_token', 'r') as f:
    API_TOKEN = f.readline().rstrip()

## Get the full list of DRA members in JSON
header = {'Authorization': 'Bearer ' + API_TOKEN}
response = requests.get('https://www.strava.com/api/v3/clubs/253520/members', \
                        headers=header)
members = json.loads(response.content)

## Create the mongoDB client and insert all of the members into the
## 'members' collection of the 'dartmouth_runners' database.
client = MongoClient('mongodb://localhost:27017/')
db = client.dartmouth_runners
db.members.delete_many({})
db.members.insert_many(members)
