__import__("random").seed(int(input("Entrez la seed: "))),(lambda h:print("Temps total travaillé : {} h {} min".format(h//60,h%60)))((lambda f:lambda a,b,c,d,e,g,h:f(f,a,b,c,d,e,g,h))(lambda l,u,v,p,w,r,y,z:y(u,"Fin du service, dure journée",z)if u>539else w+l(l,u+1,v-1,p,w,r-1,y,z)if v>0else y(u,"Prunelle est parti. \\O/",z)+l(l,u,0,0,0,0,y,z)if w else (y(u,"Il faut travailler. M'enfin.",z)+l(l,u,r+90,p,1,r,y,z)if r<20else y(u,"C'est bon, encore le temps de faire une sieste. Zzz",z)+l(l,u,20,p,0,r,y,z)) if p else y(u,"OK, Pause !",z)+(l(l,u,50,p,0,r,y,z)if p else (lambda x:y(u,"Attention, Prunelle arrive à {}".format(z(x+u)),z)+l(l,u,50,1,0,x,y,z))(__import__("random").randint(0,50)+60)if not __import__("random").randint(-1,1)else l(l,u,50,0,0,0,y,z)))(0,0,0,0,0,lambda u,s,z:[print("{}\t{}".format(z(u),format(s))),0][1],lambda u:"{}:{}".format((u//60)+9,u%60)))

#y(0,"Gaston arrive au bureau",z)