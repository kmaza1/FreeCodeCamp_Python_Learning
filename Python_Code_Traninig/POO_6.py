
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
class Personne  :
    def __init__(self, nom: str = ""):
        self.nom = nom
        if nom == "":
            self.Demander_nom()

    def SePresenter(self):
        print("Bonjour, je m'appelle " + self.nom)

    def Demander_nom(self):
        print("Mettez un vrai nom.")
        self.nom = input(f"nom de la personne { i } : ")

if __name__ == "__main__":

    nombre_Personne = int(input("Combien de personne voulez- vous : "))

    noms = []

    for i in range(nombre_Personne):
        input(f"nom de la personne {i+1} : ")

    liste_Personne = []

    for nom  in noms:
        liste_Personne.append(Personne(nom))

    for personne in liste_Personne:
        personne.SePresenter()