import pygame, sys
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
    font = pygame.font.SysFont('Jokerman', 20)

    while pantalla:
        ventana.fill(blanco)

        texto = font.render('Escoje a tu oponente', True, negro)
        ventana.blit(texto, (100, 15))
        
        F.crear_boton(ventana, "Humano", "Harlow Solid Italic", 36, (100, 80), 200, 50, gris)
        F.crear_boton(ventana, "Maquina", "Harlow Solid Italic", 36, (100, 180), 200, 50, gris)
        F.crear_boton(ventana, "Regresar", "Harlow Solid Italic", 36, (100, 280), 200, 50, gris)
        
        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            elif F.click_boton((100, 80), 200, 50, e):
                print(1)

            elif F.click_boton((100, 180), 200, 50, e):
                print(2)

            elif F.click_boton((100, 280), 200, 50, e):
                print(3)

        pygame.display.flip()

# Ejecutar la ventana principal
window()