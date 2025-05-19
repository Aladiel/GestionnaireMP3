class Genre:

    def __init__(self, id_genre, name_genre: str):
        self.__id_genre = id_genre
        self.__name_genre = name_genre


    @property
    def id_genre(self):
        return self.__id_genre

    @id_genre.setter
    def id_genre(self, value):
        self.__id_genre = value


    @property
    def name_genre(self):
        return self.__name_genre

    @name_genre.setter
    def name_genre(self, value):
        self.__name_genre = value
