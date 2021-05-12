import requests
from bs4 import BeautifulSoup
import lxml
from selenium import webdriver

def search2(stringz, checkin):
    artists = []
    titles = []
    index = []
    extras = []

    try:
        url = 'https://www.mididb.com/search.asp?q=' + str(stringz) + "&formatID=1"
        response = requests.get(url)
        soup = BeautifulSoup(response.text, 'lxml')
        soup2 = soup.findAll("div", {"class": "left song-details"})
        for sup in soup2:
            link = sup.span['id']
            title = sup.find("span", {"class": "song-title to-cart"}).select('a')[0].string
            artist = sup.find("div", {"class": "artist-name"}).select('a')[0].string
            if "s_" in link:
                link = link.replace("s_", "")
            index.append('https://www.mididb.com/midi-download/' + link + '_prt.mp3')
            titles.append(title)
            artists.append(artist)
            extras.append(" [2nd DB]")
    except:
        pass

    if checkin == 1:
        try:
            chrome_options = webdriver.ChromeOptions()
            chrome_options.headless = True
            driver = webdriver.Chrome('chromedriver.exe', options=chrome_options)

            url = 'https://www.supreme-network.com/midis/?searchword=' + stringz.replace(" ", "+") + \
                  '&option=com_muscol&search=albums&view=search&Itemid=327&limit=0&limitstart=0'

            driver.get(url)
            html = driver.page_source
            soup = BeautifulSoup(html, 'lxml')
            soup = soup.findAll("div", {"class": "related"})
            for sup in soup:
                su = str(sup.find("div", {"class": "album_name"}))
                if "MIDI" in str(su):
                    su = su[su.find('<td align="left">') + len('<td align="left">'):su.rfind(" (MIDI File)  </a>")]
                    artist = su.split("<br")[0]
                    link = su[su.find('href="') + len('href="'):su.rfind('">')]
                    title = su.rsplit('> ', 1)[1]
                    index.append(link)
                    titles.append(title)
                    artists.append(artist)
                    extras.append(" [3rd DB]")
        except:
            pass

    return index, artists, titles, extras

#index, artists, titles, extras = search2("Dua lipa")

