from googlesearch import search
import requests
from bs4 import BeautifulSoup
import os
import re

def search2(stringz, num):
    artists = []
    titles = []
    links = []
    x = num

    try:
        url = 'https://www.mididb.com/search.asp?q=' + str(stringz) + "&formatID=1"
        response = requests.get(url)
        soup = BeautifulSoup(response.text, 'html.parser')
        soup2 = soup.findAll("div", {"class": "left song-details"})
        for sup in soup2:
            link = sup.span['id']
            title = sup.find("span", {"class": "song-title to-cart"}).select('a')[0].string
            artist = sup.find("div", {"class": "artist-name"}).select('a')[0].string
            links.append(link)
            titles.append(title)
            artists.append(artist)
            print(str(x) + ") " + str(artist) + ": " + str(title) + " [2nd Database]")
            x = x+1
    except:
        pass

    try:
        url = search(str(stringz) + " supreme midi", num_results=0)[0]
        if url.count("/") == 7:
            url = url.rsplit('/', 1)[0]
        response = requests.get(url)
        soup = BeautifulSoup(response.text, 'html.parser')
        soup2 = soup.findAll("div", {"class": "related"})
        for sup in soup2:
            su = str(sup.find("div", {"class": "album_name"}))
            if "MIDI" in str(su):
                su = su[su.find('<td align="left">') + len('<td align="left">'):su.rfind(" (MIDI File)  </a>")]
                artist = su.split("<br")[0]
                link = su[su.find('href="') + len('href="'):su.rfind('">')]
                title = su.rsplit('> ', 1)[1]
                links.append(link)
                titles.append(title)
                artists.append(artist)
                print(str(x) + ") " + str(artist) + ": " + str(title) + " [3rd Database]")
                x = x + 1
    except:
        pass

    return links, artists, titles

links, artists, titles = search2("Dua lipa", 0)
print(links)

