####################################
#            INFO-F101             #
#            Projet 2              #
####################################
__author__ = 'Noël Neri'

from turtle import *
from math import radians,cos,floor

EPS = 1.0e-5
FACTEUR = cos(radians(30))

entree = lambda valeur, default, mini='', maxi='', typ=int: (lambda x: default if x == '' else x if typ == str else mini if typ(x) < mini else maxi if typ(x) > maxi else typ(x))(input(str(valeur)+"["+str(default)+"]?> "))

deform = lambda p: (lambda p,c,r:(lambda d: p if d >= r else (lambda facteur:[c[i]+(p[i]-c[i])*facteur for i in range(3)]) (r/d if d > EPS else 1)) (sum([(c[i]-p[i])**2 for i in range(3)])**0.5))(p, centre, r)

def hexagone(t, c, longueur, col1, col2, col3, deform, chemin=[[(1,0),(0.5,FACTEUR),(-0.5,FACTEUR)],[(1,0),(0.5,-FACTEUR),(-0.5,-FACTEUR)],[(-0.5,-FACTEUR),(-1,0),(-0.5,FACTEUR)]]):
    """reçoit la tortue t, le centre c, la distance longueur, les trois couleurs col[1-3]
    et la fonction importée deform, dessine un hexagone composé de trois losanges de couleurs
    différentes et et utilise la fonction deform sur chaqu'un des points déssinés
    """
    COULEURS=(col1,col2,col3) # Triplet des couleurs
    t.pu(),t.goto(c[0],c[1])
    for p,colo in enumerate(COULEURS):
        t.goto(deform((c[0],c[1],0))[:2]),t.color(colo,colo),t.fillcolor(colo),t.pd(),t.begin_fill(),[t.goto(deform((c[0]+(round(i[0]*longueur,2)),c[1]+(round(i[1]*longueur,2)),0))[:2]) for i in chemin[p]],t.end_fill()

def pavage(t, inf_gauche, sup_droit, longueur, col1, col2, col3, deform):
    """Prends la tortue t, le coin inférieur gauche et le coin supérieur droit de la fenêtre,
    la longueur des cotés de l'hexagone (utilisée pour disposer la grille)
    les trois couleurs et la fonction deform pour les passer à la fonction hexagone.
    Dessine une grille composée d'hexagone disposés en quinconce
    """
    imp = 1
    for i in range(inf_gauche,sup_droit,floor(longueur*FACTEUR)): # Rangées
        if imp == 1:
            for j in range(inf_gauche,sup_droit+int(1.5*longueur),3*longueur): # Second type de ligne
                hexagone(t, (j,i), longueur, col1, col2, col3, deform)
            imp*=-1
        elif imp == -1:
            for j in range(inf_gauche+int(1.5*longueur),sup_droit,3*longueur): # Premier type de ligne
                hexagone(t, (j,i), longueur, col1, col2, col3, deform)
            imp*=-1
# Programme
# Série d'input pour entrer toutes les données
print('Appuyez sur ENTER pour garder la valeur par défaut!')
inf_gauche = entree('Coin inférieur gauche',-300,-400,400)
sup_droit = entree('Coin supérieur droit',300,-400,400)
longueur = entree('Longueur d\'un coté',20,5,150)
col1 = entree('Couleur 1','blue', str)
col2 = entree('Couleur 2','red', str)
col3 = entree('Couleur 3','black', str)
centreX = entree('Centre (axe X) de la déformation', -100,-1000,1000)
centreY = entree('Centre (axe Y) de la déformation', -100,-1000,1000)
centreZ = entree('Centre (axe Z) de la déformation', -100,-1000,1000)
centre = (centreX, centreY, centreZ) # Redéfinition du centre en un triplet utilisé par deform
r = entree('Rayon de déformation', 200, -1000, 1000, float)

tom = Turtle() # Création de la tortue
tom.speed(0) # Définition de sa vitesse, 0 est plus rapide

pavage(tom, inf_gauche, sup_droit, longueur, col1, col2, col3, deform)
tom.ht() # Cacher la tortue à la fin de pavage
lol = input() # Ne pas terminer le programme subitement
