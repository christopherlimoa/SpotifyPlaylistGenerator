# step by step tutorial by Monash Association of Coding (MAC)
# https://www.notion.so/Session-1-143e2bb052564b02852e39f27abeaa52

import requests
import json

# STEP 1 : REQUEST SONGS SUGGESTION

endpoint_url = 'https://api.spotify.com/v1/recommendations?'
access_token = "BQCETH_QnW-jxIWy53nIyFVAUHta62VeNDbIUQ2OITXr8RMXg3OdNPKbvUWzlSaPHuFXxsiC69hsyJplWIj5sLMHann5Ocaxfp8sl61RDVBubOA9tZ70Y-1yE5lZnyqDVNs_6y2cfXXeVg_27agyMasunkwaldbOr3f25l0EahMQJhZC17GPa98Nygp8zykD8Rg"
uris = []

# FILTERS
limit = 10  # number of songs in playlist
market = "US"  # country
seed_genres = "pop,summer,happy"  # genres
target_danceability = 0.5
valence = 0.1
seed_artists = "7pbDxGE6nQSZVfiFdq9lOL,12j6dJrPXanCBwY599pZxf"

query = f'{endpoint_url}limit={limit}&market={market}&seed_genres={seed_genres}&target_danceability={target_danceability}&valence={valence}&seed_artists={seed_artists}'

response = requests.get(query,
               headers={"Content-Type":"application/json",
                        "Authorization":f"Bearer {access_token}"})

# check for response code, 200 is OK, 400 is BAD REQ, 403 is forbidden
print("song suggestion status code:", response)

json_response = response.json()

for i,j in enumerate(json_response['tracks']):
    uris.append(j['uri'])
    print(f"{i+1}) \"{j['name']}\" by {j['artists'][0]['name']}")

# STEP 2 : CREATE PLAYLIST
user_id = "31e2oc7hni7va5gdejenhuqrmt2m"

endpoint_url = f"https://api.spotify.com/v1/users/{user_id}/playlists"

request_body = json.dumps({
          "name": "MAC x Spotify Playlist",
          "description": "We made this with python request",
          "public": False # let's keep it between us - for now
        })

response = requests.post(url = endpoint_url, data = request_body, headers={"Content-Type":"application/json", "Authorization":"Bearer " + access_token})
print("\nplaylist creation status code:", response.status_code)

# STEP 3 : ADDING SONGS TO  PLAYLIST

# get the playlist id
playlist_id = response.json()['id']

endpoint_url = f"https://api.spotify.com/v1/playlists/{playlist_id}/tracks"

request_body = json.dumps({
          "uris" : uris
        })

response = requests.post(url = endpoint_url, data = request_body, headers={"Content-Type":"application/json", "Authorization":f"Bearer {access_token}"})
print("\nadding songs to playlist status code:", response.status_code)