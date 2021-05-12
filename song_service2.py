from random import randint
import requests
from bs4 import BeautifulSoup
import re
import asyncio
import time
import aiohttp

'''
async def main(urls):
    index = []
    artists = []
    titles = []
    loop = asyncio.get_event_loop()
    future = []
    response = []
    x = 0
    for url in urls:
        future.append(loop.run_in_executor(None, requests.get, url))
    for fut in future:
        response.append(await fut)
    for res in response:
        rand = []
        soup = BeautifulSoup(res.text, 'html.parser')
        soup = soup.find("div", {"class": "products list items product-items"})
        try:
            soupx = soup.findAll("div", {"class": "col-xs-12 col-sm-6"})
        except:
            print("ERRORE NON PREVISTO!")
            break
        rand.append(randint(0, 15))
        while True:
            random = randint(0, 15)
            if random not in rand:
                rand.append(random)
                break
        y = - 1
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
                print(str(x + y) + ") " + str(artist) + ": " + str(title) + " [" + str(extra) + "]")
            except:
                print(str(x + y) + ") " + str(artist) + ": " + str(title))
        x = x + 2
    return index, titles, artists


def song_serv2():
    print("\nRicerco nuovi brani...")
    urls = []
    print("")
    url = "http://songservice.it/midi-karaoke?p="
    for x in range(5):
        pag_value = randint(1, 808)
        urls.append(str(url) + str(pag_value))
    loop = asyncio.get_event_loop()
    index, titles, artists = loop.run_until_complete(main(urls))
    return index, artists, titles
'''

index = []
artists = []
titles = []
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
        index.append(int(id))
        titles.append(title)
        artists.append(artist)
        try:
            extra = soup.find("p", {"class": "song-version"}).string
            print(str(numeri) + ") " + str(artist) + ": " + str(title) + " [" + str(extra) + "]")
            numeri = numeri + 1
        except:
            print(str(numeri) + ") " + str(artist) + ": " + str(title))
            numeri = numeri + 1


async def song_serv4(urls):
    async with aiohttp.ClientSession() as session:
        await asyncio.gather(*[get(url, session) for url in urls])

def song_serv3():
    global numeri, index, artists, titles
    index = []
    artists = []
    titles = []
    numeri = 0
    print("\nRicerco nuovi brani...")
    urls = []
    print("")
    url = "http://songservice.it/midi-karaoke?p="
    for x in range(10):
        pag_value = randint(1, 808)
        urls.append(str(url) + str(pag_value))
    asyncio.get_event_loop().run_until_complete(song_serv4(urls))
    return index, artists, titles
