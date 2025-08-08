class MusicDAO:
    def __init__(self, db_connection):
        self.conn = db_connection

    def get_music_by_id(self, music_id):
        cur = self.conn.cursor()
        cur.execute("SELECT * FROM musics WHERE id = %s", (music_id,))
        return cur.fetchone()

    def insert_music(self, music):
        cur = self.conn.cursor()
        cur.execute("""
            INSERT INTO musics (user_id, title, filepath, filesize, duration_seconds)
            VALUES (%s, %s, %s, %s, %s)
        """, (music.user_id, music.title, music.filepath, music.fileSize, music.durre))
        self.conn.commit()
