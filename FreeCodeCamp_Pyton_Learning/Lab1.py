"""
============================================================
   Description   : Build a Travel Weather Planner.
   Auteur        : MAZA Kossivi Renaud
   Date          : 05/03/2025
   Niveau        : 2ème année Prépa Informatique
   Établissement : École Polytechnique de Lomé
   Environnement :pycharm
   Langage       : python 3.12
   Licence       : Freecodecamp

 ============================================================
"""
distance_mi = 50
is_raining = True
has_bike = True
has_car = True
has_ride_share_app = True

if distance_mi == False:
    print('False')
elif distance_mi <= 1:
    if not is_raining:
        print('True')
    else:
        print('False')
elif 1 < distance_mi <= 6:
    if has_bike and not is_raining:
        print('True')
    else:
        print('False')
else:
    if has_car or has_ride_share_app :
        print('True')
    else:
        print('False')








import turtle
turtle.circle(35)
turtle.circle(45)
turtle.circle(55)
turtle.circle(65)
turtle.circle(75)
turtle.circle(85)
turtle.circle(95)
turtle.circle(105)
turtle.circle(115)
turtle.circle(125)
turtle.circle(135)
turtle.circle(10)