import math

class People:
    """
    Represente chaque personne qui repond  le questionaire 
    
    """

    def __init__(self,vect_perso,vect_attentes,vect_importances):
        """

        """
        self.vect_perso=vect_perso
        self.vect_attentes=vect_attentes
        self.vect_importances=vect_importances
        self.tolerance(1.5) ### la finesse de l algo plus ce coef est grand plus il va etre stricte sur le diferences (a parametrer)

    def ponderation_norme (self,personne2):
        """
        Creer les vecteur ponderees des reponse et des attentes et calcul leur normes  
        """
        self.perso_pond=[]
        self.attente_pond=[]
        self.n_perso=0
        self.n_attentes=0
        for i in range (len(self.vect_importances)):
            val1=self.vect_perso[i]*personne2.vect_importances[i]
            self.perso_pond.append(val1)
            self.n_perso+=val1**2
            val2=self.vect_attentes[i]*self.vect_importances[i]
            self.attente_pond.append(val2)
            self.n_attentes+=val2**2

        self.n_perso=math.sqrt(self.n_perso)
        self.n_attentes=math.sqrt(self.n_attentes)
        print(self.perso_pond ,self.attente_pond ,self.n_perso ,self.n_attentes)

    def produit_scal(self,u,v):
        """
        Fait le produit scalaire entre deux vexteur 
        """
        val=0
        for i in range (len(u)):
            val+= u[i]*v[i]
        return(val)

    def similarite_cos (self,personne2):
        """
        Calcul la similarite cosinus entre les deux personnes 
        """
        self.ponderation_norme(personne2)
        personne2.ponderation_norme(self)
        simAB= self.produit_scal(self.attente_pond,personne2.perso_pond)/(self.n_attentes*personne2.n_perso)
        simBA=self.produit_scal(personne2.attente_pond,self.perso_pond)/(personne2.n_attentes*self.n_perso)
        comp= ((simAB+simBA)/2)*100
        return comp

    def tolerance (self,coef0):
        """
        Calcul 
        """
        self.coef_tolerance=[]
        for i in range (len(self.vect_importances)):
            val= coef0/(self.vect_importances[i]+0.01)
            self.coef_tolerance.append(val)

    def score_flou (self,personne2):
        score_1=0
        score_2=0

        for i in range (len(self.vect_perso)):
            val_2= personne2.vect_importances[i]*math.exp(-(((personne2.vect_attentes[i]-self.vect_perso[i])**2)/(2*((self.coef_tolerance[i])**2))))
            score_2+=val_2
            val_1= self.vect_importances[i]*math.exp(-(((self.vect_attentes[i]-personne2.vect_perso[i])**2)/(2*(personne2.coef_tolerance[i]**2))))
            score_1+=val_1
        
        compat=0.5*((score_2/sum(personne2.vect_importances))+(score_1/sum(self.vect_importances)))
        return(compat*100)
    
    def compatibilite (self,personne2,coeff):
        res=coeff*self.similarite_cos(personne2)+ ((1-coeff)*self.score_flou(personne2))
        return res
##test: 

Martin=People([1,2,5,3,8],[4,5,2,2,6],[4,2,2,6,5])
Davi=People([8,1,1,4,3],[5,2,5,4,3],[2,5,5,2,3])
Matias=People([4,5,2,2,6],[1,2,5,3,8],[40,20,20,60,50])

a=Matias

print(Martin.similarite_cos(a))

print(Martin.score_flou(a))

print(Martin.compatibilite(a,0.5))