from app.models.abstraction.AbstractDatabase import AbstractDatabase
from typing import List


def importer_donnees(mp3_list:List, db: AbstractDatabase):
    db.connect()
    for mp3 in mp3_list:
        db.insert_mp3(mp3)
    db.close()