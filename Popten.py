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

def Pop_Ten():
    pygame.display.set_caption("Conecta 4 - Pop Ten")
    ventana = pygame.display.set_mode((800, 700))
    font = pygame.font.SysFont('Jokerman', 20)

    tablero = [[None] * 7 for _ in range(6)]
    celda = 700 // 7

    cambio_fase = False
    victoria = False
    colocar = False

    alerta1 = False
    alerta2 = False
    alerta3 = False
    alerta4 = False
    
    textos1 = True
    textos2 = False
    boton_llenar = True

    contador1 = 0
    contador2 = 0

    pantalla = True
    turno = 'x'
    xs = []

    while pantalla:
        ventana.fill(negro)

        jugador = font.render('Turno:', True, blanco)
        ventana.blit(jugador, (650, 58))
        ventana.blit(imagen_x, (720, 66)) if turno == 'x' else ventana.blit(imagen_o, (720, 66))

        F.crear_boton(ventana, "Regresar", "Jokerman", 20, (640, 12), 110, 40, gris)

        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            elif F.click_boton((640, 12), 110, 40, evento):
                pantalla = False

            elif evento.type == pygame.MOUSEBUTTONDOWN:
                x, y = evento.pos
                col = x // (celda + 15)

                if y > 100:
                    if contador1 < 10 and contador2 < 10:
                        if not cambio_fase:
                            boton_llenar = True
                            textos1 = True
                            textos2 = False
                            alerta1 = False

                            for fila in range(5, -1, -1):
                                fila_llena = False
                                for columna in range(7):
                                    if tablero[fila][columna] is None:
                                        fila_llena = True
                                
                                if fila_llena:
                                    if tablero[fila][col] is None:
                                        tablero[fila][col] = turno
                                        turno = 'o' if turno == 'x' else 'x'
                                    else:
                                        alerta1 = True
                                    break

                        else:
                            textos2 = True
                            textos1 = False
                            alerta2 = False
                            alerta3 = False  
                            alerta4 = False
                            
                            if not colocar:

                                if tablero[5][col] == turno:

                                    if F.cuatro_raya(tablero, col, turno):
                                        if turno == 'x':
                                            contador1 += 1
                                        else:
                                            contador2 += 1

                                        for fila in range(5, -1, -1):
                                            if fila == 0:
                                                tablero[fila][col] = None
                                            else:
                                                tablero[fila][col] = tablero[fila - 1][col]

                                    else:
                                        alerta3 = True
                                        xs.append(col)

                                        for fila in range(5, -1, -1):
                                            if fila == 0:
                                                tablero[fila][col] = None
                                            else:
                                                tablero[fila][col] = tablero[fila - 1][col]
                                        
                                        colocar = True

                                else:
                                    alerta2 = True

                            else:
                                nueva_columna = xs[-1]

                                if nueva_columna != col:
                                    for nueva_fila in range(5, -1, -1):
                                        if tablero[nueva_fila][col] is None:
                                            tablero[nueva_fila][col] = turno
                                            turno = 'x' if turno == 'o' else 'o'
                                            colocar = False
                                            break
                                else:
                                    alerta4 = True
                    
                    else:
                        victoria = True

                if F.saturado(tablero):
                    textos2, cambio_fase = True, True
                    textos1, boton_llenar = False, False

        F.graficar_tablero(ventana, tablero)

        if alerta1:
            texto = font.render('Se debe llenar la fila primero! Vuelve a intentarlo', True, rojo)
            ventana.blit(texto, (40, 32))
            textos1 = False

        elif alerta2:
            texto = font.render('Esta ficha no te pertenece! Vuelve a intentarlo', True, rojo)
            ventana.blit(texto, (40, 32))
            textos2 = False

        elif alerta3:
            texto = font.render('La ficha que retiraste no hacia parte de 4 en linea', True, rojo)
            ventana.blit(texto, (40, 32))
            textos2 = False

        elif alerta4:
            texto = font.render('No puedes poner esta ficha en la misma columna', True, rojo)
            ventana.blit(texto, (40, 32))
            textos2 = False

        if victoria:
            ganador = 1 if contador1 == 10 else 2
            texto = font.render(f'Felicidades! Ha ganado el jugador {ganador}', True, verde)
            ventana.blit(texto, (40, 34))
            textos2 = False

            F.crear_boton(ventana, "Revancha?", "Jokerman", 20, (490, 12), 120, 40, gris)
            if F.click_boton((490, 12), 120, 40, evento):
                tablero = [[None] * 7 for _ in range(6)]
                victoria, cambio_fase = False, False
                turno = 'x' if turno == 'o' else 'o'
                contador1, contador2 = 0, 0
                textos1 = True
        
        if boton_llenar:
            F.crear_boton(ventana, "Rellenar", "Jokerman", 20, (530, 12), 100, 30, gris)
            if F.click_boton((530, 12), 100, 30, evento):
                tablero = F.llenar_tablero(tablero)
                alerta1, boton_llenar = False, False
                textos1 = False
                textos2 = True

        if textos1:
            texto = font.render('Primera fase: se llena el tablero fila por fila.', True, blanco)
            ventana.blit(texto, (40, 32))

        elif textos2:
            texto = font.render('Segunda fase: gana el primero que saque 10 fichas', True, blanco)
            texto2 = font.render('donde cada una haga parte de un 4 en linea', True, blanco)
            texto3 = font.render(f'jugador 1:      x{contador1}', True, verde)
            texto4 = font.render(f'jugador 2:      x{contador2}', True, verde)
            ventana.blit(imagen_x, (148, 66))
            ventana.blit(imagen_o, (452, 66))
            ventana.blit(texto, (40, 4))
            ventana.blit(texto2, (40, 32))
            ventana.blit(texto3, (40, 60))
            ventana.blit(texto4, (340, 60))

        pygame.display.update()