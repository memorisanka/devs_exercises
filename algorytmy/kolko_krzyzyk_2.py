# jednak nie kółko i krzyżyk

import pygame

pygame.init()
# pole gry
board = pygame.display.set_mode((500, 500))
# nagłówek
pygame.display.set_caption("Cos tam")

run = True

board_color = (175, 150, 150)
line_color = (0, 0, 0)

pygame.draw.rect(board, board_color, (10, 10, 480, 480))
# pygame.draw.line(board, line_color, (170, 10), (170, 490), 5)
# pygame.draw.line(board, line_color, (330, 10), (330, 490), 5)
# pygame.draw.line(board, line_color, (10, 170), (490, 170), 5)
# pygame.draw.line(board, line_color, (10, 330), (490, 330), 5)

# dane do ruchu myszką
x = 10
y = 10
width = 20
height = 20
step = 20

while run:
    pygame.time.delay(50)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        x -= step
    if keys[pygame.K_RIGHT]:
        x += step
    if keys[pygame.K_UP]:
        y -= step
    if keys[pygame.K_DOWN]:
        y += step
    board.fill(board_color)
    pygame.draw.rect(board, line_color, (x, y, width, height))
    pygame.display.update()
