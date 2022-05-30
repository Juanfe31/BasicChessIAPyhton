import pygame, sys
import numpy as np
import random



# iniciar pygame
pygame.init()

# poder escribir vainas
pygame.font.init()

# crear ventana
screen = pygame.display.set_mode((600, 600))

# titulo y icono
pygame.display.set_caption("Games VS IA")
icon = pygame.image.load('ai.png')
pygame.display.set_icon(icon)

# imagenes
imgPortada = pygame.image.load('LogoGames.png')
imgO = pygame.image.load('O.png')
imgX = pygame.image.load('X.png')
imgC1 = pygame.image.load('tic-tac-toe.png')
imgC2 = pygame.image.load('w_king.png')

board = np.zeros((3, 3))
arrayCopy = np.zeros((3, 3))

# contador de victorias

contadorPlayer1 = 0
contadorPlayer2 = 0
player = 1

black = (0, 0, 0)

# declara un tipo de font
font1 = pygame.font.SysFont('Arial', 35)
font2 = pygame.font.SysFont('Arial', 30)
font22 = pygame.font.SysFont('Arial', 25)
fontNumero = pygame.font.SysFont('Arial', 100)


# titulos funcion
def draw_text(text, font, color, surface, x, y):
    textobj = font.render(text, 1, color)
    textrect = textobj.get_rect()
    textrect.topleft = (x, y)
    surface.blit(textobj, textrect)


click = False


# loop mantener ventana abierta
def startMenu():
    pygame.display.set_caption("Games VS IA")
    click = False
    while True:
        # RGB (0-255)
        screen.fill((40, 40, 40))
        screen.blit(imgPortada, (60, 30))
        screen.blit(imgC1, (285, 210))
        screen.blit(imgC2, (270, 295))

        # gets mouse position
        mx, my = pygame.mouse.get_pos()

        # crear el objeto
        # pygame.Rect(left, top, width, height)
        # hacer un centrado
        buttonTLocal = pygame.Rect(50, 200, 200, 50)
        buttonTIA = pygame.Rect(350, 200, 200, 50)
        buttonChessLocal = pygame.Rect(50 , 300, 200, 50)
        buttonChessIA = pygame.Rect(350, 300, 200, 50)
        buttonExit = pygame.Rect(200, 460, 200, 50)

        # se presiona el boton
        if buttonTLocal.collidepoint((mx, my)):
            if click:
                gameVS()
        if buttonChessLocal.collidepoint((mx, my)):
            if click:
                chessPeonesLocal()
        if buttonChessIA.collidepoint((mx, my)):
            if click:
                chessPeonesIA()
        if buttonExit.collidepoint((mx, my)):
            if click:
                pygame.quit()
                sys.exit()
        if buttonTIA.collidepoint((mx, my)):
            if click:
                game()

        # renderizar el objeto
        pygame.draw.rect(screen, (10, 10, 10), buttonTLocal)
        pygame.draw.rect(screen, (0, 0, 0), buttonTLocal, 5)

        pygame.draw.rect(screen, (10, 10, 10), buttonTIA)
        pygame.draw.rect(screen, (0, 0, 0), buttonTIA,5)

        pygame.draw.rect(screen, (10, 10, 10), buttonChessLocal)
        pygame.draw.rect(screen, (0, 0, 0), buttonChessLocal,5)

        pygame.draw.rect(screen, (10, 10, 10), buttonChessIA)
        pygame.draw.rect(screen, (0, 0, 0), buttonChessIA, 5)

        pygame.draw.rect(screen, (10, 10, 10), buttonExit)
        pygame.draw.rect(screen, (0, 0, 0), buttonExit, 5)



        draw_text('Triqui Local', font1, (150, 150, 150), screen, 75, 205)
        draw_text('Triqui vs IA', font1, (150, 150, 150), screen, 380, 205)
        draw_text('Ajedrez Local', font1, (150, 150, 150), screen, 60, 305)
        draw_text('Ajedrez vs IA', font1, (150, 150, 150), screen, 365, 305)
        draw_text('Salir', font1, (200, 200, 200), screen, 265, 460)

        click = False
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True

        pygame.display.update()


def marcarCuadro(fil, col, jugador):
    board[fil][col] = jugador


def cuadroDisponible(fil, col, jugador):
    return board[fil][col] == 0


def cuadroLleno():
    for row in range(3):
        for col in range(3):
            if board[row][col] == 0:
                return False
    return True


