from app.models.Artist import Artist

class Album:
    def __init__(self, name_album: str, artist: Artist, artwork: str = "", label: str = ""):
        self.name_album = name_album
        self.artist = artist
        self.artwork = artwork
        self.label = label


    @property
    def name_album(self) -> str:
        return self.__name_album

    @name_album.setter
    def name_album(self, value):
        if not isinstance(value, str):
            raise TypeError("name_album doit être une chaîne")
        self.__name_album = value.strip()


    @property
    def artist(self) -> Artist:
        return self.__artist

    @artist.setter
    def artist(self, value):
        if not isinstance(value, Artist):
            raise TypeError("artist doit être une instance de la classe Artist")
        self.__artist = value


    @property
    def artwork(self) -> str:
        return self.__artwork

    @artwork.setter
    def artwork(self, value):
        if not isinstance(value, str):
            raise TypeError("artwork doit être une chaîne, le chemin vers l'image")
        self.__artwork = value.strip()


    @property
    def label(self) -> str:
        return self.__label

    @label.setter
    def label(self, value):
        if not isinstance(value, str):
            raise TypeError("label doit être une chaîne")
        self.__label = value.strip()