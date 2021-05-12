import requests
from bs4 import BeautifulSoup
from googlesearch import search
from difflib import SequenceMatcher
import re

def search_song(string):
    url_final = ''
    x = 0
    y = 0
    artists = []
    ricerca = ''
    titles = []
    index = []
    ratio = 0
    string = string.replace(" ", "+")
    url = search(str(string) + " basi-karaoke midi songservice", num_results=5)
    for ur in url:
        if "midi-karaoke" in ur:
            ricerca = ur.split("/")[-2]
            ratio = SequenceMatcher(None, string.lower(), ricerca.lower()).ratio()
            if ratio > 0.8:
                url_final = ur
                break
    try:
        response = requests.get(url_final)
        soup = BeautifulSoup(response.text, 'html.parser')
    except:
        pass

    try:
        if soup.find("ul", {"class": "items pages-items"}) != None:
            soup2 = soup.find("ul", {"class": "items pages-items"})
            soup2 = soup2.findAll("li", {"class": "item"})
            pag_num = int(len(soup2) - 1)
            for i in range(pag_num):
                url = url_final + '?p=' + str(i + 1)
                # url = "https://songservice.it/mlivecatalogsearch/result/?attribute-set-id=11&p="+str(int(i+1))+"&q=" + str(string)
                response = requests.get(url)
                soup = BeautifulSoup(response.text, 'html.parser')
                soup2 = soup.find("div", {"class": "products list items product-items"})
                soup2 = soup2.findAll("div", {"class": "col-xs-12 col-sm-6"})
                for sup in soup2:
                    title = sup.find("div", {"class": "song-title"}).select('a')[0].string
                    artist = sup.find("div", {"class": "artist-name"}).select('a')[0].string
                    id = re.search('filename": "(.*).MP3', str(sup)).group(1)
                    try:
                        extra = sup.find("p", {"class": "song-version"}).string
                        print(str(x) + ") " + str(artist) + ": " + str(title) + " [" + str(extra) + "]")
                        x = x + 1
                    except:
                        print(str(x) + ") " + str(artist) + ": " + str(title))
                        x = x + 1
                    index.append(int(id))
                    titles.append(title)
                    artists.append(artist)

        else:
            try:
                soup2 = soup.find("div", {"class": "products list items product-items"})
                soup2 = soup2.findAll("div", {"class": "col-xs-12 col-sm-6"})
                for sup in soup2:
                    title = sup.find("div", {"class": "song-title"}).select('a')[0].string
                    artist = sup.find("div", {"class": "artist-name"}).select('a')[0].string
                    id = re.search('filename": "(.*).MP3', str(sup)).group(1)
                    try:
                        extra = sup.find("p", {"class": "song-version"}).string
                        print(str(x) + ") " + str(artist) + ": " + str(title) + " [" + str(extra) + "]")
                        x = x + 1
                    except:
                        print(str(x) + ") " + str(artist) + ": " + str(title))
                        x = x + 1
                    index.append(int(id))
                    titles.append(title)
                    artists.append(artist)
            except:
                try:
                    soup2 = soup.find("main", {"page-main container"})
                    soup2 = soup2.find("div", {"class": "col-xs-12 col-md-8"})
                    title = soup2.find("span", {"class": "base"}).string
                    artist = soup2.find("a", {"class": "product-main-artist"}).string
                    id = re.search('filename": "(.*).MP3', str(soup2)).group(1)
                    index.append(int(id))
                    titles.append(title)
                    artists.append(artist)
                    try:
                        extra = sup.find("p", {"class": "song-version"}).string
                        print(str(0) + ") " + str(artist) + ": " + str(title) + " [" + str(extra) + "]")
                    except:
                        print(str(0) + ") " + str(artist) + ": " + str(title))
                except:
                    pass
    except:
        pass


    return index, artists, titles

#search_song("calcutta")

