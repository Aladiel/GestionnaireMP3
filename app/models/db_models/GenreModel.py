from app.models.db_models.associations import genres_mp3
from app.services.sqlalchemyManager import *

class Genre(SQLManager.Base):
    __tablename__ = 'genres'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(50))

    mp3 = relationship('MP3', secondary=genres_mp3, back_populates='genres')

    def __repr__(self):
        return f'<Genre: {self.name}>'