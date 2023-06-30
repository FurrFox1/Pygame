import pygame
from config import reescalar_imagen , obtener_rectangulos
class Personaje:
    def __init__(self, tamaño, animaciones, posicion_inicial, velocidad):
        self.ancho = tamaño[0]
        self.alto = tamaño[1]

        #GRAVEDAD
        self.gravedad = 1
        self.potencia_salto = -15
        self.limite_velocidad_caida = 15
        self.esta_saltando = False
        

        #ANIMACION
        self.contador_pasos = 0
        self.que_hace = "quieto"
        self.animaciones = animaciones
        self.reescalar_animaciones()

        #RECTANGULOS
        rectangulo = self.animaciones["run_left"][0].get_rect()
        rectangulo.x = posicion_inicial[0]
        rectangulo.y = posicion_inicial[1]
        self.lados = obtener_rectangulos(rectangulo)

        #VELOCIDAD
        self.desplazamiento_y = 0
        self.velocidad = velocidad
        

    def reescalar_animaciones(self):
        for clave in self.animaciones:
            reescalar_imagen(self.animaciones[clave], (self.ancho, self.alto))


    def animar(self, pantalla, que_animacion:str):
        animacion = self.animaciones[que_animacion]
        largo = len(animacion)

        if self.contador_pasos >= largo:
            self.contador_pasos = 0

        pantalla.blit(animacion[self.contador_pasos], self.lados["main"])
        self.contador_pasos += 1

        pass

    def mover(self, velocidad):
        for lado in self.lados:
            self.lados[lado].x += velocidad
        pass
    
    def update(self, pantalla, piso):
        match self.que_hace:
            case "derecha":
                if not self.esta_saltando:
                    self.animar(pantalla, "run_right")
                self.mover(self.velocidad)
            case "izquierda":
                if not self.esta_saltando:
                    self.animar(pantalla, "run_left")
                self.mover(self.velocidad * - 1)
            case "salta":
                if not self.esta_saltando:
                    self.esta_saltando = True
                    self.desplazamiento_y = self.potencia_salto
            case "quieto":
                if not self.esta_saltando:
                    self.animar(pantalla, "wait")

        self.aplicar_gravedad(pantalla, piso)

    def aplicar_gravedad(self, pantalla, piso):
        if self.esta_saltando:
            self.animar(pantalla, "jump")

            for lado in self.lados:
                self.lados[lado].y += self.desplazamiento_y
            
            if self.desplazamiento_y + self.gravedad < self.limite_velocidad_caida:
                self.desplazamiento_y += self.gravedad

        if self.lados["bottom"].colliderect(piso["top"]):
            self.desplazamiento_y = 0
            self.esta_saltando = False
            self.lados["main"].bottom = piso["main"].top
            

        


