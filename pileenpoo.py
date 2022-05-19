# -*- coding: utf-8 -*-

class Pile():
    def __init__(self):
        self.pile = []
        self.pile_temp = [] #pile temporaire pour les opérations nécéssitant de vider la pile principale
        
    def est_vide(self):
        if self.pile == []:
            return True
        else:
            return False
        
    def affiche(self):
        return self.pile
        
    def empiler(self, v):
        self.pile.append(v)
        return self.pile
        
    def depiler(self):
        self.pile.pop()
        return self.pile
    
    def hauteur(self):
        c = 0 #compteur initialisé a 0
        while not self.pile == []:
            self.pile_temp.append(self.pile.pop())
            c += 1 #on ajoute un à chaque itération
        while not self.pile_temp == []:
            self.pile.append(self.pile_temp.pop())
        return c
    
    def maximum(self):
        maxi = self.pile[0]
        while not self.pile == []:
            val = self.pile.pop()
            if val > maxi:
                maxi = val
            self.pile_temp.append(val)
        while not self.pile_temp == []:
            self.pile.append(self.pile_temp.pop())
        return maxi
    
    def minimum(self):
        mini = self.pile[0]
        while not self.pile == []:
            val = self.pile.pop()
            if val < mini:
                mini = val
            self.pile_temp.append(val)
        while not self.pile_temp == []:
            self.pile.append(self.pile_temp.pop())
        return mini
       
###Instanciations###
P = Pile()
P.empiler(-8)
P.empiler(9)
P.empiler(5)
P.empiler(110)
P.empiler(33)
print("Nouvelle pile:", P.affiche())
print("Dépile:", P.depiler())
print("Pile", P.affiche())
print("Hauteur:", P.hauteur())
print("Maximum:", P.maximum())
print("Minimum:", P.minimum())
print("Pile vide ?", P.est_vide())