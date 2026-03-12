
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

# ---
class Personne:
    def __init__(self, nom: str):
        self.nom = nom

    def SePresenter(self):
        print("Bonjour, je m'appelle " + self.nom)

# ---
noms = []
noms.append(input("nom de la personne 1 : "))
noms.append(input("nom de la personne 2 : "))
noms.append(input("nom de la personne 3 : "))

l = []

for nom in noms:
    l.append(Personne(nom))

for p in l:
    print(p.SePresenter())