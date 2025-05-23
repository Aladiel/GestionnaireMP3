from app.models.abstraction.AbstractDatabase import AbstractDatabase


class SQLServerDatabase(AbstractDatabase):

    conn ='Server=localhost;Database=gestionnaire_mp3;TrustedConnection=True;'

    # TODO : connection SQLServer
    #   - Stockage des métadonnées
    #   - Récupération données
    #   - Fonction de filtre
    #   - Interface Graphique
    #   - Redirection de fichiers
    #   - Gestion de playlists
    #   - finir sieste