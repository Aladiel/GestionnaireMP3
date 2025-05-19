from abc import ABC, abstractmethod


class AudioFile(ABC):
    def __init__(self, filename):
        self.__filename = filename
        # Variable extension ? Récupérer le .mp3 ou autre ?

    @abstractmethod
    def filename(self):
        pass
    @abstractmethod
    def get_artist(self):
        pass
    @abstractmethod
    def get_title(self):
        pass
    @abstractmethod
    def get_album(self):
        pass
    @abstractmethod
    def get_genre(self):
        pass
    @abstractmethod
    def get_duration(self):
        pass
