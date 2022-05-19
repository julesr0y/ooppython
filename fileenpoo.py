# -*- coding: utf-8 -*-

class File():
    def __init__(self):
        self.file = []
        self.file_temp = [] #file temporaire pour les opérations nécéssitant de vider la file principale

    def est_vide(self):
        if self.file == []:
            return True
        else:
            return False
        
    def affiche(self):
        return self.file
        
    def enfiler(self, v):
        self.file.insert(0, v)
        return self.file
    
    def defiler(self):
        self.file.pop()
        return self.file
    
    def longueur(self):
        c = 0 #compteur initialisé a 0
        while not self.file == []:
            self.file_temp.append(self.file.pop())
            c += 1 #on ajoute un à chaque itération
        while not self.file_temp == []:
            self.file.append(self.file_temp.pop())
        return c
    
    def maximum(self):
        maxi = self.file[0]
        while not self.file == []:
            val = self.file.pop()
            if val > maxi:
                maxi = val
            self.file_temp.append(val)
        while not self.file_temp == []:
            self.file.append(self.file_temp.pop())
        return maxi
    
    def minimum(self):
        mini = self.file[0]
        while not self.file == []:
            val = self.file.pop()
            if val < mini:
                mini = val
            self.file_temp.append(val)
        while not self.file_temp == []:
            self.file.append(self.file_temp.pop())
        return mini
    
###Instanciations###
F = File()
F.enfiler(-8)
F.enfiler(9)
F.enfiler(5)
F.enfiler(110)
F.enfiler(33)
print("Nouvelle file:", F.affiche())
print("Défile:", F.defiler())
print("File", F.affiche())
print("Longueur:", F.longueur())
print("Maximum:", F.maximum())
print("Minimum:", F.minimum())
print("File vide ?", F.est_vide())