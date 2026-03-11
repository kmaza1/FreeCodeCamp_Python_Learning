class Rectangle:
    """Ceci est la classe Rectangle."""

    def __init__(self, longueur=0.0, largeur=0.0, couleur="blanc"):
        """Initialisation d'un objet.

        DÃ©finition des attributs avec des valeurs par dÃ©faut.
        """
        self.longueur = longueur
        self.largeur = largeur
        self.couleur = couleur

    def calcule_surface(self):
        """MÃ©thode qui calcule la surface."""
        return self.longueur * self.largeur

    def change_carre(self, cote):
        """MÃ©thode qui transforme un rectangle en carrÃ©."""
        self.longueur = cote
        self.largeur = cote


#if __name__ == "__main__":
#InsÃ©rez ici la suite de votre programme Python
# qui va utiliser la classe Rectangle.
