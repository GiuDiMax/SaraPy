# from song_service import song_serv
# from information import get_info
from spotinfo import spotysearch
from song_service2 import song_serv3
from search_song_service import search_song
from search_midi import search2
import datetime

def select(inputa, a):
    inputa = int(inputa)
    value = index[inputa]
    try:
        int(value)
        url = str('https://mp3-karaoke.org/song-samples/MID/' + str(value) + ".MP3")
    except:
        if "s_" in value:
            value = value.replace("s_","")
            url = 'https://www.mididb.com/midi-download/' + str(value) + '_prt.mp3'
        else:
            url = 'https://www.supreme-network.com' + str(value)
    print("Canzone numero " + str(a+1) + ": " +str(url))
    import os
    os.system("start \"\" " + str(url))
    word_to_reaplace = ['Feat.',"(",")"]
    title_search = titles[inputa]
    for word in word_to_reaplace:
        title_search = title_search.replace(word,"")
    artist_search = artists[inputa]
    spotysearch(title_search, artist_search)
    a = a + 1
    file1 = open(str(datetime.datetime.now().date()) + ".txt", "a")
    file1.write("\n" + str(datetime.datetime.now().strftime("%H:%M")) + " | " + str(a) + ") " + str(
        artists[inputa] + " - " + str(titles[inputa])))
    file1.close()
    return a
    # from playsound import playsound
    # playsound(url)

file1 = open(str(datetime.datetime.now().date()) +".txt", "a+")
file1 = open(str(datetime.datetime.now().date()) +".txt", "r+")
a = 0
lineList = file1.readlines()
if lineList == []:
    file1.write("SARABANDA!\n")
    file1.write("Gioco del: " + str(datetime.datetime.now().strftime("%Y-%m-%d %H:%M"))+str("\n"))
    file1.close()
else:
    if ")" in str(lineList):
        a = lineList[-1]
        a = a.split("| ", 1)[1]
        a = int(a.split(")", 1)[0])

exit = False
while exit != True:
    inputa = input("\nQuale canzone vuoi ascoltare? Invio per canzoni casuali ")
    if inputa == "":
        index, artists, titles = song_serv3()
    elif (inputa.isnumeric()):
        try:
            a = select(inputa, a)
        except:
            print("Valore inesatto!")
            pass
    else:
        index, artists, titles = search_song(inputa)
        index2, artists2, titles2 = search2(inputa, len(index))
        index = index+index2
        artists = artists+artists2
        titles = titles+titles2
        if index == []:
            print("Nessun risultato :(")
