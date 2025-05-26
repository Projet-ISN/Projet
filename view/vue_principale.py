import tkinter as tk
from tkinter import messagebox
from creation_compte import Creation_compte #À corriger avec le nom du fichier correct

class VuePrincipale(tk.Tk):
    def __init__(self):
        super().__init__()
        self.geometry("450x300")
        self.title("INTERFACE DE CONNEXION")
        
        
        self.user_label = tk.Label(self, text='Username :')
        self.user_entry = tk.Entry(self)
        
        self.password_label = tk.Label(self, text='Mot de passe :')
        self.password_entry = tk.Entry(self)
        
        self.validate_button = tk.Button(self, text='Valider')
        self.password_perdu = tk.Button(self, text='Mot de passe oublié ?')
        self.new_user = tk.Button(self, text='Créer un nouveau compte')
        
        self.user_label.grid(row=1, column=1)
        self.user_entry.grid(row=1, column=2)
        self.password_label.grid(row=2, column=1)
        self.password_entry.grid(row=2, column=2)
        
        self.validate_button.grid(row=3, column=1, columnspan=2)
        self.password_perdu.grid(row=4, column=1)
        self.new_user.grid(row=4,column=4)
        
        self.password_perdu.bind('<Button-1>', self.mot_de_passe_perdu)
        self.new_user.bind('<Button-1>', self.creer_nouveau_compte)
        
        
    #def valider_utilisateur(self, event):
        
        
        
    def mot_de_passe_perdu(self,event):
        messagebox.showinfo(message="Dommage :(")
        
        
    def creer_nouveau_compte(self, event):
        self.destroy()
        nouvelle_interface = Creation_compte(self)
        
        

app = VuePrincipale()
app.mainloop()