def dibujarEnCuadro():
    for row in range(3):
        for col in range(3):
            if board[row][col] == 1:
                if (row == 0 and col == 0):
                    screen.blit(imgO, (167, 67))
                elif (row == 0 and col == 1):
                    screen.blit(imgO, (267, 67))
                elif (row == 0 and col == 2):
                    screen.blit(imgO, (367, 67))
                elif (row == 1 and col == 0):
                    screen.blit(imgO, (167, 167))
                elif (row == 1 and col == 1):
                    screen.blit(imgO, (267, 167))
                elif (row == 1 and col == 2):
                    screen.blit(imgO, (367, 167))
                elif (row == 2 and col == 0):
                    screen.blit(imgO, (167, 267))
                elif (row == 2 and col == 1):
                    screen.blit(imgO, (267, 267))
                elif (row == 2 and col == 2):
                    screen.blit(imgO, (367, 267))

            elif board[row][col] == 2:
                if (row == 0 and col == 0):
                    screen.blit(imgX, (167, 67))
                elif (row == 0 and col == 1):
                    screen.blit(imgX, (267, 67))
                elif (row == 0 and col == 2):
                    screen.blit(imgX, (367, 67))
                elif (row == 1 and col == 0):
                    screen.blit(imgX, (167, 167))
                elif (row == 1 and col == 1):
                    screen.blit(imgX, (267, 167))
                elif (row == 1 and col == 2):
                    screen.blit(imgX, (367, 167))
                elif (row == 2 and col == 0):
                    screen.blit(imgX, (167, 267))
                elif (row == 2 and col == 1):
                    screen.blit(imgX, (267, 267))
                elif (row == 2 and col == 2):
                    screen.blit(imgX, (367, 267))


def checkWin(player):
    # vertical win check
    for col in range(3):
        if board[0][col] == player and board[1][col] == player and board[2][col] == player:
            draw_vertical_winning_line(col, player)
            sumaAcumPlayer(player)
            dibujarEnCuadro()
            pygame.display.update()
            return True

        # horizontal win check
    for row in range(3):
        if board[row][0] == player and board[row][1] == player and board[row][2] == player:
            draw_horizontal_winning_line(row, player)
            sumaAcumPlayer(player)
            dibujarEnCuadro()
            pygame.display.update()
            return True

    # asc diagonal win check
    if board[2][0] == player and board[1][1] == player and board[0][2] == player:
        draw_diagonal(1, player)
        sumaAcumPlayer(player)
        dibujarEnCuadro()
        pygame.display.update()
        return True

    # desc diagonal win chek
    if board[0][0] == player and board[1][1] == player and board[2][2] == player:
        draw_diagonal(0, player)
        sumaAcumPlayer(player)
        dibujarEnCuadro()
        pygame.display.update()
        return True

    return False


def draw_lines():
    # Dibujo de las lineas, cuadro inicial
    # 1 horizontal
    pygame.draw.line(screen, black, (150, 150), (450, 150), 15)
    # 2 horizontal
    pygame.draw.line(screen, black, (150, 250), (450, 250), 15)
    # 1 vertical
    pygame.draw.line(screen, black, (250, 50), (250, 350), 15)
    # 2 vertical
    pygame.draw.line(screen, black, (350, 50), (350, 350), 15)

    # Lineas borde
    # 1 horizontal
    pygame.draw.line(screen, black, (150, 50), (450, 50), 15)
    # 2 horizontal
    pygame.draw.line(screen, black, (150, 350), (450, 350), 15)
    # 1 vertical
    pygame.draw.line(screen, black, (150, 50), (150, 350), 15)
    # 2 vertical
    pygame.draw.line(screen, black, (450, 50), (450, 350), 15)


def draw_vertical_winning_line(col, player):
    if (player == 1):
        color = (0, 102, 204)
    else:
        color = (153, 0, 0)

    if (col == 0):
        pygame.draw.line(screen, color, (200, 50), (200, 350), 10)
    if (col == 1):
        pygame.draw.line(screen, color, (300, 50), (300, 350), 10)
    if (col == 2):
        pygame.draw.line(screen, color, (400, 50), (400, 350), 10)


def draw_horizontal_winning_line(row, player):
    if (player == 1):
        color = (0, 102, 204)
    else:
        color = (153, 0, 0)

    if (row == 0):
        pygame.draw.line(screen, color, (150, 100), (450, 100), 10)
    if (row == 1):
        pygame.draw.line(screen, color, (150, 200), (450, 200), 10)
    if (row == 2):
        pygame.draw.line(screen, color, (150, 300), (450, 300), 10)


