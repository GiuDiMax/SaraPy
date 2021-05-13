from tkinter import ttk
import tkinter as tk
from PIL import ImageTk, Image
import vlc
from song_servicetk import song_serv3
import requests
from spotinfotk import spotysearch
from search_songservtk import search_song
from search_miditk import search2
from getmidismp3 import getmidismp3, checkin
from deezer_search import deez_search
import datetime

checkdb3 = checkin()
root = tk.Tk(className='Sarabanda stricche e stricche')
root.geometry("950x370")
url = 'ciao'
p = vlc.MediaPlayer(url)
tree = ttk.Treeview(root, column=("c1", "c2", "c3"), show='headings')
tree.column("#1", anchor=tk.CENTER, width=20)
tree.heading("#1", text="ID")
tree.column("#2", anchor=tk.CENTER, width=380)
tree.heading("#2", text="Titolo")
tree.column("#3", anchor=tk.CENTER, width=260)
tree.heading("#3", text="Artista")
tree.place(x=10, y=10)
index = []
artists = []
titles = []

infobrano = tk.StringVar()
labelbrano = tk.Label(root, textvariable=infobrano, anchor='c')
labelbrano.place(x=300, y=290)
infobrano.set("CLICCA SU CASUALI PER INIZIARE!")

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

if checkdb3:
    var1 = tk.IntVar()
    c1 = tk.Checkbutton(root, text='Database 3', variable=var1, onvalue=1, offvalue=0)
    c1.place(x=425, y=240)

var2 = tk.IntVar()
c2 = tk.Checkbutton(root, text='No Midi', variable=var2, onvalue=1, offvalue=0)
c2.place(x=425, y=260)

def updatepic(picurl):
    image1 = Image.open(requests.get(picurl, stream=True).raw)
    image1 = image1.resize((250, 250), Image.ANTIALIAS)
    test = ImageTk.PhotoImage(image1)
    label1 = tk.Label(image=test)
    label1.image = test
    label1.place(x=685, y=10)

updatepic("https://www.caffeinamagazine.it/wp-content/uploads/2016/10/12papiqua.png")

def PlayMusic():
    global p, url, a
    try:
        ind = int((tree.item(tree.focus())['values'][0]) - 1)
        url2 = index[ind]
        if url == url2:
            p.play()
        else:
            p.stop()
            url = url2
            if 'midis' in url:
                try:
                    url = getmidismp3(url)
                except:
                    pass
            p = vlc.MediaPlayer(url)
            p.play()
            artist_search = artists[ind]
            title_search = titles[ind]
            word_to_replace = ['Feat.', 'ft.', "(", ")"]
            for word in word_to_replace:
                title_search = title_search.replace(word, "")
                artist_search = artist_search.replace(word, "")
            final_album, final_single, forced = spotysearch(title_search, artist_search)
            # TIPO - NOME BRANO - ARTISTA - NOME ALBUM - ANNO - IMAGE

            a = a + 1
            file1 = open(str(datetime.datetime.now().date()) + ".txt", "a")
            file1.write("\n" + str(datetime.datetime.now().strftime("%H:%M")) + " | " + str(a) + ") " + str(
                artists[ind] + " - " + str(titles[ind])))
            file1.close()

            if len(final_album) > 0 and len(final_single) > 0:
                infobrano.set("Artista: " + final_album[2] +
                              "\nTitolo: " + final_album[1] +
                              "\nAlbum: " + final_album[3] + " (" + final_album[4] + ")" +
                              "\nSingolo/EP: " + final_single[3] + " (" + final_single[4] + ")")
                updatepic(final_single[5])
            elif len(final_album) > 0:
                infobrano.set("Artista: " + final_album[2] +
                              "\nTitolo: " + final_album[1] +
                              "\nAlbum: " + final_album[3] + " (" + final_album[4] + ")")
                updatepic(final_album[5])
            elif len(final_single) > 0:
                infobrano.set("Artista: " + final_single[2] +
                              "\nTitolo: " + final_single[1] +
                              "\nSingle/EP: " + final_single[3] + " (" + final_single[4] + ")")
                updatepic(final_single[5])
            elif len(forced) > 0:
                infobrano.set("Risultato Forzato!"+"\nArtista: " + forced[2] +
                              "\nTitolo: " + forced[1] +
                              "\nAlbum: " + forced[3] + " (" + forced[4] + ")")
                updatepic(forced[5])
            else:
                infobrano.set("INFORMAZIONI BRANO\nNON REPERIBILI")
                updatepic("https://www.caffeinamagazine.it/wp-content/uploads/2016/10/12papiqua.png")

    except:
        p.play()

def PauseMusic():
    p.pause()

def StopMusic():
    p.stop()

def Random():
    global index, artists, titles, extras
    index = []
    artists = []
    titles = []
    extras = []
    for i in tree.get_children():
        tree.delete(i)
    index, artists, titles, extras = song_serv3()
    for i in range(10):
        tree.insert("", tk.END, values=[i+1, str(titles[i] + extras[i]), artists[i]])

def Search():
    global index, artists, titles, extras
    for i in tree.get_children():
        tree.delete(i)
    index = []
    artists = []
    titles = []
    extras = []
    if var2.get() == 0:
        index, artists, titles, extras = search_song(searchstring.get())
        try:
            check3 = var1.get()
        except:
            check3 = 0
        index2, artists2, titles2, extras2 = search2(searchstring.get(), check3)
        index = index+index2
        artists = artists+artists2
        titles = titles + titles2
        extras = extras + extras2
    else:
        index, artists, titles, extras = deez_search(searchstring.get())
    for i in range(len(index)):
        tree.insert("", tk.END, values=[i+1, str(titles[i] + extras[i]), artists[i]])


searchstring = tk.StringVar()
labelricerca = ttk.Entry(root, width=40, textvariable=searchstring)
labelricerca.place(x=80, y=252)
searchstring.set("Inserisci nome artista / brano")
b4 = tk.Button(root, text="Cerca", command=Search)
b4.place(x=350, y=250)

b1 = tk.Button(root, text="Casuali", command=Random)
b1.place(x=10, y=250)
b2 = tk.Button(root, text="Play", command=PlayMusic)
b2.place(x=540, y=250)
b3 = tk.Button(root, text="Pause", command=PauseMusic)
b3.place(x=580, y=250)
b3 = tk.Button(root, text="Stop", command=StopMusic)
b3.place(x=630, y=250)

root.mainloop()
