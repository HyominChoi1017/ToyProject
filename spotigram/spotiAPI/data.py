
CLIENT_ID = 'f447245b08ed4436874b6d9099c9af29'
CLIENT_SECRET = 'd1975fef9a514dfca16e1ff7f7db3371'

import time
import datetime
import spotipy 
from spotipy.oauth2 import SpotifyClientCredentials 
import pandas as pd


def clientID():
    return CLIENT_ID

def clientSecret():
    return CLIENT_SECRET

client_credentials_manager = SpotifyClientCredentials(client_id=CLIENT_ID, client_secret=CLIENT_SECRET)
sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)


def getData():
    artist_name =[]
    track_name = []
    track_popularity =[]
    artist_id =[]
    track_id =[]
    for i in range(0,1000,50):
        track_results = sp.search(q='year:2023', type='track', limit=50, offset=i)
        for i, t in enumerate(track_results['tracks']['items']):
            artist_name.append(t['artists'][0]['name'])
            artist_id.append(t['artists'][0]['id'])
            track_name.append(t['name'])
            track_id.append(t['id'])
            track_popularity.append(t['popularity'])
    track_df = pd.DataFrame({'artist_name' : artist_name, 'track_name' : track_name, 'track_id' : track_id, 'track_popularity' : track_popularity, 'artist_id' : artist_id})
     
    track_df['artist_name'] = track_df['artist_name'].astype("string")
    track_df['track_name'] = track_df['track_name'].astype("string")
    track_df['track_id'] = track_df['track_id'].astype("string")
    track_df['artist_id'] = track_df['artist_id'].astype("string")
    track_df = track_df.sort_values(by=['track_popularity'], ascending=False)[['track_name', 'artist_name']].head(100)

    data = dict()

    for track in range(len(track_df)):
        # print(track_df.iloc[track]['artist_name'], " - ", track_df.iloc[track]['track_name'])
        data[track] = {
            'artist_name': track_df.iloc[track]['artist_name'],
            'track_name': track_df.iloc[track]['track_name']
        }

    return data
    


def getMusicChart():
    return getData()


 
 