def draw_diagonal(diag, player):
    if (player == 1):
        color = (0, 102, 204)
    else:
        color = (153, 0, 0)

    if (diag == 0):
        pygame.draw.line(screen, color, (150, 50), (450, 350), 10)
    if (diag == 1):
        pygame.draw.line(screen, color, (150, 350), (450, 50), 10)


def sumaAcumPlayer(player):
    global contadorPlayer2
    global contadorPlayer1

    if player == 1:
        contadorPlayer1 += 1
    else:
        contadorPlayer2 += 1


def restart():
    for row in range(3):
        for col in range(3):
            board[row][col] = 0
    gameVS()

def restartIA():
    for row in range(3):
        for col in range(3):
            board[row][col] = 0
    game()


def gameVS():
    running = True
    click = False
    gameOver = False
    screen.fill((30, 30, 30))
    screen.blit(imgO, (80, 425))
    screen.blit(imgX, (445, 425))
    global contadorPlayer2
    global contadorPlayer1
    global player

    # cuando jugador=1 es circulo, cuando jugador=2 es x

    cua1 = pygame.Rect(150, 50, 98, 98)
    cua2 = pygame.Rect(250, 50, 98, 98)
    cua3 = pygame.Rect(350, 50, 98, 98)
    cua4 = pygame.Rect(150, 150, 98, 98)
    cua5 = pygame.Rect(250, 150, 98, 98)
    cua6 = pygame.Rect(350, 150, 98, 98)
    cua7 = pygame.Rect(150, 250, 98, 98)
    cua8 = pygame.Rect(250, 250, 98, 98)
    cua9 = pygame.Rect(350, 250, 98, 98)
    buttonExit = pygame.Rect(160, 550, 280, 50)
    pygame.draw.rect(screen, (20, 20, 20), buttonExit)
    pygame.draw.rect(screen, (0, 0, 0), buttonExit,5)
    draw_text('Regresar al menú', font2, (200, 200, 200), screen, 195, 555)

    cuadroModo = pygame.Rect(0, 570, 120, 40)
    pygame.draw.rect(screen, (77, 0, 75), cuadroModo)
    pygame.draw.rect(screen, (107, 1, 125), cuadroModo,5)
    draw_text('V.S Jugador', font22, (200, 200, 200), screen, 5, 570)

    draw_lines()
    while running:

        draw_text(str(contadorPlayer1), fontNumero, (10, 7, 159), screen, 150, 400)
        draw_text(str(contadorPlayer2), fontNumero, (143, 4, 4), screen, 400, 400)

        mx, my = pygame.mouse.get_pos()

        if buttonExit.collidepoint((mx, my)):
            if click:
                for row in range(3):
                    for col in range(3):
                        board[row][col] = 0

                contadorPlayer1 = 0
                contadorPlayer2 = 0
                startMenu()

        if cua1.collidepoint((mx, my)):
            if click:
                if (cuadroDisponible(0, 0, player)):
                    marcarCuadro(0, 0, player)
                    if (checkWin(player)):
                        gameOver = True

                    if player == 1:
                        player = 2
                    else:
                        player = 1
                pygame.time.delay(500)
        if cua2.collidepoint((mx, my)):
            if click:
                if (cuadroDisponible(0, 1, player)):
                    marcarCuadro(0, 1, player)
                    if (checkWin(player)):
                        gameOver = True

                    if player == 1:
                        player = 2
                    else:
                        player = 1
                pygame.time.delay(500)
        if cua3.collidepoint((mx, my)):
            if click:
                if (cuadroDisponible(0, 2, player)):
                    marcarCuadro(0, 2, player)
                    if (checkWin(player)):
                        gameOver = True

                    if player == 1:
                        player = 2
                    else:
                        player = 1
                pygame.time.delay(500)
        if cua4.collidepoint((mx, my)):
            if click:
                if (cuadroDisponible(1, 0, player)):
                    marcarCuadro(1, 0, player)
                    if (checkWin(player)):
                        gameOver = True

                    if player == 1:
                        player = 2
                    else:
                        player = 1
                pygame.time.delay(500)
        if cua5.collidepoint((mx, my)):
            if click:
                if (cuadroDisponible(1, 1, player)):
                    marcarCuadro(1, 1, player)
                    if (checkWin(player)):
                        gameOver = True

                    if player == 1:
                        player = 2
                    else:
                        player = 1
                pygame.time.delay(500)
        if cua6.collidepoint((mx, my)):
            if click:
                if (cuadroDisponible(1, 2, player)):
                    marcarCuadro(1, 2, player)
                    if (checkWin(player)):
                        gameOver = True

                    if player == 1:
                        player = 2
                    else:
                        player = 1
                pygame.time.delay(500)
        if cua7.collidepoint((mx, my)):
            if click:
                if (cuadroDisponible(2, 0, player)):
                    marcarCuadro(2, 0, player)
                    if (checkWin(player)):
                        gameOver = True

                    if player == 1:
                        player = 2
                    else:
                        player = 1
                pygame.time.delay(500)
        if cua8.collidepoint((mx, my)):
            if click:
                if (cuadroDisponible(2, 1, player)):
                    marcarCuadro(2, 1, player)
                    if (checkWin(player)):
                        gameOver = True

                    if player == 1:
                        player = 2
                    else:
                        player = 1
                pygame.time.delay(500)
        if cua9.collidepoint((mx, my)):
            if click:
                if (cuadroDisponible(2, 2, player)):
                    marcarCuadro(2, 2, player)
                    if (checkWin(player)):
                        gameOver = True

                    if player == 1:
                        player = 2
                    else:
                        player = 1
                pygame.time.delay(500)

        dibujarEnCuadro()

        click = False
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.MOUSEBUTTONDOWN and not gameOver:
                if event.button == 1:
                    click = True

        if cuadroLleno() and not gameOver:
            draw_text("TIE", fontNumero, (255, 255, 255), screen, 230, 400)
            pygame.display.update()
            pygame.time.delay(1000)
            restart()

        if cuadroLleno():
            restart()

        if gameOver:
            restart()

        pygame.display.update()


