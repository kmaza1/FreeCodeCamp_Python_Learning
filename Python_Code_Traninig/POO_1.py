"""
============================================================
   Description   : Inroduction  in POO  python.
   Auteur        : MAZA Kossivi Renaud
   Date          : 09/03/2025
   Niveau        : 2ème année Prépa Informatique
   Établissement : École Polytechnique de Lomé
   Environnement : pycharm
   Langage       : python 3.12
   Licence       : Freecodecamp

 ============================================================
"""

class Maza:
    def __init__(self,age,prenom2 , niveau):
        self.age = age
        self.prenom2 = prenom2
        self.niveau = niveau
    def afficher(self):
        print(f" Votre  age est : {self.age} . Votre second prenom est : {self.prenom2} . Vous en  etes{self.niveau}" )

renaud=Maza(19, "Kossivi" ,"L2")
renaud.afficher()
print(type(renaud))
print(renaud.__dict__)
juste = Maza(19.05,"Kossigan","L1")
juste.afficher()
print(juste.__dict__)
