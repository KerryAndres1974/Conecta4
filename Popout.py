import pygame, sys, os
import Funciones as F

blanco = (255,255,255)
gris = (200,200,200)
rojo = (255,0,0)
verde = (49,170,43)
negro = (0,0,0)
gris2 = (150, 150, 150)

img_o = pygame.image.load("util/fichaR.png")
img_x = pygame.image.load("util/fichaB.png")
imagen_o = pygame.transform.scale(img_o, (20, 20))
imagen_x = pygame.transform.scale(img_x, (20, 20))

def Pop_outH():
    os.environ['SDL_VIDEO_CENTERED'] = '1'
    ventana = pygame.display.set_mode((800, 700))
    font = pygame.font.SysFont('Jokerman', 20)

    tablero = [[None] * 7 for _ in range(6)]
    celda = 700 // 7

    victoria = False
    alerta1 = False
    alerta2 = False
    alerta3 = False
    pantalla = True
    ganador = 0
    turno = 'x'

    while pantalla:
        ventana.fill(blanco)
        textos = True
        
        if not victoria:
            F.crear_boton(ventana, "Regresar", "Jokerman", 20, (640, 12), 110, 40, gris)
            jugador = font.render('Turno:', True, negro)
            ventana.blit(jugador, (650, 58))
            ventana.blit(imagen_x, (720,66)) if turno == 'x' else ventana.blit(imagen_o, (720,66))

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

                if not victoria:
                    alerta1 = False
                    alerta2 = False
                    alerta3 = False

                    if y >= 600:
                        if tablero[fil][col] == turno:
                            for fila in range(5, -1, -1):
                                tablero[fila][col] = tablero[fila - 1][col] if fila > 0 else None
                    
                        elif tablero[fil][col] is None:
                            alerta3 = True

                        elif tablero[fil][col] != turno:
                            alerta2 = True

                    elif y > 90:
                        for fila in range(5, -1, -1):
                            if tablero[fila][col] is None:
                                tablero[fila][col] = turno
                                break

                        if tablero[0][col] is not None:
                            alerta1 = True

                    fichas, ganador = F.cuatro_linea(tablero)
                    if fichas:
                        for f,c in fichas:
                            tablero[f][c] = 'g'

                    if ganador != 0:
                        victoria = True
                    elif not(alerta1 or alerta2 or alerta3):
                        turno = 'x' if turno == 'o' else 'o'

        pygame.draw.rect(ventana, verde, (0, 600, 800, 100), 2)
        F.graficar_tablero(ventana, tablero, ganador)

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
            fuente = pygame.font.SysFont('Jokerman', 30)
            texto = fuente.render(f'Felicidades! Ha ganado el jugador {ganador}', True, verde)
            ventana.blit(texto, (145, 34))
            textos = False

            F.crear_boton(ventana, f"¿Revancha jugador {1 if turno == 'o' else 2}?", "Jokerman", 20, (100, 350), 300, 60, gris2)
            F.crear_boton(ventana, "Aceptar", "Jokerman", 20, (450, 350), 120, 60, gris2)
            F.crear_boton(ventana, "Regresar", "Jokerman", 20, (600, 350), 120, 60, gris2)
            if F.click_boton((450, 350), 120, 60, evento):
                tablero = [[None] * 7 for _ in range(6)]
                turno = 'x' if turno == 'o' else 'o'
                victoria = False

            if F.click_boton((600, 350), 120, 60, evento):
                pantalla = False

        if textos:
            texto = font.render('Debes conectar 4 fichas de forma horizontal, vertical o', True, negro)
            texto2 = font.render('diagonal. Tambien puedes remover una ficha', True, negro)
            texto3 = font.render('de la primera fila.', True, negro)
            ventana.blit(texto, (40, 4))
            ventana.blit(texto2, (40, 32))
            ventana.blit(texto3, (40, 60))

        pygame.display.update()

def Pop_out():
    pantalla = True
    pygame.display.set_caption("Conecta 4 - Pop Out")
    ventana = pygame.display.set_mode((400, 400))
    font = pygame.font.SysFont('Harlow Solid Italic', 35)

    while pantalla:
        ventana.fill(blanco)

        texto = font.render('Escoje a tu oponente', True, negro)
        ventana.blit(texto, (72, 20))
        
        F.crear_boton(ventana, "Humano", "Harlow Solid Italic", 36, (100, 80), 200, 50, gris)
        F.crear_boton(ventana, "Maquina", "Harlow Solid Italic", 36, (100, 180), 200, 50, gris)
        F.crear_boton(ventana, "Regresar", "Harlow Solid Italic", 36, (100, 280), 200, 50, gris)
        
        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            elif F.click_boton((100, 80), 200, 50, e):
                Pop_outH()
                pygame.display.set_mode((400, 400))

            elif F.click_boton((100, 180), 200, 50, e):
                print(2)

            elif F.click_boton((100, 280), 200, 50, e):
                pantalla = False
                
        pygame.display.flip()