"""
============================================================
   Description   : Important Functions in python.
   Auteur        : MAZA Kossivi Renaud
   Date          : 08/03/2025
   Niveau        : 2ème année Prépa Informatique
   Établissement : École Polytechnique de Lomé
   Environnement :pycharm
   Langage       : python 3.12
   Licence       : Freecodecamp

 ============================================================
"""

# 1) "enumrate : permet de parcourir une liste et d'avoir aussi les index  "
#Utilisation :
liste1 = ["Elie", "Daniel", "Tresor", "Piaget"]
for index, value in enumerate(liste1, start=3 ):
    print(f"Index : {index } et Valeur : {value}")

# 2) "Zip: permet de parcourir 2 listes mais il faut les 2 listes ont le meme nombre d'éléments  "
#Utilisation :
liste2 = [20, 6, 22, 25]
for elment_liste1, elment_liste2 in zip(liste1, liste2):
    print(f"Il s' appelle {elment_liste1} et il est agé de {elment_liste2} ans")


# 3) "map : permet de parcourir une liste et d'effectuer un opération ou modification sur les élément de la liste"
#Voici une façon classique d' élévé les element d' une lise de valeurs au carrés
age_carre = [age**2 for age in liste2] #retourne une nouvelle liste avec les éléments au carrés
print(age_carre)
#Utilisation de map pour le faire  :
age_carre = list(map(lambda x :x**0, liste2 ))   #x réprésente chaque élément du la liste
print(age_carre)
# 4) "any() / all()  : permettent  d'effectuer un opération ou modification sur les élément de la liste en fonction de certaines conditions ou meme de faire une vérication "
#Utilisation any ():
print(any(age < 20 for age in liste2)) # Retourne True si un age de la lsite est inférieur à 20 et False sinon
#Utilisation all():
print(all(age < 20 for age in liste2)) # Retourne True si tous les ages de la liste sont  de la lsite inférieur à 20 et False sinon

# 5) "Counter()  : permet  le nombre de fois q'un nombre , string ... se repèten dans un texte ,une  liste, ... "
#Utilisation counter ():
    #Importer d' abord la méthode  de la classe collections
    #On a alors :
from collections import Counter

liste1_prim = liste1*3 + ["Elie", "Daniel",  "Daniel"]
print(liste1_prim)
occurence = Counter(liste1_prim)
print(occurence)
print(occurence.most_common(2)) # Retourne l' occurence / les occurences que apparaissent le plus et ici j' ai voulu voir les 2 premiers d' ou l' apparition de 2

# 6) "sorted()  : permet de trier une liste par ordre crossant
# #Utilisation sorted() :
print(sorted(liste1)) # Tri la liste par ordre croissant
print(sorted(liste1, key=lambda x : len(x) )) # Le tri se fait basé de la taille des élémeents
print(sorted(liste1, key=len)) # Le tri se fait  basé de la taille des élémeents

# 7) "set()  : permet de  supprimer des doublons dans une liste
# #Utilisation set() :
print(set(liste1_prim))

# 8) "combination()  : permet  de voir le nombre ce combinaison qu' on peut faire avec le éléments d' une liste
#Utilisation combinations():
    #Importer d' abord la méthode  de la classe itertools
    #On a alors :
from  itertools import combinations
print(list(combinations(liste1, 2))) #Le 2 est pour  combinaison 2 à 2 , on pouvait mettre 3,4,...

# 9) "json.dumps()  : permet  de  séréaliser les éléments d' un dictionnaire en convertissant un dictionnaire en fichier json
#Utilisation json.dumps():
    #Importer d' abord json
    #On a alors :
import json


dictionnaire = {
    'nom ':' Renaud',
    'age' :20,
    'niveau' : 'L2'
}
print(json.dumps(dictionnaire) )

# 10) "json.loads()  : permet  de convertir  un fichier json en  dictionnaire
#Utilisation json.loads():
    #Importer d' abord json
    #On a alors :

import json


dictionnaire_json = '{"nom": "Renaud", "age": 20, "niveau": "L2"}'


data = json.loads(dictionnaire_json)

