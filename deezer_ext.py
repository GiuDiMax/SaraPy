import requests
import deezer
import random

'''
playlists = client.get_chart().asdict()['playlists']
for playlist in playlists:
    print(playlist['id'])
    print(playlist['title'])


radios = client.get_radios()
for radio in radios:
    print(radio.asdict()['id'])
    print(radio.asdict()['title'])
'''

class class_track:
    def __init__(self, title=None, artist=None, album=None, preview=None):
        self.title = title
        self.artist = artist
        self.album = album
        self.preview = preview

def search():
    track_list = []
    client = deezer.Client()
    tracks = client.get_playlist('65489479').asdict()['tracks']
    for track in tracks:
        title = track['title']
        artist = track['artist']['name']
        album = track['album']['title']
        preview = track['preview']
        track_list.append(class_track(title, artist, album, preview))
    random.shuffle(track_list)
    return track_list

