#!/usr/local/bin/bash
set -e

# change the directory to the DRA Github page
cd /Users/markdjthomas/Dropbox/coding/dartmouthrunners.github.io/

# run the mongoDB update scripts
python3 strava/py/update_members.py
python3 strava/py/collect_club_data.py
python3 strava/py/summarise_activities.py

# push the changes to Github
git add strava/data/recent_activities.csv
git commit -m "updated strava stats"
git push origin master

echo "All done!"
