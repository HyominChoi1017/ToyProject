import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import pandas as pd
import time
import matplotlib.pyplot as plt
import numpy as np
import pickle  

CLIENT_ID = 'f447245b08ed4436874b6d9099c9af29'
CLIENT_SECRET = 'd1975fef9a514dfca16e1ff7f7db3371'

ccm = SpotifyClientCredentials(client_id = CLIENT_ID, client_secret=CLIENT_SECRET)
sp = spotipy.Spotify(client_credentials_manager=ccm)


def getAlbumDF():  

    df_album = pd.DataFrame()
    for i in range(0, 1000, 50):
        track_result = sp.search(q='year:2023', type='track', limit=50, offset=i)
        for i, t in enumerate(track_result['tracks']['items']):
            album_data = []
            album = t['album']
            # print(album.keys())
            album_data.append(album['album_type'])
            album_data.append(album['name'])
            album_data.append(album['release_date'])  
            album_data.append(album['artists'][0]['name'])
            album_Series = pd.Series(album_data)
            df_album = pd.concat([df_album, album_Series], axis=1)
            # print(df_album.T)

    df_album = df_album.T
    df_album.columns = ["album_type", "name", "release_date", "artost_name"]
    df_album.index = list(range(0, 1000))
    print(df_album)

def getTrackDF():

    search_range = [
            (0, 1000),
            (1000, 2000), 
            (2000, 3000),
            (3000, 4000),
            (4000, 5000),
            (5000, 6000)
            ]

    year_range = list(range(2011, 2024))


    tf_df = pd.DataFrame(columns = ['danceability', 'energy', 'key', 'loudness', 'mode', 'speechiness', 'acousticness', 'instrumentalness', 'liveness', 'valence', 'tempo', 'type', 'id', 'url', 'track_href', 'analysis_url', 'duration_ms', 'time_signature'])
    drop_cols = ['type', 'url', 'track_href', 'analysis_url', 'uri']

    start = time.time()
    for yr in year_range:
        for i in range(0, 1000, 50):
            track_result = sp.search(q='year:{}'.format(yr), type='track', limit=50, offset=i)
            track_features = []
            for _, t in enumerate(track_result['tracks']['items']):
                track_id = t['id']
                af = sp.audio_features(track_id)
                track_features.append(af) 
            for item in track_features:
                for feat in item:
                    tf_df = tf_df.append(feat, ignore_index=True)
    end = time.time()

    print('time duration for data scrolling:', end-start)

    tf_df = tf_df.drop(columns=drop_cols)
    print('Data shape:',tf_df.shape)
    return tf_df


def getArtistDF(): 

    artist_df = pd.DataFrame()
    a_popularity = []
    a_genres = []
    a_followers = [] 
    for i in range(0, 1000, 50):
        track_result = sp.search(q='year:2023', type='track', limit=50, offset=i)
        for _, t in enumerate(track_result['tracks']['items']):
            artist_id = t['artists'][0]['id']
            artist = sp.artist(artist_id)
            a_popularity.append(artist['popularity'])
            a_genres.append(artist['genres'])
            a_followers.append(artist['followers']['total'])




    
    artist_df = artist_df.assign(artist_popularity=a_popularity, artist_genres=a_genres, artist_followers=a_followers)
    return artist_df 
 


# df = getTrackDF()
# df.to_csv('fast.csv')

'''
Function about training data
'''
# pkl_df = pd.read_pickle('fast.pkl')
# pkl_df.to_csv('fast.csv')
 
# print(X, y)

'''
Working Space..!
'''
 
# print(df.columns)
# print(df.describe())

# print(X)

# import matplotlib.pyplot as plt
# import seaborn as sb
  

df = pd.DataFrame(pd.read_csv("fast.csv"))
# print(df)
X = df.drop(['id'], axis=1).copy()
y = df['id'].copy()



# from sklearn.neighbors import NearestNeighbors

# knn = NearestNeighbors(n_neighbors=6, algorithm='ball_tree')
# knn.fit(X)
# print('fit complete')

filename = 'model.sav'
# pickle.dump(knn, open(filename, 'wb'))

knn = pickle.load(open(filename, 'rb'))
print('get knn')
print(knn)
 

def recommend(music_id): 
    result = []
    distance, indices = knn.kneighbors(y.iloc[music_id-1, :].values.reshape(1, -1), n_neighbors=3)
    for i in indices[0][1:]:
        print("Similar Music: ", y.iloc[i, :]['id'])
        result.append(y.iloc[i, :]['id'])

# Use the recommend function to recommend similar music
# recommend(100)



