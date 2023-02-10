import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

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
    tf_df = pd.DataFrame(columns = ['danceability', 'energy', 'key', 'loudness', 'mode', 'speechiness', 'acousticness', 'instrumentalness', 'liveness', 'valence', 'tempo', 'type', 'id', 'url', 'track_href', 'analysis_url', 'duration_ms', 'time_signature'])
    drop_cols = ['type', 'url', 'track_href', 'analysis_url', 'uri']
    for i in range(0, 1000, 50):
        track_result = sp.search(q='year:2023', type='track', limit=50, offset=i)
        track_features = []
        for _, t in enumerate(track_result['tracks']['items']):
            track_id = t['id']
            af = sp.audio_features(track_id)
            track_features.append(af) 
        for item in track_features:
            for feat in item:
                tf_df = tf_df.append(feat, ignore_index=True)
    tf_df = tf_df.drop(columns=drop_cols)
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

def preprocess(df):
    pass




# df = getTrackDF()
# df.to_pickle('./fast.pkl')

'''
Function about training data
'''

df = pd.read_pickle('./fast.pkl')
X = df.drop(['id'], axis=1).copy()
y = df['id'].copy()

print(X, y)

'''
Working Space..!
'''
 
# print(df.columns)
# print(df.describe())

print(len(X.columns))

import matplotlib.pyplot as plt
import seaborn as sb
 
# print(X)
# sb.set(rc={'figure.figsize':(12, 10)})
# sb.heatmap(X.corr(), annot=True)
# plt.show()


# fig, axs = plt.subplots(len(X.columns), 1, figsize=(12, 10))
# for i in range(len(X.columns)):
    
#     axs[i].hist(X[X.columns[i]])
#     axs[i].set_title(X.columns[i])
# plt.show() 

from sklearn.neighbors import NearestNeighbors

knn = NearestNeighbors(n_neighbors=6, algorithm='ball_tree')
knn.fit(X)
print('fit complete')

def recommend(music_id):
    distance, indices = knn.kneighbors(y.iloc[music_id-1, :].values.reshape(1, -1), n_neighbors=6)
    for i in indices[0][1:]:
        print("Similar Music: ", y.iloc[i, :]['id'])

# Use the recommend function to recommend similar music
# recommend(100)



