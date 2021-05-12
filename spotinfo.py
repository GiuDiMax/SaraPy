import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
from difflib import SequenceMatcher

def spotysearch(title, artist):
    artist = artist.lower().replace(" e ", " ").replace(" ft. ", " ").replace(" - ", " ").replace(" & ", " ")
    sp = spotipy.Spotify(auth_manager=SpotifyClientCredentials(client_id="dd99ad9f983d4e2fa36a1b07e2c3efb7",
                                                               client_secret="452a2625506a4583aeec992225314490"))

    results = sp.search(q=str(str(title)+" "+str(artist)), limit=10)
    results = results['tracks']['items']
    final_album = [] #TIPO - NOME BRANO - ARTISTA - NOME ALBUM - ANNO
    final_single = []
    for res in results:
        nome = res['name']
        nome_album = res['album']['name']
        data = res['album']['release_date'][:4]
        tipo = res['album']['album_type']
        artisti = res['album']['artists']
        string_art = ""
        for art in artisti:
            string_art = string_art + ", " + str(art['name'])
        artisty = string_art[2:]
        ratio_title = SequenceMatcher(None, title.lower(), nome.lower()).ratio()
        ratio_artist = SequenceMatcher(None, artist.lower(), artisty.lower()).ratio()
        if "live" not in nome.lower() and "live" not in nome_album.lower():
            if tipo == "album" and ratio_title > 0.5 and ratio_artist > 0.7:
                if final_album != []:
                    if int(data) < int(final_album[4]):
                        final_album = [tipo, nome, artisty, nome_album, data]
                else:
                    final_album = [tipo, nome, artisty, nome_album, data]
            if tipo == "single" and ratio_title > 0.5 and ratio_artist > 0.7:
                if final_single != []:
                    if int(data) < int(final_single[4]):
                        final_single = [tipo, nome, artisty, nome_album, data]
                else:
                    final_single = [tipo, nome, artisty, nome_album, data]

    if final_album == [] and final_single == []:
        try:
            results = sp.search(q=str(str(title) + " " + str(artist)), limit=1)
            try:
                res = results['tracks']['items'][0]
            except:
                res = results['tracks']['items']
            try:
                nome = res['name']
            except:
                nome = ""
            nome_album = res['album']['name']
            data = res['album']['release_date'][:4]
            tipo = res['album']['album_type']
            artisti = res['album']['artists']
            string_art = ""
            for art in artisti:
                string_art = string_art + ", " + str(art['name'])
            artisty = string_art[2:]
            print("RISULTATO FORZATO!")
            print("\nTITOLO: " + str(nome))
            print("ARTISTA: " + str(artisty))
            print(str(tipo).upper() + ": " + str(nome_album) + " (" + str(data) + ")")
        except:
            print("NON TROVATO!")

    if final_album != []:
        print("\nTITOLO: " + str(final_album[1]))
        print("ARTISTA: " + str(final_album[2]))
        print("ALBUM: " + str(final_album[3]) + " (" +str(final_album[4]) + ")")
        if final_single != []:
            print("SINGOLO/EP: " + str(final_single[3]) + " (" + str(final_single[4]) + ")")
    elif final_single != []:
        print("\nTITOLO: " + str(final_single[1]))
        print("ARTISTA: " + str(final_single[2]))
        print("SINGOLO/EP: " + str(final_single[3]) + " (" +str(final_single[4]) + ")")

#spotysearch("La Canzone Del Sole", "lucio battisti")