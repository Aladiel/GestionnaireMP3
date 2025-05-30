from sqlalchemy import create_engine, Column, String, Integer,Float, ForeignKey
from sqlalchemy.orm import sessionmaker, declarative_base, relationship


class SQLManager:
    def __init__(self, engine):
        # la chaine de caractère de connection ne doit pas apparaitre en dur
        # self.__engine = create_engine('Server=localhost;Database=gestionnaire_mp3;TrustedConnection=True;', echo=True)
        self.__Base = declarative_base()

    @property
    def Base(self):
        return self.__Base
