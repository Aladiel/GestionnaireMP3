import os
from app.models.MP3 import MP3
import music_tag
from mutagen.mp3 import MP3 as MutagenMP3
from pathlib import Path

# Chemin vers un fichier MP3 réel pour tester
base = os.path.dirname(__file__)
FICHIER_TEST = os.path.join(base, "fichiers_mp3", "Khazad-Dûm.mp3")
dossier = Path("fichiers_mp3")

def get_mp3_in_file():
    for file in dossier.glob("*.mp3"):
        yield file

def test():
    for mp3 in get_mp3_in_file():
        file = MP3(mp3)
        file.extract_metadata()

        print(file.title)
        print(file.artist)
        print(file.album)
        print(file.genre)
        print(file.track_number)
        print(file.duration, "\n")




def test_mp3_class():
    if not os.path.exists(FICHIER_TEST):
        print(f"⚠️ Fichier MP3 introuvable : {FICHIER_TEST}")
        return

    print(f"🧪 Test de lecture pour : {FICHIER_TEST}")
    f = music_tag.load_file(FICHIER_TEST)
    fm = MutagenMP3(FICHIER_TEST)
    mp3 = MP3(FICHIER_TEST)

    print(str(f['title']))
    print(str(f['artist']))
    print(str(f['album']))
    print(str(f['genre']))
    print(f['track_number'].value)
    print(round(fm.info.length, 2))



    # print("🎵 Infos récupérées :")
    # print(f"  Titre     : {mp3.title}")
    # print(f"  Artiste   : {mp3.artist}")
    # print(f"  Album     : {mp3.album}")
    # print(f"  Genre     : {mp3.genre}")
    # print(f"  Piste     : {mp3.track_number}")
    # print(f"  Durée     : {mp3.duration} sec")


if __name__ == "__main__":
    test()
