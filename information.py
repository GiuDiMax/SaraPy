import musicbrainzngs

def get_info(artist, title):
    musicbrainzngs.auth("GiuDiMax", "eDua?#rSVxU4A*R")
    musicbrainzngs.set_useragent(app="0.4.7", version="2")

    # OTTIENI INFORMAZIONI ALBUM
    resultx = musicbrainzngs.search_recordings(query=title, artist=artist)
    results = resultx['recording-list'][0]
    titolo = results['title']
    print("\nTITOLO: " +str(titolo))
    artistiss = ""
    artist1 = results['artist-credit']
    for art in artist1:
        try:
            artistiss = artistiss + str(" ") + str(art['name'])
        except:
            pass
    print("ARTISTI: " + str(artistiss[1:]))

    final_album = []
    final_single = []
    final_EP = []
    for alfa in resultx['recording-list']:
        if alfa['title'] == titolo and alfa['artist-credit'][0]['name'] in artistiss:
            try:
                release = alfa['release-list']
            except:
                pass
            for rel in release:
                try:
                    rel['release-group']['secondary-type-list']
                except:
                    type = rel['release-group']['type']
                    title = rel['release-group']['title']
                    try:
                        date = rel['date'][0:4]
                    except:
                        date = 9999
                    if type == "Album":
                        if final_album != []:
                            try:
                                date = int(date)
                            except:
                                date = 9999
                            if date < int(final_album[1]):
                                final_album = [title, date]
                        else:
                            final_album = [title, date]
                    elif type == "Single":
                        if final_single != []:
                            try:
                                date = int(date)
                            except:
                                date = 9999
                            if date < int(final_single[1]):
                                final_single = [title, date]
                        else:
                            final_single = [title, date]
                    elif type == "EP":
                        if final_EP != []:
                            try:
                                date = int(date)
                            except:
                                date = 9999
                            if date < int(final_EP[1]):
                                final_EP = [title, date]
                        else:
                            final_EP = [title, date]
                    else:
                        pass
    try:
        print("ALBUM: " + str(final_album[0]) + " (" +str(final_album[1]) + ")")
    except:
        pass
    try:
        print("SINGLE: " + str(final_single[0]) + " (" + str(final_single[1]) + ")")
    except:
        pass
    try:
        print("EP: " + str(final_EP[0]) + " (" + str(final_EP[1]) + ")")
    except:
        pass