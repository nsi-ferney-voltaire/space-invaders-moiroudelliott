import pygame # importation de la librairie pygame
import sys # pour fermer correctement l'application

### INITIALISATION ###
# lancement des modules inclus dans pygame
pygame.init() 

# création d'une fenêtre de 800 par 600
screen = pygame.display.set_mode((800,600))
#nom de la fenetre
pygame.display.set_caption("Space vaders") 
# chargement de l image de fond
fond = pygame.image.load('background.png')

### BOUCLE DE JEU  ###
running = True 

while running : # boucle infinie 
    # dessin du fond
    screen.blit(fond,(0,0))
    
    ### Gestion des événements  ###
    for event in pygame.event.get(): # parcours de tous les event pygame dans cette fenêtre
        if event.type == pygame.QUIT : # si l'événement est le clic sur la fermeture de la fenêtre
            running = False # running est sur False
            sys.exit() # pour fermer correctement
       
       # gestion du clavier
        if event.type == pygame.KEYDOWN : # si une touche a été tapée
            if event.key == pygame.K_LEFT : # si la touche est la fleche gauche
                print("j'ai appuyé sur la fleche gauche")
            if event.key == pygame.K_RIGHT : # si la touche est la fleche droite
                print("j'ai appuyé sur la fleche droite")

    ### Actualisation de la scene ###
    pygame.display.update() # pour mettre à jour l'écran