def checkWinCopy(player):
    # vertical win check
    for col in range(3):
        if arrayCopy[0][col] == player and arrayCopy[1][col] == player and arrayCopy[2][col] == player:
            return True

        # horizontal win check
    for row in range(3):
        if arrayCopy[row][0] == player and arrayCopy[row][1] == player and arrayCopy[row][2] == player:
            return True

        # asc diagonal win check
    if arrayCopy[2][0] == player and arrayCopy[1][1] == player and arrayCopy[0][2] == player:
        return True

        # desc diagonal win chek
    if arrayCopy[0][0] == player and arrayCopy[1][1] == player and arrayCopy[2][2] == player:
        return True

    return False


def movimientoIA():
    global arrayCopy
    global player

    for row in range(3):
        for col in range(3):
            arrayCopy = board.copy()
            if arrayCopy[row][col] == 0:
                arrayCopy[row][col] = 2
                if checkWinCopy(2) == True:
                    board[row][col] = 2
                    player = 1
                    return
                else:
                    arrayCopy[row][col] = 0


    for row in range(3):
        for col in range(3):
            arrayCopy = board.copy()
            if arrayCopy[row][col] == 0:
                arrayCopy[row][col] = 1
            if checkWinCopy(1) == True:
                board[row][col] = 2
                player=1
                return
            else:
                arrayCopy[row][col] = 0

    rcol = 0
    rrow = 0

    while (True):
        if (board[1][1] == 0):
            board[1][1] = 2
            player = 1
            return
        else:
            rrow = random.randint(0, 2)
            rcol = random.randint(0, 2)
            if (board[rrow][rcol] == 0):
                board[rrow][rcol] = 2
                player = 1
                return





