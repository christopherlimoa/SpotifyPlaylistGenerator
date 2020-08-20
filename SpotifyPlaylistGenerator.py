# step by step tutorial by Monash Association of Coding (MAC)
# https://www.notion.so/Session-1-143e2bb052564b02852e39f27abeaa52

import requests
import json

endpoint_url = 'https://api.spotify.com/v1/recommendations?'
access_token = "BQAaDv9E76KxDEdTbCC8jMiAbjc4W-_f2C-bG9RVCR9yvgBKnTK-rZkm4aSSyflKo2UXREGuBGRZ-oaxm46jSwQei8_apMpJPJ_vIS85aldLbS2LMfVxha10YZlt9to4i_U1gxd2BaJg1eKjVdrPkjYC71_i8bnm9l9-nap-ofJpvi8HkabGPciRxwILwpx1B1U"
songs_array = []

# FILTERS
limit = 10  # number of songs in playlist
market = "AU"  # country
seed_genres = "pop"  # genres
target_danceability = 0.2
seed_artists = '12j6dJrPXanCBwY599pZxf'

query = f'{endpoint_url}limit={limit}&market={market}&seed_genres={seed_genres}&target_danceability={target_danceability}&seed_artists={seed_artists}'

response = requests.get(query,
               headers={"Content-Type":"application/json",
                        "Authorization":f"Bearer {access_token}"})

# check for response code, 200 is OK, 400 is BAD REQ, 403 is forbidden
print(response)

json_response = response.json()

for i,j in enumerate(json_response['tracks']):
    songs_array.append(j['uri'])
    print(f"{i+1}) \"{j['name']}\" by {j['artists'][0]['name']}")