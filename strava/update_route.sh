#!/usr/bin/bash

git pull
python3 strava/py/this_weeks_route.py --auth-token $1
git add strava/data/route_details.json
git add strava/py/this_weeks_route.py
git commit -m "updated route details"
git push https://markdjthomas:smb0%269QtZiN4Z%25k@github.com/dartmouthrunners/dartmouthrunners.github.io.git master
