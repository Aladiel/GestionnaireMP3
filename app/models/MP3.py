import music_tag

from typing import Optional
from app.models.abstraction.AudioFile import AudioFile


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

            if str(f['artist']) in BDD:
                db.query.get(artist_name['name_artist'])   ## --> c'est de la merde, à revoir
            else:
                self.__artist = str(f['artist'])

            if str(f['album']) in BDD:
                db.query.get(album_name['name_album'])  ## --> c'est de la merde, à revoir
            else:
                self.__album = str(f['album'])

            if str(f['genre']) in BDD:
                db.query.get(genre['genre'])  ## --> c'est de la merde, à revoir
            else:
                self.__genre = str(f['genre'])

            self.__title = str(f['title'])
            self.__track_number = f['track_number'].value

        except Exception as e:
            print(f"Erreur lecture des metadata avec music-tag : {e}")

    def get_duration(self) -> float:
        try:
            f = music_tag.load_file(self.filepath)
            return round(f.length, 2)
        except Exception:
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