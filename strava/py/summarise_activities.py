#!/usr/local/bin/python3

""" summarise_activities.py
Builds a JSON representation of the last 30 days worth of activities for
each member and includes their total number of runs and distance ran.

Author: Mark Thomas
Date: 2018-02-16
"""

## Imports
import json
import pandas as pd
from datetime import datetime, timedelta
from pymongo import MongoClient

## Create the mongoDB client and specify the database
client = MongoClient('mongodb://localhost:27017/')
db = client.dartmouth_runners

## Build a pandas DataFrame containing all of the DRA members id,
## first name, last name, and medium profile image.
cursor = db.members.find({}, {'id': 1, 'firstname': 1, 'profile': 1})
members = pd.DataFrame(list(cursor)).drop('_id', axis=1)

## Build a pandas DataFrame containing the total KMs and number
## of runs for each member over the last 7 days of activities
last_30d = (datetime.today() - timedelta(days=30)).strftime('%Y-%m-%dT%H:%M:%SZ')
cursor = db.activities.aggregate([
    {'$match': {
        'type': 'Run',
        'start_date_local': { '$gte': last_30d }
    }},
    {'$group': {
        '_id': '$athlete.id',
        'distance': {'$sum': '$distance'},
        'runs': {'$sum': 1},
        'elevation': {'$sum': '$total_elevation_gain'}
    }}])
activities = pd.DataFrame(list(cursor)).rename(index=str, columns={'_id': 'id'})

## Left join the two DataFrames by athlete 'id'
member_data = pd.merge(members, activities, on='id')
member_data.to_csv('/Users/markdjthomas/Dropbox/coding/dartmouthrunners.github.io/strava/data/recent_activities.csv', index=False)
