from abc import ABC, abstractmethod

class AbstractDatabase(ABC):
    @abstractmethod
    def connect(self):
        pass

    @abstractmethod
    def insert_mp3(self, mp3):
        pass

    @abstractmethod
    def get_all_mp3(self):
        pass

    @abstractmethod
    def close(self):
        pass
    ## Autres méthodes à ajouter au besoin