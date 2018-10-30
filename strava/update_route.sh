#!/usr/local/bin/bash
set -e

cd /Users/markdjthomas/Dropbox/coding/dartmouthrunners.github.io/

/usr/local/bin/git pull
/usr/local/bin/python3  strava/py/this_weeks_route.py
/usr/local/bin/git add strava/data/route_details.json
/usr/local/bin/git add strava/py/this_weeks_route.py
/usr/local/bin/git commit -m "updated route details"
/usr/local/bin/git push https://markdjthomas:smb0%269QtZiN4Z%25k@github.com/dartmouthrunners/dartmouthrunners.github.io.git master

echo "All done!"
