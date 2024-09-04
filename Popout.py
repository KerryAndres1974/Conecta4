import pygame, sys
import Funciones as F

blanco = (255,255,255)
gris = (200,200,200)
rojo = (255,0,0)
verde = (49,170,43)
negro = (0,0,0)

img_o = pygame.image.load("util/fichaR.png")
img_x = pygame.image.load("util/fichaB.png")
imagen_o = pygame.transform.scale(img_o, (20, 20))
imagen_x = pygame.transform.scale(img_x, (20, 20))

def Pop_out():
    pygame.display.set_caption("Conecta 4 - Pop out")
    ventana = pygame.display.set_mode((800, 700))
    font = pygame.font.SysFont('Jokerman', 20)

    tablero = [[None] * 7 for _ in range(6)]
    victoria = False
    celda = 700 // 7

    alerta1 = False
    alerta2 = False
    alerta3 = False
    pantalla = True
    turno = 'x'

    while pantalla:
        ventana.fill(negro)
        
        jugador = font.render('Turno:', True, blanco)
        ventana.blit(jugador, (650, 58))
        ventana.blit(imagen_x, (720,66)) if turno == 'x' else ventana.blit(imagen_o, (720,66))

        F.crear_boton(ventana, "Regresar", "Jokerman", 20, (640, 12), 110, 40, gris)
        textos = True

        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
                
            elif F.click_boton((640, 12), 110, 40, evento):
                pantalla = False

            elif evento.type == pygame.MOUSEBUTTONDOWN:
                x, y = evento.pos
                col = x // (celda + 15)
                fil = y // (celda + 15)
                ganador = F.cuatro_linea(tablero)

                if ganador == 0:
                    alerta1 = False
                    alerta2 = False
                    alerta3 = False

                    if y >= 600:
                        if tablero[fil][col] == turno:
                            for fila in range(5, -1, -1):
                                if fila == 0:
                                    tablero[fila][col] = None
                                else:
                                    tablero[fila][col] = tablero[fila - 1][col]
                            turno = 'o' if turno == 'x' else 'x'
                    
                        elif tablero[fil][col] is None:
                            alerta3 = True

                        elif tablero[fil][col] != turno:
                            alerta2 = True

                    elif y > 90:
                        for fila in range(5, -1, -1):
                            if tablero[fila][col] is None:
                                tablero[fila][col] = turno
                                turno = 'o' if turno == 'x' else 'x'
                                break

                        if tablero[0][col] is not None:
                            alerta1 = True
                            
                else:
                    victoria = True

        pygame.draw.rect(ventana, verde, (0, 600, 800, 100), 2)
        F.graficar_tablero(ventana, tablero)

        if alerta1:
            texto = font.render('No hay más espacios en esta columna! Prueba en otra', True, rojo)
            ventana.blit(texto, (40, 32))
            textos = False

        elif alerta2:
            texto = font.render('Esta ficha no te pertenece! Vuelve a intentarlo', True, rojo)
            ventana.blit(texto, (40, 32))
            textos = False

        elif alerta3:
            texto = font.render('No hay ficha que remover aqui! Intentalo de nuevo', True, rojo)
            ventana.blit(texto, (40, 32))
            textos = False

        elif victoria:
            texto = font.render(f'Felicidades! Ha ganado el jugador {ganador}', True, verde)
            ventana.blit(texto, (40, 32))
            textos = False

            F.crear_boton(ventana, "Revancha?", "Jokerman", 20, (490, 12), 120, 40, gris)
            if F.click_boton((500, 12), 110, 40, evento):
                tablero = [[None] * 7 for _ in range(6)]
                victoria = False

        if textos:
            texto = font.render('Debes conectar 4 fichas de forma horizontal, vertical o', True, blanco)
            texto2 = font.render('diagonal. Tambien puedes remover una ficha', True, blanco)
            texto3 = font.render('de la primera fila.', True, blanco)
            ventana.blit(texto, (40, 4))
            ventana.blit(texto2, (40, 32))
            ventana.blit(texto3, (40, 60))

        pygame.display.update()