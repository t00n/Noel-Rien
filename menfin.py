__import__("random").seed(int(input("Entrez la seed: "))),(lambda h:print("Temps total travaillé : %d h %02d min"%(h//60,h%60)))((lambda f,*a:f(f,*a))(lambda l,u,v,p,w,y,z:y(0,"Gaston arrive au bureau",z)+l(l,0,0,0,0,y,z)if u<0else y(u,"Fin du service, dure journée",z)if u>539else w+l(l,u+1,v-1,p-1,w,y,z)if v>0else y(u,"Prunelle est parti. \\O/",z)+l(l,u,0,0,0,y,z)if w else(y(u,"Il faut travailler. M'enfin.",z)+l(l,u,p+90,p,1,y,z)if p<20else y(u,"C'est bon, encore le temps de faire une sieste. Zzz",z)+l(l,u,20,p,0,y,z))if p>0else y(u,"OK, Pause !",z)+(l(l,u,50,p,0,y,z)if p>0else(lambda x:y(u,"Attention, Prunelle arrive à %s"%z(x+u),z)+l(l,u,50,x,0,y,z))(__import__("random").randint(0,50)+60)if not __import__("random").randint(-1,1)else l(l,u,50,0,0,y,z)),-1,0,0,0,lambda u,s,z:[print("%s\t%s"%(z(u),s)),0][1],lambda u:"%02d:%02d"%((u//60)+9,u%60)))