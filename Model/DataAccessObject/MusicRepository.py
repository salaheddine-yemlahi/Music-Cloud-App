class MusicRepository:
    def __init__(self, music_dao):
        self.dao = music_dao

    def find_by_title(self, title):
        # Logique métier possible ici
        return self.dao.get_music_by_title(title)