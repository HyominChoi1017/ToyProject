import requests
import json
from spotipy.oauth2 import SpotifyClientCredentials
import spotipy
import sys
import pprint

CLIENT_ID = 'f447245b08ed4436874b6d9099c9af29'
CLIENT_SECRET = 'd1975fef9a514dfca16e1ff7f7db3371'


search_str = 'Radiohead'

ccm = SpotifyClientCredentials(client_id = CLIENT_ID, client_secret=CLIENT_SECRET)

sp = spotipy.Spotify(client_credentials_manager=ccm)






def get_artist(name):
    results = sp.search(q='artist:' + name, type='artist')
    items = results['artists']['items']
    
    return items

def get_album(album):
    results = sp.search(q='album:' + album, type='album')
    items = results['albums']['items']

    return items

def get_track(track):
    results = sp.search(q='track:' + track, type='track')
    items = results['tracks']['items']
    for i in items: 
        del i['available_markets']
        del i['album']['available_markets']
        print(i['album'].keys())
        # print(i.keys())
    return items


def show_recommendations_for_artist(artist):
    results = sp.recommendations(seed_artists=[artist['id']])
    for track in results['tracks']:
        print('Recommendation: {} - {}'.format(track['name'], track['artists'][0]['name']))


def recommendation_for_artist_by_model(artist): 
    results = sp.recommendations(seed_artist=artist)
    rec = {'recommendations':[]}
    for track in results['tracks']:
        res = sp.search(q='track:' + track['name'], type='track')
        for r in res:
            if r['artists']['name'] == track['artist'][0]['name']:
                rec['recommendations'].append(r['id'])
    return rec


# pprint.pprint(get_track('wonderwall'))
# get_track("wonderwall")