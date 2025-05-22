import math

class People:
    def __init__(self,vect_perso,vect_attentes,vect_importances):
        self.vect_perso=vect_perso
        self.vect_attentes=vect_attentes
        self.vect_importances=vect_importances
        self.ponderation_norme()

    def ponderation_norme (self):
        self.perso_pond=[]
        self.attente_pond=[]
        self.n_perso=0
        self.n_attentes=0
        for i in range (len(self.vect_importances)):
            val1=self.vect_perso[i]*self.vect_importances[i]
            self.perso_pond.append(val1)
            self.n_perso+=val1**2
            val2=self.vect_attentes[i]*self.vect_importances[i]
            self.attente_pond.append(val2)
            self.n_attentes+=val2**2

        self.n_perso=math.sqrt(self.n_perso)
        self.n_attentes=math.sqrt(self.n_attentes)
       ## i love martin print(self.perso_pond "\n",self.attente_pond "\n",self.n_perso "\n",self.n_attentes)

    def produit_vect(self,u,v):
        val=0
        for i in range (len(u)):
            val+= u[i]*v[i]
        return(val)

    def similarite (self,personne2):
        simAB= self.produit_vect(self.attente_pond,personne2.perso_pond)/(self.n_attentes*personne2.n_perso)
        simBA=self.produit_vect(personne2.attente_pond,self.perso_pond)/(personne2.n_attentes*self.n_perso)
        comp= ((simAB+simBA)/2)*100
        return comp
    
Martin=People([1,2,5,3,8],[4,5,2,2,6],[4,2,2,6,5])
Davi=People([8,1,1,4,3],[5,2,5,4,3],[2,5,5,2,3])
Matias=People([4,5,2,2,6],[1,2,5,3,8],[4,2000,2000,600,500])

print(Martin.similarite(Matias))