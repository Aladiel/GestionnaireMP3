from abc import ABC, abstractmethod
import os
from pathlib import Path

class AudioFile(ABC):
    def __init__(self, filepath: Path):
        if not os.path.isfile(filepath):
            raise FileNotFoundError(f"Fichier introuvable : {filepath}")
        self.filepath = filepath

    @abstractmethod
    def extract_metadata(self):
        pass

    @abstractmethod
    def get_duration(self, music_tag_obj) -> float:
        pass
