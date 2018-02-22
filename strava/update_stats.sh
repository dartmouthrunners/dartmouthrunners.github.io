#!/usr/local/bin/bash
set -e

# change the directory to the DRA Github page
cd /Users/markdjthomas/Dropbox/coding/dartmouthrunners.github.io/

# run the mongoDB update scripts
/usr/local/bin/python3 strava/py/update_members.py
/usr/local/bin/python3 strava/py/collect_club_data.py
/usr/local/bin/python3 strava/py/summarise_activities.py

# push the changes to Github
/usr/local/bin/git add strava/data/recent_activities.csv
/usr/local/bin/git commit -m "updated strava stats"
/usr/local/bin/git push

echo "All done!"
