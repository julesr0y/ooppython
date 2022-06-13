# -*- coding: utf-8 -*-
"""
@author: jules
"""
#import unidecode
import re

class Recherchetxt():
    def __init__(self, chaine, texte):
        self.chaine = chaine
        self.texte = texte
        
    def recherche(self):
        liste_positions = []
        chaine_positions = ""
        self.texte = self.texte.lower()
        liste_txt = self.texte.split(" ")
        for i in range(len(liste_txt)):
            if self.chaine in liste_txt[i] and len(liste_txt[i]) == len(self.chaine):
                liste_positions.append(i)
        if liste_positions == []:
            return "Aucun résultat"
        else:
            cpt = 0
            liste_positions = list(reversed(liste_positions))
            while liste_positions != []:
                new = liste_positions.pop()
                chaine_positions += str(new + 1) + " "
                cpt += 1
            if cpt == 1:
                return "La séquence recherchée ('" + self.chaine + "') apparait une fois en position n°: " + chaine_positions
            else:
                return "La séquence recherchée ('" + self.chaine + "') apparait " + str(cpt) + " fois, aux positions n°: " + chaine_positions
            
    def compter(self):
        texte_formate = re.sub("\,|\;|\.|\!|\?", "", self.texte)
        liste_txt = texte_formate.split(" ")
        print(liste_txt)
        compteur = 0
        for mot in liste_txt:
            if "'" in mot:
                compteur += 2
            elif mot == "":
                compteur += 0
            else:
                compteur += 1
        return "Il y a " + str(compteur) + " mots dans ce texte"

###Instanciations###     
a = Recherchetxt("la", "Alors qu'elle est une des plus anciennes équipes nationales de football, l'équipe d'Irlande du Nord est en 1957-1958 une nouvelle venue dans le monde du football international car c'est la première fois qu'elle participe aux qualifications à la Coupe du monde. Jusqu'alors, son activité internationale se limitait à des matchs contre des équipes britanniques et à d'occasionnels matchs internationaux amicaux. Après s'être qualifiée à la surprise générale en éliminant le Portugal et l'Italie, l'équipe voit sa préparation pour la compétition troublée par plusieurs évènements.")
print(a.recherche())
print(a.compter())

b = Recherchetxt("la", "Alors ; qu'elle")
print(b.recherche())
print(b.compter())