
CLIENT_ID = 'f447245b08ed4436874b6d9099c9af29'
CLIENT_SECRET = 'd1975fef9a514dfca16e1ff7f7db3371'

import time
import datetime
import spotipy 
from spotipy.oauth2 import SpotifyClientCredentials 
import pandas as pd


client_credentials_manager = SpotifyClientCredentials(client_id=CLIENT_ID, client_secret=CLIENT_SECRET)
sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)


def getData():
    artist_name = []
    track_name = []
    track_popularity = []
    artist_id = []
    track_id = []
    for i in range(0, 1000, 50):
        track_result = sp.search(
            q='year:{}'.format(datetime.date.today().year), 
            type='track', 
            limit=50, 
            offset=i
            )
        for i, t in enumerate(track_result['tracks']['items']):
            artist_name.append(t['artists'][0]['name'])
            artist_id.append(t['artists'][0]['id'])
            track_name.append(t['name'])
            track_id.append(t['id'])
            track_popularity.append(t['popularity'])

    track_data = pd.DataFrame(
        {
            'artist_name':artist_name, 
            'track_name':track_name, 
            'track_id':track_id, 
            'track_popularity': track_popularity, 
            'artist_id':artist_id
        })
    
    return track_data
    


def getMusicChart():
    return getData().to_json()



def getArtistChart():
    start_time = time.time()
    artist_popularity = []
    artist_genres = []
    artist_followers =[]
    track_df = getData()
 
    for a_id in track_df.artist_id:
        artist = sp.artist(a_id)
        artist_popularity.append(artist['popularity'])
        artist_genres.append(artist['genres'])
        artist_followers.append(artist['followers']['total'])

    track_df = track_df.assign(
        artist_popularity=artist_popularity, 
        artist_genres=artist_genres, 
        artist_followers=artist_followers
        )
    end_time = time.time()
    print("실행시간:", end_time - start_time)
    return track_df.to_json()


print(pd.DataFrame(getArtistChart()))