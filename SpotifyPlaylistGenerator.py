import requests
import json

endpoint_url = 'https://api.spotify.com/v1/recommendations?'
access_token = "BQAaDv9E76KxDEdTbCC8jMiAbjc4W"

# FILTERS
limit = 10  # number of songs in playlist
market = "AU"  # country
seed_genres = "pop"  # genres
target_danceability = 0.2
seed_artists = '12j6dJrPXanCBwY599pZxf'

