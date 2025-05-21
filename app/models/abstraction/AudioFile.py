from abc import ABC, abstractmethod
import os

class AudioFile(ABC):
    def __init__(self, filepath: str):
        if not os.path.isfile(filepath):
            raise FileNotFoundError(f"Fichier introuvable : {filepath}")
        self.filepath = filepath

    @abstractmethod
    def extract_metadata(self):
        pass

    @abstractmethod
    def get_duration(self) -> float:
        pass
