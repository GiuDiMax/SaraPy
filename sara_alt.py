from tkinter import ttk
import tkinter as tk
from PIL import ImageTk, Image
import vlc
from deezer_ext import search
import requests

root = tk.Tk(className='Sarabanda stricche e stricche [DEEZER VERSION]')
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

infobrano = tk.StringVar()
labelbrano = tk.Label(root, textvariable=infobrano, anchor='c')
labelbrano.place(x=300, y=290)
infobrano.set("CLICCA SU CASUALI PER INIZIARE!")
track_list = []


def updatepic(picurl):
    image1 = Image.open(requests.get(picurl, stream=True).raw)
    image1 = image1.resize((250, 250), Image.ANTIALIAS)
    test = ImageTk.PhotoImage(image1)
    label1 = tk.Label(image=test)
    label1.image = test
    label1.place(x=685, y=10)

updatepic("https://www.caffeinamagazine.it/wp-content/uploads/2016/10/12papiqua.png")

def PlayMusic():
    global p, url, track_list
    try:
        ind = int((tree.item(tree.focus())['values'][0]))
        url2 = track_list[ind].preview
        if url == url2:
            p.play()
        else:
            p.stop()
            url = url2
            p = vlc.MediaPlayer(url)
            p.play()

    except:
        p.play()

def PauseMusic():
    p.pause()

def StopMusic():
    p.stop()

def Random():
    global track_list
    for i in tree.get_children():
        tree.delete(i)
    track_list = search()
    for i in range(len(track_list)):
        tree.insert("", tk.END, values=[i, track_list[i].title, track_list[i].artist])

def Search():
    global links, artists, titles, extras
    for i in tree.get_children():
        tree.delete(i)
    #links, artists, titles, albums = search_song(searchstring.get())
    for i in range(len(links)):
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
