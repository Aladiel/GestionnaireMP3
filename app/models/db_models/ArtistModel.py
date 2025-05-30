from app.models.db_models.associations import artists_mp3
from app.services.sqlalchemyManager import *

class Artist(SQLManager.Base):
    __tablename__ = 'artists'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(50))

    mp3 = relationship('MP3', secondary=artists_mp3, back_populates='artists')

    def __repr__(self):
        return f'<Artist: {self.name}>'