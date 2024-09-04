import pygame, sys
from Clasico import Clasico
from Popout import Pop_out
from Popten import Pop_Ten
import Funciones as F

# Inicializar Pygame
pygame.init()

# Colores
negro = (0, 0, 0)
blanco = (255, 255, 255)
gris = (200, 200, 200)

# Función para la ventana principal
def window():
    pantalla = True
    ventana = pygame.display.set_mode((400, 400))
    pygame.display.set_caption("Conecta 4")
    font = pygame.font.SysFont("Harlow Solid Italic", 30)
    verdadero = False

    while pantalla:
        ventana.fill(blanco)
        
        F.crear_boton(ventana, "Clasico", "Harlow Solid Italic", 36, (100, 70), 200, 50, gris)
        F.crear_boton(ventana, "Pop Out", "Harlow Solid Italic", 36, (100, 170), 200, 50, gris)
        F.crear_boton(ventana, "Pop Ten", "Harlow Solid Italic", 36, (100, 270), 200, 50, gris)
        
        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                pantalla = False
                pygame.quit()
                sys.exit()

            elif F.click_boton((100, 70), 200, 50, e):
                verdadero = True

            elif F.click_boton((100, 170), 200, 50, e):
                Pop_out()
                pygame.display.set_mode((400, 400))

            elif F.click_boton((100, 270), 200, 50, e):
                Pop_Ten()
                pygame.display.set_mode((400, 400))

        if verdadero:
            ventana.fill(blanco)
            texto = font.render("Escoje a tu oponente", True, negro)
            ventana.blit(texto, (96, 10))

            F.crear_boton(ventana, "Humano", "Harlow Solid Italic", 36, (100, 70), 200, 50, gris)
            F.crear_boton(ventana, "Maquina", "Harlow Solid Italic", 36, (100, 170), 200, 50, gris)
            F.crear_boton(ventana, "Regresar", "Harlow Solid Italic", 36, (100, 270), 200, 50, gris)

            if F.click_boton((100, 70), 200, 50, e):
                Clasico()
                pygame.display.set_mode((400, 400))

            elif F.click_boton((100, 170), 200, 50, e):
                print("Holaa")

            elif F.click_boton((100, 270), 200, 50, e):
                verdadero = False
            

        pygame.display.flip()

# Ejecutar la ventana principal
window()