# Noel Neri
# BA1 2015-2016
# Programmation - Projet 2

(lambda e=lambda v,d,m='',n='',t=int:(lambda x:d if x=='' else x if t==str else m if t(x)<m else n if t(x)>n else t(x))(input(str(v)+" (Défaut: "+str(d)+"): ")):(lambda g,d,l,x,y,z,c,r:(lambda f,*a:f(f,*a))(lambda a,t,g,d,l,x,y,z,i,o=1,e=lambda p:(lambda d:p if d>=r else(lambda f:[c[i]+(p[i]-c[i])*f for i in range(3)])(r/d if d>1.0e-5else 1))(sum([(c[i]-p[i])**2 for i in range(3)])**0.5),h=lambda t,c,l,x,y,z,e,f=__import__("math").cos(__import__("math").radians(30)):(t.pu(),t.goto(c[0],c[1]),[(t.goto(e((c[0],c[1],0))[:2]),t.color(k,k),t.fillcolor(k),t.pd(),t.begin_fill(),[t.goto(e((c[0]+(round(i[0]*l,2)),c[1]+(round(i[1]*l,2)),0))[:2]) for i in [[(1,0),(0.5,f),(-0.5,f)],[(1,0),(0.5,-f),(-0.5,-f)],[(-0.5,-f),(-1,0),(-0.5,f)]][p]],t.end_fill())for p,k in enumerate((x,y,z))]):t.ht()if i>d else([h(t,(j,i),l,x,y,z,e)for j in range(g+int(1.5*l*(not o)),d+int(1.5*l*o),3*l)],a(a,t,g,d,l,x,y,z,i+__import__("math").floor(l*__import__("math").cos(__import__("math").radians(30))),not o)),(lambda t:(t.speed(0),t))(__import__("turtle").Turtle())[1],g,d,l,x,y,z,g))(e('Inf gauche',-300,-400,400),e('Sup droit',300,-400,400),e('Longueur',20,5,50),e('Couleur 1','red',str),e('Couleur 2','blue',str),e('Couleur 3','black',str),(e('Déformation x',-100,-300,300),e('Déformation y',-100,-300,300),e('Déformation z',-100,-300,300)),e('Déformation rayon',200,-300,300,float)))(),input()
