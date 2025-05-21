import sqlite3

from app.models.abstraction.AbstractDatabase import AbstractDatabase


class SQLiteDatabase(AbstractDatabase):
    def __init__(self, db_path):
        self.__db_path = db_path
        self.__conn = None

    def connect(self):
        self.__conn = sqlite3.connect(self.__db_path)

    def insert_mp3(self, mp3):
        cursor = self.__conn.cursor()
        cursor.execute(
            "INSERT INTO mp3 (title, artist, album, genre, track_number, duration) VALUES (?, ?, ?, ?, ?, ?)",
            (
                mp3.title,
                mp3.artist,
                mp3.album,
                mp3.genre,
                mp3.track_number,
                mp3.duration
            )
        )
        self.__conn.commit()

    def get_all_mp3(self):
        cursor = self.__conn.cursor()
        cursor.execute("SELECT * FROM mp3")
        return cursor.fetchall()

    def close(self):
        self.__conn.close()
