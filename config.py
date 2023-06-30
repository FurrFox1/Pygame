import pygame
############################################

def reescalar_imagen(lista_imagenes, tamaño):
    for i in range(len(lista_imagenes)):
        lista_imagenes[i] = pygame.transform.scale(lista_imagenes[i], tamaño)



def girar_imagen(lista_original, flip_x, flip_y):
    lista_girada = []
    for imagen in lista_original:
        lista_girada.append(pygame.transform.flip(imagen, flip_x, flip_y))

    return lista_girada

def obtener_rectangulos(principal)-> dict:
    dict = {}
    dict["main"] = principal
    dict["bottom"] = pygame.Rect(principal.left, principal.bottom -10, principal.width, 10)
    dict["right"] = pygame.Rect(principal.right -2, principal.top, 2, principal.height)
    dict["left"] = pygame.Rect(principal.left, principal.top, 2, principal.height)
    dict["top"] = pygame.Rect(principal.left, principal.top, principal.width, 10)
    return dict

############################################



player_run = [pygame.image.load("Run/Run_1.png"), 
              pygame.image.load("Run/Run_2.png"),
              pygame.image.load("Run/Run_3.png"), 
              pygame.image.load("Run/Run_4.png")]

player_jump = [pygame.image.load("Jump/Jump_1.png"),
               pygame.image.load("Jump/Jump_2.png"), 
               pygame.image.load("Jump/Jump_3.png")]

player_wait = [pygame.image.load("Wait/wait_1.png"),
               pygame.image.load("Wait/wait_2.png"),]

player_run_left = girar_imagen(player_run, True, False)