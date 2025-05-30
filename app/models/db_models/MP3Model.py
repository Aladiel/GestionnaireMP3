from app.models.db_models.associations import artists_mp3, playlists_mp3, genres_mp3
from app.services.sqlalchemyManager import *

class MP3Model(SQLManager.Base):
    __tablename__ = 'mp3'

    id = Column(Integer, primary_key=True, autoincrement=True)
    title = Column(String(50), nullable=False)
    duration = Column(Float)
    track_number = Column(Integer)
    filepath = Column(String(50), nullable=False)
    id_album = Column(Integer, ForeignKey('albums.id'))

    albums = relationship('Album', back_populates='mp3')
    artists = relationship('Artist', secondary = artists_mp3, back_populates='mp3')
    playlists = relationship('Playlist', secondary = playlists_mp3, back_populates='mp3')
    genre = relationship('Genre', secondary = genres_mp3, back_populates='mp3')

    def __repr__(self):
        return f'<mp3 (id= {self.id})>'