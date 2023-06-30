import pygame, sys
from config import *
from pygame.locals import *
from player import Personaje
from modo import *

############################################
def actualizar_pantalla(pantalla, un_personaje: Personaje, background, lados_piso):
    pantalla.blit(background, (0, 0))
    #PLATAFORMA
    un_personaje.update(pantalla, lados_piso)
############################################


#SCREEN
W, H = 1000, 800
size_screen = (W,H)
screen = pygame.display.set_mode(size_screen)
reloj = pygame.time.Clock()
FPS = 20
pygame.display.set_caption("Sonic on the jump")
tick = pygame.USEREVENT + 0
pygame.time.set_timer(tick, 100)
screen.fill("White")


#BG
background = pygame.image.load("Background\paper_texture_green_hill.png")
background = pygame.transform.scale(background, size_screen)
suelo = pygame.image.load("Plataforma.png")

#PLAYER
posicion_inicial = (H/2 - 300, 550)
tamaño = (150, 150)

dict_animation = {}
dict_animation["run_left"] = player_run_left
dict_animation["run_right"] = player_run
dict_animation["jump"] = player_jump
dict_animation["wait"] = player_wait

mi_personaje = Personaje(tamaño, dict_animation, posicion_inicial, 10)

#SUELO
piso = pygame.Rect(0,0,W, 20)
piso.top = mi_personaje.lados["main"].bottom
lados_piso = obtener_rectangulos(piso)

#PLATAFORMA
while True:
    reloj.tick(FPS)
    for event in pygame.event.get():
        print(event)
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_TAB:
                cambiar_modo()
            

    keys = pygame.key.get_pressed()
    if keys[pygame.K_RIGHT]:
        mi_personaje.que_hace = "derecha"
    elif keys[pygame.K_LEFT]:
        mi_personaje.que_hace = "izquierda"
    elif keys[pygame.K_UP]:
        mi_personaje.que_hace = "salta"
    else:
        mi_personaje.que_hace = "quieto"

    actualizar_pantalla(screen, mi_personaje, background, lados_piso)

    if get_modo():
        for lado in lados_piso:
            pygame.draw.rect(screen, "Red", lados_piso[lado], 2)  
        for lado in mi_personaje.lados:
            pygame.draw.rect(screen, "Green", mi_personaje.lados[lado], 2)


    
        


    #Actualizar pantalla
    pygame.display.flip()
    
    pass
