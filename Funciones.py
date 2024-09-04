import pygame, random

negro = (0,0,0)
gris = (200,200,200)

# Crear un botón
def crear_boton(lienzo, texto, fuente, tamaño, pos, ancho, alto, color):
    pygame.draw.rect(lienzo, color, (pos[0], pos[1], ancho, alto))
    font = pygame.font.SysFont(fuente, tamaño)
    text_surface = font.render(texto, True, negro)
    lienzo.blit(text_surface, (pos[0] + (ancho - text_surface.get_width()) // 2, pos[1] + (alto - text_surface.get_height()) // 2))

# Función para manecolumnaar los eventos de los botones
def click_boton(pos, ancho, alto, e):
    if e.type == pygame.MOUSEBUTTONDOWN:
        if pos[0] < e.pos[0] < pos[0] + ancho and pos[1] < e.pos[1] < pos[1] + alto:
            return True
    return False

def graficar_tablero(ventana, tab):
    celda = 700 // 7
    img_x = pygame.image.load("util/fichaB.png")
    img_o = pygame.image.load("util/fichaR.png")
    imagen_x = pygame.transform.scale(img_x, (celda + 15, celda + 15))
    imagen_o = pygame.transform.scale(img_o, (celda + 15, celda + 15))

    for fila in range(len(tab)):
        for col in range(len(tab[0])):
            x = col * (celda + 15) + (celda + 15) // 2
            y = fila * celda + celda // 2 + 100

            if tab[fila][col] is None:
                pygame.draw.circle(ventana, gris, (x, y), 45)
            elif tab[fila][col] == 'x':
                ventana.blit(imagen_x, (col * (celda + 15), fila * celda + 90))
            elif tab[fila][col] == 'o':
                ventana.blit(imagen_o, (col * (celda + 15), fila * celda + 90))

def cuatro_linea(tab):
    ganador = 0

    # Vertical
    for i in range(len(tab) - 3):
        for columna in range(len(tab[0])):
            if tab[i][columna] == 'x' and tab[i+1][columna] == 'x' and tab[i+2][columna] == 'x' and tab[i+3][columna] == 'x':
                ganador = 1
            elif tab[i][columna] == 'o' and tab[i+1][columna] == 'o' and tab[i+2][columna] == 'o' and tab[i+3][columna] == 'o':
                ganador = 2

    # Horizontal
    for i in range(len(tab)):
        for columna in range(len(tab[0]) - 3):
            if tab[i][columna] == 'x' and tab[i][columna+1] == 'x' and tab[i][columna+2] == 'x' and tab[i][columna+3] == 'x':
                ganador = 1
            elif tab[i][columna] == 'o' and tab[i][columna+1] == 'o' and tab[i][columna+2] == 'o' and tab[i][columna+3] == 'o':
                ganador = 2

    # Diagonales
    for i in range(len(tab) - 3):
        for columna in range(len(tab[0])):
            if columna <= len(tab[0]) - 4:
                if tab[i][columna] == 'x' and tab[i+1][columna+1] == 'x' and tab[i+2][columna+2] == 'x' and tab[i+3][columna+3] == 'x':
                    ganador = 1
                elif tab[i][columna] == 'o' and tab[i+1][columna+1] == 'o' and tab[i+2][columna+2] == 'o' and tab[i+3][columna+3] == 'o':
                    ganador = 2

            if columna >= 3:
                if tab[i][columna] == 'x' and tab[i+1][columna-1] == 'x' and tab[i+2][columna-2] == 'x' and tab[i+3][columna-3] == 'x':
                    ganador = 1
                elif tab[i][columna] == 'o' and tab[i+1][columna-1] == 'o' and tab[i+2][columna-2] == 'o' and tab[i+3][columna-3] == 'o':
                    ganador = 2

    return ganador

def saturado(tab):
    for i in range(6):
        if tab[0][i] is None:
            return False
    return True

def cuatro_raya(tab, columna, turno):
    filas = len(tab)
    columnas = len(tab[0])

    # Vertical
    if tab[5][columna] == turno and tab[4][columna] == turno and \
        tab[3][columna] == turno and tab[2][columna] == turno:
        return True
    
    # Horizontal
    cola = max(0, columna - 3)
    colz = min(columnas, columna + 4)
    for j in range(cola, colz - 3):
        if tab[5][j] == turno and tab[5][j + 1] == turno and \
            tab[5][j + 2] == turno and tab[5][j + 3] == turno:
            return True
        
    # Diagonal derecha
    for i in range(-3, 1):
        if 0 <= columna + i < columnas and \
           0 <= columna + i + 3 < columnas and 0 <= 2 < filas:
            if (tab[5][columna + i] == turno and
                tab[5 - 1][columna + i + 1] == turno and
                tab[5 - 2][columna + i + 2] == turno and
                tab[5 - 3][columna + i + 3] == turno):
                return True

    # Diagonal izquierda
    for i in range(-3, 1):
        if 0 <= columna - i < columnas and \
           0 <= columna - i - 3 < columnas and 0 <= 2 < filas:
            if (tab[5][columna - i] == turno and
                tab[5 - 1][columna - i - 1] == turno and
                tab[5 - 2][columna - i - 2] == turno and
                tab[5 - 3][columna - i - 3] == turno):
                return True

    return False

def llenar_tablero(tablero):
    residuo = random.choice([1, 0])

    for i in range(6):

        xs = tablero[i].count('x')
        os = tablero[i].count('o')

        if i % 2 == residuo:
            fichas = ['x'] * (4 - xs) + ['o'] * (3 - os)
        else:
            fichas = ['o'] * (4 - os) + ['x'] * (3 - xs)

        random.shuffle(fichas)

        for j in range(7):
            if tablero[i][j] is None:
                tablero[i][j] = fichas.pop(0)

    return tablero