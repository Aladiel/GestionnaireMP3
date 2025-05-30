from app.services.sqlalchemyManager import *

class Artist(SQLManager.Base):
    __tablename__ = 'artists'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(50))
    year = Column(Integer)
    label = Column(String(50))
    artwork_url = Column(String(200))
    id_artist = Column(Integer, ForeignKey('artists.id'))

    mp3 = relationship('MP3', back_populates='artists')
    artists = relationship('Artist', back_populates='mp3')

    def __repr__(self):
        return f'<Artist: {self.name}>'