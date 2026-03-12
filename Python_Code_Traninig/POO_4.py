"""
============================================================
   Description   : Inroduction  in POO  python.
   Auteur        : MAZA Kossivi Renaud
   Date          : 11/03/2025
   Niveau        : 2ème année Prépa Informatique
   Établissement : École Polytechnique de Lomé
   Environnement : pycharm
   Langage       : python 3.12
   Licence       : Freecodecamp

 ============================================================
"""
# POO EXERCICE DE MISE EN SITUATION 2
class Personne:
    def __init__(self, nom: str , age: int):
        self.nom = nom   # crée une variable d'instance : nom
        self.age = age
        print("Constructeur personne " + self.nom)

    def SePresenter(self):
        # Bonjour, je m'appelle Jean, j'ai 30 ans
        # Je suis majeur
        print("Bonjour, je m'appelle " + self.nom + ", j'ai " + str(self.age) + " ans")

        Maturite = "Je suis majeur" if self.EstMajeur() else "Je suis mineur"
        print(Maturite)

        print()

    def EstMajeur(self):
        return self.age >= 18


personne1 = Personne("Jean",25)
personne1.SePresenter()

personne2 = Personne("Emilie", 17)
personne2.SePresenter()
tuple = (personne1, personne2)
tuple[0].SePresenter()