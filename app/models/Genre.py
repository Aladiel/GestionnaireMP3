class Genre:

    def __init__(self, name_genre: str):
        self.__name_genre = name_genre

    @property
    def name_genre(self) -> str:
        return self.__name_genre

    @name_genre.setter
    def name_genre(self, value):
        if not isinstance(value, str):
            raise TypeError("name_genre must be a string")

        self.__name_genre = value.strip().lower()
