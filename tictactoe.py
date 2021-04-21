import pygame

pygame.init()
pygame.font.init()

MYFONT = pygame.font.SysFont('Comic Sans MS', 60)
SCREEN_HEIGHT, SCREEN_WIDTH = 720, 680

win = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
num_clicks = 0
moves_list = {}

def draw_board(window):
    window.fill((122, 122, 122))

    square1 = pygame.Rect(20, 60, 200, 200) 
    square2 = pygame.Rect(20, 280, 200, 200)
    square3 = pygame.Rect(20, 500, 200, 200)
    square4 = pygame.Rect(240, 60, 200, 200)
    square5 = pygame.Rect(240, 280, 200, 200)
    square6 = pygame.Rect(240, 500, 200, 200)
    square7 = pygame.Rect(460, 60, 200, 200)
    square8 = pygame.Rect(460, 280, 200, 200)
    square9 = pygame.Rect(460, 500, 200, 200)

    global squares
    squares = [square1, square2, square3, square4, square5, square6, square7, square8, square9]

    pygame.draw.rect(win, (0, 0, 0), square1)
    pygame.draw.rect(win, (0, 0, 0), square2)
    pygame.draw.rect(win, (0, 0, 0), square3)
    pygame.draw.rect(win, (0, 0, 0), square4)
    pygame.draw.rect(win, (0, 0, 0), square5)
    pygame.draw.rect(win, (0, 0, 0), square6)
    pygame.draw.rect(win, (0, 0, 0), square7)
    pygame.draw.rect(win, (0, 0, 0), square8)
    pygame.draw.rect(win, (0, 0, 0), square9)

def check_for_winner(sq1, sq2, sq3):
    if sq1 in moves_list and sq2 in moves_list and sq3 in moves_list:
        if moves_list[sq1] == moves_list[sq2] == moves_list[sq3]: 
            if moves_list[sq1] == "X":
                win.fill((0, 255, 0))
                textsurface = MYFONT.render("X wins!", False, (255, 255, 255))
                win.blit(textsurface, (250, 280))
                return
            else:
                win.fill((0, 0, 255))
                textsurface = MYFONT.render("O wins!", False, (255, 255, 255))
                win.blit(textsurface, (250, 280))
                return

def draw_game():
    win.fill((255, 0, 0))
    textsurface = MYFONT.render("DRAW", False, (255, 255, 255))
    win.blit(textsurface, (250, 280))
    

def check_if_clicked(object, pos):

    if object.collidepoint(pos):
        global num_clicks

        num_clicks += 1
        turn = ""

        if object == squares[0]:
            
            if num_clicks % 2 == 1:
                turn = "X"
            else:
                turn = "O"

            textsurface = MYFONT.render(turn, False, (255, 255, 255))
            win.blit(textsurface, (100, 120))
            
            moves_list.update({"S1" : turn}) 

        if object == squares[1]:
 
            if num_clicks % 2 == 1:
                turn = "X"
            else:
                turn = "O"

            textsurface = MYFONT.render(turn, False, (255, 255, 255))
            win.blit(textsurface, (100, 340))
            
            moves_list.update({"S2" : turn}) 
             
        if object == squares[2]:
            
            if num_clicks % 2 == 1:
                turn = "X"
            else:
                turn = "O"

            textsurface = MYFONT.render(turn, False, (255, 255, 255))
            win.blit(textsurface, (100, 560))
            
            moves_list.update({"S3" : turn}) 
             
        if object == squares[3]:
            
            if num_clicks % 2 == 1:
                turn = "X"
            else:
                turn = "O"

            textsurface = MYFONT.render(turn, False, (255, 255, 255))
            win.blit(textsurface, (320, 120))
            
            moves_list.update({"S4" : turn}) 

        if object == squares[4]:
            
            if num_clicks % 2 == 1:
                turn = "X"
            else:
                turn = "O"

            textsurface = MYFONT.render(turn, False, (255, 255, 255))
            win.blit(textsurface, (320, 340))
            
            moves_list.update({"S5" : turn})

        if object == squares[5]:

            if num_clicks % 2 == 1:
                turn = "X"
            else:
                turn = "O"

            textsurface = MYFONT.render(turn, False, (255, 255, 255))
            win.blit(textsurface, (320, 560))
            
            moves_list.update({"S6" : turn})
             
        if object == squares[6]:
            
            if num_clicks % 2 == 1:
                turn = "X"
            else:
                turn = "O"

            textsurface = MYFONT.render(turn, False, (255, 255, 255))
            win.blit(textsurface, (540, 120))
            
            moves_list.update({"S7" : turn})
             
        if object == squares[7]:
            
            if num_clicks % 2 == 1:
                turn = "X"
            else:
                turn = "O"

            textsurface = MYFONT.render(turn, False, (255, 255, 255))
            win.blit(textsurface, (540, 340))
            
            moves_list.update({"S8" : turn})

        if object == squares[8]:
            
            if num_clicks % 2 == 1:
                turn = "X"
            else:
                turn = "O"
 
            moves_list.update({"S9" : turn})
            textsurface = MYFONT.render(turn, False, (255, 255, 255))

            win.blit(textsurface, (540, 560))

        if len(moves_list) >= 5:
            check_for_winner("S1", "S2", "S3")
            check_for_winner("S1", "S5", "S9")
            check_for_winner("S1", "S4", "S7")
            check_for_winner("S2", "S5", "S8")
            check_for_winner("S3", "S6", "S9")
            check_for_winner("S3", "S5", "S7")
            check_for_winner("S4", "S5", "S6")
            check_for_winner("S7", "S8", "S9")

            if len(moves_list) == 9:
                draw_game()
            

draw_board(win)

run = True
while run: 
    pygame.display.flip()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            x, y = event.pos            
            
            for square in squares:
                check_if_clicked(square, (x, y))
