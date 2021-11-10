import pygame  # necessaire pour charger les images et les sons
import random as r

class Joueur : # classe pour créer le vaisseau du joueur
    def __init__(self) :
        self.x=400
        self.direc=None
        self.image=pygame.image.load("vaisseau.png")
        pass
    
    def setDirection(self, dir):
        self.direc=dir
    
    def deplacer(self):
        if self.direc=="gauche" and self.x>40: self.x=self.x-4
        elif self.direc=="droite" and self.x<700: self.x=self.x+4
        else: pass
    
    def getPosition(self):
        return self.x
    
    def tirer(self):
        self.direc=None
        
    
class Balle:
    def __init__(self, p):
        self.etat="chargee"
        self.image=pygame.image.load("balle.png")
        self.depart=p.x
        self.hauteur=500
        self.player=p
    def bouger(self):
        if self.etat == "tiree" : self.hauteur=self.hauteur-10
        if self.etat == "chargee" : self.depart=self.player.x
        if self.hauteur<0:
            self.etat="chargee"
            self.hauteur=500
            self.depart=self.player.x
            
class Ennemi:
    def __init__(self):
        self.depart=r.randint(60, 700)
        self.hauteur=20
        self.type=r.randint(1, 2)
        self.NbEnnemis=3
        if self.type==1:
            self.image=pygame.image.load("invader1.png")
            self.vitesse=4
        else:
            self.image=pygame.image.load("invader2.png")
            self.vitesse=6
    def avancer(self):
        self.hauteur=self.hauteur+self.vitesse
            
        
        
        
            
        
        
        
            
        