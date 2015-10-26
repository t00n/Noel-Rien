####################################
#            INFO-F101             #
#            Projet 2              #
####################################
__author__ = 'Tom Simonart'

from turtle import *
from math import radians,cos,floor

EPS = 1.0e-5
FACTEUR = cos(radians(30))

# Fonctions
def entree(valeur,default,mini='',maxi=''):
    """Vérifier les valeurs entrées par l'utilisateur et les comparer ces valeurs avec mini et maxi"""
    ret = input(str(valeur)+"["+str(default)+"]?> ")
    if ret == '':
        ret = default # Utiliser la valeur par défaut si l'utilisateur appuie sur ENTER
    elif type(mini) == int and type(maxi) == int: 
        if int(ret) < mini:
            print('La valeur entrée est trop petite et à été changée par \''+str(mini)+"\'")
            ret = mini
        elif int(ret) > maxi:
            print('La valeur entrée est trop grande et à été changée par \''+str(maxi)+"\'")
            ret = maxi
    return ret

def deformation(p,c,r):
    """reçoit le point p =(x_p,y_p,z_p), le centre c=(x_c,y_c,z_c),
    et le rayon r tout les trois avant déformation,
    revoit un point p2 après déformation
    """
    def distance(p,q):
        """distance entre les 2 points p et q"""
        return ((q[0]-p[0])**2 + (q[1]-p[1])**2 + (q[2]-p[2])**2)**0.5
    d = distance(p,c)
    if d >= r:
        res = p
    else:
        if d > EPS:
         facteur = r/d
        else:
         facteur = 1
        x2 = c[0] + (p[0]-c[0]) * facteur
        y2 = c[1] + (p[1]-c[1]) * facteur
        z2 = c[2] + (p[2]-c[2]) * facteur
        res = (x2,y2,z2)
    return res
deform = lambda p: deformation(p,centre,r) #définition de la fonction deform envoyée à pavage

def hexagone(t, c, longueur, col1, col2, col3, deform):
    """reçoit la tortue t, le centre c, la distance longueur, les trois couleurs col[1-3]
    et la fonction importée deform, dessine un hexagone composé de trois losanges de couleurs
    différentes et et utilise la fonction deform sur chaqu'un des points déssinés
    """
    COULEURS=(col1,col2,col3) # Triplet des couleurs
    chemin=[[(1,0),(0.5,FACTEUR),(-0.5,FACTEUR)],
    [(1,0),(0.5,-FACTEUR),(-0.5,-FACTEUR)],
    [(-0.5,-FACTEUR),(-1,0),(-0.5,FACTEUR)]] # Tableau de facteurs pour chaque losange
    t.pu()
    t.goto(c[0],c[1])
    for p,colo in enumerate(COULEURS): # Crée deux variables avec l'indice et le nom de la couleur
        t.goto(deform((c[0],c[1],0))[:2]) # Le centre de l'hexagone est déplaçe selon la déformation
        t.color(colo,colo)
        t.fillcolor(colo) # La couleur et la couleur de remplissage actuelle sont définis pour chaque losange
        t.pd()
        t.begin_fill() # Ajoute la couleur dans le losange
        for i in chemin[p]: # Utilise l'indice p qui correspond à l'indice de la couleur actuelle
            # Dessine et déforme chaque point du losange qui doit passer dans goto
            t.goto(deform((c[0]+(round(i[0]*longueur,2)),c[1]+(round(i[1]*longueur,2)),0))[:2])
            # La tortue se déplace depluis le centre vers 'chemin' * 'longueur' => chaque coin de losange
        t.end_fill()

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
inf_gauche = int(entree('Coin inférieur gauche',-300,-400,400))
sup_droit = int(entree('Coin supérieur droit',300,-400,400))
longueur = int(entree('Longueur d\'un coté',20,5,150))
col1 = entree('Couleur 1','blue',)
col2 = entree('Couleur 2','red')
col3 = entree('Couleur 3','black')
centreX = int(entree('Centre (axe X) de la déformation', -100,-1000,1000))
centreY = int(entree('Centre (axe Y) de la déformation', -100,-1000,1000))
centreZ = int(entree('Centre (axe Z) de la déformation', -100,-1000,1000))
centre = (centreX, centreY, centreZ) # Redéfinition du centre en un triplet utilisé par deform
r = float(entree('Rayon de déformation', 200, -1000, 1000))

tom = Turtle() # Création de la tortue
tom.speed(0) # Définition de sa vitesse, 0 est plus rapide

pavage(tom, inf_gauche, sup_droit, longueur, col1, col2, col3, deform)
tom.ht() # Cacher la tortue à la fin de pavage
lol = input() # Ne pas terminer le programme subitement
