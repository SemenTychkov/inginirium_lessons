import pygame

pygame.init()

win = pygame.display.set_mode((600, 500))

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
    color = (0, 0, 0)

    win.fill(color)

    pygame.draw.line(win, (255, 255, 255),  (0, 0), (600, 500), 5)
    pygame.draw.line(win, (255, 255, 255), (600, 0), (0,500), 5)

    pygame.display.update()