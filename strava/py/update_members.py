import json
import requests
from pymongo import MongoClient

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
coll = db.members.insert_many(members)
