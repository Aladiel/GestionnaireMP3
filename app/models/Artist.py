class Artist:

    def __init__(self, name_artist: str):
        self.__name_artist = name_artist

    @property
    def name_artist(self) -> str:
        return self.__name_artist

    @name_artist.setter
    def name_artist(self, value):
        if not isinstance(value, str):
            raise TypeError("name_artist must be a string")

        self.__name_artist = value.strip().lower()
