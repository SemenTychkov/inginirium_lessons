import pygame

pygame.init()

win = pygame.display.set_mode((500, 500))

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
    color = (0, 0, 0)

    win.fill(color)

    pygame.draw.line(win, (255, 255, 255),  (0, 0), (500, 500), 5)
    pygame.draw.line(win, (255, 255, 255), (500, 0), (0,500), 5)

    pygame.display.update()