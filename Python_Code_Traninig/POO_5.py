"""
============================================================
   Description   : Inroduction  in POO  python.
   Auteur        : MAZA Kossivi Renaud
   Date          : 12/03/2025
   Niveau        : 2ème année Prépa Informatique
   Établissement : École Polytechnique de Lomé
   Environnement : pycharm
   Langage       : python 3.12
   Licence       : Freecodecamp

 ============================================================
"""
class Chat:
    def __init__(self, nom_facfultatif = "inconnu"):
        self.nom = nom_facfultatif

    def SePresenter(self):
        print(f"Bonjour, je suis un chat et je m'appelle  {self.nom}" )

# ---
class Personne:
    def __init__(self, nom: str):
        self.nom = nom

    def SePresenter(self):
        print(f"Bonjour, je suis une personne et je m'appelle  {self.nom}" )

if __name__ == "__main__":


    chat1 = Chat()
    chat1.SePresenter()  # Bonjour, je suis un chat et je m'appelle inconnu

    chat2 = Chat("Garfield")
    chat2.SePresenter()  # Bonjour, je suis un chat et je m'appelle Garfield

    personne = Personne("Jean")
    personne.SePresenter()  # Bonjour, je suis une personne et je m'appelle Jean
