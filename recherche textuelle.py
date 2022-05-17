# -*- coding: utf-8 -*-
"""
@author: jules
"""
#import unidecode

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
            # if liste_txt[i] == "'":
            #     liste_txt.pop(i)
            if self.chaine in liste_txt[i] and len(liste_txt[i]) == len(self.chaine):
                liste_positions.append(i)
            # elif liste_txt[i] == ',' or liste_txt[i] == '.':
            #     liste_txt.pop(i)
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
                return "Le séquence recherchée ('" + self.chaine + "') apparait " + str(cpt) + " fois, aux positions n°: " + chaine_positions
            
    def compter(self):
        liste_txt = self.texte.split(" ")
        return "Il y a " + str(len(liste_txt)) + " mots dans ce texte"
        
a = Recherchetxt("la", """Alors qu'elle est une des plus anciennes équipes nationales de football, l'équipe d'Irlande du Nord 
                 est en 1957-1958 une nouvelle venue dans le monde du football international car c'est la première fois qu'elle 
                 participe aux qualifications à la Coupe du monde. Jusqu'alors, son activité internationale se limitait à des matchs 
                 contre des équipes britanniques et à d'occasionnels matchs internationaux amicaux. Après s'être qualifiée à la 
                 surprise générale en éliminant le Portugal et l'Italie, l'équipe voit sa préparation pour la compétition troublée 
                 par plusieurs évènements. Le premier est l'accident aérien de Munich le 6 février 1958, qui décime l'équipe de 
                 Manchester United où exerçaient deux joueurs essentiels de l'équipe nationale nord-irlandaise : Jackie Blanchflower, 
                 qui est obligé d'arrêter la pratique du football de haut niveau, et Harry Gregg, profondément marqué physiquement et 
                 psychologiquement. Ensuite, une longue querelle se déclenche au sein de la nation nord-irlandaise sur la pratique du 
                 football le dimanche, ce qui semble compromettre la participation de l'équipe à la Coupe du monde.""")
print(a.recherche())
print(a.compter())