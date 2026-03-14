"""
============================================================
   Description   : Build an Apply Discount Function.
   Auteur        : MAZA Kossivi Renaud
   Date          : 06/03/2025
   Niveau        : 2ème année Prépa Informatique
   Établissement : École Polytechnique de Lomé
   Environnement :pycharm
   Langage       : python 3.12
   Licence       : Freecodecamp

 ============================================================
"""

def apply_discount(price, discount):
    if not isinstance(price, int or float):
        return "The price should be a number"

    elif not isinstance(discount, int or float):
        return "The discount should be a number"

    elif price <= 0:
        return "The price should be greater than 0"

    elif not (0 <= discount < 100):
        return "The discount should be between 0 and 100"

    else:
        price = price - price * discount * pow(10, -2)
        return price


print(apply_discount(50, 0))
print(apply_discount(50,'z'))