import pygame

# Dimensiones de la ventana del juego
ANCHO = 800
ALTO = 600

# Colores
BLANCO = (255, 255, 255)
AZUL = (0, 0, 255)

# Clase para el jugador
class Jugador(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((40, 40))
        self.image.fill(AZUL)
        self.rect = self.image.get_rect()
        self.rect.x = 50
        self.rect.y = ALTO - self.rect.height
        self.vel_y = 0

    def update(self):
        self.rect.y += self.vel_y

        # Gravedad
        if self.vel_y == 0:
            self.vel_y = 1
        else:
            self.vel_y += 0.35

        # Colisión con el suelo
        if self.rect.y >= ALTO - self.rect.height and self.vel_y >= 0:
            self.vel_y = 0
            self.rect.y = ALTO - self.rect.height

    def saltar(self):
        self.vel_y = -10


# Inicialización de Pygame
pygame.init()
ventana = pygame.display.set_mode((ANCHO, ALTO))
pygame.display.set_caption("Juego de Plataformas")

# Grupo de sprites
sprites = pygame.sprite.Group()
jugador = Jugador()
sprites.add(jugador)

# Bucle principal del juego
jugando = True
reloj = pygame.time.Clock()

while jugando:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            jugando = False
        elif evento.type == pygame.KEYDOWN:
            if evento.key == pygame.K_SPACE:
                jugador.saltar()

    sprites.update()

    ventana.fill(BLANCO)
    sprites.draw(ventana)

    pygame.display.flip()
    reloj.tick(60)

pygame.quit()
