import requests
from bs4 import BeautifulSoup
import re
import lxml

def search_song(string):
    url_final = ''
    artists = []
    titles = []
    index = []
    extras = []
    string = string.replace(" ", "+")
    url_base = 'https://songservice.it/mlivecatalogsearch/result/?attribute-set-id=11&q='
    url = url_base + '&q=' +string
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'lxml')

    try:
        if soup.find("ul", {"class": "items pages-items"}) != None:
            soup2 = soup.find("ul", {"class": "items pages-items"})
            soup2 = soup2.findAll("li", {"class": "item"})
            pag_num = int(len(soup2) - 1)
            for i in range(pag_num):
                url = url_base + '&p=' + str(i + 1) + '&q=' + string
                response = requests.get(url)
                soup = BeautifulSoup(response.text, 'lxml')
                soup2 = soup.find("div", {"class": "products list items product-items"})
                soup2 = soup2.findAll("div", {"class": "col-xs-12 col-sm-6"})
                for sup in soup2:
                    title = sup.find("div", {"class": "song-title"}).select('a')[0].string
                    artist = sup.find("div", {"class": "artist-name"}).select('a')[0].string
                    id = re.search('filename": "(.*).MP3', str(sup)).group(1)
                    try:
                        extra = sup.find("p", {"class": "song-version"}).string
                        extras.append(" ["+str(extra)+"]")
                    except:
                        extras.append("")
                    index.append('https://mp3-karaoke.org/song-samples/MID/'+id+'.mp3')
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
                        extras.append(" ["+str(extra)+"]")
                    except:
                        extras.append("")
                    index.append('https://mp3-karaoke.org/song-samples/MID/'+id+'.mp3')
                    titles.append(title)
                    artists.append(artist)
            except:
                try:
                    soup2 = soup.find("main", {"page-main container"})
                    soup2 = soup2.find("div", {"class": "col-xs-12 col-md-8"})
                    title = soup2.find("span", {"class": "base"}).string
                    artist = soup2.find("a", {"class": "product-main-artist"}).string
                    id = re.search('filename": "(.*).MP3', str(soup2)).group(1)
                    index.append('https://mp3-karaoke.org/song-samples/MID/'+id+'.mp3')
                    titles.append(title)
                    artists.append(artist)
                    try:
                        extra = soup2.find("p", {"class": "song-version"}).string
                        extras.append(" ["+str(extra)+"]")
                    except:
                        extras.append("")
                except:
                    pass
    except:
        pass
    return index, artists, titles, extras

'''
index, artists, titles, extras = search_song("coldplay")
print(index)
print(artists)
print(titles)
print(extras)
'''