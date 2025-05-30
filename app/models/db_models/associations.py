from app.services.sqlalchemyManager import *
from sqlalchemy import Table

artists_mp3 = Table('artists_mp3',
                    Base.metadata,
                    Column('artist_id', Integer, ForeignKey('artists.id')),
                    Column('mp3_id', Integer, ForeignKey('mp3.id'))
                    )


playlists_mp3 = Table('playlists_mp3',
                      Base.metadata,
                      Column('playlist_id', Integer, ForeignKey('playlists.id')),
                      Column('mp3_id', Integer, ForeignKey('mp3.id'))
                      )

genres_mp3 = Table('genre_mp3',
                  Base.metadata,
                  Column('genre_id', Integer, ForeignKey('genres.id')),
                  Column('mp3_id', Integer, ForeignKey('mp3.id'))
                  )