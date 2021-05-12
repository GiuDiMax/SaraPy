from selenium import webdriver

def getmidismp3(url):
    chrome_options = webdriver.ChromeOptions()
    chrome_options.headless = True
    driver = webdriver.Chrome('chromedriver.exe', options=chrome_options)
    url = 'https://www.supreme-network.com' + url
    driver.get(url)
    html = driver.page_source
    link = html[html.find("songs_position_url[0] = '") + len("'songs_position_url[0] = "):html.rfind("';\nvar star_icon_path")]
    return link

def checkin():
    try:
        chrome_options = webdriver.ChromeOptions()
        chrome_options.headless = True
        driver = webdriver.Chrome('chromedriver.exe', options=chrome_options)
        return True
    except:
        return False

#getmidismp3('/midis/browse/D/1545-dua-lipa/9488-swan-song')