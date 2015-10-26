####################################
#            INFO-F101             #
#            Projet 2              #
####################################
__author__ = 'Noël Neri'

entree = lambda valeur, default, mini='', maxi='', typ=int: (lambda x: default if x == '' else x if typ == str else mini if typ(x) < mini else maxi if typ(x) > maxi else typ(x))(input(str(valeur)+" ("+str(default)+"): "))


# Programme
# Série d'input pour entrer toutes les données
print('Ne rien entrer pour les valeurs par défaut')
inf_gauche = entree('Inf gauche',-300,-400,400)
sup_droit = entree('Sup droit',300,-400,400)
longueur = entree('Longueur',20,5,150)
col2 = entree('Couleur 1','red', str)
col1 = entree('Couleur 2','blue', str)
col3 = entree('Couleur 3','black', str)
centreX = entree('Déformation x', -100,-1000,1000)
centreY = entree('Déformation y', -100,-1000,1000)
centreZ = entree('déformation z', -100,-1000,1000)
centre = (centreX, centreY, centreZ) # Redéfinition du centre en un triplet utilisé par deform
r = entree('Déformation rayon', 200, -1000, 1000, float)

(lambda f,*a:f(f,*a))(lambda a,t, inf_gauche, sup_droit, longueur, col1, col2, col3,i,odd=1,deform=lambda p: (lambda p,c,r:(lambda d: p if d >= r else (lambda facteur:[c[i]+(p[i]-c[i])*facteur for i in range(3)]) (r/d if d > 1.0e-5 else 1)) (sum([(c[i]-p[i])**2 for i in range(3)])**0.5))(p, centre, r),hexagone=lambda t, c, longueur, col1, col2, col3, deform,FACTEUR=__import__("math").cos(__import__("math").radians(30)):(t.pu(),t.goto(c[0],c[1]),[(t.goto(deform((c[0],c[1],0))[:2]),t.color(colo,colo),t.fillcolor(colo),t.pd(),t.begin_fill(),[t.goto(deform((c[0]+(round(i[0]*longueur,2)),c[1]+(round(i[1]*longueur,2)),0))[:2]) for i in [[(1,0),(0.5,FACTEUR),(-0.5,FACTEUR)],[(1,0),(0.5,-FACTEUR),(-0.5,-FACTEUR)],[(-0.5,-FACTEUR),(-1,0),(-0.5,FACTEUR)]][p]],t.end_fill()) for p,colo in enumerate((col1,col2,col3))]):t.ht()if i>sup_droit else ([hexagone(t, (j,i), longueur, col1, col2, col3, deform) for j in range(inf_gauche+int(1.5*longueur*(not odd)),sup_droit+int(1.5*longueur*odd),3*longueur)],a(a,t,inf_gauche,sup_droit,longueur,col1,col2,col3,i+__import__("math").floor(longueur*__import__("math").cos(__import__("math").radians(30))),not odd)),(lambda t: (t.speed(0),t))(__import__("turtle").Turtle())[1], inf_gauche, sup_droit, longueur, col1, col2, col3,inf_gauche)
lol = input()