def game():
    running = True
    click = False
    gameOver = False
    screen.fill((30, 30, 30))
    screen.blit(imgO, (80, 425))
    screen.blit(imgX, (445, 425))
    global contadorPlayer2
    global contadorPlayer1
    global player


    # cuando jugador=1 es circulo, cuando jugador=2 es x

    cua1 = pygame.Rect(150, 50, 98, 98)
    cua2 = pygame.Rect(250, 50, 98, 98)
    cua3 = pygame.Rect(350, 50, 98, 98)
    cua4 = pygame.Rect(150, 150, 98, 98)
    cua5 = pygame.Rect(250, 150, 98, 98)
    cua6 = pygame.Rect(350, 150, 98, 98)
    cua7 = pygame.Rect(150, 250, 98, 98)
    cua8 = pygame.Rect(250, 250, 98, 98)
    cua9 = pygame.Rect(350, 250, 98, 98)
    buttonExit = pygame.Rect(160, 550, 280, 50)
    pygame.draw.rect(screen, (20, 20, 20), buttonExit)
    pygame.draw.rect(screen, (0, 0, 0), buttonExit,5)
    draw_text('Regresar al menú', font2, (200, 200, 200), screen, 195, 555)

    cuadroModo = pygame.Rect(0, 570, 110, 40)
    pygame.draw.rect(screen, (194, 81, 0), cuadroModo)
    pygame.draw.rect(screen, (255, 69, 10), cuadroModo,5)
    draw_text('V.S IA', font22, (200, 200, 200), screen, 25, 570)

    draw_lines()
    while running:

        draw_text(str(contadorPlayer1), fontNumero, (10, 7, 159), screen, 150, 400)
        draw_text(str(contadorPlayer2), fontNumero, (143, 4, 4), screen, 400, 400)

        mx, my = pygame.mouse.get_pos()

        if buttonExit.collidepoint((mx, my)):
            if click:
                for row in range(3):
                    for col in range(3):
                        board[row][col] = 0

                contadorPlayer1 = 0
                contadorPlayer2 = 0
                startMenu()

        if cua1.collidepoint((mx, my)):
            if click:
                if (cuadroDisponible(0, 0, player)):
                    marcarCuadro(0, 0, player)
                    if (checkWin(player)):
                        gameOver = True

                    if player == 1:
                        player = 2
                    else:
                        player = 1
                pygame.time.delay(500)
        if cua2.collidepoint((mx, my)):
            if click:
                if (cuadroDisponible(0, 1, player)):
                    marcarCuadro(0, 1, player)
                    if (checkWin(player)):
                        gameOver = True

                    if player == 1:
                        player = 2
                    else:
                        player = 1
                pygame.time.delay(500)
        if cua3.collidepoint((mx, my)):
            if click:
                if (cuadroDisponible(0, 2, player)):
                    marcarCuadro(0, 2, player)
                    if (checkWin(player)):
                        gameOver = True

                    if player == 1:
                        player = 2
                    else:
                        player = 1
                pygame.time.delay(500)
        if cua4.collidepoint((mx, my)):
            if click:
                if (cuadroDisponible(1, 0, player)):
                    marcarCuadro(1, 0, player)
                    if (checkWin(player)):
                        gameOver = True

                    if player == 1:
                        player = 2
                    else:
                        player = 1
                pygame.time.delay(500)
        if cua5.collidepoint((mx, my)):
            if click:
                if (cuadroDisponible(1, 1, player)):
                    marcarCuadro(1, 1, player)
                    if (checkWin(player)):
                        gameOver = True

                    if player == 1:
                        player = 2
                    else:
                        player = 1
                pygame.time.delay(500)
        if cua6.collidepoint((mx, my)):
            if click:
                if (cuadroDisponible(1, 2, player)):
                    marcarCuadro(1, 2, player)
                    if (checkWin(player)):
                        gameOver = True

                    if player == 1:
                        player = 2
                    else:
                        player = 1
                pygame.time.delay(500)
        if cua7.collidepoint((mx, my)):
            if click:
                if (cuadroDisponible(2, 0, player)):
                    marcarCuadro(2, 0, player)
                    if (checkWin(player)):
                        gameOver = True

                    if player == 1:
                        player = 2
                    else:
                        player = 1
                pygame.time.delay(500)
        if cua8.collidepoint((mx, my)):
            if click:
                if (cuadroDisponible(2, 1, player)):
                    marcarCuadro(2, 1, player)
                    if (checkWin(player)):
                        gameOver = True

                    if player == 1:
                        player = 2
                    else:
                        player = 1
                pygame.time.delay(500)
        if cua9.collidepoint((mx, my)):
            if click:
                if (cuadroDisponible(2, 2, player)):
                    marcarCuadro(2, 2, player)
                    if (checkWin(player)):
                        gameOver = True

                    if player == 1:
                        player = 2
                    else:
                        player = 1
                pygame.time.delay(500)

        dibujarEnCuadro()

        click = False
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.MOUSEBUTTONDOWN and not gameOver:
                if event.button == 1:
                    click = True

        if cuadroLleno() and not gameOver:
            draw_text("TIE", fontNumero, (255, 255, 255), screen, 230, 400)
            pygame.display.update()
            pygame.time.delay(1000)
            restartIA()

        if cuadroLleno():
            restartIA()

        if gameOver:
            restartIA()

        if (player == 2):
            movimientoIA()
            if (checkWin(2)):
                gameOver = True
                pygame.time.delay(500)

        pygame.display.update()


def chessPeonesLocal():
    import chessPeones
    chessPeones.chess(pygame.display.set_mode((chessPeones.WIDTH, chessPeones.WIDTH)), chessPeones.WIDTH)

def chessPeonesIA():
    import chessPeonesIA
    chessPeonesIA.chess(pygame.display.set_mode((chessPeonesIA.WIDTH, chessPeonesIA.WIDTH)), chessPeonesIA.WIDTH)


startMenu()