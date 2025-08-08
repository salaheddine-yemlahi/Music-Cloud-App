


class Music:
    def __init__(self, idMusic, title, filepath, fileSize, durree, uploadedAt):
        self.idMusic = idMusic
        self.title = title
        self.filepath = filepath
        self.fileSize = fileSize
        self.durre = durree
        self.uploadedAt = uploadedAt

    def to_dict(self):
        return {
            "id": self.idMusic,
            "title": self.title,
            "filepath": self.filepath,
            "fileSize": self.fileSize,
            "durree": self.durre,
            "uploadedAt": self.uploadedAt
        }

    def afficher_info(self):
        print(f"ID: {self.idMusic}")
        print(f"Titre: {self.title}")
        print(f"Chemin: {self.filepath}")
        print(f"Taille: {self.fileSize} octets")
        print(f"Durée: {self.durre} sec")
        print(f"Uploadé le: {self.uploadedAt}")

    def play(self):
        print(f"Lecture de {self.title} depuis {self.filepath}")