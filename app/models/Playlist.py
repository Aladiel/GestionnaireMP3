class Playlist:

    def __init__(self, name_playlist: str, description):
        self.__name_playlist = name_playlist
        self.__description = description
        self.__mp3_list = []

    @property
    def name_playlist(self) -> str:
        return self.__name_playlist

    @name_playlist.setter
    def name_playlist(self, value):
        if not isinstance(value, str):
            raise TypeError("name_playlist must be a string")

        self.__name_playlist = value.strip().lower()

    @property
    def description(self) -> str:
        return self.__description

    @description.setter
    def description(self, value):
        if not isinstance(value, str):
            raise TypeError("description must be a string")

        self.__description = value

    @property
    def mp3_list(self) -> list:
        return self.__mp3_list

    def add_mp3_list(self, mp3):
        # mp3 doit être une instance de la classe MP3
        self.__mp3_list.append(mp3)

    def remove_mp3_list(self, mp3):
        self.__mp3_list.remove(mp3)
