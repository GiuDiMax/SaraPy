import deezer
import random

def deez_search(stringz):
    artists = []
    titles = []
    index = []
    extras = []
    client = deezer.Client()
    tracks = client.search(stringz,limit=50)
    for track in tracks:
        titles.append(track.asdict()['title'])
        artists.append(track.asdict()['artist']['name'])
        extras.append(" [mp3]")
        index.append(track.asdict()['preview'])
    return index, artists, titles, extras