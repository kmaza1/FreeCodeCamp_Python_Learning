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

# POO EXERCICE DE MISE EN SITUATION 1
# genre
#   False : Femme
#   True  : Homme


class Personne:
    def __init__(self, nom: str = "", age: int = 0, genre: bool = None ):
        self.nom = nom   # crée une variable d'instance : nom
        self.age = age
        self.genre = genre

        if nom == "":
            print("Veuillez entrez quelque chose comme nom .")
            self.Demander_nom()
        if  not age >0  :
            print("Veuillez entrez un age correct .")
            self.Demander_age()
        if  not isinstance(genre, bool) :
            print("Veuillez entrez True si vous etes un homme et False sinon .")
            self.Demander_genre()


    def SePresenter(self):
        # Bonjour, je m'appelle Jean, j'ai 30 ans
        # Je suis majeur
        print("Constructeur personne " + self.nom)
        print("Bonjour, je m'appelle " + self.nom + ", j'ai " + str(self.age) + " ans")

        if self.genre:
            Maturite = "Je suis majeur" if self.EstMajeur() else "Je suis mineur"
            Genre = "Masculin"
        else :
            Maturite = "Je suis majeure" if self.EstMajeur() else "Je suis mineure"
            Genre = "Feminin"
        print(Maturite)
        print(f"Genre : {Genre}")
        # Signifie que Maturite = "Je suis majeur" si self.EstMajeur() == True et Maturite = "Je suis majeure" sinon

        print()

    def EstMajeur(self):
        return self.age >= 18

    def Demander_nom(self):
        self.nom = input("Veuillez entrez votre nom : ")

    def Demander_age(self):
        self.age = int(input("Veuillez entrez votre age : "))

    def Demander_genre(self):
        self.genre = input("Veuillez entrez votre genre : ")
if __name__ == "__main__" :
    personne1 = Personne("Renaud", 20, True)
    personne2 = Personne("Ruth", 17, False)
    personne3 = Personne("Piaget", 25, True)
    personne4 = Personne()

    lis_Personne = [personne1, personne2, personne3]
    lis_Personne.append(personne4)
    for personne in lis_Personne:
        personne.SePresenter()

"""
    tuple_personnes  = (personne1, personne2,  personne3)

    for i in range(len(tuple_personnes)):
        tuple_personnes[i].SePresenter()
        print()

    for personne in tuple_personnes:
        personne .SePresenter()
        print() """






