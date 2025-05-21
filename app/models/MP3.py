import music_tag

from typing import Optional
from app.models.abstraction.AudioFile import AudioFile
from app.models.Genre import Genre
from app.models.Artist import Artist
from app.models.Album import Album


class MP3(AudioFile):
    def __init__(self, filepath:str):
        super().__init__(filepath)
        self.__title:Optional[str] = None
        self.__artist:Optional[Artist] = None
        self.__album:Optional[Album] = None
        self.__genre :Optional[Genre] = None
        self.__track_number:Optional[str] = None
        self.__duration:float = self.get_duration()

    def extract_metadata(self):
        try:
            f = music_tag.load_file(self.filepath)

            # if str(f['artist']) in BDD:
            #     db.query.get(artist_name['name_artist'])   ## --> c'est de la merde, à revoir
            # else:
            #     self.__artist = str(f['artist'])
            #
            # if str(f['album']) in BDD:
            #     db.query.get(album_name['name_album'])  ## --> c'est de la merde, à revoir
            # else:
            #     self.__album = str(f['album'])
            #
            # if str(f['genre']) in BDD:
            #     db.query.get(genre['genre'])  ## --> c'est de la merde, à revoir
            # else:
            #     self.__genre = str(f['genre'])
            self.__title = str(f['title'])
            self.__artist = str(f['artist'])
            self.__album = str(f['album'])
            self.__genre = str(f['genre'])
            self.__track_number = f['track_number'].value
            self.__duration = self.__get_duration

        except Exception as e:
            print(f"Erreur lecture des metadata avec music-tag : {e}")


    def __get_duration(self, music_tag_obj) -> float:
        # Essai avec music-tag (si disponible)
        try:
            return round(music_tag_obj.length, 2)
        except AttributeError:
            pass  # continue vers fallback mutagen

        # Fallback avec mutagen
        try:
            from mutagen.mp3 import MP3 as MutagenMP3
            audio = MutagenMP3(self.filepath)
            return round(audio.info.length, 2)
        except Exception as e:
            print(f"[Erreur] Durée non récupérable : {e}")
            return 0.0


    @property
    def title(self) -> str:
        return self.__title
    @property
    def artist(self) -> Artist:
        return self.__artist
    @property
    def album(self) -> Album:
        return self.__album
    @property
    def genre(self) -> Genre:
        return self.__genre
    @property
    def track_number(self) -> str:
        return self.__track_number
    @property
    def duration(self) -> float:
        return self.__duration