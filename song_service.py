from random import randint
import requests
from bs4 import BeautifulSoup
import re
import time

def song_serv():
    index = []
    artists = []
    titles = []
    print("")
    for x in range(3):
        x = x * 3
        rand = []
        pag_value = randint(1, 808)
        url = "http://songservice.it/midi-karaoke?p="
        rand.append(randint(0, 15))
        while True:
            random = randint(0, 15)
            if random not in rand:
                rand.append(random)
                break
        while True:
            random = randint(0, 15)
            if random not in rand:
                rand.append(random)
                break
        url = requests.get(str(url) + str(pag_value))
        soup = BeautifulSoup(url.content, 'html.parser')
        soup = soup.find("div", {"class": "products list items product-items"})
        soupx = soup.findAll("div", {"class": "col-xs-12 col-sm-6"})
        y = -1
        for rand_song in rand:
            y = y + 1
            soup = soupx[rand_song]
            title = soup.find("div", {"class": "song-title"}).select('a')[0].string
            artist = soup.find("div", {"class": "artist-name"}).select('a')[0].string
            id = re.search('filename": "(.*).MP3', str(soup)).group(1)
            index.append(int(id))
            titles.append(title)
            artists.append(artist)
            try:
                extra = soup.find("p", {"class": "song-version"}).string
                print(str(x + y + 1) + ") " + str(artist) + ": " + str(title) + " [" + str(extra) + "]")
            except:
                print(str(x + y + 1) + ") " + str(artist) + ": " + str(title))

    return index, artists, titles

'''
start_time = time.time()
song_serv()
print("--- %s seconds ---" % (time.time() - start_time))
'''