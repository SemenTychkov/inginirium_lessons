import pygame

pygame.init()

win = pygame.display.set_mode((600, 500))

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
    color = (255,255,255)


    win.fill(color)

    pygame.draw.rect(win, (255,255,0), (0,0,600,500))
    pygame.draw.circle(win, (0,0,0), (200,200), 30)
    pygame.draw.polygon(win, (0,0,0), [(0,100),(100,50), (100,150)], False)
    pygame.draw.line(win, (0,255,255), (0,0), (100,100), 5)
    pygame.draw.lines(win, (0,0,0),True, ((200,200),(300,150),(300,250)), 10 )


    
    pygame.display.update()