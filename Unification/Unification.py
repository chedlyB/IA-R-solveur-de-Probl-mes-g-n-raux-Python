


# Creation des classes qui represente le type des elements a unifier  


class Variable :
    def __init__(self,nom):
        self.nom = nom

class Constante :    
    def __init__(self,nom):
        self.nom = nom

 

        #L'algorithme d'unification de Robinson 

 

#Methodes Unifier atomes qui est appelée par la methode Unifier 

def unifierAtomes(e1,e2,fichier): 
       # Supposons que soit e1 ou e2 est un atome
        # Etape1 Interchanger les param de sorte que e1 soit atome :
       
        if (isinstance(e2,Constante) or isinstance(e2,Variable))  : #nekes cas ?
            f = e1
            e1 = e2
            e2 = f
        if (isinstance(e2,list) and isinstance(e1,Constante)): 
            fichier.write("ECHEC\n") 
            return "ECHEC"
        if (isinstance(e2,list) and isinstance(e1,Variable)): 
            if e1 in e2 : 
                fichier.write("ECHEC\n")
                return "ECHEC"
            else :
                t =False
                var=""
                var = e2[0].nom
                print(var)
                for i in range(1,len(e2)):
                    if isinstance(e2[i],list):
                        if e1 in e2[i] :
                            fichier.write("ECHEC\n")
                            return 'ECHEC'
                        else:
                            Z=Unifier(e1,e2[i],fichier)
                            print(Z)
                            Lis = Z.split("/")
                            val = Lis[1]
                            val1 = val.replace("?","")
                            
                            var = var +","+val1
                    else:
                        var = var +","+ e2[i].nom
                fichier.write("?"+e1.nom + "/" + "["+var+"]")
                return "?"+e1.nom + "/" + "["+var+"]"
                    
              
        # Etape 2 si identique alors NULL
        
        if (isinstance(e1,Constante) and  isinstance(e2,Constante)) or (isinstance(e1,Constante) and  isinstance(e2,Constante)) :
           if e1.nom == e2.nom : return "NULL"
        # Etape 3 :
        if isinstance(e1,Variable):
            if  isinstance(e2,Constante) :
                return "?"+e1.nom + "/" + e2.nom
        if  isinstance(e2,Variable): 
            if isinstance(e1,Variable):
                return "?"+e2.nom + "/" +"?"+e1.nom
            if isinstance(e1,Constante):
                return "?"+e2.nom + "/"+e1.nom
        return "ECHEC"



#Methode Unifier qui permet l'unification de deux elements (Liste,atome ,Fonction .. ) 

def Unifier(e1,e2,fichier):
       if  isinstance(e2,Constante) or isinstance(e2,Variable) or isinstance(e1,Constante) or isinstance(e1,Variable) :
           return unifierAtomes(e1,e2,fichier)    
       if (e1 == [] and e2 == []) : 
           return "    ===>  FIN "
       f1 = e1[0]
       f2 = e2[0]
       T1 = e1[1:]
       T2 = e2[1:]
       Z1 = Unifier(f1,f2,fichier)
       fichier.write(str(Z1)+"\n")
       print(Z1)
       if Z1 == 'ECHEC' : return 'ECHEC'
       if (T1 == [] and T1 == []) : return  Z1
       G1 = substituer (T1,Z1)
       G2 = substituer (T2,Z1)
       Z2 = Unifier(G1,G2,fichier)
       if Z2 == 'ECHEC' : return 'ECHEC'
       return Z1+"   "+ Z2 
       


#Methode substituer qui permet la mise a jour des expressions lorsqu'il y'a des changements  

def substituer(e1,subs):
       if subs == "NULL": return e1
       ar = subs.split("   ")
       if len(ar) == 1 :
           liste =[]
           Lis = subs.split("/")
           var = Lis[0].replace("?","")
           val = Lis[1]
           val1 = val.replace("?","")
           if (val == "?"+val1):  v = Variable(val1)
           else: v = Constante(val)
           for i in range(0,len(e1)):
               if isinstance(e1[i],Variable) :
                   if e1[i].nom == var : e1[i]= v
               if isinstance(e1[i],list):
                   for j in range(0,len(e1[i])):
                       if isinstance(e1[i][j],Variable):
                           if e1[i][j].nom == var : e1[i][j]= v
                       else:
                           if isinstance(e1[i][j],list) :
                               e1[i][j] = substituer(e1[i][j],subs)
       else:
           liste =[]
           for l in range(1,len(ar)):
               print(ar[l])
               Lis = ar[l].split("/")
               var = Lis[0].replace("?","")
               val = Lis[1]
               val1 = val.replace("?","")
               if (val == "?"+val1):  v = Variable(val1)
               else: v = Constante(val)
               for i in range(0,len(e1)):
                   if isinstance(e1[i],Variable) :
                       if e1[i].nom == var : e1[i]= v
                       if isinstance(e1[i],list):
                           for j in range(0,len(e1[i])):
                               if isinstance(e1[i][j],Variable):
                                   if e1[i][j].nom == var : e1[i][j]= v
                                   else:
                                       if isinstance(e1[i][j],list) :
                                           e1[i][j] = substituer(e1[i][j],subs)
       return e1

  
   


   #ouverture du  fichier de trace 
fichier = open("C:/Users/Chedly Binous/Desktop/Insat/chedly RT4/Intelligence artificielle/Unification/Unification/fichier.txt","w") 





#Declaration des elements (Constantes,Variable...)
a = Constante('a')
b = Constante('b')
c = Constante('c')
d = Constante('d')
e = Constante("e")
p = Constante('p')
f = Constante('f')
g= Constante('g')
x=Variable('x')
y=Variable('y')
z=Variable('z')
w = Variable('w')



#Unifier(p(B,C,?x,?z,f(A,?z,B)), p(?y,?z?y,C,?w)) ==>

fichier.write("Unifier( [p,b,c,x,z,[f,a,z,b]] et  [p,y,z,y,c,w] ) \n")
Unifier([p,b,c,x,z,[f,a,z,b]],[p,y,z,y,c,w],fichier)

#Unifier (P(?x, f(g(?x)), A), P(b,? xy, ?z)) ==>

fichier.write("Unifier([p,x,[f,[g,x]],a] et [p,b,x,y,z])\n")
Unifier([p,x,[f,[g,x]],a],[p,b,x,y,z],fichier)

#Unifier(q(f(A,?x),?x),q(f(?z,f(?z,D)),?z)) ==>

fichier.write("Unifier([p,[f,a,x],x] et [p,[f,z,[f,z,d]],z])\n")
Unifier([p,[f,a,x],x],[p,[f,z,[f,z,d]],z],fichier)

#Unifier(?x, g(?x)) ==>
fichier.write("Unifier(x et [g,x])\n")
Unifier(x,[g,x],fichier)

#Fermeture du fichier de trace 
fichier.close()
