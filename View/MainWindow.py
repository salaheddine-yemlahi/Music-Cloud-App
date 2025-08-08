import tkinter as tk
from tkinter import messagebox, simpledialog, Entry, ttk


class Vue(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("MusicApp 🎵")
        self.geometry("1000x400")
        self.resizable(False, False)
        self.current_user = None
        self.frame_accueil = tk.Frame(self)

        self.header_frame = tk.Frame(self, height=80, bg='lightgray')
        self.header_frame.pack(fill='x', side='top')
        self.header_frame.pack_propagate(False)  # Garde la taille fixe
        self.header_frame.pack_propagate(True)

        self.userNameText = Entry(self.header_frame)
        self.passwordText = Entry(self.header_frame)
        self.buttonConnecter = tk.Button(self.header_frame, text="Connecter")
        self.buttonInscrire = tk.Button(self.header_frame, text="Inscrire")
        self.buttonDeconnecter = tk.Button(self.header_frame, text="Deconnecter")
        self.usernameLabel = tk.Label(self.header_frame, text="username")
        self.passwordLabel = tk.Label(self.header_frame, text="password")

        self.usernameLabel.grid(row=0, column=0)
        self.userNameText.grid(row=0, column=1)
        self.passwordLabel.grid(row=0, column=2)
        self.passwordText.grid(row=0, column=3)
        self.buttonConnecter.grid(row=0, column=4)
        self.buttonInscrire.grid(row=0, column=5)
        self.buttonDeconnecter.grid(row=0, column=6)


        self.main_frame = tk.Frame(self, height=500 , bg='white')
        self.main_frame.pack(fill='x')
        self.main_frame.pack_propagate(True)

        columns = ('ID', 'Titre', 'Chemin', 'Taille', 'Durée', 'Upload')
        self.table = ttk.Treeview(self.main_frame, columns=columns, show='headings')

        self.table.heading('ID', text='ID')
        self.table.heading('Titre', text='Titre')
        self.table.heading('Chemin', text='Chemin du fichier')
        self.table.heading('Taille', text='Taille')
        self.table.heading('Durée', text='Durée')
        self.table.heading('Upload', text='Date Upload')

        # Exemples de données
        self.table.insert('', tk.END, values=(1, 'Ma Chanson', '/music/song1.mp3', '3.2 MB', '3:45', '2024-01-15'))
        self.table.insert('', tk.END, values=(2, 'Autre Song', '/music/song2.mp3', '4.1 MB', '4:12', '2024-01-16'))

        self.table.pack(fill='both', expand=True)

        self.table.grid(row=0, column=0)




        self.frame_accueil.pack(pady=20)


if __name__ == "__main__":
    app = Vue()
    app.mainloop()