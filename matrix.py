import pygame
import random
import cv2
import numpy as np

# Initialiser Pygame
pygame.init()

# Dimensions de la fenêtre
width, height = 800, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Matrix Animation")

# Couleurs
black = (0, 0, 0)
green = (0, 255, 0)

# Liste de caractères
characters = list("GLEAPHE")

# Positions des gouttes
drops = [0] * (width // 20)  # Pour chaque colonne

# Configuration pour l'enregistrement vidéo
fourcc = cv2.VideoWriter_fourcc(*'mp4v')
out = cv2.VideoWriter('matrix_animation.mp4', fourcc, 20.0, (width, height))

# Boucle principale de l'animation
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            
    screen.fill(black)

    # Remplissage de l'écran avec des caractères en colonnes
    for col in range(0, width, 20):  # Parcourir les colonnes
        # Choisir un caractère aléatoire
        char = random.choice(characters)
        
        # Vérifier la position de la goutte
        if drops[col // 20] < height:
            font = pygame.font.SysFont('Arial', 20)
            text = font.render(char, True, green)
            screen.blit(text, (col, drops[col // 20]))
            
            # Incrémenter la position de la goutte
            drops[col // 20] += 20
            
        # Réinitialiser la goutte si elle atteint le bas de l'écran
        if drops[col // 20] >= height or random.random() < 0.05:
            drops[col // 20] = 0
            
    pygame.display.flip()
    
    # Capture de l'écran pour l'enregistrement vidéo
    frame = pygame.surfarray.array3d(pygame.display.get_surface())
    frame = np.rot90(frame)  # Rotation pour passer de (width, height, 3) à (height, width, 3)
    frame = np.flipud(frame)  # Inverser l'axe Y pour corriger l'orientation
    frame = cv2.cvtColor(frame, cv2.COLOR_RGB2BGR)
    out.write(frame)

    pygame.time.delay(100)  # Délai pour contrôler la vitesse de l'animation

# Libérer les ressources
out.release()
pygame.quit()
