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
"""#Version procéduerale du code
def afficher_personne(nom, age):
    print(f"La personne s' appelle {nom} et elle est  agée est {age} ans")

def demander_infos():
    nom = input("Veuillez entrez votre nom : ")
    age = int(input("Veuillez entrz votre nom  : "))
    return nom, age

nom1, age1 = demander_infos()
nom2, age2 = demander_infos()
nom3, age3 = demander_infos()

afficher_personne(nom1, age1)
afficher_personne(nom2, age2)
afficher_personne(nom3, age3)
 
"""
#version POO de code procédurale

class Personne:

    def __init__(self, nom : str = '', age : int = 0):
        self.nom = nom
        self.age = age

    def question_mariage(self):
        self.Le_veux_tu = input("La voulez vous comme femme jusqu' à ce que la mort s'en suive (O/N) : ")
        return  self.Le_veux_tu

    def afficher_personne(self):
        print(f"La personne s' appelle {self.nom} et elle est  agée est {self.age} ans et elle a dit {self.Le_veux_tu}")

    def demander_infos(self):
        self.nom = input("Veuillez entrez votre nom : ")
        self.age = int(input("Veuillez entrez votre age  : "))






personne1 = Personne()
personne2 = Personne("Elisée",100)


personne1.question_mariage()
personne1.demander_infos()
personne1.afficher_personne()



