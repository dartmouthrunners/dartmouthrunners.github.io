#!/usr/bin/bash

curl -X POST https://www.strava.com/api/v3/oauth/token \
  -d client_id=23327 \
  -d client_secret=894e5e0f2e02890f508926827edd33c7eaa09523 \
  -d grant_type=refresh_token \
  -d refresh_token=afe3595509c4286d0a57432683d47d7a147f1b87
