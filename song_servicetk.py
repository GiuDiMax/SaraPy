from random import randint
from bs4 import BeautifulSoup
import re
import asyncio
import aiohttp

index = []
artists = []
titles = []
extras = []
numeri = 0

async def get(url, session):
    global numeri, index, artists, titles
    async with session.get(url=url) as response:
        resp = await response.read()
        soup = BeautifulSoup(resp, 'lxml')
        soup = soup.find("div", {"class": "products list items product-items"})
        try:
            soupx = soup.findAll("div", {"class": "col-xs-12 col-sm-6"})
        except:
            print("ERRORE NON PREVISTO!")
        soup = soupx[randint(0, 15)]
        title = soup.find("div", {"class": "song-title"}).select('a')[0].string
        artist = soup.find("div", {"class": "artist-name"}).select('a')[0].string
        id = re.search('filename": "(.*).MP3', str(soup)).group(1)
        index.append('https://mp3-karaoke.org/song-samples/MID/'+id+'.mp3')
        titles.append(title)
        artists.append(artist)
        try:
            extra = soup.find("p", {"class": "song-version"}).string
            extras.append(" ["+str(extra)+"]")
        except:
            extras.append("")
        numeri = numeri + 1


async def song_serv4(urls):
    async with aiohttp.ClientSession() as session:
        await asyncio.gather(*[get(url, session) for url in urls])

def song_serv3():
    global numeri, index, artists, titles, extras
    index = []
    artists = []
    titles = []
    numeri = 0
    #print("\nRicerco nuovi brani...")
    urls = []
    url = "http://songservice.it/midi-karaoke?p="
    for x in range(10):
        pag_value = randint(1, 808)
        urls.append(str(url) + str(pag_value))
    asyncio.get_event_loop().run_until_complete(song_serv4(urls))
    return index, artists, titles, extras
