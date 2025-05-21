import os

from app import create_app
from app.models import MP3
from app.models.database.SQLiteDatabase import SQLiteDatabase
from app.services.mp3_manager import importer_donnees

app = create_app()

db = SQLiteDatabase("data/gestionnaire.db")


mp3_list = []   #TODO : implémenter un moyen de récupérer une liste de mp3 contenus dans un dossier et la stocker dans cette variable sous forme de liste
importer_donnees(mp3_list, db)

if __name__ == "__main__":
    app.run(debug=True)
